from django.shortcuts import render
from django.views import generic
from .models import Blogpost
from assets.settings import base as sets
# Create your views here.

class GetNewsPosts(generic.ListView):

    def get(self, request, *args, **kwargs):

        limit = sets.BLOG_LIMIT
        posts = Blogpost.objects.order_by('-created_on')[:limit]
        ctx = {'posts': posts}
        return render(request, 'blog/view_latest.html', ctx)


class GetSinglePost(generic.DetailView):

    def get(self, request, p_id, *args, **kwargs):
        post = Blogpost.objects.get(id=p_id)
        tags = post.tags.select_related()
        ctx = {'post': post, 'tags': tags}
        return render(request, 'blog/view_single.html', ctx)

class GetPostsByTag(generic.ListView):

    def get(self, request, tag_id, *args, **kwargs):
        posts = Blogpost.objects.all().filter(tags__id=tag_id)
        ctx = {'posts': posts}
        return render(request, 'blog/view_latest.html', ctx)