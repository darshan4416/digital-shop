from django.shortcuts import HttpResponse, redirect

def login_required(get_response):
    def middleware(request, product_id):
        user = request.session.get('user')
        if user:
            response = get_response(request,product_id)
            return response
        else:
            url = request.path
            return redirect(f'/login?return_url={url}')
    return middleware
