import validators
import re

from feature import Feature

feature_validator = re.compile(r'^\s*([_\w\s-]+)\s*:\s*'
                               r'([-_\w\d]+)\s*,\s*'
                               r'(single|multiple)\s*,\s*'
                               r'([!\w]+)\s*,\s*'
                               r'([_\w-]+)\s*=(\s*[_\w\s-]+)+')


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
            match = feature_validator.match(line.strip())
            if match:
                values = match.groups()
                if values[1] in patterns:
                    attributes = {values[i]:values[i+1] for i in range(4, len(values), 2)}
                    print(values)
                    features.append(Feature(*values[:4], attributes, patterns))
                else:
                    invalid += 1
            else:
                
                invalid += 1
    return features, invalid