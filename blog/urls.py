from django.urls.conf import path
from . import views

urlpatterns = [
    path('post_list/',views.post_list,name='post_list')
]
