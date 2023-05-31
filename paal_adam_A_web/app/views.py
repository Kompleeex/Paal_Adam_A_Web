from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import *
from .forms import *
from .filters import tesztFilter

tesztId = None


def index(request):
    global tesztId
    tesztek = Teszt.objects.all()
    tesztekFilter = tesztFilter(request.GET, queryset = tesztek)
    recept = tesztek.filter(Q(id__exact = tesztId)).first()

    context = {
        "tesztek" : tesztek,
        "tesztekFilter" : tesztekFilter,
        "recept" : recept
    }

    return render(request, 'index.html', context = context)

def feltolt(request):
    form = tesztForm(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            return redirect(index)
    else:
        form = tesztForm()

    context = {
        "form" : form
    }

    return render(request, "feltoltes.html", context = context)



