
# This script detects and masks Personally Identifiable Information (PII) like emails, phone numbers, and card details.
# It uses regular expressions to find PII in the input text and replaces them with predefined mask tokens.
# The function also returns metadata with the position, type, and original value of each masked entity.




import re

# Dictionary of PII patterns and their replacement tokens

PII_PATTERNS = {
    "email": (r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[email]"),
    "phone_number": (r"\b\d{10}\b", "[phone_number]"),
    "dob": (r"\b(?:\d{1,2}[-/])?(?:\d{1,2}[-/])?\d{2,4}\b", "[dob]"),
    "aadhar_num": (r"\b\d{4}[- ]\d{4}[- ]\d{4}\b", "[aadhar_num]"),
    "credit_debit_no": (r"\b(?:\d[ -]*?){13,16}\b", "[credit_debit_no]"),
    "cvv_no": (r"\b\d{3}\b", "[cvv_no]"),
    "expiry_no": (r"\b(0[1-9]|1[0-2])\/\d{2,4}\b", "[expiry_no]"),
    "full_name": (r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b", "[full_name]"),  # Simplified pattern
}


def mask_pii(text):
    masked_text = text
    offset = 0
    masked_entities = []
    
    # Loop through each PII pattern and apply masking

    
    for entity_type, (pattern, mask_token) in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.start(), match.end()
            original_value = match.group()

            # Track the masked entity with position and type
            
            masked_entities.append({
                "position": [start + offset, end + offset],
                "classification": entity_type,
                "entity": original_value
            })

            # Replace the detected PII with the mask token and adjust offset

            masked_text = masked_text[:start] + mask_token + masked_text[end:]
            offset += len(mask_token) - len(original_value)

    return masked_text, masked_entities

if __name__ == "__main__":
    email = "Hi, I am John Doe. My email is john@example.com and phone is 9876543210. My card is 4111 1111 1111 1111."
    masked_text, entities = mask_pii(email)
    print("Masked Email:", masked_text)
    print("Entities:", entities)
