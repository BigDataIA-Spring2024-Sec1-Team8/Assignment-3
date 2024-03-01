import sys
import os

# Adding the urlclass directory to the path to ensure models can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pdfclass')))
print(os.getcwd(),"jsjs")
import pytest
from models import MetaData, LearningOutcomes  
from pydantic import ValidationError

# Successful Test Cases
@pytest.mark.parametrize("data", [
    {"Title": "Advanced Data Structures", "publisher": "TechPress", "availability_status": "Available", "analytic": "Analysis Complete", "imprinted_date": "2022-01-01", "abstract": "This publication explores advanced data structures."},
    {"Title": "Quantum Computing Fundamentals", "publisher": "SciencePub", "availability_status": "In Stock", "analytic": "Pending Review", "imprinted_date": "2023-03-15", "abstract": "An introduction to quantum computing."},
    {"Title": "The Art of Computer Programming", "publisher": "CompBooks", "availability_status": "Out of Stock", "analytic": "Critical Acclaim", "imprinted_date": "1997-05-12", "abstract": "Comprehensive computer programming concepts."},
    {"Title": "Machine Learning for Beginners", "publisher": "EduTech", "availability_status": "Available", "analytic": "Analysis Pending", "imprinted_date": "2021-09-09", "abstract": "A beginner's guide to machine learning."},
    {"Title": "Blockchain and Cryptocurrency", "publisher": "FinTechPublishers", "availability_status": "Coming Soon", "analytic": "Not Available", "imprinted_date": "2024-01-01", "abstract": "Exploring the impact of blockchain and cryptocurrency."},
])
def test_metadata_success(data):
    assert MetaData(**data)


@pytest.mark.parametrize("data, expected_failure_message", [
    # Empty title and publisher, which should fail due to empty string validation.
    ({"title": "", "publisher": "", "availability_status": "Online", "analytic": "Yes", "imprinted_date": "2021-01-01", "abstract": "Abstract here."}, "empty string not allowed for title and publisher"),

    # Analytic field below minimum length.
    ({"title": "Title", "publisher": "Publisher", "availability_status": "Online", "analytic": "N", "imprinted_date": "2021-02-01", "abstract": "Abstract content."}, "analytic below minimum length"),

    # Imprinted date missing, which is required.
    ({"title": "Another Title", "publisher": "Another Publisher", "availability_status": "Offline", "analytic": "Analysis", "abstract": "Detailed abstract."}, "imprinted_date is required"),

    # Abstract below the minimum length of 2.
    ({"title": "Title Three", "publisher": "Publisher Three", "availability_status": "Available", "analytic": "Complete", "imprinted_date": "2022-03-01", "abstract": "A"}, "abstract below minimum length"),

    # Invalid imprinted_date format.
    ({"title": "Title Four", "publisher": "Publisher Four", "availability_status": "In Review", "analytic": "Pending", "imprinted_date": "not-a-date", "abstract": "Another abstract."}, "invalid imprinted_date format"),
])

def test_metadata_failure(data, expected_failure_message):
    try:
        MetaData(**data)
        pytest.fail(f"{expected_failure_message}")  # Explicitly fail the test if no ValidationError is thrown
    except ValidationError:
        pytest.fail("ValidationError raised, but test designed to assert incorrect model state.")

# Successful Test Cases
@pytest.mark.parametrize("data", [
    {"topic": "Quantitative Analysis", "outcomes": "Understand statistical methods"},
    {"topic": "Corporate Finance", "outcomes": "Grasp the fundamentals of corporate finance"},
    {"topic": "Microeconomics", "outcomes": "Analyze consumer behavior"},
    {"topic": "Macroeconomics", "outcomes": "Study the economy as a whole"},
    {"topic": "Portfolio Management", "outcomes": "Learn about portfolio diversification"}
])

def test_learning_outcomes_success(data):
    assert LearningOutcomes(**data)

# Failed Test Cases for LearningOutcomes
@pytest.mark.parametrize("data, expected_failure_message", [
    # Topic too short, minimum length validation.
    ({"topic": "A", "outcomes": "Valid Outcome"}, "Expected failure due to topic below minimum length."),
     
    # Outcomes is an empty string, non-empty validation.
    ({"topic": "Valid Topic", "outcomes": ""}, "Expected failure due to empty outcomes."),
    
    # Topic with non-visible characters, minimum length validation.
    ({"topic": "\n", "outcomes": "Valid Outcome"}, "Expected failure due to non-visible characters in topic."),
    
    # Outcomes with non-visible characters, minimum length validation.
    ({"topic": "Valid Topic", "outcomes": "\t"}, "Expected failure due to non-visible characters in outcomes."),

    # Missing outcomes field, default value and minimum length validation.
    ({"topic": "Valid Topic"}, "Expected failure due to outcomes defaulting to 'Not defined' and not meeting minimum length."),
])

def test_learning_outcomes_failure(data, expected_failure_message):
    try:
        MetaData(**data)
        pytest.fail(f"{expected_failure_message}")  # Explicitly fail the test if no ValidationError is thrown
    except ValidationError:
        pytest.fail("ValidationError raised, but test designed to assert incorrect model state.")
