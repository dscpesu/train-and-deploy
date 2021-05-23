from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report
#from sklearn.metrics import accuracy_score
import joblib
import numpy as np

iris = load_iris()
X=iris.data
y=iris.target
print(X)
X_train,X_test,y_train,y_test =  train_test_split(X,y,test_size=0.3,random_state=42)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)
joblib.dump(logreg, 'model.pkl')
#predictions=logreg.predict(X_test)
#print(classification_report(y_test, predictions) )
#print(accuracy_score(y_test, predictions))
#print(logreg.score(X_train,y_train))
#X_new = np.array([[1.0,2.0,3.0,4.0],[4.0,3.4,2.1,3.2]])
#print(logreg.predict(X_new))
columns= list(iris.feature_names)
joblib.dump(columns,'columns.pkl')




 
