from django.urls import path,include
from .views import ListPostViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('project',ListPostViewSet,basename='project-apis')
urlpatterns = [
    
    
    path('',include(router.urls))

]