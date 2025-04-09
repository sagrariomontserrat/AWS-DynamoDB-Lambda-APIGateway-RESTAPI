import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    http_method = event['httpMethod']
    path_params = event.get('pathParameters') or {}

    if http_method == 'GET':
        if path_params.get('user_id'):
            return get_user(path_params['user_id'])  # GET /users/{user_id}
        else:
            return list_users()  # GET /users
    elif http_method == 'POST':
        return create_user(event)
    elif http_method == 'PUT':
        return update_user(event, path_params.get('user_id'))
    elif http_method == 'DELETE':
        return delete_user(path_params.get('user_id'))
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'message': 'Método no permitido'})
        }

def get_user(user_id):
    try:
        response = table.get_item(Key={'user_id': user_id})
        item = response.get('Item')
        if item:
            return {'statusCode': 200, 'body': json.dumps(item)}
        else:
            return {'statusCode': 404, 'body': json.dumps({'message': 'Usuario no encontrado'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

def list_users():
    try:
        response = table.scan()
        items = response.get('Items', [])
        return {'statusCode': 200, 'body': json.dumps(items)}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

def create_user(event):
    body = json.loads(event['body'])
    try:
        table.put_item(Item=body)
        return {'statusCode': 201, 'body': json.dumps({'message': 'Usuario creado'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

def update_user(event, user_id):
    body = json.loads(event['body'])
    try:
        response = table.update_item(
            Key={'user_id': user_id},
            UpdateExpression="set #n = :n, email = :e",
            ExpressionAttributeNames={'#n': 'name'},
            ExpressionAttributeValues={
                ':n': body['name'],
                ':e': body['email']
            },
            ReturnValues="UPDATED_NEW"
        )
        return {'statusCode': 200, 'body': json.dumps({'message': 'Usuario actualizado', 'data': response['Attributes']})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}

def delete_user(user_id):
    try:
        table.delete_item(Key={'user_id': user_id})
        return {'statusCode': 200, 'body': json.dumps({'message': 'Usuario eliminado'})}
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
