# Stock Sentiment Analysis using News Articles

## Idea
The idea is to analyze the image or screenshot of a news article and predict whether the stock price will go up or down.

## About the Web-App
Web-App is used to upload an image of the news article that needs to be analyzed. Then [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) is used to extract the text from the news article. The extracted text is used by an NLP model to predict whether the price will go up or down. The result gets displayed onto the screen.
 
## About the dataset used.
📌 The data set in consideration is a combination of the world news and stock price shifts available on Kaggle.

📌 The dataset contains news headlines ranging from 2000 to 2016.

📌 There are 25 columns of top news headlines for each day in the data frame.

📌 Class 1- the stock price increased.

📌 Class 0- the stock price stayed the same or decreased.

## About the approach.
📌 Used TF-IDF and Bag of Words for extracting features from the headlines.

📌 Used Random Forest Classifier, Multinational Naive Bayes, and Passive-Aggressive Classifier for analysis.

## Screenshots
<img alt="Home Page" src="images/Screenshot from 2020-09-21 16-21-48.png" align="left" height="350" width="347" ><br>
<img alt="Uploading Image" src="images/Screenshot from 2020-09-21 16-21-13.png" align="left" height="350" width="347" >
<img alt="Predicted result" src="images/Screenshot from 2020-09-21 16-21-04.png" align="left" height="350" width="347" ><br>
<img alt="Uploading Image" src="images/Screenshot from 2020-09-21 16-21-27.png" align="left" height="350" width="347" >
<img alt="Predicted Result" src="images/Screenshot from 2020-09-21 16-22-35.png" align="left" height="350" width="347" >
