from django.shortcuts import render, redirect
from .models import Customer

def customer_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address
        )

        return redirect('customer_list')

    return render(request, 'insurance/customer_form.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(
        request,
        'insurance/customer_list.html',
        {'customers': customers}
    )
