from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from .models import MyUser
from .forms import RegForm,LoginForm
# Create your views here.
class UserRegistration(TemplateView):
    model=MyUser
    form_class=RegForm
    template_name = "register.html"
    context={}

    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            self.context["form"]=form
            return render(request, self.template_name, self.context)

class LoginView(TemplateView):
    form_class=LoginForm
    template_name = "login.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            # user = MyUser.objects.get(email=email)
            user=authenticate(request,username=email,password=password)

            # if (user.email==email) & (user.password==password):
            if user:
                print("sucess")
                login(request, user)
                return redirect("home")
            else:
                form=self.form_class()
                self.context["form"] = form
                return render(request, self.template_name, self.context)
