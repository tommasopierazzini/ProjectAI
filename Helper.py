import DataSet
import random

datasetWithID = ['breastCancer.txt', 'ecoli.txt'] #only these datasets have the attribute id

def setForDataset(file, attrnames, target, values):
    #reading from the file dataset.txt it creates examples, attributes and input and then creates the object dataset
    examples = []
    for line in open(file).readlines():
        content = line.split(',')
        if file in datasetWithID:                                   #only these datasets have the attribute id
            content.pop(0)                                            #remove the first element, I guess I would do tests on the attribute id
        content = [c.rstrip() for c in content]
        example = []
        for j in range(0,len(content)):
            example.append(content[j])
        examples.append(example)                                    #creates examples (each line of file)
    attributes=[]
    for i in range(0,len(attrnames)):
        attributes.append(i)                                        #creates attributes
    inputs = removeTarget(attributes, target)                       #creates the input without the classification
    return DataSet.DataSet( examples, inputs, attributes, target, attrnames, values)#crates dataset for use

def removeTarget(attributes, target): #return a list of attribute without target (that is the classification)
    input = list(attributes)
    input.pop(input.index(target))
    return input

def shuffleDataTrain(dataset):
    #given the train test, the order of the examples is randomized and a subset is taken
    l = len(dataset.examples)
    sds = random.sample(dataset.examples, l)            #sample function takes n random examples from the dataset. Set n = number of examples to simulate a total randamization
    for i in range(0,l/2):                              #della meta' degli esempi ne prendo un sottoinsime per cercare di creare alberi un po' diversi tra loro
        a = random.randint(0,4)
        if a == 1:
            sds.pop(i)
    #create examples, attributes and inputs as before...
    examples = []
    for i in range(len(sds)):
        example = []
        for j in range(len(sds[0])):
            example.append(sds[i][j])
        examples.append(example)
    attributes = []
    for i in range(0,len(example)):
        attributes.append(i)
    inputs = removeTarget(attributes, dataset.target)
    return DataSet.DataSet( examples, inputs, attributes, dataset.target, dataset.attrnames, dataset.values)#crates dataset for use


def divideDataSet(file, attrnames, target, values):
    #the dataset is divided into train (90%) and test (10%) and the two dataset objects are created
    trainsize = (file_len(file)*90)/100                     #90% train 10% test
    allExamples= list()
    for line in open(file).readlines():
        content = line.split(',')
        if file in datasetWithID:                           #only these datasets have the attribute id
            content.pop(0)                                    #remove the first element, I guess I would do tests on the attribute id
        content = [c.rstrip() for c in content]
        allExamples.append(content)
    train = random.sample(allExamples, trainsize)                  #take 90% of the examples in dataset for the train
    dsetC = list(allExamples)                                      #copy the list to work without modifying it
    trainC = list(train)                                    #copy the list to work without modifying it
    inCommon = [val for val in dsetC if val in trainC]      #find common elements
    for i in range(len(inCommon)):                          #remove elements in common from both
        dsetC.remove(inCommon[i])
        if inCommon[i] in trainC:
            trainC.remove(inCommon[i])
    test = dsetC + trainC                                   #join to get exactly the remaining 10% of the examples for the test
    #creates dataset structure for the Train
    examples = []
    for i in range(len(train)):
        example = []
        for j in range(len(train[0])):
            example.append(train[i][j])
        examples.append(example)
    attributes = []
    for i in range(0, len(example)):
        attributes.append(i)
    inputs = removeTarget(attributes, target)
    DataTrain= DataSet.DataSet( examples, inputs, attributes, target, attrnames, values)#crates dataset for use
    #creates dataset structure for the Test
    examples = []
    for i in range(len(test)):
        example = []
        for j in range(len(test[0])):
            example.append(test[i][j])
        examples.append(example)
    attributes = []
    for i in range(0, len(example)):
        attributes.append(i)
    inputs = removeTarget(attributes, target)
    DataTest= DataSet.DataSet( examples, inputs, attributes, target, attrnames, values)#crates dataset for use

    return DataTest, DataTrain

#used in divideDataSet function
def file_len(fname):                #returns number of lines in the file
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
