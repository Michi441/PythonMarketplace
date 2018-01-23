
from .models import Profile

def save_avatar(backend, user, response, *args, **kwargs):
    try:
        profile = Profile.objects.get(user_id=user.id)
    except Profile.DoesNotExist:
        profile = Profile(user_id=user.id)

    if backend.name == 'github':
        profile.avatar = 'https://github.com/images/error/octocat_happy.gif'


    profile.save()
