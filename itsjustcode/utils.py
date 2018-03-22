import re

SPLITTER_RE = re.compile(r'''
        [A-Z][A-Z0-9]+(?![a-z]) #   ACRONYM
    |   [A-Z][a-z]*             #   capitalized / single capital
    |   [a-z]+                  #   all-lowercase
    |   [0-9]+                  #   numbers
    |   _+                      #   underscores
    ''', re.VERBOSE)

IDENTIFIER_RE = re.compile(r'^[A-Za-z_]\w*\Z')


def split_name(name):
    '''
    split_name('Some_FUNNYName') -> [Some, FUNNY, Name]
    '''
    if not IDENTIFIER_RE.match(name):
        raise ValueError('Name is not a valid identifier for Python')

    parts = SPLITTER_RE.findall(name)

    if not (parts[0].strip('_') and parts[-1].strip('_')):
        raise ValueError('Name cannot start or end with underscores')

    return [s for s in parts if s.strip('_')]


def short_name(name):
    '''
    '''
    parts = split_name(name)

    return parts[-1].lower()


def spine_case(name):
    '''
    '''
    return '-'.join(s.lower() for s in split_name(name))


def snake_case(name):
    '''
    '''
    return '_'.join(s.lower() for s in split_name(name))


def camel_case(name):
    '''
    '''
    parts = split_name(name)

    return parts[0].lower() + ''.join(s.capitalize() for s in parts[1:])


def pascal_case(name):
    '''
    '''
    return ''.join(s.capitalize() for s in split_name(name))


def label_case(name):
    '''
    '''
    return ' '.join(s.capitalize() for s in split_name(name))
