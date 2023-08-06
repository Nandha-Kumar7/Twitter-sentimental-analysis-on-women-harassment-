import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import joblib

 # Set variables for the search query and date range
search_terms = "#WORDS RELATED TO WOMAN HARRASSMENT# lang:en"
start_date = "2022-01-01"
end_date = "2022-12-31"

        # Define a list to hold the tweets
tweets_list = []

        # Use snscrape to search for tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_terms} since:{start_date} until:{end_date}').get_items()):
            tweets_list.append([tweet.date, tweet.id, tweet.rawContent])

            # Print a message every 1000 tweets scraped
            if i == 1000 and i > 0:
                print(f"{i} tweets scraped.")
                break

        # Convert the tweets list to a DataFrame and save to CSV
df = pd.DataFrame(tweets_list, columns=["date", "id", "text"])
df.to_csv("data.csv", index=False)

def preprocess_tweet(tweet):
            # Remove URLs
            tweet = re.sub(r"http\S+", "", tweet)
            # Remove user mentions
            tweet = re.sub(r"@\S+", "", tweet)
            # Remove hashtags
            tweet = re.sub(r"#\S+", "", tweet)
            # Remove special characters and digits
            tweet = re.sub(r"[^a-zA-Z]", " ", tweet)
            # Convert to lowercase
            tweet = tweet.lower()
            # Tokenize the tweet
            tokens = word_tokenize(tweet)
            # Remove stopwords
            stop_words = set(stopwords.words("english"))
            filtered_tokens = [token for token in tokens if token not in stop_words]
            # Join the tokens back into a string
            processed_tweet = " ".join(filtered_tokens)
            return processed_tweet
        # Load the CSV and preprocess the text
df = pd.read_csv("data.csv")
df["text"] = df["text"].apply(preprocess_tweet)
df.to_csv("data_cleaned.csv", index=False)


df = pd.read_csv("women_harassment_words.csv")
# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df["Words"], df.index, test_size=0.2, random_state=42)

# Convert y_train and y_test to binary labels
y_train_bin = pd.Series(y_train).apply(lambda x: 0 if x < len(y_train)/2 else 1)
y_test_bin = pd.Series(y_test).apply(lambda x: 0 if x < len(y_test)/2 else 1)

# Vectorize the text data
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(stop_words="english")
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# Train and evaluate BinomialLR model
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(solver="liblinear")
lr.fit(X_train_counts, y_train_bin)


# Train and evaluate MultinomialNB model
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_counts, y_train_bin)


# Train and evaluate MultinomialLR model
lr = LogisticRegression(multi_class="multinomial", solver="lbfgs")
lr.fit(X_train_counts, y_train_bin)


# Train and evaluate SVM classifier
from sklearn.svm import LinearSVC
svm = LinearSVC()
svm.fit(X_train_counts, y_train_bin)


# Train and evaluate Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train_counts, y_train_bin)


# Train and evaluate Random Forest Classifier
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train_counts, y_train_bin)


# Train and evaluate Extra Trees Classifier
from sklearn.ensemble import ExtraTreesClassifier
etc = ExtraTreesClassifier()
etc.fit(X_train_counts, y_train_bin)



# Train and evaluate XG Boost Classifier
import xgboost as xgb
xgb = xgb.XGBClassifier()
xgb.fit(X_train_counts, y_train_bin)


# Save the vectorizer
joblib.dump(vectorizer, "vectorizer.joblib")

# Save the models
joblib.dump(lr, "lr.joblib")
joblib.dump(nb, "nb.joblib")
joblib.dump(svm, "svm.joblib")
joblib.dump(dtc, "dtc.joblib")
joblib.dump(rfc, "rfc.joblib")
joblib.dump(etc, "etc.joblib")
joblib.dump(xgb, "xgb.joblib")