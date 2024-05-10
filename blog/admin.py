from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    display_list = ('id','title','content')

