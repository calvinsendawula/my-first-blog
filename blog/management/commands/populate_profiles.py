from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Profile

class Command(BaseCommand):
    help = 'Populate user profiles with profile pictures'

    def handle(self, *args, **options):
        for user in User.objects.all():
            profile, created = Profile.objects.get_or_create(user=user)
            if not created:
                # Update existing profile if it already exists
                profile.picture = f"blog/profile_pictures/{user.username}.jpeg"
                profile.save()
