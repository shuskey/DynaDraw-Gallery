import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
#from enum import Enum
from decimal import Decimal
import os

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

# class GalleryType(Enum):
#     Trash = "Trash"
#     Review = "Review"
#     Pulished = "Published"
#     BodyShop = "BodyShop"

def get(event, context):
    dynamodb = boto3.resource('dynamodb')
    tableGallery = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    response = tableGallery.scan(FilterExpression=Attr('galleryType').eq("Published"))
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET,OPTIONS'
        },
        'body': json.dumps(response['Items'], cls=DecimalEncoder)
    }