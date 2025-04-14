from app.data_handler import extract_papers

mock_json = {
    "organic_results": [
        {
            "title": "Sample Paper",
            "link": "https://example.com/sample",
            "snippet": "This is a sample abstract."
        }
    ]
}

def test_extract_papers():
    papers = extract_papers(mock_json)
    assert isinstance(papers, list)
    assert len(papers) == 1
    assert papers[0]["title"] == "Sample Paper"
