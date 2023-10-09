from django.shortcuts import get_object_or_404, redirect, render
from .models import BasketItem
from store.models import Product

def add_to_basket(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    basket_items = request.session.get('basket_items', [])

    for item in basket_items:
        if item['product_id'] == product_id:
            item['quantity'] += 1
            break
    else:
        basket_items.append({'product_id': product_id, 'quantity': 1})

    request.session['basket_items'] = basket_items

    return redirect('product_detail', product_slug=product.slug)




def remove_from_basket(request, product_id):
    basket_items = request.session.get('basket_items', [])

    for item in basket_items:
        if item['product_id'] == product_id:
            if item['quantity'] > 1:
                item['quantity'] -= 1
            else:
                basket_items.remove(item)
            break

    request.session['basket_items'] = basket_items

    return redirect('basket_view')





def view_basket(request):
    basket_items = []
    total = 0

    basket_items_data = request.session.get('basket_items', [])

    for item_data in basket_items_data:
        product = get_object_or_404(Product, pk=item_data['product_id'])
        quantity = item_data['quantity']
        subtotal = product.price * quantity

        basket_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

        total += subtotal

    print(basket_items)  

    return render(request, 'basket.html', {'basket_items': basket_items, 'total': total})


