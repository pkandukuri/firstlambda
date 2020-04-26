"""
This program is to Read and Write json file from/to S3
updated
"""
import  boto3
import json

def lambda_handler(event, context):
    
    BUCKET = 'source-s3-json'
    FILE_TO_READ = 'employees.json'

    #User: pra-service-id
    client = boto3.client('s3')

    #Read from the S3
    result = client.get_object(Bucket=BUCKET, Key=FILE_TO_READ)

    content = result['Body']
    jsonObject = json.loads(content.read())

    #Enriching json data
    for record in jsonObject:
        record['salary']= record['salary'] +10

    #Printing contents
    #for record in jsonObject:
    #    print (record)

    #Writing enhancded datea to new Json to S3
    client.put_object(Body=json.dumps(jsonObject), Bucket='target-s3-json', Key='modified_employees.json')

    return {
        'statusCode': 200,
        'body': json.dumps('Successfuly executed FetchAndWrite Lambda!')
    }
