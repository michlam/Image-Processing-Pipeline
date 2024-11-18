import json
import boto3
import time

def lambda_handler(event, context):
    # ===========================================================================
    # CALL INSTANCE OF CONTAINER
    # ===========================================================================
    client = boto3.client('ecs')
    response = client.run_task(
        cluster='group3-image-processing-cluster',
        taskDefinition='arn:aws:ecs:ca-central-1:941377123257:task-definition/process-image:1',
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    'subnet-0bd4969a96acdf28f',
                ],
                'securityGroups': [
                    'sg-0ae29ac73fe58eafc',
                ],
                'assignPublicIp': 'ENABLED'
            }
        },
        count=1,
    )

    # ===========================================================================
    # WAIT FOR RESPONSE
    # ===========================================================================
    task_arn = response['tasks'][0]['taskArn']
    
    while True:
        # Check task status
        task_description = client.describe_tasks(
            cluster='group3-image-processing-cluster',
            tasks=[task_arn]
        )
        task_status = task_description['tasks'][0]['lastStatus']
        
        print(f"Task status: {task_status}")
        
        # Break the loop if the task is completed or stopped
        if task_status in ['STOPPED']:
            break
        
        # Wait for a few seconds before polling again
        time.sleep(5)

    # Get exit code or result (if applicable)
    stopped_task = client.describe_tasks(
        cluster='group3-image-processing-cluster',
        tasks=[task_arn]
    )
    
    exit_code = stopped_task['tasks'][0]['containers'][0].get('exitCode', None)
    print(f"Task exit code: {exit_code}")

    # ===========================================================================
    # RETRIEVE LATEST JSON RESPONSE
    # ===========================================================================
    s3 = boto3.client('s3')
    bucket_name = 'openalpr-image-upload'
    folder_name = 'result/'

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    objects = response['Contents']
    objects.sort(key=lambda obj: obj['LastModified'], reverse=True)

    latest_file_key = objects[0]['Key']
    tmp_file_name = '/tmp/latest_file.json'

    s3.download_file(bucket_name, latest_file_key, tmp_file_name)
    with open(tmp_file_name, 'r') as f:
        json_data = json.load(f)
    

    # ===========================================================================
    # FORMULATE RESPONSE TO RDS
    # ===========================================================================
    images_folder_s3_uri = "s3://openalpr-image-upload/images/"
    
    returnJson = {
        "link": images_folder_s3_uri + latest_file_key[7:],
        "region": json_data["results"][0]["region"],
        "plate": json_data["results"][0]["plate"],
        "confidence": json_data["results"][0]["confidence"],
        "datetime": json_data["epoch_time"]
    }

    return {
        'statusCode': 200,
        'body': json.dumps(returnJson)
    }
