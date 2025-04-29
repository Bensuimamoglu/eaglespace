from django.http.response import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def giris(request):
    return render(request, "landing/giris.html")
def index(request):
    if not request.user.is_authenticated:
        return redirect("post-list")
    return render(request, "landing/index.html", )

