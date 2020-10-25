from django.urls import path
from .views import homepage, post_detail, forum, AddCommentView, AddForumCommentView

urlpatterns = [
    path('', homepage, name = 'home'),
    path('post_detail/<int:pk>/', post_detail, name = 'post_detail'),
    path('post_detail/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'),
    path('forum', forum, name = 'forum'),
    path('forum/forum_comment', AddForumCommentView.as_view(), name = 'add_forum_comment'),
]