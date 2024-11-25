import json
import boto3
import time
import os
import mysql.connector
from datetime import datetime

def lambda_handler(event, context):
    # ===========================================================================
    # RETRIEVE LATEST JSON RESPONSE
    # ===========================================================================
    s3 = boto3.client('s3')

    bucket_name = 'openalpr-image-upload'
    bucket = boto3.resource('s3').Bucket(bucket_name)


    keys = []
    for obj in bucket.objects.all():
        keys.append(obj.key)
    
    latest_file_key = keys[len(keys) - 1]
    print(latest_file_key)
    tmp_file_name = '/tmp/latest_file.json'

    s3.download_file(bucket_name, latest_file_key, tmp_file_name)
    with open(tmp_file_name, 'r') as f:
        json_data = json.load(f)
    
    # ===========================================================================
    # FORMULATE RESPONSE FOR RDS
    # ===========================================================================
    images_folder_s3_uri = "s3://openalpr-image-upload/images/"
    
    # convert to datetime object
    epoch_time_ms = json_data["epoch_time"]

    dt_object = datetime.utcfromtimestamp(epoch_time_ms/1000)
    my_datetime = dt_object.strftime('%Y-%m-%d %H:%M:%S')

    returnJson = {
        "link": images_folder_s3_uri + latest_file_key[7:],
        "region": json_data["results"][0]["region"],
        "plate": json_data["results"][0]["plate"],
        "confidence": json_data["results"][0]["confidence"],
        "datetime": my_datetime
    }

    print(json.dumps(returnJson))

    return {
            'statusCode': 200,
            'body': json.dumps(returnJson)
        }

    # insert_query = """
    # INSERT INTO plates (link, region, plate, confidence, datetime)
    # VALUES (%s, %s, %s, %s, %s);
    # """
    
    # entry_data = (
    #     returnJson["link"], 
    #     returnJson["region"], 
    #     returnJson["plate"], 
    #     returnJson["confidence"], 
    #     datetime 
    # )
    
    try:
    #     # connect to DB
    #     connection = mysql.connector.connect(
    #         host=os.environ["DB_HOST"],
    #         database=os.environ["DB_NAME"],
    #         user=os.environ['DB_USER'],
    #         password = os.environ['DB_PASSWORD'],
    #         port=int(os.environ['DB_PORT'])
    #     )
    #     cursor = connection.cursor()
        
    #     # Execute the insert query
    #     cursor.execute(insert_query, entry_data)
    #     connection.commit()
        
        return {
            'statusCode': 200,
            'body': json.dumps(returnJson)
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }

    # finally:
    #     # Close connection
    #     if 'cursor' in locals():
    #         cursor.close()
    #     if 'connection' in locals() and connection.is_connected():
    #         connection.close()     
