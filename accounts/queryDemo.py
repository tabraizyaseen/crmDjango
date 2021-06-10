from .models import *

customers = Customer.objects.all()

firstCustomer = Customer.objects.first()
lastCustomer = Customer.objects.last()

customerByName = Customer.objects.get(name='Tabraiz')
customerByid = Customer.objects.get(id=2)

# Return all orders related to first customer
firstCustomer.order_set.all()

#Return orders customer name : (Query parent mode)
order = Order.objects.all()
parentName = order.customer.name

products = Product.objects.filter(catergory='Out Door')

# Order/Sort
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# Retrieve with the help of many to many relation
products_tags = Product.objects.filter(tags__name='Sprots')

#if customers has purchased one/many items in bulk this code block will help you
all_orders = {}
for one in firstCustomer.order_set.all():
    if one.product.name in all_orders():
        all_orders[one.product.name] += 1
    else:
        all_orders[one.product.name] = 1

# Return will be like = all_orders: {'Ball':2, 'BBQ Grill':1}


