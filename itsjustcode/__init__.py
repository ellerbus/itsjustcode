import __main__
import os
import sys

from sqlalchemy import MetaData, create_engine
from jinja2 import Template, Environment, FileSystemLoader
from jinja2.filters import FILTERS

from .strutils import (
    split_name, short_name,
    spine_case, snake_case,
    camel_case, pascal_case,
    label_case
)

from .typeutils (
    typescript_type, python_type
)

FILTERS['split_name'] = split_name
FILTERS['short_name'] = short_name
FILTERS['spine_case'] = spine_case
FILTERS['snake_case'] = snake_case
FILTERS['camel_case'] = camel_case
FILTERS['pascal_case'] = pascal_case
FILTERS['label_case'] = label_case

FILTERS['typescript_type'] = typescript_type
FILTERS['python_type'] = python_type


# def get_absolute_path(path):
#     if path[0] == '.':
#         current_dir = os.path.abspath(os.curdir)
#         path = os.path.join(current_dir, path)
#         path = os.path.abspath(path)
#     return path


def get_template_search_paths(user_defined_paths):
    search_paths = []

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
        raise ValueError('template_file or template_contents must be provided')

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
