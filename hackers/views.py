from django.views.generic.edit import UpdateView
from hackers.models import Hacker
from hackers.forms import HackerUpdateForm

class HackerUpdate(UpdateView):
    model = Hacker
    form_class = HackerUpdateForm
    def get_object(self):
        return self.request.user
