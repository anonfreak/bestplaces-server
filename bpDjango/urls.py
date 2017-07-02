"""bpDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views as rest_views

from BestPlaces import views as own_views
from BestPlaces.views import SearchView, PlacesView, get_google_api_key

router = routers.DefaultRouter()
router.register(r'user', own_views.UserViewSet)
router.register(r'visit', own_views.VisitViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', rest_views.obtain_auth_token),
    url(r'^place/search$', SearchView.as_view()),
    url(r'^place/(?P<placeId>.+)/$', PlacesView.as_view()),
    url(r'^google-token/', get_google_api_key)
]

