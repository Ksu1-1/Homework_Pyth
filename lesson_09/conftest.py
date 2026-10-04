import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from lesson_09.db import db


@pytest.fixture
def connection():
    conn = db.connect()
    try:
        yield conn
    finally:
        conn.close()
