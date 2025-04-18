# This script trains a text classification model to categorize emails based on their content.
# It uses TF-IDF with a LinearSVC pipeline, evaluates the model, saves it, and provides functions to load and predict.
# A sample prediction is demonstrated in the __main__ block for quick testing.





import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

def train_and_save_model(data_path="data/combined_emails_with_natural_pii.csv", model_path="model.pkl"):
    # Load the dataset containing emails and their corresponding categories

    df = pd.read_csv(data_path)

    X = df["email"]
    y = df["type"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build a pipeline with TF-IDF vectorizer and Linear SVM classifier

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LinearSVC())
    ])

    pipeline.fit(X_train, y_train)
    
    if len(X_test) > 0:
        predictions = pipeline.predict(X_test)
        print("Classification Report:\n", classification_report(y_test, predictions))

    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")
    return pipeline


# Load a saved model from disk
def load_model(model_path="model.pkl"):
    return joblib.load(model_path)

# Predict the category of a given email using the trained model
def predict_category(email_text, model):
    return model.predict([email_text])[0]

if __name__ == "__main__":
    model = train_and_save_model()
    test_email = "Hi team, I need help with a payment issue on my last invoice."
    print("Predicted category:", predict_category(test_email, model))
