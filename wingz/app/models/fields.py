from django.db import models
from django.core.validators import BaseValidator


class PhoneField:
    INVALID_ERROR = "Enter a valid phone number."

    @staticmethod
    def build(blank, unique=False):
        error_messages = {}
        if unique is not False and unique is not True:
            error_messages = {
                "unique": unique,
            }
        return models.CharField(
            max_length=15,
            blank=blank,
            error_messages=error_messages,
            unique=unique,
            null=True,
            validators=[
                BaseValidator(
                    15,
                    message=PhoneField.INVALID_ERROR,
                ),
                BaseValidator(
                    15,
                    message=PhoneField.INVALID_ERROR,
                ),
            ],
        )
