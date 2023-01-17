from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse_lazy
from . models import Country,Countrylanguage, City

# Create your views here.

def Country_view_search(request):
    if request.COOKIES.get('can_otp_enter'):
        if request.method == "POST":
            lookup = request.POST.get('searched')
            # print(Country.objects.filter(name__icontains=lookup))
            country=Country.objects.filter(Q(name__iexact=lookup))  
            city = City.objects.filter(Q(name__iexact=lookup))
            language = Countrylanguage.objects.filter(Q(language__icontains=lookup))
            return render(request, 'country/searchlist.html',{'country': country, 'city': city, 'language': language})
        
        else :
            country =Country.objects.all()
            city = City.objects.all()
            language= Countrylanguage.objects.all()
            return render(request, 'country/search.html', {'country': country, 'city': city, 'language': language})
        
    else:
        return HttpResponseRedirect(reverse_lazy('account:login'))

def countryviewlist(request,code):
    country= Country.objects.filter(code=code)
    return render(request, 'country/searchview.html',{'country': country})