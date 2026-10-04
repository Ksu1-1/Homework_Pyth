import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    ),
)

import pytest  # noqa: E402
from lesson_09.db import db  # noqa: E402


@pytest.fixture
def connection():
    conn = db.connect()
    try:
        yield conn
    finally:
        conn.close()
