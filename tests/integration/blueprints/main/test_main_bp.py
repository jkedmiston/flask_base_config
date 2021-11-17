"""
Testing of endpoints.
"""


def test_main_bp(app):
    with app.test_client() as c:
        rv = c.get("/")
        assert b"hi" in rv.data
