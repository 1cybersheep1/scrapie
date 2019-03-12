class Feature:
    def __init__(self, name, data_type, multiple_values, tag, attributes, patterns):
        self.name = name
        self.tag = tag
        self.attributes = attributes
        self.pattern = patterns[data_type]
        self.multiple_values = multiple_values
             
