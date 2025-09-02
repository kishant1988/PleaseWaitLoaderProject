import redis

def connect_to_redis():
    """
    Connects to a Redis server and performs a PING command.
    """
    try:
        # Connect to Redis
        r = redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

        # Check the connection
        if r.ping():
            print("Successfully connected to Redis!")

            # Example: Set and Get a key
            r.set('mykey', 'Hello from Python!')
            value = r.get('mykey')
            print(f"Set and got a key from Redis: '{value}'")

    except redis.exceptions.ConnectionError as e:
        print(f"Could not connect to Redis: {e}")

if __name__ == "__main__":
    connect_to_redis()
