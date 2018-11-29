import os
import sys

from jinja2 import Environment, FileSystemLoader, Template
from jinja2.filters import FILTERS
from sqlalchemy import MetaData, create_engine

import __main__

from .language import plural, singular
from .strutils import (camel_case, label_case, pascal_case, short_name,
                       snake_case, spine_case, split_name)

FILTERS['split_name'] = split_name
FILTERS['short_name'] = short_name
FILTERS['spine_case'] = spine_case
FILTERS['snake_case'] = snake_case
FILTERS['camel_case'] = camel_case
FILTERS['pascal_case'] = pascal_case
FILTERS['label_case'] = label_case
FILTERS['plural'] = plural
FILTERS['singular'] = singular


def get_template_search_paths(user_defined_paths):
    search_paths = []

    if user_defined_paths is not None:
        for path in user_defined_paths.split(';'):
            search_paths.append(path.rstrip())

    built_in = os.path.dirname(__file__)
    built_in = os.path.join(built_in, 'templates/')
    search_paths.append(built_in)

    main_dir = os.path.abspath(sys.path[0])
    search_paths.append(main_dir)

    return search_paths


def generateit(**kwargs):
    '''
    Generate - blah de blah

    :param engine:

    :param db_uri:

    :param table:

    :param template_search:

    :param template_file:

    :param out_file:

    :param bindings:
    '''

    engine = kwargs.pop('engine', None)
    db_uri = kwargs.pop('db_uri', None)
    table = kwargs.pop('table', None)
    template_search = kwargs.pop('template_search', None)
    template_file = kwargs.pop('template_file', None)
    out_file = kwargs.pop('out_file', None)
    bindings = kwargs.pop('bindings', {})

    if engine is None and db_uri is None:
        raise ValueError('engine or db_uri must be provided')

    if template_file is None:
        raise ValueError('template_file must be provided')

    if engine is None:
        engine = create_engine(db_uri)

    metadata = MetaData(engine)
    metadata.reflect(only=[table])

    paths = get_template_search_paths(template_search)

    env = Environment(loader=FileSystemLoader(paths))

    tmpl = env.get_template(template_file)

    results = tmpl.render(table=metadata.tables[table], **bindings)

    with open(out_file, 'w') as f:
        f.write(results)
