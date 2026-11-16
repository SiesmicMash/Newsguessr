from fastapi.testclient import TestClient

from app.main import app, redact_text

client = TestClient(app)


def test_redact_text_removes_place_and_person():
    redacted, removed = redact_text("Justin Trudeau spoke in Ottawa on Tuesday.")
    assert "Ottawa" not in redacted
    assert "Trudeau" not in redacted
    assert "Ottawa" in removed


def test_redact_text_leaves_plain_text_alone():
    text = "The weather was mild and the market was busy."
    redacted, removed = redact_text(text)
    assert redacted == text
    assert removed == []


def test_redact_endpoint():
    response = client.post(
        "/redact", json={"text": "Justin Trudeau spoke in Ottawa on Tuesday."}
    )
    assert response.status_code == 200
    body = response.json()
    assert "Ottawa" not in body["redacted_text"]
    assert "Ottawa" in body["removed_terms"]


def test_health():
    assert client.get("/health").json() == {"status": "ok"}