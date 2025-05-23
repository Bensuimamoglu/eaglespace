from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect("post-list")
   
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("post-list")
        else:
            return render(request, "account/login.html", {
                "error": "The username or password is incorrect. Please try again."
            })

    

    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("post-list")

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html",
                               {
                                   "error":"Username is used. Please, log in your username again!", 
                                   "username":username,
                                   "email":email,
                                   "firstname":firstname,
                                   "lastname":lastname
                                   
                                })
            else:
               if User.objects.filter(email=email).exists():
                return render(request, "account/register.html",
                               {
                                   "error":"E-mail is used. Please, log in your e-mail again!",
                                   "username":username,
                                   "email":email,
                                   "firstname":firstname,
                                   "lastname":lastname
                                   
                                })
               else:
                   user = User.objects.create_user(username=username,email=email,first_name=firstname, 
                                              last_name=lastname,password=password)
                   user.save()
                   return redirect("login")
        
                    


        else:
            return render(request, "account/register.html", 
                          {
                                "error": "Password does not match!",
                                "username":username,
                                "email":email,
                                "firstname":firstname,
                                "lastname":lastname
                            })


    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("giris")

