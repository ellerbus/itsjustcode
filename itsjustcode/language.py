import re


class LanguageRule(object):
    __slots__ = ['regex', 'replace']

    def __init__(self, rule, replace):
        self.regex = re.compile(rule, re.IGNORECASE)
        self.replace = replace


PLURAL_RULES = [
    # https://github.com/rails/rails/blob/master/activesupport/lib/active_support/inflections.rb
    LanguageRule(r'^person$', r'people'),
    LanguageRule(r'^sheep$', r'sheep'),
    LanguageRule(r'^man$', r'men'),
    LanguageRule(r'^woman$', r'women'),
    LanguageRule(r'^child$', r'children'),
    LanguageRule(r'^(zombie)$', r'\1s'),
    LanguageRule(r'(quiz)$', r'\1zes'),
    LanguageRule(r'^(oxen)$', r'\1'),
    LanguageRule(r'^(ox)$', r'\1en'),
    LanguageRule(r'^(m|l)ice$', r'\1ice'),
    LanguageRule(r'^(m|l)ouse$', r'\1ice'),
    LanguageRule(r'(matr|vert|ind)(?:ix|ex)$', r'\1ices'),
    LanguageRule(r'(x|ch|ss|sh)$', r'\1es'),
    LanguageRule(r'([^aeiouy]|qu)y$', r'\1ies'),
    LanguageRule(r'(hive)$', r'\1s'),
    LanguageRule(r'(?:([^f])fe|([lr])f)$', r'\1\2ves'),
    LanguageRule(r'sis$', r'ses'),
    LanguageRule(r'([ti])a$', r'\1a'),
    LanguageRule(r'([ti])um$', r'\1a'),
    LanguageRule(r'(buffal|tomat)o$', r'\1oes'),
    LanguageRule(r'(bu)s$', r'\1ses'),
    LanguageRule(r'(alias|status)$', r'\1es'),
    LanguageRule(r'(octop|vir)i$', r'\1i'),
    LanguageRule(r'(octop|vir)us$', r'\1i'),
    LanguageRule(r'^(ax|test)is$', r'\1es'),
    LanguageRule(r's$', r's'),
]

SINGULAR_RULES = [
    # https://github.com/rails/rails/blob/master/activesupport/lib/active_support/inflections.rb
    LanguageRule(r'^people$', r'person'),
    LanguageRule(r'^men$', r'man'),
    LanguageRule(r'^women$', r'woman'),
    LanguageRule(r'^(child)ren$', r'\1'),
    LanguageRule(r'^(zombie)s$', r'\1'),
    LanguageRule(r'(database)s$', r'\1'),
    LanguageRule(r'(quiz)zes$', r'\1'),
    LanguageRule(r'(matr)ices$', r'\1ix'),
    LanguageRule(r'(vert|ind)ices$', r'\1ex'),
    LanguageRule(r'^(ox)en', r'\1'),
    LanguageRule(r'(alias|status)(es)?$', r'\1'),
    LanguageRule(r'(octop|vir)(us|i)$', r'\1us'),
    LanguageRule(r'^(a)x[ie]s$', r'\1xis'),
    LanguageRule(r'(cris|test)(is|es)$', r'\1is'),
    LanguageRule(r'(shoe)s$', r'\1'),
    LanguageRule(r'(o)es$', r'\1'),
    LanguageRule(r'(bus)(es)?$', r'\1'),
    LanguageRule(r'^(m|l)ice$', r'\1ouse'),
    LanguageRule(r'(x|ch|ss|sh)es$', r'\1'),
    LanguageRule(r'(m)ovies$', r'\1ovie'),
    LanguageRule(r'(s)eries$', r'\1eries'),
    LanguageRule(r'([^aeiouy]|qu)ies$', r'\1y'),
    LanguageRule(r'([lr])ves$', r'\1f'),
    LanguageRule(r'(tive)s$', r'\1'),
    LanguageRule(r'(hive)s$', r'\1'),
    LanguageRule(r'([^f])ves$', r'\1fe'),
    LanguageRule(r'(^analy)(sis|ses)$', r'\1sis'),
    LanguageRule(
        r'((a)naly|(b)a|(d)iagno|(p)arenthe|(p)rogno|(s)ynop|(t)he)(sis|ses)$', r'\1sis'),
    LanguageRule(r'([ti])a$', r'\1um'),
    LanguageRule(r'(n)ews$', r'\1ews'),
    LanguageRule(r'(ss)$', r'\1'),
    LanguageRule(r's$', r''),
]


def plural(word):
    for rule in PLURAL_RULES:
        if rule.regex.search(word) is not None:
            return rule.regex.sub(rule.replace, word)
    return word + 's'


def singular(word):
    for rule in SINGULAR_RULES:
        if rule.regex.search(word) is not None:
            return rule.regex.sub(rule.replace, word)
    return word
