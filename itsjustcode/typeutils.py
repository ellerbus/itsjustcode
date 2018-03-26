
def get_duck_type(column):
    # from: https://github.com/seanharr11/etlalchemy/
    base_classes = map(
            lambda c: c.__name__.upper(),
            column.type.__class__.__bases__)

    if 'ENUM' in base_classes:
        return 'enum'

    if 'BOOLEAN' in base_classes:
        return 'bool'

    if 'STRING' in base_classes \
        or 'VARCHAR' in base_classes \
        or 'TEXT' in base_classes:
        # varchar_length = column.type.length
        return 'string'

    if 'DATE' in base_classes \
        or 'DATETIME' in base_classes:
        return 'datetime'
    
    if 'INTEGER' in base_classes:
        return 'int'

    if 'NUMERIC' in base_classes \
        or 'FLOAT' in base_classes \
        or 'DECIMAL' in base_classes:
        return 'float'
    
    if 'VARBINARY' in base_classes \
        or 'BINARY' in base_classes \
        or '_BINARY' in base_classes:
        return 'binary'
        
    # if class_name == 'array': return 'list'
    # if class_name == 'bigint': return 'int'
    # if class_name == 'biginteger': return 'int'
    # if class_name == 'binary': return 'bytes'
    # if class_name == 'blob': return 'bytes'
    # if class_name == 'boolean': return 'bool'
    # if class_name == 'char': return 'str'
    # if class_name == 'clob': return 'any'
    # if class_name == 'date': return 'date'
    # if class_name == 'datetime': return 'datetime'
    # if class_name == 'decimal': return 'float'
    # if class_name == 'enum': return 'int|string'
    # if class_name == 'float': return 'float'
    # if class_name == 'int': return 'int'
    # if class_name == 'integer': return 'int'
    # #if class_name == 'interval': return '?'
    # #if class_name == 'json': return '?'
    # if class_name == 'largebinary': return 'bytes'
    # if class_name == 'nchar': return 'str'
    # if class_name == 'nvarchar': return 'str'
    # if class_name == 'numeric': return 'float'
    # #if class_name == 'pickletype': return '?'
    # if class_name == 'real': return 'float'
    # if class_name == 'smallint': return 'int'
    # if class_name == 'smallinteger': return 'int'
    # if class_name == 'string': return 'str'
    # if class_name == 'text': return 'str'
    # if class_name == 'time': return 'time'
    # if class_name == 'timestamp': return 'timedelta'
    # #if class_name == 'typedecorator': return '?'
    # if class_name == 'unicode': return 'str'
    # if class_name == 'unicodetext': return 'str'
    # if class_name == 'varbinary': return 'bytes'
    # if class_name == 'varchar': return 'str'

    raise ValueError('Unknown Duck Type for - {}'.format(base_classes))
       


def typescript_type(column):
    duck_type = get_duck_type(column)

    if duck_type == 'bool':
        return 'boolean'
    elif duck_type == 'enum':
        return 'number|string'
    elif duck_type == 'datetime':
        return 'Date'
    elif duck_type == 'int' or duck_type == 'float':
        return 'number'
    elif duck_type == 'string':
        return 'string'
    else:
        return 'any'


def python_type(column):
    duck_type = get_duck_type(column)

    if duck_type == 'bool':
        return 'bool'
    elif duck_type == 'enum':
        return 'enum'
    elif duck_type == 'datetime':
        return 'Date'
    elif duck_type == 'int':
        return 'int'
    elif duck_type == 'float':
        return 'float'
    elif duck_type == 'string':
        return 'str'
    else:
        return ''