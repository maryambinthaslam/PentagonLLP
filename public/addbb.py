from django.shortcuts import render
from product.models import Product
from product.models import Category
from django.core.files.storage import FileSystemStorage


def add_business(request):
    uid=request.session["u_id"]
    ob1 = Category.objects.all()
    ob = Product.objects.all()
    context = {
        'x': ob,
        'y': ob1
    }
    if request.method == "POST":
        ob = Product()
        ob.product_name = request.POST.get('pname')
        ob.product_price = request.POST.get('pprice')
        myfile = request.FILES['pm']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        ob.product_image = myfile.name
        ob.category_id = request.POST.get('ctg')
        ob.product_description = request.POST.get('pdesc')
        ob.available_qty = request.POST.get('availqty')
        ob.product_expiry = request.POST.get('pexpiry')
        ob.seller_details = request.POST.get('sellerdet')
        ob.farmer_id = uid
        ob.save()
    return render(request, 'businessbasket.html', context)