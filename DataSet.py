class DataSet:
    def __init__(self, examples=None, inputs=None, attributes=None, target=None, attrnames=None, values=None):
        self.examples = examples
        self.target = target
        self.values = values
        self.inputs = inputs
        self.attributes = attributes
        self.attrnames = attrnames or attributes
#examples       : is the list of all examples of the dataset
#target         : is the position of the attribute that indicates the classification of the example
#values         : contains the values of the classification
#inputs         : attributes except the classification
#attributes     : all the attributes
#attrnames      : name of the attributes in the dataset
