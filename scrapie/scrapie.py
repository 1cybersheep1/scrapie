import configparser
import re
import os

import click

from .utility import read_urls


__version__ = "0.2.0"

@click.command()
#@click.option('--urls', default=1, help='')
#@click.option('--n', prompt='', help='T')
#f = Feature('div', {'class':'updListPrice'}, 'float', True)
@click.argument('urls', type=click.Path(exists=True))
def main(urls):
    config = configparser.ConfigParser()
    config.read(os.getcwd()+'\config\example.ini')
    PATTERNS = {}
    for key, value in config['type regex patterns'].items():
        PATTERNS[key] = re.compile(value)


    print(read_urls(urls))
