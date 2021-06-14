from django.shortcuts import HttpResponse, redirect

def canNotAcessAfterLogin(get_response):
    def middleware(request):
        user = request.session.get('user')
        if user:
           return redirect('index')
        else:
            return get_response(request)
    return middleware
