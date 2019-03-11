import validators

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