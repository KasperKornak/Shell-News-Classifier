## Table of contents

1. [Introduction](https://github.com/KasperKornak/Shell-News-Classifier#introduction)
2. [How to run the classifier?](https://github.com/KasperKornak/Shell-News-Classifier#how-to-run-the-classifier)
3. [How I did it?](https://github.com/KasperKornak/Shell-News-Classifier#how-i-did-it)
4. [Troubleshooting](https://github.com/KasperKornak/Shell-News-Classifier#troubleshooting)

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
1. You need to have `news_classifier.py`, `cleaned.csv` and `first_try.joblib` in the same directory to run the code.

2. Head to [NewsAPI](https://newsapi.org) website, sign-up and get an API key. You will need it to scrape news from the web.

3. Run the code by typing `python3 news_classifier.py` in the terminal. Be sure to have all the modules needed installed!

4. After running it, you will be asked to provide an API key. Just paste it and hit enter:

<p align="center">
  <img width="539" alt="Zrzut ekranu 2022-07-17 o 16 13 31" src="https://user-images.githubusercontent.com/80947256/179402472-f1f61280-4cc3-44db-a5ad-317e105fb756.png">
</p>

5. After that, the file `articles.txt` will be created. It stores all positively classified articles and URLs. Now, the program will ask you whether you would like to train the model or not:

<p align="center">
  <img width="297" alt="Zrzut ekranu 2022-07-17 o 16 16 27" src="https://user-images.githubusercontent.com/80947256/179402574-08d99d23-c94c-4d45-a9bb-5304870a8af8.png">
</p>

6. If you select to train the model, the program will ask you to label the data: 'y' for correctly classified entries, 'n' for badly classified ones. You may add your own articles headlines in the `articles.txt` file. If you wish to do so, you must do it before the program asks you if you want to train the model. Here is an example of how to label articles correctly:

<p align="center">
  <img width="481" alt="Zrzut ekranu 2022-07-17 o 16 21 56" src="https://user-images.githubusercontent.com/80947256/179402784-37718af2-ccea-46c1-b80e-a26771646015.png">
</p>

As you can see, you don't need to add any quotation marks, apostrophes or spaces. Just one, continuous, long string 😀. Please watch out for any typos, as model won't be able to recognize any other values than 'y' and 'n'.

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

### The (first) training
At this point I had to select the best possible classifier for the purpose of the project. After some tests, the best performing one was Logistic Regression Classifier pipelined with `CountVectorizer` and `TfidfTransformer` all from sklearn module. I split the dataset, created a before-mentioned pipeline and achieved an accuracy of about **83%**. Lastly, I exported the trained model into .joblib file.
TFIDF and SVM are baselines that I wanted to start with, since I know them well. 

### Main script
To run the program in a loop, I had to define three functions: *basic_ops(apis)*, *data_preparation()* and *model_training()*:

- *basic_ops(apis )* gets the NewsAPI key, sends the query, classifies the articles and writes them down to `articles.txt`. It's just a slightly changed version of the first `news_classifier.py` code.
- *data_preparation()* opens the `articles.txt` file, gets all the titles, cleans them (makes characters lowercase, uses regex to clean unnecessary parts of the headlines, etc.), gets the labels for classified headlines and appends them to exsisting `cleaned.csv` file. `cleaned.csv` is crucial as it enables model to learn more.
- *model_training()* is basically 1:1 copy of training.py - it uses same pipeline to train the model.

The last thing to write was a loop which you can see on a flowchart [here](https://github.com/KasperKornak/Shell-News-Classifier/blob/main/Shell_news_classifier_flowchart.png)

So, to sum up, what happens in this code is:

0. Program checks if you have `articles.txt` in a working directory. If yes, program deletes it.
1. You get the news headlines from the web via News API.
2. Using pretrained model, you classify which headlines are good, which ones are not. Then, they are exported to the `articles.txt` file.
3. If you decide to train the model, the program will clean and prepare the data from `articles.txt` and append it to the `cleaned.csv`, which is the dataset used to train the first model.
4. The program will train the model based on the updated dataset and overwrite the exsisting model with the newly trained one.


## Troubleshooting
After running the program for the first time, you may encounter this error:

> File "pandas/_libs/parsers.pyx", line 801, in pandas._libs.parsers.TextReader.read_low_memory                                                             
> File "pandas/_libs/parsers.pyx", line 857, in pandas._libs.parsers.TextReader._read_rows                                                                  
> File "pandas/_libs/parsers.pyx", line 843, in pandas._libs.parsers.TextReader._tokenize_rows                                                                
> File "pandas/_libs/parsers.pyx", line 1925, in pandas._libs.parsers.raise_parser_error
pandas.errors.ParserError: Error tokenizing data. C error: Expected 2 fields in line 4321, saw 3

The problem lies in `cleaned.csv` file, which sometimes, while appending labeled headlines, doesn't append the label and headline in the new line:

<p align="center">
  <img width="1138" alt="Zrzut ekranu 2022-07-19 o 18 36 46" src="https://user-images.githubusercontent.com/80947256/179806188-97cf9b37-7156-4ef1-b214-05471e5a8168.png">
</p>

To fix it, just hit enter before the label, so that it will be counted as a full entry. Look for an exact line in which this bug happens. It is written in error message. After the removal, the program should be running smoothly. If you have more issues, please open a new issue [here](https://github.com/KasperKornak/Shell-News-Classifier/issues).
