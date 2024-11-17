import redis
from app import redis as redis_client

# Function to handle Redis caching setup
def initialize_redis():
    try:
        redis_client.ping()
        print("Connected to Redis successfully.")
    except redis.ConnectionError:
        print("Could not connect to Redis.")
