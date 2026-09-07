import pytest
import pandas as pd
import numpy as np
import sys
import os

root = os.path.abspath(".")

if root not in sys.path:
    sys.path.insert(0, root)
    

from src.cleaner import(
    standardise_column_names,
    strip_string_whitespace,
    remove_duplicates,
    impute_categorical_missing,
    impute_total_charges,
    fix_senior_citizen_encoding,
    fix_total_charges_type
)

# FIXTURES

@pytest.fixture
def minimal_raw_df():
    raw_df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003", "C004"],
        "senior_citizen": [0, 1, 0, 1],
        "tenure_months": [0, 5, 0, 24],
        "monthly_charges": [29.85, 56.95, 53.85, 42.30],
        "total_charges": ["", "284.75", " ", "1014.20"],
        "churn": ["No", "Yes", "No", "No"],
    })
    return raw_df
@pytest.fixture
def duplicate_df():
    duplicate_df = pd.DataFrame({
        "customer_id": ["C001", "C001", "C002", "C003", "C003"],
        "tenure_months": [12, 12, 6, 24, 24],
        "monthly_charges": [50.0, 50.0, 30.0, 70.0, 70.0],
        "total_charges": ["600", "600", "180", "1680", "1680"],
        "senior_citizen": [0, 0, 1, 0, 0],
        "churn": ["No", "No", "Yes", "No", "No"],
    })
    return duplicate_df
@pytest.fixture
def categorical_missing_df():
    return pd.DataFrame({
        "customer_id": ["C001", "C002", "C003", "C004", "C005"],
        "dependents": ["Yes", np.nan, "No", "No", np.nan],
        "payment_method": [
            "Electronic check",
            "Electronic check",
            np.nan,
            "Mailed check",
            "Electronic check",
        ],
    })
#-------TEST----------
def test_standardise_column_names_lowercases():
    df= pd.DataFrame({"CustomerID":[1], "Monthly Charges":[50.0]})
    result=standardise_column_names(df)
    print(result)
if __name__=="__main__":
    test_standardise_column_names_lowercases()