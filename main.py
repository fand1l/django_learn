import django_setup
from second_app.models import User, Group

user1 = User(username="Петро",
             email="petro@example.com",
             role="admin"
).save()