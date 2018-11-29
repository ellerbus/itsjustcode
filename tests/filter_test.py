from jinja2 import Template

from itsjustcode import FILTERS


class TestJinjaFilters(object):

    def get_template_results(self, template):
        return Template(template).render()

    def test_short_name(self):
        tmplt = '{{ "Some_FUNNYName" | short_name }}'
        results = self.get_template_results(tmplt)
        assert results == 'name'

    def test_spine_case(self):
        tmplt = '{{ "Some_FUNNYName" | spine_case }}'
        results = self.get_template_results(tmplt)
        assert results == 'some-funny-name'

    def test_snake_case(self):
        tmplt = '{{ "Some_FUNNYName" | snake_case }}'
        results = self.get_template_results(tmplt)
        assert results == 'some_funny_name'

    def test_camel_case(self):
        tmplt = '{{ "Some_FUNNYName" | camel_case }}'
        results = self.get_template_results(tmplt)
        assert results == 'someFunnyName'

    def test_pascal_case(self):
        tmplt = '{{ "Some_FUNNYName" | pascal_case }}'
        results = self.get_template_results(tmplt)
        assert results == 'SomeFunnyName'
