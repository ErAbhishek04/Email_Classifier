
# This script processes email text by masking PII and classifying the email into a category.
# It uses utility functions to handle PII masking and a preloaded model for category prediction.
# The final output is a structured JSON containing the original text, masked version, entities, and predicted category.



from utils import mask_pii
from models import load_model, predict_category

model = load_model()  

def process_email(email_text):
    # Step 1: Mask PII
    masked_email, masked_entities = mask_pii(email_text)

    # Step 2: Classify masked email
    predicted_category = predict_category(masked_email, model)

    # Step 3: Construct output JSON
    response = {
        "input_email_body": email_text,
        "list_of_masked_entities": masked_entities,
        "masked_email": masked_email,
        "category_of_the_email": predicted_category
    }

    return response


# Testing the functionality 
if __name__ == "__main__":
    sample_email = """Subject: Invoice Issue - My name is Aman Sharma and my email is aman@example.com. My card is 1234-5678-9876-5432."""
    result = process_email(sample_email)
    from pprint import pprint
    pprint(result)
