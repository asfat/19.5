from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .models import Musician
from .forms import MusicianCreationForm,MusicianForm
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.shortcuts import render, get_object_or_404

# Create your views here.
class Usrlogin(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class Register(CreateView):
        model = Musician
        form_class = MusicianCreationForm
        template_name = 'register.html'	
        def get_success_url(self):
            return reverse_lazy('home')
        def form_valid(self, form):
            self.object = form.save()
            return super().form_valid(form)		

def UrsLogout(request):
     logout(request)
     return redirect('login')

def editmusic(request, id):
    print(f"Available Musician IDs: {Musician.objects.values_list('id', flat=True)}")
    musician = get_object_or_404(Musician, pk=id)
    musicianForm = MusicianForm(instance=musician)
    return render(request, 'login.html', {'musicianForm': musicianForm})