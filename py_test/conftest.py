import pytest
from pytest_factoryboy import register
from py_test.factories import UserFactory, CommentFactory, PostFactory, CategoryFactory

register(UserFactory)
register(CategoryFactory)
register(PostFactory)
register(CommentFactory)
