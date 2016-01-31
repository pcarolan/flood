import boto3

def destroy_drop_table():
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
        table = dynamodb.Table('Drops')
        table.delete()
        print("Deleted Table:", "Drops")
    except:
        print("Delete Table:", "Unsuccessful")

def create_drop_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")
    table = dynamodb.create_table(
        TableName='Drops',
        KeySchema=[
            {
                'AttributeName': 'drop_id',
                'KeyType': 'HASH'  #Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'drop_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    print("Table status:", table.table_status)

def main():
    destroy_drop_table()
    create_drop_table()

if __name__ == '__main__':
    main()
