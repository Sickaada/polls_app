from django.urls import path
from . import views
# <xyz> <--- this captures the int part of the url
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/',views.details, name = 'details'),
    path('<int:question_id>/results/',views.results, name = 'results'),
    path('<int:question_id>/vote/',views.vote, name = 'vote')
]