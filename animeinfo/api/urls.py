from django.urls import path, include

from . import routes


app_name = 'api'


urlpatterns = [
    path("", include(routes.router.urls)),
]
