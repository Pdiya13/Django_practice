from django.shortcuts import render
from .models import ChaiVarity,store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais' : chais})

def temp(request):
    return render(request,'chai/temp.html')

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVarity,pk=chai_id)
    return render(request,"chai_details.html",{'chai': chai})

def chai_print(request,chai_type):
    chai = get_object_or_404(ChaiVarity, type__iexact=chai_type)
    return render(request,"chai_details.html",{'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()