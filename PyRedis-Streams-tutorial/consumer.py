"""
It reads the REDIS STREAM events
Using the xread, it gets 1 event per time (from the oldest to the last one)

"""
from os import environ
from redis import Redis

STREAM_KEY = environ.get("STREAM", "teststream-1")

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

def get_data(redis_connection):
    last_id = 0
    sleep_ms = 5000

    # set true so that we will always be listening to.
    while True:
        try:
            resp = redis_connection.xread(
                # pick from beggining of stream
                {STREAM_KEY: last_id},
                count = 1, # continue counting down the stream
                block=sleep_ms # sleep if there's nothing else
            )
            
            # if something is in stream.
            if resp:
                key, msg = resp[0]
                last_id,data = msg[0]

                print("REDIS ID: ", last_id)
                print(" From teststream-1 --> ", data)
        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))

# test
if __name__ == '__main__':
    connection = connect_to_redis_server()
    get_data(connection)