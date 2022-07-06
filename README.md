## Table of contents

1. [Introduction](https://github.com/KasperKornak/Shell-News-Classifier/edit/main/README.md#introduction)
2. [How to run the classifier?](https://github.com/KasperKornak/Shell-News-Classifier/edit/main/README.md#how-to-run-the-classifier)
3. [How I did it?](https://github.com/KasperKornak/Shell-News-Classifier/edit/main/README.md#how-i-did-it)
4. [Future](https://github.com/KasperKornak/Shell-News-Classifier/edit/main/README.md#future)

## Introduction
I don't know about you, but I love dividend stocks. One of my holdings is Shell plc. Since I don't have much time, I use [investing.com](investing.com) as a primary resource for news regarding companies that I own. But there is a problem:

<p align="center">
  <img width="676" alt="SHEL news as of 28 06 2022" src="https://user-images.githubusercontent.com/80947256/177621284-f520ba05-96ec-491c-ad8e-150c5fa4fff8.png">
</p>

I'm writing this on sixth of July 2022. As you can see, the news aren't updated frequently. Okay, but can't you look at the news on Google News? Yeah, about that:

<p align="center">
  <img width="764" alt="Zrzut ekranu 2022-07-6 o 20 52 27" src="https://user-images.githubusercontent.com/80947256/177622180-d2dc8d27-4828-4b2d-ad76-9d81c8c64489.png">
</p>

It's inconsistent. Yes, the top news are usually spot on, but the rest of the articles are ones that I don't care about. So, to overcome this problem, I made simple logistic regression classifier. In next part, I will show you how to run it and for the curious ones - I'll go through the whole process in the third paragraph.

## How to run the classifier?
First things first: you will need `news_classifier.py` and `first_try.joblib` in the same folder to run the program. After classifing articles, it will return the titles and URLs in `articles.txt` file that will appear in the same folder as `news_classifier.py`.
1. Get the News API key at [News API](https://newsapi.org) website and register, you will need it.

2. Insert the API key into the `news_classifier.py` code:
<p align="center">
  <img width="581" alt="Zrzut ekranu 2022-07-6 o 21 17 49" src="https://user-images.githubusercontent.com/80947256/177626283-7ffd6346-05de-40e4-869c-1cdbfb82ae88.png">
</p>

3. That's it! Run it and you will get the filtered results!😄
Please note that each time you run the code, the articles will be appended to exsisting ones. To avoid that, delete `articles.txt` after you finished using them.

## How I did it?
### The articles
To get the articles I used *pygooglenews*. Most of the modules that I used, needed either paid APIs or weren't as easily configurable as *pygooglenews*. *pygooglenews* has a limit of 100 articles per query. To overcome that, I made a list of over 100 queries (you can see all of them in `googlenews.py`) and appended all of them in one .csv file *UnlabeledDataset.csv*. This way, I could get over ten thousand articles headlines, here is how it looked at first:

![Zrzut ekranu 2022-07-6 o 21 38 17](https://user-images.githubusercontent.com/80947256/177629493-f7f29c1a-ae8c-4906-bbd4-04baa3ba24f1.png)

As you probably noticed, this file lacked column names and it was quite messy. The next step was to delete URLs column, delete duplicates, make all words lowercase and add new column for labeling. I had to label each entry manually, so it took me some time. After that the transformed dataset looked like that:

![Zrzut ekranu 2022-07-6 o 21 42 58](https://user-images.githubusercontent.com/80947256/177630230-9fcd2bc5-360f-48e9-a382-661eb6b8996e.png)

The way that `pygooglenews` works is that after the title of the articles it adds the website that it was scraped from. So, I had to get rid of it. I used this regex `\-.*` to do that. The final step was to clear the dataset out of an unusal and special characters and characters that interrputed during reading of .csv file. Here's the the look at the final datset, after labeling:

<p align="center">
  <img width="581" alt="Zrzut ekranu 2022-07-6 o 21 17 49" src="https://user-images.githubusercontent.com/80947256/177633084-8b742dd4-5cc9-4202-92b9-dbce947bcae2.png">
</p>

### The training
At this point I had to select the best possible classifier for the purpose of the project. After some tests, the best performing one was Logistic Regression Classifier pipelined with `CountVectorizer` and `TfidfTransformer` all from sklearn module. I split the dataset, created a before-mentioned pipeline and achieved an accuracy of about **83%**. Lastly, I exported the trained model into .joblib file.
TFIDF and SVM are baselines that I wanted to start with, since I know them well. In the future updates, I may switch to another tokenization and classification techniques.

### Main script
In `news_classifier.py`, I decided to use News API, since it covers more than just Google News. Again, the code is simple: send a query to News API, get the response, import titles and URLs to lists, use titles and trained model to classify the articles, then if the label of article is "y", export it and URL to `articles.txt` file.

## Future
My main goal is to create a program that will be able to improve itself based on the responses from the user. Secondly, I would like to explore improving used classification techniques. Thirdly, I would like to solve articles.txt problem (deleting the file everytime you finish using it).

Thank you.

