from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method=='POST':
        # req.POST is to acccess post data
        form=UserCreationForm(request.POST)
        # it validates the form --> is the username ok etc
        if form.is_valid():
            user = form.save()
            # log the user
            login(request, user)
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        # data is not the 1st parameter of fn by default
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user
            user = form.get_user()
            login(request, user)
            #  if there is next query 
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('articles:list')
    else:
        form=AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')