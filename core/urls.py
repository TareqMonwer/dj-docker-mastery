from django.urls import path
from core.views import homepage_view


app_name = 'core'
urlpatterns = [
    path('', homepage_view, name='homepage_url'),
]
