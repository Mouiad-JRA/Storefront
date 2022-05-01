from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


# Create your views here.

def say_hello(request):
    # query_set = Product.objects.all()  # objects is a manger (Interface to the data base)
    # product = Product.objects.get(pk=1)  # objects is a manger (Interface to the data base)
    # product = Product.objects.filter(pk=1).exists()  # objects is a manger (Interface to the data base)
    # The query set is lazy (evaluate at later points)
    # the query_set evaluate when iterate, convert to list or access object (or slice)
    # for product in query_set:
    #     print(product)
    # list(query_set)
    # query_set[0:5]
    # query_set.filter()  # not evaluate
    queryset = Product.objects.filter(unit_price__range=(20, 30))

    return render(request, "hello.html", {"name": "momo", "products": list(queryset)})
