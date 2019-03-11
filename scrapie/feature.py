class Feature:
    def __init__(self, tag, attributes, data_type, multiple_values, patterns):
        self.tag = tag
        self.attributes = attributes
        self.pattern = patterns[data_type]
        self.multiple_values = multiple_values
             
