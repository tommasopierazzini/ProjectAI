import DecisionTree
import math

def DecisionTreeLearner(dataset):

    def decisionTreeLearning(examples, attributes, parents_examples=()):
        if len(examples) == 0:
            return pluralityValue(parents_examples) #returns the most frequent classification among the examples
        elif allSameClass(examples):
            return DecisionTree.Leaf(examples[0][dataset.target]) #if they all have the same class, I return the class of the first example
        elif len(attributes) == 0:
            return pluralityValue(examples) #returns the most frequent classification among the examples
        else:
            mostImpAtt, threshold = chooseAttribute(attributes, examples)
            tree = DecisionTree.DecisionTree(mostImpAtt, threshold, dataset.attrnames[mostImpAtt])
            ExampleMinor, ExampleMajor = splittingOnThreshold(mostImpAtt, threshold, examples)#separate based on threshold
            #do recursion and add to the tree
            branchesLeft = decisionTreeLearning(ExampleMinor, removeAttr(mostImpAtt, attributes), examples)#recursion
            branchesRight = decisionTreeLearning(ExampleMajor, removeAttr(mostImpAtt, attributes), examples)#recursion
            tree.addLeft(threshold, branchesLeft)
            tree.addRight(threshold, branchesRight)
            return tree

    def chooseAttribute(attributes, examples): # found the most important attribute, ande threshold, according to information gain
        maxgainAttr = 0
        thresholdAttr = 0
        listValuesForAttribute = getListValuesForAttribute(dataset.examples, dataset.target)  # prepare a list of values for each attribute to find the most important
        global mostImportanceA
        for attr in attributes:
            maxgainValue = 0
            threshValue = 0
            for i in listValuesForAttribute[attr]:      # for each attribute of each "column" (values) in the dataset
                gain = float(informationGain(attr, float(i), examples))     # calcolate his gain
                if gain > maxgainValue :                                          # if gain greater assign it
                    maxgainValue = gain
                    threshValue = float(i)
            if maxgainValue  >= maxgainAttr:
                maxgainAttr = maxgainValue
                mostImportanceA = attr
                thresholdAttr = threshValue
        return mostImportanceA, thresholdAttr

    def pluralityValue(examples):
        i = 0
        global popular
        for v in dataset.values: #for each classification count the occurrences. Then choose the most popular
            count = counting(dataset.target, v, examples)
            if  count > i:
                i = count
                popular = v
        return DecisionTree.Leaf(popular)

    def allSameClass(examples): # return True if all examples have the same class
        sameClass = examples[0][dataset.target] #take that of the first example as a reference
        for e in examples:
            if e[dataset.target] != sameClass:
                return False
        return True

    def informationGain(attribute, threshold, examples):
        def entropy(examples):
            entr = 0
            if len(examples) != 0:
                for v in dataset.values:
                    p = float(counting(dataset.target, v, examples)) / len(examples)
                    if p != 0:
                        entr += (-p) * math.log(p, 2.0)
            return float(entr)
        def remainder(examples):
            N = float(len(examples))
            ExampleMinor, ExampleMajor = splittingOnThreshold(attribute, threshold, examples)
            remainderExampleMinor = (float((len(ExampleMinor))) / N) * entropy(ExampleMinor)
            remainderExampleMajor = (float((len(ExampleMajor))) / N) * entropy(ExampleMajor)
            return (remainderExampleMinor + remainderExampleMajor)

        # formula to calculate information gain
        return entropy(examples) - remainder(examples)

    def counting(attribute, value, example): #count the number of examples that have attribute = value
        return sum(e[attribute] == value for e in example)

    def removeAttr(delAttr, attributes): #delAttr is the attribute to remove
        result=list(attributes)
        result.remove(delAttr)
        return result

    def splittingOnThreshold(attribute, threshold, examples):
        ExampleMinor, ExampleMajor = [], []
        for e in examples:
            if float(e[attribute]) <= threshold: # divide the examples based on the threshold with respect to a given attribute
                ExampleMinor.append(e)
            else:
                ExampleMajor.append(e)
        return ExampleMinor, ExampleMajor

    return decisionTreeLearning(dataset.examples, dataset.inputs)

def getListValuesForAttribute(exemples, nA): #create a list of list with singles values of attributes
    valuesList = []
    for n in range(nA):
        l = []
        for i in range(0,len(exemples)):
            l.append(exemples[i][n])#values for each attribute
        l = list(set(l))#remove duplicates
        valuesList.append(l)  #attributes without duplicate (to improve speed)
    return valuesList