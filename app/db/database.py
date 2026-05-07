from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USER_NAME")
db_password = os.getenv("DB_PASSWORD")
uri = f"mongodb+srv://{db_username}:{db_password}@cluster0.tw7vd.mongodb.net/?appName=Cluster0"

client = AsyncMongoClient(uri)  
async def connect_db():
    try:
        print("🔗 Connecting to MongoDB...")
        await client.admin.command('ping')
        print("✅ Connected to MongoDB!")
    except Exception as e:
        print("❌ Connection failed:", e.__str__())

db = client["DeliveryApp"]
OrderTable=db["orders"]
UserTable=db["users"]
RoleTable=db["roles"]
OrderStatusTable=db["order_status"]
ActivityLogTable=db["activity_logs"]
