import snscrape.modules.twitter as sntwitter
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
import xgboost
from sklearn.metrics import accuracy_score
import joblib
import csv

filename = '#LOCATION OF THE FILE'

# Open the CSV file in read mode
with open(filename, 'r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Read the data from the CSV file and store it in a list
    tweets_list = list(csv_reader)


# Preprocess the tweets
cleaned_tweet = [tweet['Cleaned Tweet'] for tweet in tweets_list]
# Load the pre-trained vectorizer
vectorizer = joblib.load('vectorizer.joblib')

# Vectorize the tweets
X = vectorizer.transform(cleaned_tweet)

# Load the pre-trained classifiers
lr = joblib.load("lr.joblib")
nb = joblib.load("nb.joblib")
svm = joblib.load("svm.joblib")
dtc = joblib.load("dtc.joblib")
rfc = joblib.load("rfc.joblib")
etc = joblib.load("etc.joblib")
xgb = joblib.load("xgb.joblib")

# Predict the sentiment of the tweets using each classifier
lr_pred = lr.predict(X)
nb_pred = nb.predict(X)
svm_pred = svm.predict(X)
dtc_pred = dtc.predict(X)
rfc_pred = rfc.predict(X)
etc_pred = etc.predict(X)
xgb_pred = xgb.predict(X)

#1 -> Abusive content
#0 -> No abusive content

# Combine the predictions into a single DataFrame
predictions_df = pd.DataFrame({
    "Date": [tweet['Date'] for tweet in tweets_list],
    "ID": [tweet['ID'] for tweet in tweets_list],
    "Content": [tweet['Content'] for tweet in tweets_list],
    "Cleaned Tweet": cleaned_tweet,
    "Logistic regression":lr_pred,
    "Naive Bayes": nb_pred,
    "Support Vector Machine": svm_pred,
    "Decision Tree": dtc_pred,
    "Random Forest": rfc_pred,
    "Extra Trees": etc_pred,
     "XG Boost": xgb_pred 
     })

predictions_df.to_csv("PREDICTIONS.csv", index=False)

