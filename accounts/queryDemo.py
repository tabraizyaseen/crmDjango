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




# Execute Custom SQL
    '''
    cursor = connection.cursor()
    cc = 'scrapper_tbl_amazon_category'
    sql = f'select * from {cc} where title like "%%m31%%"'
    # sql = 'create table tbl_test2(test_name VARCHAR(50))'
    # sql = "update scrapper_tbl_amazon_category  set title='Samsung Galaxy M31s' where sku='B08FMN63DV'"
    cursor.execute(sql)
    # posts = dictfetchall(cursor)
    '''





    # __contains works same like 'like' in sql but it's case-sensitive
    '''
    tbl_amazon_category.objects.filter(title__contains='Apple')
    '''

    #This block is to fetch data from database
    '''
    all_data = tbl_amazon_category.objects.all()


    for data in all_data:
        print(data.sku)
        print(data.title)
    
    return render(request,'home.html',{})
    '''

    # This block will insert and commit one by one
    '''
    results = category(url)
    for result in results:
        category_result = tbl_amazon_category(
            sku=result[0],
            url=result[1],
            title=str(result[2]),
            image=result[3],
            price=result[4],
            old_price=result[5]
            )
        category_result.save()
    

    return render(request,'home.html',{})
    '''

    # This Block is for saving single record
    '''
    p_id,link,title,image,price,old_price = category(url)
    category_result = tbl_amazon_category(
        sku=p_id,
        url=link,
        title=title,
        image=image,
        price=price,
        old_price=old_price
        )
    category_result.save()
    return render(request,'home.html',{})
    '''



    # Check query running behind ORM
    '''
    from django.db import connection
    print(connection.queries)
    '''

    # Or Query 
    '''
    print(tbl_amazon_category.objects.filter(title__startswith="Samsung")) |
    tbl_amazon_category.objects.filter(sku__startswith="B"))
    '''

    # Q objects
    '''
    from django.db.models import Q
    print(tbl_amazon_category.objects.filter(Q(title__startswith="Samsung") | Q(sku__startswith="B") | ~Q(price__lt=100))
    #lt >>> less then
    #lte >>> less then or equal
    #gt >>> greater then 
    #gte >>> greater then or equal
    '''

    # And Query
    '''
    from django.db.models import Q
    print(tbl_amazon_category.objects.filter(Q(title__startswith="Samsung") & ~Q(sku__startswith="B"))
    '''

    # Union Query
    '''
    table1.objects.all().values_list("id").union(table2.objects.all().values_list("id"))
    # The repeated items will be replaced with one
    # if we use values instead of values_list the fetched data will be in dictionary form
    '''

    # Selecting specific columns
    '''
    tbl_amazon_category.objects.values_list('sku','price')
    '''

    # selecting individuals
    '''
    tbl_amazon_category.objects.filter(price__gte=100).only('title')
    '''


