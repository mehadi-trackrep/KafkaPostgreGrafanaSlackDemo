import json
import psycopg2
from kafka import KafkaConsumer
from config import BROKER_EXTERNAL_PORT, KAFKA_TOPIC_NAME, DOCKER_CONTAINER_HOST, \
    DB_TABLE_NAME

# Create Kafka consumer
consumer = KafkaConsumer(
    KAFKA_TOPIC_NAME,  # replace with your Kafka topic
    bootstrap_servers=f'localhost:{BROKER_EXTERNAL_PORT}',  # replace with your bootstrap servers
    group_id='demo',  # replace with your group id
    auto_offset_reset='earliest',
)

"""
 If we are unsure what to use, consider using a name that describes the role of the consumer 
 in our application. For example, if the consumer's job is to process logs, we might choose 
 a group.id like 'log_processor'. Remember, the group.id should be unique within your Kafka 
 cluster for each consumer group.
"""

# PostgreSQL connection configuration
pg_conf = {
    'dbname': 'cryptocurrency-info',  # replace with your database name
    'user': 'admin',  # replace with your username
    'password': 'admin',  # replace with your password
    # 'host': f'host.docker.internal:{DB_PORT}' # replace with your host
    'host': DOCKER_CONTAINER_HOST # replace with your host
    
}

# Connect to PostgreSQL database
conn = psycopg2.connect(**pg_conf)
cur = conn.cursor()

try:
    for msg in consumer:
        '''
            CREATE TABLE IF NOT EXISTS test (
                id serial PRIMARY KEY,
                usd_rate_float INTEGER,
                gbp_rate_float INTEGER,
                eur_rate_float INTEGER,
                timestamp timestamp default current_timestamp,
                UNIQUE (id, usd_rate_float, gbp_rate_float, eur_rate_float)
            );
        
        '''

        decoded_msg = json.loads(msg.value.decode('utf-8'))
        print(f"msg: {decoded_msg}")
        print(f"=>msg: {list(decoded_msg.values())}")
        
        # Write message value to PostgreSQL database
        cur.execute(
            f"INSERT INTO {DB_TABLE_NAME}(usd_rate_float, gbp_rate_float, eur_rate_float) VALUES {tuple(list(decoded_msg.values()))}"
            , 
        )
        conn.commit()

except KeyboardInterrupt:
    pass
finally:
    # Close PostgreSQL connection
    cur.close()
    conn.close()
