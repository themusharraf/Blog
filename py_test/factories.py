import factory
from faker import Faker
from blog.models import Comment, Post, Category
from django.contrib.auth.models import User

faker = Faker()


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    body = faker.text()
    created_at = faker.date_time()


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = faker.bothify(text='????????')
    body = faker.text()
    image = faker.image_url()
    view_count = faker.random_int()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = faker.email()
    username = factory.Faker('user_name')
    first_name = faker.first_name()
    last_name = faker.last_name()
    password = faker.password()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = faker.text()
