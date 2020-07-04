from django.urls import path
from . import views
from .views import PostListView
urlpatterns = [
    
    path('', PostListView.as_view(), name='projects'),
    path('post/', views.createpost, name='create-post'),

    path('ajax/newsletter/', views.newsletter, name='newsletter')

]
