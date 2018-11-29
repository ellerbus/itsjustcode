import re

from jinja2 import Template

from itsjustcode import FILTERS, plural, singular


class TestJinjaLanguageFilters(object):

    def get_template_results(self, template):
        return Template(template).render()

    def test_plural_person(self):
        results = plural('person')
        assert results == 'people'

    def test_plural_bus(self):
        results = plural('bus')
        assert results == 'buses'

    def test_plural_run(self):
        results = plural('run')
        assert results == 'runs'

    def test_singular_people(self):
        results = singular('people')
        assert results == 'person'

    def test_singular_buses(self):
        results = singular('buses')
        assert results == 'bus'

    def test_singular_runs(self):
        results = singular('runs')
        assert results == 'run'
