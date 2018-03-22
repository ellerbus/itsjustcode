import __main__

import os

from sqlalchemy import MetaData, create_engine
from jinja2 import Template
from jinja2.filters import FILTERS

from .utils import (
    split_name, short_name,
    spine_case, snake_case,
    camel_case, pascal_case
)

FILTERS['split_name'] = split_name
FILTERS['short_name'] = short_name
FILTERS['spine_case'] = spine_case
FILTERS['snake_case'] = snake_case
FILTERS['camel_case'] = camel_case
FILTERS['pascal_case'] = pascal_case

def get_absolute_path(path):
    full_path = path
    if not os.path.isabs(full_path):
        dir_path = os.path.dirname(__main__.__file__)
        full_path = os.path.join(dir_path, path)
    return full_path

def generateit(**kwargs):
    '''
    Generate - blah de blah

    :param engine:

    :param db_uri:

    :param table:

    :param template_file:

    :param template_contents:

    :param out_file:
    '''

    engine = kwargs.pop('engine', None)
    db_uri = kwargs.pop('db_uri', None)
    table = kwargs.pop('table', None)
    template_file = kwargs.pop('template_file', None)
    template_contents = kwargs.pop('template_contents', None)
    out_file = kwargs.pop('out_file', None)

    if engine is None and db_uri is None:
        raise ValueError('engine or db_uri must be provided')

    if template_file is None and template_contents is None:
        raise ValueError('template_file or template_contents must be provided')

    if engine is None:
        engine = create_engine(db_uri)

    metadata = MetaData(engine)
    metadata.reflect(only=[table])

    if template_contents is None:
        template_file_path = get_absolute_path(template_file)
        with open(template_file_path, 'r') as f:
            template_contents = f.read()

    results = Template(template_contents).render(table=metadata.tables[table])

    with open(out_file, 'w') as f:
        f.write(results)
