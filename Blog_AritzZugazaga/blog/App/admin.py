from django.contrib import admin

from .models import App, Comment, ForumComment

# Register your models here.
admin.site.register(App)
admin.site.register(Comment)
admin.site.register(ForumComment)