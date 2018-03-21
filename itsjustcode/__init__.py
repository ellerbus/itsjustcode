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

__all__ = ('generateit')


def generateit(sqlalchemy_url, table, template_file=None, template_contents=None):
    '''
    Generate - blah de blah

    :param sqlalchemy_url:

    :param table:

    :param template_file:

    :param template_contents:
    '''
    if template_file is None and template_contents is None:
        raise ValueError('template_file or template_contents must be provided')

    engine = create_engine(sqlalchemy_url)

    metadata = MetaData(engine)
    metadata.reflect(only=[table])

    if template_contents is None:
        with open(template_file, 'r') as f:
            template_contents = f.read()

    results = Template(template_contents).render(table=metadata.tables[table])

    return results
