from django.shortcuts import render,redirect
from . models import  user_signup
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate

@never_cache
def login(request):
   if 'username' in request.session:
      return redirect(home)
   if 'username2' in request.session:
      return redirect(admin_home)
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get("password")
      try:
          user = user_signup.objects.get(username = username,password = password)
          if user:
             request.session['username'] = username
             return redirect(home)
      except:
         return render(request,'app1\login.html',{'taken':'User not Found...!'})
   return render(request,'app1\login.html')


@never_cache
def signup(request):
   if 'username' in request.session:
       return render(request,'app1/home.html')
   if 'username2' in request.session:
      return redirect(admin_home)
   if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
      cpassword = request.POST.get('cpassword')
      if password == cpassword:
         if user_signup.objects.filter(username = username).exists():
            return render(request,'app1/signup.html',{'message':'Username Already Exits...!'})
         if user_signup.objects.filter(email = email).exists():
            return render(request,'app1/signup.html',{'message':'Email Already Exists...!'})
         else:
            user_signup(username=username,password=password, email=email).save()
            return render(request,'app1/signup.html',{'taken':'Successfully Registered...'})
      else:
         return render(request,'app1/signup.html',{'message':'Password Incorrect...!'})
   return render(request,'app1\signup.html')

@never_cache
def home(request):
   if 'username' in request.session:
       return render(request,'app1/home.html')
   if 'username2' in request.session:
      return redirect(admin_home)
   else:
      return redirect(login)
    
def logout(request):
   if request.method =='POST':
       request.session.flush()
       return redirect(login)
   
@never_cache
def admin_login(request):
   if 'username2' in request.session:
      return redirect(admin_home)
   if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username = username , password = pass1)
        if user:
           request.session['username2'] = username
           datas = user_signup.objects.all()
           return redirect(admin_home)
        else:
           return render(request,'app1/admin_login.html',{'message':'invalid credantials..!'})
   return render(request,'app1/admin_login.html')

   
@never_cache
def admin_home(request):
   if 'username2' in request.session:
      search = request.POST.get('search')
      if search:
          return render(request,'app1/admin_home.html',{'datas':user_signup.objects.filter(username__istartswith = search)})

      return render(request,'app1/admin_home.html',{'datas':user_signup.objects.all()})
   else:
      return redirect(admin_login)

   
@never_cache
def admin_adduser(request):
    if 'username2' in request.session:
         if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            if password == cpassword:
               if user_signup.objects.filter(username = username).exists():
                  return render(request,'app1/admin_adduser.html',{'message':'Username Already Exits...!'})
               if user_signup.objects.filter(email = email).exists():
                  return render(request,'app1/admin_adduser.html',{'message':'Email Already Exists...!'})
               else:
                  user_signup(username=username,password=password, email=email).save()
                  return render(request,'app1/admin_adduser.html',{'taken':'Successfully Registered...'})
            else:
               return render(request,'app1/admin_adduser.html',{'message':'Password Incorrect...!'})
         return render(request,'app1/admin_adduser.html')
    else:
       return redirect(admin_login)

   

def admin_edit(request,id):
   user = user_signup.objects.get(id=id)
   if request.method == 'POST':
      user.username = request.POST.get('username')
      user.email = request.POST.get('email')
      user.save()
      return redirect(admin_home)
   return render(request,'app1/admin_edit.html',{'user':user})

   

def admin_delete(request,id):
   user = user_signup.objects.get(id=id)
   user.delete()
   return redirect(admin_home)

@never_cache
def admin_logout(request):
   if 'username2' in request.session:
      request.session.flush()
      return redirect(admin_login)






# Create your views here.
