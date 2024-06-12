from django.urls import path

from posts import views


app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/edit',
         views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/followers/',
         views.profile_followers, name='profile_followers'),
    path('profile/<str:username>/followings/',
         views.profile_followings, name='profile_followings'),
    path('profile/<str:username>/profile-group-list/',
         views.profile_group_list, name='profile_group_list'),
    path('posts/<int:post_id>/comment/',
         views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/like/', views.post_like, name='post_like'),
    path('posts/<int:post_id>/dislike/',
         views.post_dislike, name='post_dislike'),
    path('posts/<int:post_id>/likes/', views.post_likes, name='post_likes'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/search/', views.post_search, name='post_search'),
    path('groups/', views.groups_list, name='groups_list'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('group/<slug:slug>/follow/', views.group_follow, name='group_follow'),
    path('group/<slug:slug>/unfollow/',
         views.group_unfollow, name='group_unfollow'),
    path('group/<slug:slug>/members/',
         views.group_members, name='group_members'),
    path('group/<slug:slug>/members-m/',
         views.group_role_m, name='group_role_m'),
    path('group/<slug:slug>/administrators/',
         views.group_administrators, name='group_administrators'),
    path('group/<slug:slug>/edit/', views.group_edit, name='group_edit'),
    path('group/<slug:slug>/delete/', views.group_delete, name='group_delete'),
    path('group/<slug:slug>/add-administrator/<str:username>/',
         views.group_add_administrator, name='group_add_administrator'),
    path('group/<slug:slug>/demote-administrator/',
         views.group_demote_administrator, name='group_demote_administrator'),
    path('group-create/', views.group_create, name='group_create'),
    path('create/', views.post_create, name='post_create'),
    path('follow/', views.follow_index, name='follow_index'),
    path('groups-follow/',
         views.group_follow_index, name='group_follow_index'),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
    path('comment/<int:comment_id>/edit/',
         views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
]
