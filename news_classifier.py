import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import joblib
from newsapi import NewsApiClient
import os
apis = ''
i = 0
j = 0
k = 0

def basic_ops(apis):
    os.remove('articles.txt')
    #insert your News API keys here, also model is being loaded
    loaded_model = joblib.load('first_try.joblib')
    api = NewsApiClient(api_key = apis)

    #sending request to API
    news = api.get_everything(q='Shell plc')
    X_predict = []
    urls = []
    news_to_use = news['articles']

    #splitting and putting titles and urls to lists
    for new in news_to_use:
        X_predict.append(new['title'])
        urls.append(new['url'])

    #using model to classify labels and zipping labels with urls and titles
    labels = loaded_model.predict(X_predict)
    to_file = list(zip(X_predict, labels,urls))

    #writing positively classified articles to .txt
    for i in to_file:
        if i[1] == 'y':
            with open('articles.txt', 'a',encoding="utf-8") as the_file:
                the_file.writelines('\n')
                the_file.write(i[0])
                the_file.writelines('\n')
                the_file.write(i[2])
        else:
            continue

def data_preparation():
    with open('articles.txt') as file:
        lines = file.readlines()
    all_lines = lines[1:]
    all_titles = []
    i = 0
    for line in all_lines:
        if i % 2 == 0:
            all_titles.append(line)
            i += 1
        else:
            i += 1
            continue

    re_titles = []
    for tit in all_titles:
        text = tit.lower().rstrip()
        re_titles.append(re.sub('\-.*','',text))

    print('Enter a string of labels. Labels to enter: ', len(re_titles))
    labels = input()
    zipped_package = zip(labels, re_titles)
    csvf = pd.DataFrame(list(zipped_package))
    print(csvf)
    csvf.to_csv('cleaned.csv', mode='a', index=False, header=False, sep=';')

def model_training():
    set = pd.read_csv('cleaned.csv', sep=';')

    X = set["title"]
    y = set["isgood"]
    names = ['y', 'n']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', MultinomialNB()),
                         ])

    text_clf = text_clf.fit(X_train, y_train)
    predicted1 = text_clf.predict(X_test)

    metrics.accuracy_score(y_test, predicted1)
    print(metrics.classification_report(y_test, predicted1, target_names=sorted(names)))

    filename = "first_try.joblib"
    joblib.dump(text_clf, filename)

while i < 1:
    print('Hello! Welcome to Shell News Classifier!')
    while j < 1:
        print('Please, enter your NewsAPI key here: ')
        apis = input()
        if len(apis) != 32:
            print('You have entered a wrong key! [T]ry again or press any other key to exit.')
            key = input()
            if (key == 'T') or (key == 't'):
                continue
            else:
                exit(0)
        else:
            basic_ops(apis)
            while k < 1:
                print('Do you wish to teach the model? y/n')
                answer = input()
                if answer == 'n':
                    exit(0)
                if answer == 'y':
                    data_preparation()
                    model_training()
                    k += 1
            print('Model trained successfully!')
            j += 1
            i += 1




