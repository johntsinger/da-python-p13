from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Address model."""
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(9999),
        ]
    )
    street = models.CharField(
        max_length=64
    )
    city = models.CharField(
        max_length=64
    )
    state = models.CharField(
        max_length=2,
        validators=[
            MinLengthValidator(2),
        ]
    )
    zip_code = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(99999),
        ]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[
            MinLengthValidator(3),
        ]
    )

    class Meta:
        # plural verbose name
        verbose_name_plural = 'addresses'

    def __str__(self):
        """String representation of the model"""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Letting model."""
    title = models.CharField(
        max_length=256
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """String representation of the model"""
        return self.title
