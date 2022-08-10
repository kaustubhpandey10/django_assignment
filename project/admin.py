from django.contrib import admin

from .models import Project, User, Issue, Label, Comment, Assign, Watcher

admin.site.register([Project,User,Issue,Label,Comment,Assign,Watcher])
