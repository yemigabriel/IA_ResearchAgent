import os
import tempfile
from app.db import init_db, save_paper, get_saved_papers

TEST_DB_PATH = tempfile.NamedTemporaryFile(delete=False).name

# Patch the db module to use a test database
import app.db
app.db.CACHE_DB = TEST_DB_PATH

def test_db_insertion_and_retrieval():
    init_db()
    test_paper = {
        "title": "Test Title",
        "link": "https://example.com/test",
        "snippet": "This is a test snippet."
    }
    save_paper(test_paper)
    saved = get_saved_papers()
    assert not saved.empty
    assert test_paper["title"] in saved["title"].values

# Clean up after test
import atexit
atexit.register(lambda: os.remove(TEST_DB_PATH))
