import csv

import click

from .utility import read_urls, read_features
from .page import get_page_content, extract_features

__version__ = "0.1.0"

@click.command()
@click.argument('urls', type=click.Path(exists=True))
@click.argument('features', type=click.Path(exists=True))
def main(urls, features):
    urls = read_urls(urls)[0]
    features = read_features(features)[0]
    result = []
    for url in urls:
        result.append(extract_features(get_page_content(url), features))
    
    csvData = [[f.name for f in features]] + result
    with open('output.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
        