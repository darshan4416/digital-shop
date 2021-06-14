from django.views import View
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password, make_password
from shop.models import User


class SigninView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == "POST":
            try:
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                password = request.POST.get('password')
                hashed_password = make_password(password=password)
                user = User(name=name, email=email, phone=phone, password=hashed_password)
                result = user.save()
                return render(request, 'login.html')
            except:
                return render(request, 'signup.html', {'error': "User already registered"})
