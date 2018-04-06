Per ottenere i risultati eseguire il modulo RandomForest.py, nel seguente modo:

1) [opzionale] In RandomForest.py, alla ultima riga di codice, impostare il numero di alberi per l'implementazione della foresta, passandolo come paramentro della funzione.

2) Eseguire il modulo RandomForest.py: interagire con la console per selezionare il dataset che si desidera testare selezionando il codice opportuno e premendo Invio.
   Dopodichè verranno stampati i risultati ottenuti.

---------------------------------------------------------------------------------------------------------------
Moduli presenti nel progetto:

°Dataset.py implementa una classe che crea oggetti di tipo dataset, per poterci lavorare più facilmente negli altri moduli.
°DecisionTree.py contiene le classi per l'albero decisionale e la foglia.
°DecisionTreeLearning.py contiene il codice per l'apprendimento di singoli alberi decisionali (la soluzione proposta è valida per 5 dataset a valori continui).
°Helper.py contiene funzioni usate negli altri moduli per creazione di train set, test set e uno script per randomizzare il train test per la creazione di alberi nella foresta.
°RandomForest.py contiene lo script per l'implementazione della foresta e la sua predizione sulla classificazione degli esempi forniti dal test set. Contiene anche del codice per interazione utente-console per la scelta del dataset da testare.
---------------------------------------------------------------------------------------------------------------
NOTA BENE:

Tempi di esecuzione (circa): [su computer dalle seguenti specifiche: Intel Core Duo 2.20GHz, RAM 4GB, 64 bit]


- ecoli dataset (7 inputs), foresta 50 alberi ---> 1:20 minuti

- breast cancer dataset (9 inputs), foresta 50 alberi ---> 0:20 minuti

- liver dataset (9 inputs), foresta 50 alberi ---> 0:30 minuti

- vehicle dataset (18 inputs), foresta 50 alberi ---> 18 minuti

- ionoshpere dataset (34 inputs), foresta 50 alberi ---> 19 minuti


E' possibile diminuire il tempo di esecuzione riducendo il numero di alberi nella foresta (vedi passo 1 sopra), perdendo un po' di affidabilità sulla predizione

----------------------------------------------------------------------------------------------------------------

Riferimenti:

L'implementazione dei singoli alberi di decisione ed il loro apprendimento, quindi i moduli DecisionTree.py e DecisionTreeLearning.py, sono state riprese dalla seguente repository pubblica:

https://github.com/aimacode/aima-python/blob/master/learning.py , facendo riferimento anche a Russell & Norvig 18.3.

Da tale repository è stato anche usato il codice per implementare il modulo DataSet.py

Alcune parti potrebbero essere state modificate per necessità, tutto al fine di implementare la Random Forest.