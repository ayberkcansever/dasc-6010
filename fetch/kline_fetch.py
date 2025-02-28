import time, requests, json
import psycopg2
from psycopg2 import OperationalError
from datetime import datetime, timedelta


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query, data):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.executemany(query, data)
        print("Query executed successfully")
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")


cryptos = ['BTCUSDT', 'ADAUSDT', 'ATOMUSDT', 'BCHUSDT', 'BNBUSDT', 'DOGEUSDT', 'ETHUSDT', 'LTCUSDT', 'SOLUSDT']

base_start_date = datetime(2021, 1, 1)
end_date = datetime.now()
max_hours_per_request = 24

db_name = "anayltics"
db_user = "postgres"
db_password = "postgres"
db_host = "localhost"
db_port = "9432"

connection = create_connection(db_name, db_user, db_password, db_host, db_port)

binance_base_url = "https://api.binance.us/api/v3/klines"
interval = "15m"

for crypto in cryptos:
    print(f"Processing {crypto} ...")
    coin_start_date = base_start_date

    base_symbol = crypto.replace("USDT", "").lower()
    table_name = f"kline_{base_symbol}"

    insert_query = f"""
    INSERT INTO {table_name} (moment, high, open, low, close, volume)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON CONFLICT (moment) DO UPDATE SET
        high = EXCLUDED.high,
        open = EXCLUDED.open,
        low = EXCLUDED.low,
        close = EXCLUDED.close,
        volume = EXCLUDED.volume
    """

    while coin_start_date < end_date:
        period_end_date = min(coin_start_date + timedelta(hours=max_hours_per_request), end_date)
        start_timestamp = int(coin_start_date.timestamp() * 1000)
        end_timestamp = int(period_end_date.timestamp() * 1000)

        params = {
            "symbol": crypto,
            "interval": interval,
            "startTime": start_timestamp,
            "endTime": end_timestamp,
            "limit": 1000
        }

        result = requests.get(url=binance_base_url, params=params)
        if result.status_code != 200:
            print(f"Error fetching data for {crypto}: {result.status_code}, {result.text}")
            break

        data = result.json()

        if not data:
            print(f"No data returned for {crypto} between {coin_start_date} and {period_end_date}")
            coin_start_date = period_end_date + timedelta(seconds=1)
            continue

        insert_data = [
            (kline[0], float(kline[2]), float(kline[1]), float(kline[3]), float(kline[4]), float(kline[5]))
            for kline in data
        ]

        execute_query(connection, insert_query, insert_data)

        print(f"Inserted data for {crypto} up to {period_end_date}")
        coin_start_date = period_end_date + timedelta(seconds=1)
        time.sleep(1)

connection.close()
print("All coins processed and connection closed.")