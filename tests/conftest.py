from pathlib import Path

import pytest


TEST_DIR = Path(__file__).parent


@pytest.fixture
def payment_request_data():
    filepath = TEST_DIR / 'data' / 'avtalegiro_payment_request.txt'
    with filepath.open('r', encoding='iso-8859-1') as fh:
        return fh.read()
