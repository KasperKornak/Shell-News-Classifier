import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib

#importing cleaned dataset
dataset = pd.read_csv('cleaned.csv',sep=';')

#splitting the data
X=dataset["title"]
y=dataset["isgood"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=11)

#creating pipeline
model = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf2', LogisticRegression(solver='liblinear'))])

#training and evaluating model
model = model.fit(X_train, y_train)
prediction = model.predict(X_test)
print(metrics.accuracy_score(y_test, prediction))

#exporting model to file
filename = "first_try.joblib"
joblib.dump(model, filename)
