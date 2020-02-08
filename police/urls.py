from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
	path('get_analysis', get_analysis, name='get_analysis')
]