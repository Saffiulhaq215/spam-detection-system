import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# 1. Load the data
# The file uses tabs (\t) instead of commas. We give the columns names.
df = pd.read_csv('notebooks/spam.csv', sep='\t', names=['label', 'message'])

# 2. Convert text labels to numbers
# Machine Learning models prefer numbers: 'spam' = 1, 'ham' = 0
df['label'] = df['label'].map({'spam': 1, 'ham': 0})

# 3. Split the data
# We use 80% to train the model and 20% to test if it actually works.
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], 
    df['label'], 
    test_size=0.2, 
    random_state=42
)

# 4. Turn text into math (Vectorization)
# TF-IDF calculates how important a word is to a document.
# 
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train the Model
# Naive Bayes is a classic, fast algorithm for text classification.
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# 6. Save the results
# We save both the model and the vectorizer to the 'models' folder.
# We need the vectorizer later to turn NEW messages into the same math format.
if not os.path.exists('models'):
    os.makedirs('models')

joblib.dump(model, 'models/spam_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Success: Model and Vectorizer saved in /models folder!")

