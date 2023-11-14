from sqlalchemy import Table, Column, Integer, Float, String, TIMESTAMP, Boolean
from src.database import metadata
import datetime

query = Table(
    'query',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('cadastral_number', String(16)),
    Column('longitude', Float),
    Column('latitude', Float),
    Column('result', Boolean),
    Column('create_time', TIMESTAMP, default=datetime.datetime.utcnow),
    )

