import DecisionTreeLearning
import Helper
from collections import Counter

def RandomForest(dataset, N=20): #N number of trees in the forest
    forest=[]
    test, train = Helper.divideDataSet(filesource, fileAttr, posClassification, fileClass)
    print '\nDataset in use: ',filesource
    print 'Dataset divided into Train (90%) and Test(10%)'
    print '\nCreating forest of', N, 'trees...'
    print 'Creating tree number:',
    for i in range(0,N):  #at each iteration I shuffle the train set, create the tree and join it to the forest
        shuffleTrain = Helper.shuffleDataTrain(train)
        tree = DecisionTreeLearning.DecisionTreeLearner(shuffleTrain)
        print i,',',
        forest.append(tree)
    print
    prediction(test, forest) #for each example of the dataset see every tree what it vote. Then take more popular for prediction

def prediction(test, forest):
    predictionOneTree=[]
    predictionForest=[]
    votes=[]
    trueClassification = []
    for i in range(len(forest)):        #for each tree in the forest see the classification of the test set example
        for example in test.examples:
            predictionOneTree.append(forest[i](example))
        predictionForest.append(predictionOneTree)             #result is a list of lists with the votes of each tree for all the examples. E.g. [[],[],[]...]
        predictionOneTree=[]
    for j in range(0, len(predictionForest[0])):
        temp=[]
        for i in range(0, len(predictionForest)):
            temp.append(predictionForest[i][j]) #list with votes of each of the trees for AN EXAMPLE dataset
        votes.append(temp)            #list of list with every votes of the trees for EACH EXAMPLES dataset
    most = mostVotes(votes)           #find the highest rated classification for each example
    print
    for e in test.examples:
        trueClassification.append(e[posClassification])
    print 'Data Test classification:'
    print trueClassification
    print 'Random Forest predicter classification:'
    print most
    print '\nTest set errors:',errorPerc(trueClassification, most),'%'

def mostVotes(votes):       #find the highest rated classification for each example
    #votes: contains lists of votes from all trees for each example
    vot=[]
    for v in votes:         #for each group of votes find the most common with function count
        most = count(v)
        vot.append(most)
    return vot

def count(array):
    cnt = Counter(array)
    a = cnt.most_common(1)
    return a[0][0]          #a[0][0] most frequent element, a[0][1] frequency

def errorPerc(true, predict):#calculates error
    err=0
    for i in range(len(true)):
        if true[i]!=predict[i]:
            err += 1
    if err == 0:
        return 0
    else:
        perc= (float(err)/len(true))*100
    return perc

#------------------------------------------------------------------------------------------------------------------
cod = input('Select dataset to test:\n'
            '1. Liver\n2. Ecoli\n3. Breast Cancer\n4. Vehicle\n5. Ionosphere\n--> type code here:')
if cod ==1:
    filesource = 'liver.txt'
    fileAttr = ['mcv', 'alkphos', 'sgpt', 'sgot', 'gammagt', 'drinks', 'Type']
    posClassification = 6
    fileClass = ['1','2'] #1:set1, 2:set2
    fileDataset = Helper.setForDataset(filesource, fileAttr, posClassification, fileClass)
elif cod==2:
    filesource = 'ecoli.txt'
    fileAttr = ['id',  'mcg',  'gvh', 'lip', 'chg',  'aah', 'alm1',  'alm2',  'class']
    posClassification = 7
    fileClass = ['cp','im','pp','imU','om','omL','imL','imS'] #cp  (cytoplasm), im  (inner membrane without signal sequence),
    #pp  (perisplasm), imU (inner membrane, uncleavable signal sequence), om  (outer membrane), omL (outer membrane lipoprotein)
    #imL (inner membrane lipoprotein), imS (inner membrane, cleavable signal sequence)
    fileDataset = Helper.setForDataset(filesource, fileAttr, posClassification, fileClass)
elif cod==3:
    filesource = 'breastCancer.txt'
    fileAttr = ['id',  'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion',
                'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']
    posClassification = 9
    fileClass = ['2','4'] #2:benign, 4:malignant
    fileDataset = Helper.setForDataset(filesource, fileAttr, posClassification, fileClass)
elif cod==4:
    filesource = 'vehicle.txt'
    fileAttr = ['COMPACTNESS', 'CIRCULARITY ',  'DISTANCE CIRCULARITY',  'RADIUS RATIO','PR.AXIS ASPECT RATIO',  'MAX.LENGTH ASPECT RATIO',
                'SCATTER RATIO', 'ELONGATEDNESS','PR.AXIS RECTANGULARITY', 'MAX.LENGTH RECTANGULARITY',  'SCALED VARIANCE ALONG MAJOR AXIS',
                'SCALED VARIANCE ALONG MINOR AXIS ',  'SCALED RADIUS OF GYRATION', 'SKEWNESS ABOUT MAJOR AXIS','SKEWNESS ABOUT MINOR AXIS',
                'KURTOSIS ABOUT MINOR AXIS ', 'KURTOSIS ABOUT MAJOR AXIS', 'HOLLOWS RATIO',  'CLASS']
    posClassification = 18
    fileClass = ['opel','saab','van','bus']
    fileDataset = Helper.setForDataset(filesource, fileAttr, posClassification, fileClass)
else:
    filesource = 'ionosphere.txt'
    fileAttr = [ 'antenna0', 'antenna1', 'antenna2',  'antenna3',  'antenna4',  'antenna5', 'antenna6', 'antenna7',  'antenna8', 'antenna9',
                 'antenna10',  'antenna11', 'antenna12',  'antenna13',  'antenna14',  'antenna15',  'antenna16', 'antenna17',  'antenna18',
                 'antenna19',  'antenna20',  'antenna21',  'antenna22', 'antenna23',  'antenna24',  'antenna25',  'antenna26', 'antenna27',
                 'antenna28', 'antenna29',  'antenna30',  'antenna31',  'antenna32',  'antenna33',  'class']
    posClassification = 34
    fileClass = ['g','b']#g:good, b:bad
    fileDataset = Helper.setForDataset(filesource, fileAttr, posClassification, fileClass)

#[optional] set the number of trees in the forest
RandomForest(fileDataset, 20)