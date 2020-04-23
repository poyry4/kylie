from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

#def signupView(request):
#    if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             #  log the user in
#             login(request, user)
#             return redirect('accounts:signup')
#    else:
#        form = UserCreationForm()
#    return render(request, 'accounts/signup.htm', { 'form': form })

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()
            login(request, user)
            #return redirect('commercial:adminCommercial')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.htm', { 'form': form })

def logoutView(request):
    if request.method == 'POST':
            logout(request)
            return redirect('accounts:login')