from django.db import models
from django.utils import timezone
from django.urls import URLResolver, reverse
# Create your models here.


class Post(models.Model):
    auther = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # default create date will be created
    created_at = models.DateTimeField(
        default=timezone.now())
    # default publish date will be none
    published_date = models.DateTimeField(
        blank=True, null=True)
    # default create date will be created
    updated_at = models.DateTimeField(
        default=timezone.now())


    # when publish method is triggered manually only then the published_date wll be entered
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # will return only approved comments
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # write it as it is
    # when a post is created go to the post_detail page with the post just created
    # default django method
    def get_absolute_url(self):
        # pk refers to primary key
        # kwargs is key-wargs
        return reverse("post_detail", kwargs={'pk': self.pk})

    # not necessary
    def __str__(self):
        # if model is called it will return title
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        "blog.Post", related_name='comments', on_delete=models.CASCADE)
    auther = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now())
    updated_at = models.DateTimeField(
        default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    # approve comment
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # return to the post_list page as comments need to be approved first
        return reverse("post_list")
    
    # not necessary
    def __str__(self):
        # return comment text
        return self.text
