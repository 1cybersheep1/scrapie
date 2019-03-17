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
        print('Timeout')
        return ''
    except:
        print("Error")
        return ''
        
    
def extract_features(page_content, features):
    extracted_features = []
    for feature in features:
        tag_content = page_content.select(feature.selector)[0].text
        values = re.findall(feature.pattern, tag_content)    
        extracted_features.append(', '.join(values) if feature.multiple_values else values[0])
    return extracted_features