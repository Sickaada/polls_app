from django.urls import path
from . import views
app_name = 'polls'
# <xyz> <--- to capture a value from url, angle brackets are used( here int)
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.DetailsView.as_view(), name = 'details'),
    path('<int:pk>/results/',views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/votes_count/',views.votes_count, name = 'votes_count')
]