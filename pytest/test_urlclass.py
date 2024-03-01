import sys
import os

# Adding the urlclass directory to the path to ensure models can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'urlclass')))

import pytest
from models import URLClass
from pydantic import ValidationError
# Successful Test Cases
@pytest.mark.parametrize("data", [
    # Tests if all fields properly formatted.
    {"id": 1, "name_of_the_topic": "Modern Economics", "year": 2022, "level": "Level I", "topics": "Economics", "learning_outcomes": "Understand the basics of modern economics", "introduction": "An overview of modern economics", "summary": "A brief summary of economic principles", "pdf_link": "http://example.com/economics.pdf", "link_to_the_summary_page": "https://example.com/summary_economics"},
    
    # Verifies valid year, level, and links.
    {"id": 2, "name_of_the_topic": "Advanced Algebra", "year": 2021, "level": "Level II", "topics": "Mathematics", "learning_outcomes": "Master advanced algebraic techniques", "introduction": "Deep dive into algebra", "summary": "Key algebraic concepts explored", "pdf_link": "http://example.com/algebra.pdf", "link_to_the_summary_page": "https://example.com/summary_algebra"},
    
    # Ensures correct processing of finance-related content and URL validation.
    {"id": 3, "name_of_the_topic": "Quantitative Finance", "year": 2023, "level": "Level III", "topics": "Finance", "learning_outcomes": "Apply quantitative methods to finance", "introduction": "Quantitative approaches in finance", "summary": "Quantitative finance summary", "pdf_link": "http://example.com/quant_finance.pdf", "link_to_the_summary_page": "https://example.com/summary_quant_finance"},
    
    # Tests the model's ability to handle default values for optional fields.
    {"id": 4, "name_of_the_topic": "Behavioral Psychology", "year": 2020, "level": "Level I", "topics": "Psychology", "learning_outcomes": "Explore behavioral psychology", "introduction": "Introduction to behavioral psychology", "summary": "Behavioral psychology overview", "pdf_link": "http://example.com/behavioral_psychology.pdf", "link_to_the_summary_page": "https://example.com/summary_behavioral_psychology"},
    
    # Checks on link validation.
    {"id": 5, "name_of_the_topic": "Cryptography Basics", "year": 2024, "level": "Level II", "topics": "Computer Science", "learning_outcomes": "Understand the basics of cryptography", "introduction": "Cryptography in computer science", "summary": "Introduction to cryptographic principles", "pdf_link": "http://example.com/cryptography.pdf", "link_to_the_summary_page": "https://example.com/summary_cryptography"},
])

def test_urlclass_success(data):
    assert URLClass(**data)

# Failed Test Cases
@pytest.mark.parametrize("data, expected_failure_message", [
    # Test case 1: Checks multiple validation errors including id <= 0, curriculum year out of valid range, level not starting with "Level", empty fields, and invalid pdf_link format.
    ({"id": 0, "title": " ", "curriculum": 1899, "level": "Not a Level", "topics": " ", "learning_outcomes_section": "", "introduction": "", "summary_bullets": "", "pdf_link": "not_a_pdf_url"}, "Expected failure due to various validation errors"),
    
    # Test case 2: Validates that the curriculum year must be within the specified range (1900-2024). Here, 2025 is out of range, expecting to trigger a failure.
    ({"id": 7, "title": "Future Analysis", "curriculum": 2025, "level": "Level I", "topics": "Future Studies", "learning_outcomes_section": "Future learning outcomes...", "introduction": "Future introduction...", "summary_bullets": "Future bullets...", "pdf_link": "http://example.com/future.pdf"}, "Expected failure due to curriculum year above range"),
    
    # Test case 3: Checks for required fields not being empty. Here, the title is empty which should trigger a validation error. It demonstrates the model's enforcement of required and non-empty fields.
    ({"id": 8, "title": "", "curriculum": 2021, "level": "Level II", "topics": "Missing Title", "learning_outcomes_section": "No title.", "introduction": "No title here.", "summary_bullets": "No title.", "pdf_link": "http://example.com/missingtitle.pdf"}, "Expected failure due to missing title"),
    
    # Test case 4: Ensures that the pdf_link must be a valid URL that ends with ".pdf". This case provides an invalid URL that does not end with ".pdf", testing the model's URL validation logic.
    ({"id": 9, "title": "Invalid PDF Link", "curriculum": 2023, "level": "Level II", "topics": "Valid Topic", "learning_outcomes_section": "Valid outcomes.", "introduction": "Valid intro.", "summary_bullets": "Valid summary.", "pdf_link": "http://example.com/not_pdf_link"}, "Expected failure due to invalid pdf_link"),
    
    # Test case 5: Verifies that the level field starts with the specified prefix "Level". This case has "Lv II" which does not meet the requirement, aiming to validate the model's enforcement of field content rules.
    ({"id": 10, "title": "Level Keyword Missing", "curriculum": 1922, "level": "Lv II", "topics": "Keyword Testing", "learning_outcomes_section": "Testing level keyword.", "introduction": "Intro keyword.", "summary_bullets": "Summary keyword.", "pdf_link": "http://example.com/levelkeywordmissing.pdf"}, "Expected failure due to level not starting with 'Level'"),
])

def test_urlclass_failure(data, expected_failure_message):
    try:
        model_instance = URLClass(**data)
        assert expected_failure_condition(model_instance), "Data conforms to model constraints unexpectedly."
    except ValidationError:
        pytest.fail("ValidationError raised, but test designed to assert incorrect model state.")

