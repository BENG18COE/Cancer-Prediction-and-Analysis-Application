from urllib.request import HTTPRedirectHandler
from django.http import Http404, HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import authenticate, login

class LoginPage(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')

    def post(self,request,*args, **kwargs):
       username=request.POST['username']
       password=request.POST['password'] 

       user = authenticate(request, username=username, password=password)
       if user is not None:
            login(request, user)

            return HttpResponseRedirect('/home/')
       else:
            return HttpResponseRedirect('/')
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
       
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...




# class LoginPageView(View):
#     template_name = 'authentication/login.html'
#     form_class = forms.LoginForm
    
#     def get(self, request):
#         form = self.form_class()
#         message = ''
#         return render(request, self.template_name, context={'form': form, 'message': message})
        
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Login failed!'
#         return render(request, self.template_name, context={'form': form, 'message': message})