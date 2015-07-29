from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'latest/$', views.GetNewsPosts.as_view(), name='LatestBlogs'),
    url(r'details/(?P<p_id>[^\s]+)$', views.GetSinglePost.as_view(), name='SingleBlog')
]