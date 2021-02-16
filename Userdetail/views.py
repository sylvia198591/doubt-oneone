from django.shortcuts import render,redirect
from Userdetail.forms import RegistrationForm, EditUserDetailsForm
# from ownerapp.models import Mobile,Brand
from Userdetail.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse,HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import *
from django.views.generic import *
# from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
# from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# from django.conf import settings
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib import messages
import urllib.parse
# from urlparse import urlparse
# Create your views here.
class createUser(TemplateView):
    form_class=RegistrationForm

    model_name=User

    template_name = "Userdetail/registration.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["form1"] = self.form_class1
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        # form1=self.form_class1(request.POST)
        # User = get_user_model()
        if form.is_valid():
            print("aa2")
            # form.save()
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            accno = form.cleaned_data["accno"]
            # username, first_name, last_name, email, password, accno = kwargs['username'], kwargs['first_name'], kwargs[
            #     'last_name'], kwargs['email'], kwargs['password1'], kwargs['accno']
            qs = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)

            qs.set_password(password1)
            qs.save()
            rs=User.objects.get(username=username)
            print("rs:",rs.username)
            qs1 = cuser.objects.create(username=qs,accno=accno)
            qs1.save()
            # qs = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, \
            #                          username=username,password1=password1, password2
            #                          =password2, accno=accno)
            # # )
            #
            # def get_success_url(self):
            #
            #     print("qs")
            #     pk = self.kwargs["pk"]
            pk=qs.id
            print(pk)
            # return reverse("upd", pk=kwargs[pk])
            # qs.save()
            return redirect("login")
        else:
            # return JsonResponse({"message": "loginSuccess", 'status': 200})

            # else:
            return render(request, self.template_name, {"form": form})



    # def get_success_url(self):
    #     return reverse('author-detail', kwargs={'pk': self.object.pk})
class LoginView(FormView):
    form_class = AuthenticationForm

    success_url = reverse_lazy('userHome')
    template_name = 'Userdetail/login.html'
    # def post(self,request,*args,**kwargs):
    #     print("aa")
        # form=self.form_class(request.POST)
    # def form_valid(self, form_class):
    #     print("aa")
    #     # form=self.form_class(request.POST)

class userUpdate(UpdateView):
    model = User
    fields=['email']
    template_name="Userdetail/login.html"
# class LoginView(FormView):
#     form_class = AuthenticationForm
#
#     success_url = reverse_lazy('userhome')
#     template_name = 'Userdetail/login.html'
def userHome(request):
    return render(request, "Userdetail/userhome.html")
    # def get(self,request,*args,**kwargs):
    #     context={}
    #     context["form"]=self.form
    #     # context["form1"] = self.form_class1
    #     return render(request,self.template_name,context)
    #
    # def post(self, request, *args, **kwargs):
    #     print('aa')
    #     # form = self.get_form_class()
    #     form = self.form(request.POST)
    #     # Verify form is valid
    #     if form.is_valid():
    #         print("AA")
    #         # Call parent form_valid to create model record object
    #         super(LoginView, self).form_valid(form)
    #         # Add custom success message
    #         messages.success(request, 'Item created successfully!')
    #         # Redirect to success page
    #         return HttpResponseRedirect(self.get_success_url())
    #     else:
    #         print("bg")
    #     # Form is invalid
    #     # Set object to None, since class-based view expects model record object
    #     # self.object = None
    #     # Return class-based view form_invalid to generate form with errors
    #     return render(request, self.template_name, {"form": form})

    # def form_valid(self, form_class):
    #     super(LoginView, self).form_valid(form_class)
    #     # Add action to valid form phase
    #     messages.success(self.request, 'Item created successfully!')
    #     return HttpResponseRedirect(self.get_success_url())
    #
    # def form_invalid(self, form_class):
    #     # Add action to invalid form phase
    #     return self.render_to_response(self.get_context_data(form=form_class))
# def userRegistration(request):
#     form=RegistrationForm()
#     print("aa")
#     context={}
#     context["form"]=form
#     if request.method=='POST':
#         print("aa1")
#         form=RegistrationForm(request.POST)
#         print("aa3")
#         if form.is_valid():
#             print("aa2")
#             # form.save()
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             email = form.cleaned_data["email"]
#             password1 = form.cleaned_data["password1"]
#             password2 = form.cleaned_data["password2"]
#             accno = form.cleaned_data["accno"]
#             qs = User.objects.create(first_name=first_name, last_name=last_name, email=email, \
#                                       password1=password1, password2
#                                       =password2, accno=accno)
#                                         # )
#
#             qs.save()
#             return redirect("login")
#         else:
#             context["form"]=form
#             return render(request, "Userdetail/registration.html", context)
#
#     return render(request,"Userdetail/registration.html",context)

# Create your views here.

# def userRegistration(request):
#     form=RegistrationForm()
#     print("aa")
#     context={}
#     context["form"]=form
#     if request.method=='POST':
#         print("aa1")
#         form=RegistrationForm(request.POST)
#         print("aa3")
#         if form.is_valid():
#             print("aa2")
#
#             form.save()
#             cuser.save()
#             return redirect("login")
#         else:
#             context["form"]=form
#             return render(request, "Userdetail/registration.html", context)
#
#     return render(request,"Userdetail/registration.html",context)



@login_required(login_url='login')
def userLogout(request):
    logout(request)
    return redirect("login")

def editUserDetails(request):
    user=User.objects.get(username=request.user)
    form=EditUserDetailsForm(instance=user)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=EditUserDetailsForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("userhome")
        else:
            context["form"]=form
            return render(request,"Userdetail/editprofile.html",context)
    return render(request, "Userdetail/editprofile.html", context)



