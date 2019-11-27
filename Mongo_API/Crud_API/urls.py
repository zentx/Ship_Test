from django.conf.urls import url
from Mongo_API.Crud_API import views


urlpatterns = [
    url(r'^(?P<id>[-\w]+)$', views.ShipViewSet.as_view()),
]
