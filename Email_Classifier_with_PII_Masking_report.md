
# Email Classifier with PII Masking

## 1. Overview

This project is a machine learning-based email classification system with PII (Personally Identifiable Information) masking. It classifies emails into various categories and ensures user privacy by masking sensitive information. The project is developed using traditional ML techniques and deployed as a RESTful API using FastAPI, hosted on Hugging Face Spaces.

---

## 2. Features

- **Email Classification**: Classifies emails into predefined categories such as Work, Personal, Spam, etc.  
- **PII Masking**: Automatically detects and masks sensitive information like phone numbers, email addresses, and names.  
- **FastAPI-based API**: Clean and lightweight REST API interface for submitting emails and getting back results.  
- **Hosted on Hugging Face Spaces**: Easily accessible via a public URL.  

---

## 3. Tech Stack

- **Language**: Python  
- **Libraries**:  
  - `scikit-learn`: Vectorization and traditional ML classification  
  - `re`: Regular expressions for PII detection  
  - `FastAPI`: API framework  
  - `Uvicorn`: ASGI server for FastAPI  
- **Deployment**: Hugging Face Spaces using Docker or native Python environment  

---

## 4. Project Structure

```
Email_Classifier/
├── api.py                         # FastAPI app
├── model.py                       # ML model loading and classification
├── app.py                         # Functionality checker
├── utils.py                       # Preprocessing and helpers
├── data/
│   └── combined_emails_with_natural_pii.csv   # Sample dataset
│   └── model.pkl                              # Pickled classifier
├── requirements.txt              # Dependencies
├── Dockerfile                    # (Optional) For containerization
├── README.md                     # Project summary
└── Email_Classifier_with_PII_Masking_report.md # This report
```

---

## 5. Machine Learning Approach

- **Vectorization**: Used `TfidfVectorizer` to convert email text to feature vectors.  
- **Model**: A lightweight traditional ML classifier (e.g., `LinearSVC`) trained on labeled email data.  
- **Evaluation**: Accuracy, precision, recall, and F1-score used for evaluation on a held-out validation set.  

---

## 6. PII Masking

PII masking is done using regular expressions:

- **Email addresses**: masked as `[EMAIL]`  
- **Phone numbers**: masked as `[PHONE]`  
- **Names** (if extracted from patterns or datasets): masked as `[NAME]`  

**Example:**

- Original: `Hello John, contact me at john@example.com or 9876543210.`  
- Masked: `Hello [NAME], contact me at [EMAIL] or [PHONE].`

---

## 7. API Endpoint

### `POST /classify_email/`

---

## 8. Request (JSON):

```json
{
  "email_text": "Hello, this is a reminder for your meeting with HR."
}
```

---

## 9. Response:

```json
{
  "masked_email": "Hello, this is a reminder for your meeting with [NAME].",
  "category": "Work"
}
```

---

## 10. Evaluation Criteria Mapping

| Criterion              | Addressed In Project                         |
|------------------------|---------------------------------------------|
| API Deployment         | Yes, via Hugging Face Spaces with FastAPI   |
| Code Quality (PEP8)    | Follows standard structure and naming       |
| Proper File Structuring| Modularized by purpose                      |
| Hidden Test Case Handling | Handles unexpected input formats         |
| Detailed Report        | Included in REPORT.md                       |

---

## 11. Model Selection and Justification

We employed a **TF-IDF vectorizer** combined with a **Linear Support Vector Classifier (LinearSVC)**. The primary objective is to accurately classify emails into categories (e.g., Work, Personal, Spam) using traditional ML.

---

### 12. Feature Extraction: TF-IDF Vectorization

**TF-IDF** (Term Frequency-Inverse Document Frequency) measures word importance in a document relative to a corpus.

- **TF**: Frequency of a term in the document  
- **IDF**: Reduces weight of commonly used words

#### Benefits:

- Lightweight and efficient  
- Removes noise from high-frequency words  
- Suitable for sparse datasets  
- No external embedding required  

---

### 13. Classifier: Linear Support Vector Classifier (LinearSVC)

**LinearSVC** is chosen for:

1. **Efficiency** in high-dimensional spaces  
2. **L2 regularization** for overfitting control  
3. **Interpretability** through model coefficients  
4. **Speed** over kernel SVMs  
5. **Baseline robustness** in NLP tasks  

---

## 14. How to Run Locally

```bash
# Clone the repository
git clone https://github.com/ErAbhishek04/Email_Classifier.git
cd Email_Classifier

# Install dependencies
pip install -r requirements.txt

# Start the API
uvicorn app.main:app --reload
```

---

## 15. Future Improvements

- Add NER (Named Entity Recognition) for advanced PII detection  
- Replace LinearSVC with deep learning models (e.g., BERT)  
- Add authentication and logging for production use  
- Build a simple UI or front-end client  

---
# Run the API Uploaded on Cloud of HuggingFace with PowerShell

## Step 1: Create the JSON Data

First, define the email data that you want to classify. In this example, we're using a test email with some PII.

```powershell
$json = @{
    email_text = "Hi John, please send the contract to me at john.doe@example.com. My phone is 9876543210."
} | ConvertTo-Json
```

## Step 2: Create the JSON Data
```powershell
$response = Invoke-RestMethod -Uri "https://Abhi0420-filing.hf.space/classify_email" `
                              -Method Post `
                              -Body $json `
                              -ContentType "application/json"
```

## Step-III : Enter the command

```powershell

$response | ConvertTo-Json -Depth 5

```


## 16. Links

- **GitHub**: [https://github.com/ErAbhishek04/Email_Classifier](https://github.com/ErAbhishek04/Email_Classifier)  
- **Live API**: [https://huggingface.co/spaces/Abhi0420/filing](https://huggingface.co/spaces/Abhi0420/filing)
