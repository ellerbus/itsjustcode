from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String

from itsjustcode import generateit


def create_db_sample():
    db_uri = 'sqlite://'
    engine = create_engine(db_uri)
    meta = MetaData(engine)

    # Register t1, t2 to metadata
    t1 = Table('sample_table',
               meta,
               Column('id', Integer, primary_key=True),
               Column('name', String))

    # Create all tables in meta
    meta.create_all()

    return engine


if __name__ == '__main__':
    engine = create_db_sample()

    generateit(engine=engine,
               table='sample_table',
               template_file='./sample_templates/list.html',
               out_file='./sample_output/sample_table.list.html')
