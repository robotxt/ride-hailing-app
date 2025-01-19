from rest_framework import routers
from app import endpoints


router = routers.DefaultRouter()
router.register("ride", endpoints.RideAPI, basename="ride-api")
router.register("login", endpoints.LoginAPI, basename="login-api")
