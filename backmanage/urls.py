from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.feedback, name='feedback'),
    path('forum_task/', views.forum_task, name='forum_task'),
    path('system_state/', views.system_state, name='system_state'),
    path('user_manage/', views.user_manage, name='user_manage'),
    path('set_admin/<int:user_id>', views.set_admin, name='set_admin'),
    path('remove_admin/<int:user_id>', views.remove_admin, name='remove_admin'),
    path('forbid_user/<int:user_id>', views.forbid_user, name='forbid_user'),
    path('reset_password/<int:user_id>', views.reset_password, name='reset_password'),
    path('remove_post/<int:post_id>', views.remove_post, name='remove_post'),
    path('about/', views.about, name='guanyu'),
    path('star/<int:feedback_id>', views.star, name='star'),
    path('pass_post/<int:post_id>', views.pass_post, name='pass_post'),
    path('fail_post/<int:post_id>', views.fail_post, name='fail_post'),
    path('advise/', views.advise, name='advise')

]
