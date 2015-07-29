from django.shortcuts import render
from django.views import generic
from blog.models import Blogpost
from assets.settings import base as sets
import logging
# Create your views here.

class GetNewsPosts(generic.ListView):

    def get(self, request, *args, **kwargs):

        limit = sets.BLOG_LIMIT
        posts = Blogpost.objects.order_by('-created_on')[:limit]
        ctx = {'posts': posts}
        return render(request, 'blog/view_latest.html', ctx)


class GetSinglePost(generic.DetailView):

    def get(self, request, p_id, *args, **kwargs):
        logger = logging.getLogger('project')
        post = Blogpost.objects.get(id=p_id)
        tags = post.tags.select_related()
        logger.debug('Tags: {}'.format(post.tags))
        ctx = {'post': post,'tags': tags}
        return render(request, 'blog/view_single.html', ctx)