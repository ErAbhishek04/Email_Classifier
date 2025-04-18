

# 📧 Email Classification and PII Masking API

This project is a FastAPI-based web service that classifies incoming emails into predefined categories and masks any Personally Identifiable Information (PII) such as names, emails, phone numbers, Aadhar numbers, and credit card details.

---

## 🧠 Project Features

- 🔐 Masks PII from email content using regex-based patterns.
- 🧾 Classifies the masked email using a machine learning model (Linear SVM with TF-IDF).
- 🌐 Provides an API endpoint to send email text and receive a structured response.
- 🧪 Includes test functionality for local development.

---

## 📁 File Structure & Purpose

| File/Folder             | Description |
|-------------------------|-------------|
| `app.py`                | Main logic that processes input email: masks PII, predicts category, and returns a structured JSON. |
| `models.py`             | Contains code to train, load, and use a text classification model (SVM + TF-IDF). |
| `utils.py`              | Contains regex logic for identifying and masking PII from input text. |
| `api.py`                | FastAPI application defining API endpoints and request/response logic. |
| `requirements.txt`      | All Python dependencies to be installed in the environment. |
| `Dockerfile`            | Containerizes the application for deployment. |
| `data/`                 | Folder containing the training CSV file. |
| `model.pkl`             | Trained classification model (generated after training). |

---

## 🛠️ Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 🔹 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running Locally

### 🔸 Step 1: Train the Classification Model

Before starting the API, you need to train and save the model. This will generate `model.pkl`.

```bash
python models.py
```

This uses the training dataset in `data/combined_emails_with_natural_pii.csv`.

### 🔸 Step 2: Run the FastAPI Server

Start the API server using the `api.py` file:

```bash
python api.py
```

You should see output like:

```
Uvicorn running on http://0.0.0.0:8000
```

---

## 📫 API Usage

### ✅ Health Check

**GET** request to:

```
http://localhost:8000/
```

Response:
```json
{
  "Confirm": "The API is up and Running"
}
```

---

### 📩 Classify Email Endpoint

**POST** request to:

```
http://localhost:8000/classify_email
```

#### Request Body:

```json
{
  "email_text": "Hi, my name is Aman Sharma. My email is aman@example.com and my card is 1234-5678-9876-5432."
}
```

#### Response:

```json
{
  "message": "Request processed successfully ✅",
  "data": {
    "input_email_body": "...",
    "list_of_masked_entities": [...],
    "masked_email": "...",
    "category_of_the_email": "billing"
  }
}
```

---

## 🐳 Docker (Optional)

To build and run the app using Docker:

```bash
# Build the image
docker build -t email-api .

# Run the container
docker run -p 7860:7860 email-api
```

Access API at: `http://localhost:7860`

---

## 🧪 Test Code Locally

You can test masking and classification locally by running:

```bash
python app.py
```

This will print the masked output and predicted category for a sample email.

---

## 📌 Requirements

- Python 3.9+
- FastAPI
- Scikit-learn
- Uvicorn
- Pandas
- Joblib
- Pydantic

All dependencies are listed in `requirements.txt`.

---

## 📖 Summary

| Task | Command |
|------|---------|
| Train Model | `python models.py` |
| Run API | `python api.py` |
| Test Locally | `python app.py` |
| Use API | `POST /classify_email` at `http://localhost:8000` |

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



