import re
import requests

from bs4 import BeautifulSoup


def get_page_content(url, timeout=5):
    try:
        # Make the request
        response = requests.get(url, stream=True,timeout=timeout)
        # Check status code
        if response.status_code != 200:
            raise Exception(response.status_code)
        return BeautifulSoup(response.content, "html.parser")
        # If the request timed out print a warning
    except requests.Timeout:
        raise Exception('Timeout')
    except:
        raise Exception('Error')
    

def extract_features(page_content, features):
    extracted_features = []
    for feature in features:
        tag_content = page_content.select(feature.selector)
        text = tag_content[0].text if tag_content else ''
        values = re.findall(feature.pattern, text)
        extracted_features.append(', '.join(values) if feature.multiple_values else values[0])
    return extracted_features