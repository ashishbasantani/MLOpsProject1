import pandas as pd

parameters = pd.read_csv('hyperparameters.csv')

epoch = (parameters['epochs'])
numberoflayers = (parameters['layers'])
numberofneurons = (parameters['neurons'])
activationfunction = (parameters['activationfunction'])
learningrate = (parameters['learningrate'])

epoch = int(epoch[0])
numberoflayers = int(numberoflayers[0])
numberofneurons = int(numberofneurons[0])
actiavationfunction = str(activationfunction[0])
learningrate = float(learningrate[0])

epoch = epoch + 5
numberoflayers = numberoflayers + 2
numberofneurons = numberofneurons + 3

parameters.to_csv('hyperparameters.csv')