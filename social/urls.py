from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns=[
path("",views.feed,name="feed"),path("register/",views.register,name="register"),
path("login/",auth_views.LoginView.as_view(template_name="social/login.html"),name="login"),
path("logout/",auth_views.LogoutView.as_view(),name="logout"),
path("post/new/",views.create_post,name="create_post"),path("post/<int:post_id>/delete/",views.delete_post,name="delete_post"),
path("post/<int:post_id>/like/",views.toggle_like,name="toggle_like"),path("post/<int:post_id>/comment/",views.add_comment,name="add_comment"),
path("comment/<int:comment_id>/delete/",views.delete_comment,name="delete_comment"),
path("u/<str:username>/",views.profile,name="profile"),path("u/<str:username>/edit/",views.edit_profile,name="edit_profile"),
path("u/<str:username>/follow/",views.toggle_follow,name="toggle_follow"),
path("u/<str:username>/<str:kind>/",views.connections,name="connections")]
