## itsjustcode

Database First Code Generator that uses the [SQL Alchemy][sqlalchemy] and [Jinja2][jinja2].

### It's Just Code - Generate It

*itsjustcode* is intended to generate code from Jinja templates using SQL Alchemy's metadata. If
you are looking for a library to generate class models from an existing database, this isn't
it ... try [sqlacodegen][sqlacodegen]. *itsjustcode* is inteded to provide boilerplate code from templates to flesh out HTML files, or baseline javascript files for any number of available JavaScript frameworks (or TypeScript).

At the present moment, *itsjustcode* requires access to an existing database where it has been
created via SQL Alchemy models (or created with regular SQL scripts). *itsjustcode* uses SQL Alchemy
to access the metadata of a database in a conistent manner.

### Sample Usage

Generate boilerplate code either by passing in a template for a path to a template file.

```python
from itsjustcode import generateit

generateit(db_uri='mysql://username:password@localhost/database',
           table='table_name',
           template_file='./code_templates/list.html',
           out_file='../myweb/static/table_name.list.html')
```

https://python-packaging.readthedocs.io/en/latest/

[sqlalchemy]: http://www.sqlalchemy.org/
[jinja2]: http://jinja.pocoo.org/
[sqlacodegen]: https://pypi.python.org/pypi/sqlacodegen
