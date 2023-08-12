from django.shortcuts import render,redirect
from .models import Products,Cart,CartItem

# Create your views here.

def product(request):
    
    p={
        'pro':Products.objects.all()
    }

    return render(request,'product.html',p)
# class cartview(View):
#     def get(self,request,pk):
#         item=Products.objects.get(pk=pk)
#         return render(request,'cart.html',locals())
     
     
# cart.py
def add_to_cart(request, product_id):
    product = Products.objects.get(pk=product_id)
    cart, created = Cart.objects.get_or_create()
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart, created = Cart.objects.get_or_create()
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})