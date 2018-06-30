from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

engine = create_engine('sqlite:///db.sqlite3', echo=False)

metadata = MetaData()
metadata.bind = engine

# todoテーブルの定義
todo = Table(
    'todo', metadata,
    Column('id', Integer, primary_key=True),
    Column('contents', String),
    Column('created_at', DateTime)
)
