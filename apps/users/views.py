from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/register_success.html')
        else:
            return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})