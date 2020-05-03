from django.shortcuts import render, get_object_or_404, redirect
# timezone
from django.utils import timezone

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post,Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
# login required during class based views
from django.contrib.auth.mixins import LoginRequiredMixin

# login required for fun/ def
from django.contrib.auth.decorators import login_required

# Create your views here.

 
class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    # allow us to use django orm on generic views
    def get_queryset(self):
        # (-publish_date) refers to decending order
        # lte (less than or equals too) : short form  
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    # mandatory fields with LoginRequiredMixins
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostUpdateView(LoginRequiredMixin , UpdateView):
    # not a mandatory fields with LoginRequiredMixins
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin , DeleteView):
    # not a mandatory fields with LoginRequiredMixins
    model = Post

    # reverse_lazy : wait for the query to perform and then execute
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    # not a mandatory fields with LoginRequiredMixins
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    # form_class = PostForm
    model = Post

    def get_queryset(self):
        # publish_date__isnull : if publish date is null
        return Post.objects.filter(publish_date__isnull=True).order_by('-created_at')

######################################################################################
# comments
###################################################################################### 

@login_required 
#code below this reqired to be logged in

def add_comment_to_post(request , pk):
    # get_object_or_404( model_name , key )
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST' :
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/comment_form.html', {'form' : form})


@login_required 
#code below this reqired to be logged in
def comment_approve(args , pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)