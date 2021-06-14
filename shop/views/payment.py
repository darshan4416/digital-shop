from django.shortcuts import render, HttpResponse, redirect
from app.settings import PRIVATE_API_KEY, PRIVATE_AUTH_TOKEN
from instamojo_wrapper import Instamojo
from shop.models import Product, User, Payment
import math

api = Instamojo(api_key=PRIVATE_API_KEY,
                    auth_token=PRIVATE_AUTH_TOKEN,
                    endpoint='https://test.instamojo.com/api/1.1/');

def createPayment(request, product_id):

    user = request.session.get('user')
    print(user)
    userObject = User.objects.get(id=user.get('id'))
    product = Product.objects.get(id=product_id)
    amount = (product.price - (product.price * (product.discount/100)))

    # Create a new Payment Request
    response = api.payment_request_create(
        amount=math.floor(amount),
        purpose=f'Payment for {product.name}',
        buyer_name=userObject.name,
        send_email=True,
        email="darshanhirekurbar@gmail.com",
        redirect_url="http://localhost:8000/complete-payment"
    )
    # print the long URL of the payment request.
    print(response)
    payment_request_id = response['payment_request']['id']
    payment = Payment(user=User(id=user.get('id')),
                      product=product,
                      payment_request_id=payment_request_id)
    payment.save()
    url = response['payment_request']['longurl']
    # print the unique ID(or payment request ID)
    print(url)
    return redirect(url)

def verifyPayment(request):
    user = request.session.get('user')
    userObject = User.objects.get(id=user.get('id'))

    payment_id = request.GET.get('payment_id')
    payment_request_id = request.GET.get('payment_request_id')

    response = api.payment_request_payment_status(payment_request_id, payment_id)

    status = response['payment_request']['status']
    print("status", status)
    if status == "Completed":
        payment = Payment.objects.get(payment_request_id = payment_request_id)
        payment.payment_id = response['payment_request']['payment']['payment_id']
        payment.status = status
        payment.save()
        print("if")
        return render(request, "download_after_payment.html", {'payment':payment})
    else:
        print("else")
        return render(request, "payment_failed.html")

    print(response)

def downloadPaidProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    session_user = request.session.get('user')
    user = User(id=session_user.get('id'))
    try:
        payment = Payment.objects.filter(product=product.id, user=user)
        if len(payment) > 0:
            print(len(payment))
            return redirect(product.file.url)
        else:
            return redirect('index')
    except:
        return redirect('index')














