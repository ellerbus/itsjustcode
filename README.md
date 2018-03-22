## itsjustcode

Database First Code Generator that uses the [SQL Alchemy][sqlalchemy] and [Jinja2][jinja2]

### It's Just Code - Generate It

*itsjustcode* is intended to generate code from Jinja templates using SQL Alchemy's metadata. If
you are looking for a library to generate class models from an existing database, this isn't
it ... try [sqlacodegen][sqlacodegen]. *itsjustcode* is inteded to provide boilerplate code from templates to flesh out HTML files, or baseline javascript files for any number of available JavaScript frameworks (or TypeScript).

At the present moment, *itsjustcode* requires access to an existing database where it has been
created via SQL Alchemy models (or created with regular SQL scripts). *itsjustcode* uses SQL Alchemy
to access the metadata of a database in a conistent manner.

### Sample Usage

Also check out the [samples][samples] folder for templates, and outputs. It's just code
is intended to be integrated into a developer's workflow, as deemed by the project so 
there isn't a hard lined approach as to its integration.

```python
# generic sample
from itsjustcode import generateit

generateit(db_uri='mysql://username:password@localhost/database',
           table='table_name',
           template_search='my_proj/coding/templates/'
           template_file='framework/template.j2',
           out_file='my_proj/application/framework/template.extension')
```

```python
# generic cmd line implementation sample
# codeit.py
import argparse

from itsjustcode import generateit

parser = argparse.ArgumentParser()
parser.add_argument('--table', action='store', dest='table')
parser.add_argument('--template', action='store', dest='template')
args = parser.parse_args()

out_file = 'my_proj/application/' + args.template

generateit(db_uri='mysql://username:password@localhost/database',
           table=args.table,
           template_search='my_proj/coding/templates/'
           template_file=args.template + '.j2',
           out_file=out_file)

# ** .j2 just gives the template another extesion (check samples for examples)
```

```powershell
# generic cmd line sample
$> python codeit.py --table table_name --template framework/file.extension
```




[python-pkg]: https://python-packaging.readthedocs.io/en/latest/
[sqlalchemy]: http://www.sqlalchemy.org/
[jinja2]: http://jinja.pocoo.org/
[sqlacodegen]: https://pypi.python.org/pypi/sqlacodegen
[samples]: https://github.com/ellerbus/itsjustcode/tree/master/samples
