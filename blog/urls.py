from django.urls.conf import path,re_path
from . import views

urlpatterns = [
    path('post_list/',views.post_list,name='post_list'),
    # path('post/<int:>/',views.get_num,name='post_detail')
    re_path(r'^post/(?P<p>\d+)/$',views.get_num,name='get_num')
]
