import pandas as pd
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

dataset = pd.read_csv('./Churn_Modelling.csv')
parameters = pd.read_csv('./hyperparameters.csv')

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

y = dataset['Exited']
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary']]

geo = dataset['Geography']
geo = pd.get_dummies(geo, drop_first=True)
gender = dataset['Gender']
gender = pd.get_dummies(gender, drop_first=True )
X = pd.concat([X,gender,geo], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = Sequential()
model.add(Dense(units=numberofneurons, input_dim=11, activation=activationfunction[0] ))

for _ in range(numberoflayers):
	model.add(Dense(units=numberofneurons, activation=activationfunction[0]))

model.add(Dense(units=1,  activation='sigmoid' ))
model.compile(optimizer=Adam(learning_rate=learningrate),loss='binary_crossentropy' )
model.fit(X_train,y_train , epochs=epoch , verbose=0)

# model.add(Dense(units=6, activation='relu'))
# model.add(Dense(units=6, activation='relu'))


model.save('model.h5')
