from django.shortcuts import render, HttpResponse, redirect, reverse 
from django.conf import settings
import stripe 


# Create your views here.

def donation(request):
    return render(request, "donation/ask.template.html")
    
    
def charge(request):
    if request.method == 'GET':  
        amount = request.GET['amount'] 
        stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'donation/donate.template.html', {
                'publishable_key':stripe_publishable_key,
                'amount_in_dollars':amount,
                'amount':int(amount)*100
            })
        # return HttpResponse("here")
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST["stripeToken"]
        charge = stripe.Charge.create(amount=request.POST["amount"],
            currency='usd',
            source=stripe_token
        )
        return HttpResponse("Submitted")

