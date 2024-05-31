from django.shortcuts import render, redirect

from .forms import SignUpForm


def hello(request):
    return render(request, "accounts/hello.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("accounts:login")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})
