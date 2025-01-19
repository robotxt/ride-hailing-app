import logging
from django.utils import timezone
from django.core.management.base import BaseCommand
from app.models import User, Ride, RideEvent
from faker import Faker


logger = logging.getLogger(__name__)
faker = Faker()


def _create_user(email, role: str):
    user, _ = User.objects.get_or_create(
        email=email,
        defaults={
            "first_name": faker.unique.first_name(),
            "last_name": faker.unique.last_name(),
            "email": email,
            "phone": "11921223",
            "role": role,
        },
    )

    return user


def create_latlng():
    loc = faker.local_latlng()
    return loc[0], loc[1]


class Command(BaseCommand):
    help = "Create Sender"

    def handle(self, *args, **options):
        admin = _create_user("admin@example.com", role=User.ADMIN)
        admin.set_password("Password101")
        admin.save()

        rider = _create_user("rider@example.com", role=User.RIDER)
        driver = _create_user("driver@example.com", role=User.DRIVER)

        for _ in range(1, 5):
            pickup_lat, pickup_lng = create_latlng()
            dropoff_lat, dropoff_lng = create_latlng()

            ride = Ride.objects.create(
                rider=rider,
                driver=driver,
                pickup_latitude=pickup_lat,
                pickup_longitude=pickup_lng,
                dropoff_latitude=dropoff_lat,
                dropoff_longitude=dropoff_lng,
                pickup_time=timezone.now(),
                status=Ride.EN_ROUTE,
            )

        for _ in range(1, 5):
            pickup_lat, pickup_lng = create_latlng()
            dropoff_lat, dropoff_lng = create_latlng()

            ride = Ride.objects.create(
                rider=rider,
                driver=driver,
                pickup_latitude=pickup_lat,
                pickup_longitude=pickup_lng,
                dropoff_latitude=dropoff_lat,
                dropoff_longitude=dropoff_lng,
                pickup_time=timezone.now(),
                status=Ride.PICKUP,
            )

            RideEvent.objects.create(ride=ride, description=RideEvent.PICKUP_DESC)

        for _ in range(1, 5):
            pickup_lat, pickup_lng = create_latlng()
            dropoff_lat, dropoff_lng = create_latlng()

            ride = Ride.objects.create(
                rider=rider,
                driver=driver,
                pickup_latitude=pickup_lat,
                pickup_longitude=pickup_lng,
                dropoff_latitude=dropoff_lat,
                dropoff_longitude=dropoff_lng,
                pickup_time=timezone.now(),
                status=Ride.DROPOFF,
            )

            RideEvent.objects.create(ride=ride, description=RideEvent.DROPOFF_DESC)
