from django.contrib import admin
from django.urls import path, include
from .views.index import index, logout
from .views import LoginView, SigninView
from .views.products import productDetails
from .views.download import downloadFree
from .views.payment import createPayment, verifyPayment, downloadPaidProduct
from .middlewares.login_required import login_required
from .middlewares.can_not_acess_after_login import canNotAcessAfterLogin


urlpatterns = [
    path('', index, name='index'),

    path('login/', canNotAcessAfterLogin(LoginView.as_view()), name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', canNotAcessAfterLogin(SigninView.as_view()), name='signup'),
    # path('send-otp/', sendOtp, name="send_otp"),

    path('product/<int:product_id>/', productDetails, name='product_details'),
    path('download-free/<int:product_id>/', downloadFree, name='downloadFree'),

    path('create-payment/<int:product_id>/', login_required(createPayment), name='createPayment'),
    path('complete-payment/', verifyPayment, name='verifyPayment'),
    path('download/paid/<int:product_id>/', login_required(downloadPaidProduct), name='downloadPaidProduct'),
]
