from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic as views
from django.contrib.auth.models import User

from authentication_and_authorization.web.decorators import allow_groups


# Function-Based View
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse (f'You are {request.user.username}')


# Class-Based View
class ProfileView(LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f'You are {request.user.username}')


@allow_groups(groups=['Users'])
def index(request):
    print(
        authenticate(username='bogomila', password='123'),
        authenticate(username='kats', password='123'),
    )
    # new_user = User.objects.create_user(
    #     username='bogomilak',
    #     password='B0g0K123',
    #     first_name='Bogomila',
    # )
    user_message = '' if request.user.is_authenticated else 'not'
    return HttpResponse(f'The user is {user_message} authenticated.')

'''
The User Methods Examples:
1. get_username() - returns the username for the user
2. get_full_name() - returns f"{first name} {last_name}"
3. get_short_name() - returns first_name only
'''

'''
Ways to create users:
1. python manage.py createsuperuser
2. from admin by superuser => log in Django Admin -> Users -> Add
3. with code: User.objects.create_user() and User.objects.create_superuser()
'''


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='User.objects.create_',
    )
    # Creates the session and attaches 'user' to request
    login(request, user)


def permissions_debug(request):
    usernames = {'bogomila', 'kats'}
    users = User.objects.filter(username__in=usernames)
    for user in users:
        print('-' * 30)
        print(user)
        print(user.has_perms('auth.add_user'))
        print('-' * 30)
    print(users)
    return HttpResponse('It works')
