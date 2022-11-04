from django.urls import path

from authentication_and_authorization.web.views import index, create_user_and_login, permissions_debug, show_profile, \
    ProfileView

urlpatterns = (
    path('', index, name='index'),
    path('create_user_and_login/', create_user_and_login, name='create user and login'),
    path('permissions_debug/', permissions_debug, name='permission debug'),
    path('show_profile/1/', show_profile, name='show profile'),
    path('show_profile/2/', ProfileView.as_view(), name='show profile'),

)
