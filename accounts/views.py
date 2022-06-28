from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method=='POST':
        # req.POST is to acccess post data
        form=UserCreationForm(request.POST)
        # it validates the form --> is the username ok etc
        if form.is_valid():
            form.save()
            # log the user
            return redirect('articles:list')
    else:
        form=UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})
