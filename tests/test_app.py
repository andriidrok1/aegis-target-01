from app import app


def test_health():
    assert app.test_client().get("/health").get_json() == {"ok": True}
