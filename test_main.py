from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_summarize_valid_url(monkeypatch):
    # Mock funkcji zwracających artykuł i streszczenie
    def fake_extract(url):
        return "To jest przykładowy artykuł o czymś ważnym."

    def fake_summary(text):
        return ["Punkt 1", "Punkt 2", "Punkt 3"]

    import summarizer
    monkeypatch.setattr("summarizer.extract_article_text", fake_extract)
    monkeypatch.setattr("summarizer.summarize_with_gpt", fake_summary)

    response = client.post("/summarize", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert "summary" in response.json()
    assert len(response.json()["summary"]) == 3