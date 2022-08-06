from django.shortcuts import render
from .models import QRcode
from .forms import QrcodeCreate
# from .qr import *

# Create your views here.


def qrcode_detail_dy_view(request, code_id):
    # TODO: apply this
    obj = QRcode.objects.get(id=code_id)
    context = {
        'title': obj.title,
        'date': obj.date_created,
        'url': obj.base_url,
        'type': obj.type_qr,
        'stats': obj.stats
    }
    return render(request, 'qr_gen/qr_detail.html', context)


def qrcode_create_view(request):

    qr_form = QrcodeCreate()
    if request.method == "POST":
        qr_form = QrcodeCreate(request.POST)
        if qr_form.is_valid():
            QRcode.objects.create(**qr_form.cleaned_data)
            # qr_form.save()
            # qr_form = QrcodeCreate()
        else:
            print(qr_form.errors)

    context = {'form': qr_form}
    return render(request, 'qr_gen/qr_create.html', context)
"""
    initial_data = {
        'light': 'white',
        'dark' : 'black'
    }
    qr_form = QrcodeCreate(request.POST, initial=initial_data)
    """