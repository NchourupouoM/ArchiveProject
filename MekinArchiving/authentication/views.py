from django.views.generic import View
from authentication import forms, models
from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login

class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm
    
    def get(self,request):
        form = self.form_class()
        message = ''
        return render(request,self.template_name,context = {'form':form,'message':message})
    
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None :
                login(request,user)
                return redirect('home')
        message = "Identifiants invalide."
        return render(request,self.template_name,context = {'form':form,'message':message})

def logout_user(request):
    logout(request)
    return redirect('login')

def mon_compte(request):
    user = request.user
    return render(request,'authentication/mon_compte.html',{"user":user})

def photo_upload(request):
    form = forms.PhotoProfil(instance=request.user)
    if request.method == 'POST':
        form = forms.PhotoProfil(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('mon-compte')
    return render(request,'authentication/updated_profil_photo.html',{'form':form})