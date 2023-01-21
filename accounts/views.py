from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['age', 'email']
    success_url = reverse_lazy('home')  # TODO change to detailed view
    template_name = 'registration/user_update.html'
