class Feature:
    def __init__(self, name, selector, data_type, number_of_values, patterns):
        self.name = name
        self.selector = selector
        self.pattern = patterns[data_type]
        self.multiple_values = number_of_values != 'single'