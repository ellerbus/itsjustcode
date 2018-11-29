import unittest

from itsjustcode.strutils import (
    split_name, short_name, spine_case, snake_case,
    camel_case, pascal_case, label_case
)


class TestStrUtils(object):

    def test_split_name(self):
        assert split_name('Some_FUNNYName') == ['Some', 'FUNNY', 'Name']

    def test_short_name(self):
        assert short_name('Some_FUNNYName') == 'name'

    def test_spine_case(self):
        assert spine_case('Some_FUNNYName') == 'some-funny-name'

    def test_snake_case(self):
        assert snake_case('Some_FUNNYName') == 'some_funny_name'

    def test_camel_case(self):
        assert camel_case('Some_FUNNYName') == 'someFunnyName'

    def test_pascal_case(self):
        assert pascal_case('Some_FUNNYName') == 'SomeFunnyName'

    def test_label_case(self):
        assert label_case('Some_FUNNYName') == 'Some Funny Name'
