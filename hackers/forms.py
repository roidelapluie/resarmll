from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from hackers.models import Hacker

class HackerChangeForm(UserChangeForm):
    class Meta:
        model = Hacker

class HackerUpdateForm(ModelForm):
    class Meta:
        model = Hacker
        fields = ('username', 'email', 'first_name',
                'last_name', 'address', 'language',
                'gender', 'badge_type', 'badge_text',
                'comments', 'pgp_fingerprint', 'is_volunteer')

