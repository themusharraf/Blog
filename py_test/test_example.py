import pytest


@pytest.mark.django_db
def test_user(db, user_factory):
    user = user_factory.create()
    print(user.username)
    assert True
