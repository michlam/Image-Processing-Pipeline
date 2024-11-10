import json
import boto3

def lambda_handler(event, context):
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

    print(response)  
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
