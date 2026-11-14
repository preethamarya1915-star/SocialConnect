from django.contrib import admin
from .models import Profile,Post,Like,Comment,Follow
admin.site.register([Profile,Post,Like,Comment,Follow])
