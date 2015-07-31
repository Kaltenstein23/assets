from django.shortcuts import render
from django.views import generic
from .models import Blogpost, Tag
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
        ctx = {'post': post, 'tags': tags}
        return render(request, 'blog/view_single.html', ctx)

class GetPostsByTag(generic.ListView):

    def get(self, request, tag_id, *args, **kwargs):
        logger = logging.getLogger('project')
        logger.debug('Getting posts with tag id {} assigned'.format(tag_id))
        posts = Blogpost.objects.all().filter(tags__id=tag_id)
        logger.debug('Found {} posts with tag id {}'.format(posts.count(), tag_id))
        ctx = {'posts': posts}
        return render(request, 'blog/view_latest.html', ctx)