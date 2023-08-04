import pytest


@pytest.mark.django_db
def test_user(db, user_factory):
    user = user_factory.create()
    print(user.username)
    assert True


@pytest.mark.django_db
def test_category(db, category_factory):
    category = category_factory.create()
    print(category.name)
    assert True


@pytest.mark.django_db
def test_post(db, post_factory, user_factory, category_factory):
    category = category_factory.create()
    user = user_factory.create()
    post = post_factory.create(author=user, category=category)
    print(post.title)
    assert True


@pytest.mark.django_db
def test_comment(db, comment_factory, user_factory, post_factory, category_factory):
    user = user_factory.create()
    category = category_factory.create()
    post = post_factory.create(author=user, category=category)
    comment = comment_factory.create(owner=user, post=post)
    print(comment.post)
    assert True
