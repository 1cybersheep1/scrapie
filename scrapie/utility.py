import configparser
import validators
import re

from .feature import Feature

feature_validator = re.compile(r'^\s*([_\w\s-]+)\s*:\s*'
                               r'([-\w\d]+)\s*,\s*'
                               r'(single|multiple)\s*,\s*'
                               r'([!\w-]+)\s*'
                               r'((?:,\s*[\w\s\d-]+=[\w\s\d-]+\s*)+)$')

patterns = {'any':'.*','string':'\w+', 'float': '\-?\d+[.,]\d+', 'int': '\-?\d+'}


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


def read_features(file):
    features = []
    invalid = 0
    data = configparser.ConfigParser()
    data.read(file)
    for feature_name in data.sections():
        try:
            features.append(Feature(feature_name, 
                                    data[feature_name]['selector'],
                                    data[feature_name]['type'],
                                    data[feature_name]['quantity'],
                                    patterns))
        except:
            invalid += 1
    return features, invalid