import requests
import re

from bs4 import BeautifulSoup


class Page:
    def __init__(self, url, timeout=5):
        try:
            # Make the request
            response = requests.get(url, timeout=timeout)
            # Check status code
            assert response.status_code == 200, response.status_code  
            self.content = BeautifulSoup(response.content, "html.parser")     
            # If the request timed out print a warning
        except requests.Timeout as e:
            print("Timeout")  
            print(str(e))
        except Exception as e:
            print("Error")
            print(str(e))
            
    def extract_feature(self, feature):
        tag_content = self.content.find(feature.tag, feature.attributes).text
        values = re.findall(feature.pattern, tag_content)
        return ', '.join(values) if feature.multiple_values else values[0]