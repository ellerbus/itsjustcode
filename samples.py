from sqlalchemy import (
    create_engine, MetaData,
    Table, Column,
    Integer, String, DateTime, Float
)

from itsjustcode import generateit


def create_db_sample():
    db_uri = 'sqlite://'
    engine = create_engine(db_uri)
    meta = MetaData(engine)

    # Register t1, t2 to metadata
    t1 = Table('sample_table',
               meta,
               Column('id', Integer, primary_key=True),
               Column('name', String),
               Column('cost', Float),
               Column('started_at', DateTime))

    # Create all tables in meta
    meta.create_all()

    return engine


if __name__ == '__main__':
    engine = create_db_sample()

    templates = [
        'angularjs/model.ts',
        'angularjs/repository.ts',
        'angularjs/listcontroller.ts',
        'angularjs/list.html',
        'angularjs/detailcontroller.ts',
        'angularjs/detail.html'
    ]

    bindings = dict(namespace='Just.Code')

    for template in templates:
        generateit(engine=engine,
                   table='sample_table',
                   template_search='samples/templates/',
                   template_file=template + '.j2',
                   out_file='samples/output/' + template,
                   bindings=bindings)
