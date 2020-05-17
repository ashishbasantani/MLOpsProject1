import pandas as pd
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model
from sklearn.metrics import accuracy_score

model = load_model('model.h5')

dataset = pd.read_csv('Churn_Modelling.csv')

y = dataset['Exited']
X = dataset[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary']]
geo = dataset['Geography']
geo = pd.get_dummies(geo, drop_first=True )
gender = dataset['Gender']
gender = pd.get_dummies(gender, drop_first=True )
X = pd.concat([X,gender,geo], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

pred = model.predict(X_test)
pred = pred.astype(float)
y_test = y_test.astype(float)
pred = pred.reshape(len(pred),1)
pred = pred.round(decimals = 0)


acc = accuracy_score(pred,y_test,normalize=True)

acc = acc * 100
acc = int(acc)

print(acc)