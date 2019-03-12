import validators
import re

from .feature import Feature

feature_validator = re.compile(r'^\s*([_\w\s-]+)\s*:\s*'
                               r'([-_\w\d]+)\s*,\s*'
                               r'(single|multiple)\s*,\s*'
                               r'([!\w]+)\s*'
                               r'((?:,\s*[\w\s\d]+=[\w\s\d]+\s*)+)$')

def read_urls(file):
    urls = []
    invalid = 0
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if validators.url(line):
                urls.append(line)
            else:
                invalid += 1
    return urls, invalid


def read_features(file, patterns):
    features = []
    invalid = 0
    with open(file, 'r') as f:
        for line in f:
            try:
                match = feature_validator.match(line.strip())
                values = match.groups()
                assert values[1] in patterns
                attributes = dict([x.strip().split('=') for x in values[4].split(',') if x.strip() != ''])
                features.append(Feature(*values[:4], attributes, patterns))
            except:
                invalid += 1
    return features, invalid