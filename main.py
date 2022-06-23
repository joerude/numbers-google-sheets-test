import os

import sqlalchemy as sa
from dotenv import load_dotenv
from utils import exchange_rate_usdrub_today, gsheet2df

load_dotenv()
DATABASE = os.environ.get("DATABASE")
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")

connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (USER, PASSWORD, HOST, str(PORT), DATABASE)
engine = sa.create_engine(connection_string)
connection = engine.connect()

df = gsheet2df('Тестовое', sheet_num=0)

# if df['стоимость, $']:
df['стоимость в руб.'] = df['стоимость, $'] * exchange_rate_usdrub_today()

df = df.round(2)

print(df)

df.to_sql('test_data', con=engine, if_exists='replace', index=False, schema="test")

connection.close()
