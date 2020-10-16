from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404,redirect
from django.http import *

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import *
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from .models import *
from .forms import *
from django.db.models import Q


class HomeView(ListView):
    queryset = Product.objects.filter(is_available=True)
    template_name = 'home.html'
    paginate_by=4
    context_object_name = 'car'
    
    '''def get_context_data(self,**kwargs):
        ctx = super(HomeView,self).get_context_data(**kwargs)

        cars = Car.objects.filter(is_available=True)
        
        ctx['cars']=cars
        return ctx
    '''
    
'''class CarDetail(DetailView):
    template_name='car_detail.html'
    model = Car
    context_object_name = 'car_list'

    def get_context_data(self,*args):
        print(args)
        ctx = super(CarDetail,self).get_context_data(**kwargs)

        cars = Detail.objects.get(is_available=True)
        
        ctx['cars']=cars
        return ctx'''

def  CarDetail(request,d):
    car_list=Product.objects.get(id=d)
    ob=Product.objects.all()
    return render(request,"car_detail.html",{"car_list":car_list,"ob":ob})




'''def CarDetail(request, category_slug=None,d):


    category =Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        
    return render(request, 'car_detail.html', {'category': category,
                                                      
                                                      })'''






def NewBooking(request,c):
    car = Product.objects.get(id=c)
    if request.method == "POST":
        form = Booking_form(request.POST)
        if form.is_valid():
           
            #car = Product.objects.get(name=c)
            new_booking=form.save(commit=False)
            
            

            new_booking.car=car

            new_booking.is_approved = False

            new_booking.save()
            

            
            
            
            
            return HttpResponse('mission over')
            #return redirect('listinfo',car=car.id)
            
    else:
        form=Booking_form()
    
    return render(request,'book_car.html',{'form':form})
       
        
    
    
class BookingDetail(ListView):
    '''
    def get_car(self):
        car_pk = self.kwargs['car']
        car = Car.objects.get(pk=car_pk)

        return car
    '''
    def get(self,request,*args,**kwargs):
        car = Product.objects.get(id=self.kwargs['car'])
        #car=self.get_car()
        info = Booking.objects.get(car=car)
        return render(request,'booking_detail.html',{'info':info})
    
    
def search(request):
    if request.method =='POST':

        
        squery = request.POST.get('search_box', None)
        s = Product.objects.filter(Q(name__icontains=squery) | Q(price__icontains=squery ))
        if s:
            return render(request,'car_search.html',{'q':s})
        else:
            return render(request,'car_notfound.html')
            
            
    return render(request,'car_search.html',{'q':s})


def contactus(request):
    return render(request,"contactus.html")


def login(request):
    return render(request,"login.html")

def auth_view(request):
    print("hello")
    username=request.POST["username"]
    password=request.POST["password"]

    user=auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)

        return HttpResponseRedirect("/logged_in/")

    else:

        return HttpResponseRedirect("/invalid/")

def loggedin(request):
    if request.user.is_authenticated():
        return render(request,"loggedin.html",{"fullname":request.user.username})

    else:
        return HttpResponse("Page not found")



def register_user(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/register_success/")

    else:
        form=UserCreationForm()
    return render(request,"register.html",{"form":form})

def register_success(request):
    return render(request,'register_success.html')

def invalid_login(request):
    return render(request,"invalid_login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def nextpage(request):
    return render(request,'contact.html')
