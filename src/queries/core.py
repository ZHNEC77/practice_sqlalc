from sqlalchemy import text, insert
from database import sync_engine, async_engine
from models import metadata_obj, workers_table


def create_tables():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


def insert_data():
    with sync_engine.connect as conn:
        stmt = insert(workers_table).values(
            [
                {"username": "Bobr"},
                {"username": "volk"},
            ]
        )
        conn.execute(stmt)
        conn.commit()
