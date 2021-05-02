import json
import boto3
import uuid
import os

from datetime import datetime
#from enum import Enum

# class GalleryType(Enum):
#     Trash = "Trash"
#     Review = "Review"
#     Pulished = "Published"
#     BodyShop = "BodyShop"

def post(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    tableGallery = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    body = json.loads(event['body'])
    dynaDrawSavedItem = body['dynaDrawSavedItem']
    
    id = uuid.uuid4()
    creationDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Putting a try/catch to log to user when some error occurs
    try:
        tableGallery.put_item(
            Item={
                'id': str(id),
                'creationDateTime': creationDateTime,
                'dynaDrawSavedItem': dynaDrawSavedItem,
                'galleryType': "Review"
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully added gallery item for review!')
        }
    except:
        print('Closing lambda function')
        return {
            'statusCode': 400,
            'body': json.dumps('Error adding gallery item for review')
        }