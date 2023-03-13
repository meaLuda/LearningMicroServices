"""
It sends a python dict (producer, some_id, count)
to REDIS STREAM (using the xadd method)

Usage:
  PRODUCER=Roger MESSAGES=10 python producer.py
"""
from os import environ
from redis import Redis
from uuid import uuid4
from time import sleep

# stream key
STREAM_KEY = environ.get("STREAM", "teststream-1")
PRODUCER = environ.get("PRODUCER", "user-1")
MAX_MESSAGES = int(environ.get("MESSAGES", "2"))

def connect_to_redis_server():
    hostname = environ.get("REDIS_HOSTNAME", "localhost")
    port = environ.get("REDIS_PORT", 6379)

    # try connect
    try:
        r= Redis(
            hostname,
            port,
            retry_on_timeout=True
        )
        return r
    except ConnectionRefusedError as e:
        print(e)
    
def send_data(redis_connection,max_msgs):
    count = 0

    while count < max_msgs:
        try:
            # random data
            data = {
                "producer": PRODUCER,
                "some_id": uuid4().hex,  # Just some random data
                "count": count,
            }

            # Add data to stream
            resp = redis_connection.xadd(
                STREAM_KEY,
                data
            )

            print(resp)
            count += 1 
        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))
        
        # sleep for 5 seconds before going to the next process
        sleep(0.5)

# test
if __name__ == "__main__":
    connection = connect_to_redis_server()
    send_data(connection,MAX_MESSAGES)