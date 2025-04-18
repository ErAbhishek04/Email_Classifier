# This FastAPI app exposes endpoints to classify emails and mask PII from the input text.
# It provides a health check at `/` and a POST endpoint `/classify_email` to process emails.
# The classification and masking logic is handled by the `process_email` function from `app.py`.



from fastapi import FastAPI
from pydantic import BaseModel
from app import process_email
import uvicorn

app = FastAPI()

class EmailRequest(BaseModel):
    email_text: str

# Confirming the availability
@app.get("/")
def getting():
    return {"Confirm":"The API is up and Running"}

#The endpoint to check the working

@app.post("/classify_email")
def classify_email(req: EmailRequest):
    result = process_email(req.email_text)
    return {
        "message": "Request processed successfully ✅",
        "data": result
    }

# For local testing
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
