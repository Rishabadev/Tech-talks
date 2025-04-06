from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            user.set_password(raw_password)
            user.save()

            # Add user to 'User' group
            user_group = Group.objects.get(name='User')
            user.groups.add(user_group)

            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})
    

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if user.groups.filter(name='Admin').exists():
            return reverse_lazy('admin_app:home')
        else:
            return reverse_lazy('techtalks:home')

