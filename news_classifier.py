from newsapi import NewsApiClient
import joblib

#insert your News API keys here, also model is being loaded
loaded_model = joblib.load('first_try.joblib')
api = NewsApiClient(api_key = '')

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
        with open('articles.txt', 'a') as the_file:
            the_file.writelines('\n')
            the_file.write(i[0])
            the_file.writelines('\n')
            the_file.write(i[2])
    else:
        continue