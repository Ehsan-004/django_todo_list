from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout


class LoginView(View):
    template_name = 'login.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        if request.user and request.user.is_authenticated:
            return redirect('todo_user:profile')
        return render(request, self.template_name)

    def post(self, request):
        if request.user and request.user.is_authenticated:
            return redirect('todo_user:profile')
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if False in [username, password]:
            return render(request, self.template_name, {'error': 'Please enter both username and password'})
        user = authenticate(username=username, password=password)
        try:
            login(request, user)
            return redirect('todos:index')
        except:
            return render(request, self.template_name, {'error': 'Wrong username or password'})


class RegisterView(View):
    template_name = 'register.html'
    http_method_names = ['get', ]

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todo_user:profile')
        return render(request, self.template_name)


class ProfileView(View):
    template_name = 'profile.html'
    http_method_names = ['get', ]

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('todos:index')
        logout(request)
        return redirect('todos:index')
