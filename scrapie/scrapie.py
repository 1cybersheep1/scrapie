import csv

import click
import pyfiglet


from .utility import read_urls, read_features
from .page import get_page_content, extract_features



__version__ = "0.1.0"

@click.command()
@click.argument('urls', type=click.Path(exists=True))
@click.argument('features', type=click.Path(exists=True))
def main(urls, features):   
    click.clear()
    click.secho(pyfiglet.figlet_format("Scrapie"), fg='bright_cyan')
 
    click.echo('Loading urls...')
    urls_info = read_urls(urls)
    urls_list = urls_info[0]
    click.echo('Loaded {} urls, {} invalid.\n'.format(len(urls_list), urls_info[1]))
    
    click.echo('Loading features...')
    features_info = read_features(features)
    features = features_info[0]
    click.echo('Loaded {} features, {} invalid.\n'.format(len(features), features_info[1]))

    result = []
    n_errors = 0
    with click.progressbar(urls_list, label='Processing urls') as test:
        for url in test:
            try:
                result.append(extract_features(get_page_content(url), features))
            except Exception:
                n_errors += 1

    click.echo('\nWriting data...')
    click.echo('Done writing {} rows! {} error{} encountered.'.format(len(result), n_errors, '' if n_errors == 1 else 's' ))
    csvData = [[f.name for f in features]] + result
    with open('output.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)