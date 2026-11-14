from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404,redirect,render
from .forms import RegisterForm,PostForm,ProfileForm,CommentForm
from .models import Post,Like,Comment,Follow
def feed(request):
    posts=Post.objects.select_related("author").prefetch_related("likes","comments__user")
    return render(request,"social/feed.html",{"posts":posts})
def register(request):
    if request.user.is_authenticated: return redirect("feed")
    form=RegisterForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        user=form.save(); login(request,user); messages.success(request,"Welcome to SocialConnect!")
        return redirect("feed")
    return render(request,"social/register.html",{"form":form})
@login_required
def create_post(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if request.method=="POST" and form.is_valid():
        post=form.save(commit=False); post.author=request.user; post.save()
        messages.success(request,"Your post has been published."); return redirect("feed")
    return render(request,"social/create_post.html",{"form":form})
@login_required
def profile(request,username):
    person=get_object_or_404(User,username=username)
    return render(request,"social/profile.html",{"person":person,"posts":person.posts.all(),"is_following":Follow.objects.filter(follower=request.user,followed=person).exists() if request.user.is_authenticated else False,"followers_count":person.followers.count(),"following_count":person.following.count()})
@login_required
def edit_profile(request):
    obj=request.user.profile
    form=ProfileForm(request.POST or None,request.FILES or None,instance=obj)
    if request.method=="POST" and form.is_valid():
        form.save(); messages.success(request,"Profile updated."); return redirect("profile",username=request.user.username)
    return render(request,"social/edit_profile.html",{"form":form})
@login_required
def toggle_like(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    like,created=Like.objects.get_or_create(user=request.user,post=post)
    if not created: like.delete()
    return redirect(request.META.get("HTTP_REFERER","feed"))
@login_required
def add_comment(request,post_id):
    post=get_object_or_404(Post,pk=post_id); form=CommentForm(request.POST)
    if form.is_valid(): Comment.objects.create(user=request.user,post=post,body=form.cleaned_data["body"])
    return redirect(request.META.get("HTTP_REFERER","feed"))
@login_required
def delete_comment(request,comment_id):
    get_object_or_404(Comment,pk=comment_id,user=request.user).delete()
    return redirect(request.META.get("HTTP_REFERER","feed"))
@login_required
def toggle_follow(request,username):
    person=get_object_or_404(User,username=username)
    if person!=request.user:
        obj,created=Follow.objects.get_or_create(follower=request.user,followed=person)
        if not created: obj.delete()
    return redirect("profile",username=username)
@login_required
def delete_post(request,post_id):
    get_object_or_404(Post,pk=post_id,author=request.user).delete()
    messages.success(request,"Post deleted."); return redirect("feed")
@login_required
def connections(request,username,kind):
    person=get_object_or_404(User,username=username)
    users=User.objects.filter(following__followed=person) if kind=="followers" else User.objects.filter(followers__follower=person)
    return render(request,"social/connections.html",{"users":users,"heading":f"{kind.title()} of {person.username}"})
