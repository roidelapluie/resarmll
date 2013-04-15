from hackers.models import Hacker
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from hackers.forms import HackerChangeForm

class HackerAdmin(UserAdmin):

    list_filter = ('is_admin', 'is_active')
    filter_horizontal = ()
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
                    (None, {'fields': ('username', 'password')}),
                    (_('Personal info'), {'fields': ('email', 'first_name', 'last_name',
                    'language', 'address', 'gender', 'badge_type', 'badge_text', 'comments',
                    'pgp_fingerprint', 'is_volunteer')}),
                    (_('User account'), {'fields': ('is_admin','is_active')}),
    )

    form = HackerChangeForm

admin.site.register(Hacker, HackerAdmin)
admin.site.unregister(Group)
