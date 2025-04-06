from sqlalchemy import text, insert, select
from database import sync_engine, async_engine, session_factory, Base
from models import WorkersOrm


# def create_tables():
#     Base.metadata.drop_all(sync_engine)
#     Base.metadata.create_all(sync_engine)


# def insert_data():
#     worker_bobr = WorkersOrm(username="Bobr")
#     with session_factory() as session:
#         session.add(worker_bobr)


class SyncOrm:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all()
        Base.metadata.create_all()
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersOrm(username="Jack")
            worker_michael = WorkersOrm(username="Michael")
            session.add_all([worker_jack, worker_michael])
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            # worker_id = 1
            # worker_jack = session.get(WorkersOrm, worker_id)
            query = select(WorkersOrm)
            result = session.execute(query)
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = "Misha"):
        pass
