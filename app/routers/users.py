from fastapi import APIRouter, status, HTTPException
from app.schemas.users import UpdateUser, Users, UserBase
import boto3

router = APIRouter()

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: Users
):
    try:
        data = table.get_item(Key={'username': user.username, 'last_name':user.last_name})
        breakpoint()
        if 'Item' not in data:
             table.put_item(
                Item= user.dict()
            )
        raise Exception      
    except:
        raise HTTPException(status_code=409, detail="The user is already registered")
    

@router.delete("/delete", status_code=status.HTTP_200_OK)
async def delete_user(
    user:UserBase
):
    data = table.get_item(Key={'username': user.username, 'last_name':user.last_name})
    try:
        if 'Item' in data:
            table.delete_item(
                Key={
                    'username': user.username,
                    'last_name': user.last_name,
                })
    except:
        raise HTTPException(status_code=404, detail='The user has not been found')
    return {"message":"The user has been removed succesfully"}
    
@router.put("/update", status_code=status.HTTP_200_OK)
async def update_user(
    user: UserBase,
    new_data: UpdateUser
):
    data = table.get_item(Key={'username': user.username, 'last_name':user.last_name})
    try:
        unpacked = new_data.dict()
        for i in list(unpacked):
            if unpacked[i] == "string":
                unpacked.pop(i)
        items = unpacked.keys()
        breakpoint()
        for i in items:
            table.update_item(
            Key={
                'username': user.username,
                'last_name': user.last_name
            },
            UpdateExpression=f'SET {i} = :val1',
            ExpressionAttributeValues={
                ':val1':unpacked[i]
            }
        )
        breakpoint()
        
    except:
        raise HTTPException(status_code=400)
    raise HTTPException(status_code=200, detail="The user data has been updated")