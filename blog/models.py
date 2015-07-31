from django.db import models
from authtools.models import User
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class Tag(models.Model):

    class Meta:

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=250,verbose_name='Post tags')
    slug = models.SlugField(verbose_name='Tag Slug')

    @python_2_unicode_compatible
    def __str__(self):
        return self.name

class Blogpost(models.Model):

    class Meta:

        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        ordering = ['-created_on']

    title = models.CharField(max_length=500, default='Untitled Post', verbose_name='Post title')
    slug = models.SlugField(max_length=250, verbose_name='Post slug')
    body = models.CharField(max_length=12500, verbose_name='Post body', default='Post body belongs here')
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, related_name='posts')
    created_on = models.DateTimeField("Posted on", auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField("Last updated on", auto_now=True, auto_now_add=False)
    update_count = models.IntegerField("Update Count", blank=True, null=True)

    @python_2_unicode_compatible
    def __str__(self):
        return '{}'.format(self.title)

    def save(self):
        if self.pk is not None:
            self.update_count += 1
        super(Blogpost, self).save()


class Comment(models.Model):

    from uuid import uuid4

    class Meta:

        verbose_name = 'Post comment'
        verbose_name_plural = 'Post comments'
        ordering = ['-created_on']

    id = models.UUIDField(default=uuid4, blank=True, editable=False, primary_key=True)
    owner = models.ForeignKey(User)
    post = models.ForeignKey(Blogpost)
    body = models.CharField(max_length=12500)
    created_on = models.DateTimeField("Posted on",  auto_now_add=True)
