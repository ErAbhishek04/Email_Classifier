Email Classifier with PII Masking
 
1       Overview
This project is a machine learning-based email classification system with PII (Personally Identifiable Information) masking. It classifies emails into various categories and ensures user privacy by masking sensitive information. The project is developed using traditional ML techniques and deployed as a RESTful API using FastAPI, hosted on Hugging Face Spaces.
________________________________________
2      Features
●	Email Classification: Classifies emails into predefined categories such as Work, Personal, Spam, etc.
●	PII Masking: Automatically detects and masks sensitive information like phone numbers, email addresses, and names.
●	FastAPI-based API: Clean and lightweight REST API interface for submitting emails and getting back results.
●	Hosted on Hugging Face Spaces: Easily accessible via a public URL.
________________________________________
3      Tech Stack
●	Language: Python
●	Libraries:
○	scikit-learn: Vectorization and traditional ML classification
○	re: Regular expressions for PII detection
○	FastAPI: API framework
○	Uvicorn: ASGI server for FastAPI
●	Deployment: Hugging Face Spaces using Docker or native Python environment
________________________________________



4      Project Structure
Email_Classifier/
├─
│   ├── api.py              # FastAPI app
│   ├── model.py          # ML model loading and classification
│   ├── app.py              # functionality checker
│   └── utils.py             # Preprocessing and helpers
├── data/
│   └── combined_emails_with_natural_pii.csv       	# Sample dataset
│    | model.pkl    # Pickled classifier
├── requirements.txt     	# Dependencies
├── Dockerfile           	# (Optional) For containerization
├── README.md            	# Project summary
└── Email_Classifier_with_PII_Masking_report.md            	# This report
________________________________________
5      Machine Learning Approach
●	Vectorization: Used TfidfVectorizer to convert email text to feature vectors.
●	Model: A lightweight traditional ML classifier (e.g., Multinomial Naive Bayes or Logistic Regression) trained on labeled email data.
●	Evaluation: Accuracy, precision, recall, and F1-score used for evaluation on a held-out validation set.
________________________________________
6      PII Masking
PII masking is done using regular expressions:
●	Email addresses: masked as [EMAIL]
●	Phone numbers: masked as [PHONE]
●	Names (if extracted from patterns or datasets): masked as [NAME]
 
 
Example:
Original: Hello John, contact me at john@example.com or 9876543210.
Masked:   Hello [NAME], contact me at [EMAIL] or [PHONE].
________________________________________
 
 
7       API Endpoint
●	POST /classify_email/
 
 
8      Request (JSON):
{
  "email_text": "Hello, this is a reminder for your meeting with HR."
}
 
9      Response:
{
  "masked_email": "Hello, this is a reminder for your meeting with [NAME].",
  "category": "Work"
}
________________________________________
 
10   Evaluation Criteria Mapping
Criterion	Addressed In Project
API Deployment	Yes, via Hugging Face Spaces with FastAPI
Code Quality (PEP8)	Follows standard structure and naming
Proper File Structuring	Modularized by purpose
Hidden Test Case Handling	Handles unexpected input formats
Detailed Report	Included in REPORT.md
________________________________________
 
 
 
Model Selection and Justification
 
For this email classification project, we employed a TF-IDF vectorizer combined with a Linear Support Vector Classifier (LinearSVC) within a Scikit-learn pipeline. The primary objective of the model is to accurately classify emails into predefined categories (e.g., Work, Personal, Spam, etc.) using traditional machine learning techniques. This section outlines the rationale behind the model choices, their implementation, and expected performance.
 
11   Feature Extraction: TF-IDF Vectorization
12  What is TF-IDF?
TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents (corpus). The core idea is:
●	TF (Term Frequency): Measures how frequently a word appears in a document.
●	IDF (Inverse Document Frequency): Diminishes the weight of terms that occur very frequently across documents (like "the", "is") and increases the weight of terms that are rare.
 
13  Why TF-IDF?
●	Lightweight and computationally efficient
●	Removes bias from high-frequency but non-informative words
●	Works well with linear classifiers
●	Does not require word embeddings or external models
 
14  Classifier: Linear Support Vector Classifier (LinearSVC)
15  What is LinearSVC?
LinearSVC is a linear classifier based on the Support Vector Machine (SVM) algorithm. It is suitable for high-dimensional datasets like those generated from TF-IDF matrices.
16  Why LinearSVC?
1.	High Dimensional Efficiency: Text datasets often have thousands of features (one per word). LinearSVC handles these well due to its underlying optimization method (liblinear).
2.	Regularization: Automatically applies L2 regularization, which helps reduce overfitting.
3.	Interpretability: Coefficients can be inspected to understand which words are influential for each class.
4.	Speed: Faster than kernel-based SVMs and performs well on sparse datasets.
5.	Robust Baseline: Widely adopted for NLP tasks, especially as a baseline for text classification problems.
 
 
 
 
 
 

17   How to Run Locally
 
# Clone the repository
git clone https://github.com/ErAbhishek04/Email_Classifier.git
cd Email_Classifier
 
# Install dependencies
pip install -r requirements.txt
 
# Start the API
uvicorn app.main:app --reload
________________________________________
18   Future Improvements
●	Incorporate named entity recognition (NER) for more robust PII detection
●	Enhance classification with deep learning or fine-tuned transformers
●	Add user authentication for secured usage
●	Improve front-end or build a UI wrapper around the API
________________________________________
19   Links
●	GitHub:  https://github.com/ErAbhishek04/Email_Classifier
●	Live API: https://huggingface.co/spaces/Abhi0420/filing
 

