import os
import json
import boto3
import secrets
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DDB_TABLE_NAME']) # type: ignore

def generate_short_id(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def lambda_handler(event, context):
    method = event.get('requestContext', {}).get('http', {}).get('method', '')
    path = event.get('rawPath', '')
    
    def respond(status_code, body=None, headers=None):
        base_headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type"
        }
        if headers:
            base_headers.update(headers)
        return {
            "statusCode": status_code,
            "headers": base_headers,
            "body": json.dumps(body) if body is not None else ""
        }
    
    # Handle preflight OPTIONS request for CORS
    if method == 'OPTIONS':
        return respond(200)
    
    if method == 'POST' and path == '/shorten':
        body = json.loads(event.get('body', '{}'))
        long_url = body.get('url')
        if not long_url or not long_url.startswith(('http://', 'https://')):
            return respond(400, {"message": "Invalid URL"})
        # Generate unique short ID (check for collision)
        for _ in range(5):
            short_id = generate_short_id()
            resp = table.get_item(Key={'id': short_id})
            if 'Item' not in resp:
                break
        else:
            return respond(500, {"message": "Could not generate unique short ID"})
        table.put_item(Item={'id': short_id, 'url': long_url})
        base_url = os.environ.get('BASE_URL', 'https://your-lambda-url')
        return respond(201, {"short_url": f"{base_url}/{short_id}"})
    
    elif method == 'GET':
        short_id = path.lstrip('/')
        resp = table.get_item(Key={'id': short_id})
        if 'Item' in resp:
            url = resp['Item']['url']
            return {
                "statusCode": 302,
                "headers": {
                    "Location": url,
                    "Access-Control-Allow-Origin": "*"
                },
                "body": ""
            }
        else:
            return respond(404, {"message": "Not found"})
    else:
        return respond(405, {"message": "Method Not Allowed"})
