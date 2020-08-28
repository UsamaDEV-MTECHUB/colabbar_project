from django.urls import path
from . import views
import _json
urlpatterns = [
    path('', views.feed, name="feed"),
    path('logout', views.logout, name="logout"),
]
