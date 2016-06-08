from mongoengine import connect

MONGODB_DB_NAME='stock'
MONGODB_USER_NAME='stock_admin'
MONGODB_PASSWORD='SstIq4r80iHMK7Xd'
MONGODB_HOST='202.112.114.3'
MONGODB_PORT=27017


def get_mongodb_connection():
    connect(MONGODB_DB_NAME,host=MONGODB_HOST, port=MONGODB_PORT, username=MONGODB_USER_NAME, password=MONGODB_PASSWORD)
