import pytest
import pandas as pd
# import context
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

@pytest.fixture
def get_test_df():
    csv_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', 'ratings.csv')
    return pd.read_csv(csv_path, sep = ',')
