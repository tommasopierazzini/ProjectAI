class DecisionTree:

    def __init__(self, attribute, threshold, attrname=None, default_child=None, branches=None):
        """Initialize by saying what attribute this node tests."""
        self.attr = attribute
        self.threshold = threshold
        self.attrname = attrname or attribute
        self.default_child = default_child
        self.branches = branches or {}
        #I have to split on <= o> values of the threshold, so I need a way to create two decision paths
        self.Left=0
        self.Right=1

    def __call__(self, example):  #find the decision of the tree given an example
        attrvalue = example[self.attr]
        if float(attrvalue) > self.threshold:
            return self.branches[(self.threshold, self.Right)](example)
        else:
            return self.branches[(self.threshold, self.Left)](example)

    def addLeft(self, value, subtree):
        self.branches[(value,self.Left)] = subtree

    def addRight(self, value, subtree):
        self.branches[(value, self.Right)] = subtree


class Leaf:
    def __init__(self, result):
        self.result = result

    def __call__(self, example):
        return self.result

