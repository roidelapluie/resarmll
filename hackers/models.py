from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('EN', _('English')),
    ('FR', _('French')),
    ('NL', _('Dutch')),
    ('DE', _('German')),
)
GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class HackerManager(BaseUserManager):
    def create_user(self, username, email, last_name, first_name, password=None, **extra_fields):
        print password
        user = self.model(
                username=username,
                email=email,
                last_name=last_name,
                first_name=first_name,
                **extra_fields
                )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
                username=username,
                email=email,
                last_name=last_name,
                first_name=first_name,
                password=password,
                )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class HackerBadge(models.Model):
    badge_name = models.CharField(_('badge type'))
    badge_name = models.BooleanField(_('hidden'))

class Hacker(AbstractBaseUser):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=64,
        unique=True,
        db_index=True,
    )
    email = models.EmailField(
        verbose_name=_('email address'),
        max_length=255,
        unique=True,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=64,
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=64,
    )
    address = models.TextField(
        verbose_name=_('address'),
        help_text=_('''Address is useful for speakers or people who'll get a refund.'''),
        blank = True,
    )
    language = models.CharField(
        verbose_name=_('language'),
        choices=LANGUAGES,
        max_length=2,
        blank = True,
    )
    gender = models.CharField(
        verbose_name=_('gender'),
        choices = GENDERS,
        help_text = _('The Gender is not mandatory but could be useful for room distribution.'),
        max_length=1,
        blank = True,
    )
    badge_type = models.ForeignKey(
        'HackerBadge',
        null=True,
        blank=True,
    )
    badge_text = models.CharField(
        verbose_name=_('badge text'),
        max_length=64,
        help_text = _('Free text printed on your badge (should not be too long).'),
        blank = True,
    )
    comments = models.TextField(
        verbose_name=_('comments'),
        help_text=_('''Distinctiveness (moving with a wheelchair, glad to use an available magnetic-field loop, blind, deep geek, ...).'''),
        blank = True,
    )
    pgp_fingerprint = models.CharField(
        verbose_name=_('PGP/GPG Fingerprint'),
        max_length=256,
        help_text=_('With size. Example: 1024/D:7729 65E9 4533 414E A1D4 C790 C793 E99F 8A1D E03D'),
        blank = True,
    )
    is_volunteer = models.BooleanField(_('I want to help'),default=False, help_text=_('Would you like to give some hours to help during the event?'))
    is_active = models.BooleanField(_('Active'),default=True)
    is_admin = models.BooleanField(_('Administrator'), default=False)

    objects = HackerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

