import factory
import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory
from faker import Faker


logging.getLogger("faker").setLevel(logging.ERROR)

faker = Faker()


def fake_email():
    return f"fake-{faker.unique.random_int()}@example.com"


def fake_password():
    return faker.password()


class GroupFactory(DjangoModelFactory):
    class Meta:
        model = Group

    name = factory.Sequence(lambda n: f"Group #{n}")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("email",)

    email = factory.Sequence(lambda n: f"user-{n}@example.com")
    password = "fake-password"

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # simple build, do nothing
            return

        if extracted:
            for group in extracted:
                self.groups.add(group)
