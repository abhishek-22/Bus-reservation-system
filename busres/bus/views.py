from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm
from django.db.models import Q
from bus.models import BusDet, Bookingdets
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required
def busbooking(request):
    if request.method == 'POST':
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        bus = []
        if q1:
            if q2:
                if q3:
                    bus = BusDet.objects.filter(
                        origin__icontains=q1, destination__icontains=q2, date=q3)
                else:
                    bus = None
            else:
                bus = None
        else:
            bus = None
        if bus:
            return render(request, 'busresults.html', {'bus': bus})
        else:
            messages.info(
                request, "The bus you have searched is not available")
            return redirect('busbooking')
    else:
        return render(request, 'bussearch.html')


@login_required
def seat(request, id):
    object = BusDet.objects.get(pk=id)
    return render(request, 'seatselect.html', {'object': object})


@login_required
def bookingconf(request, id):
    if request.method == "GET":
        object = BusDet.objects.get(pk=id)
        sc = int(request.GET.get('seats'))
        if object.seats >= sc:
            if request.user.is_authenticated:
                bcnf = Bookingdets.objects.create(
                    user=request.user, bus=object, nos=sc)
                object.seats = object.seats - sc
                object.save()
                messages.success(request, "Your booking has been confirmed")
                return redirect('home')
            else:
                messages.error(
                    request, "The user has not logged in, hence booking incomplete")
                return redirect('home')
        else:
            messages.error(
                request, "Seats not available, hence booking incomplete")
            return redirect('home')
    messages.error(
        request, "Sorry! error occured while booking please try again!")
    return render(request, 'home.html')


@login_required
def bookinghist(request):
    us = request.user
    object = Bookingdets.objects.filter(user=request.user)
    return render(request, 'bookinghist.html', {'object': object})


@login_required
def bookingcancel(request, id):
   obj = Bookingdets.objects.filter(id=id)
   bs = obj.bus
   ns = obj.nos
   obj.delete()
   bs.seats = bs.seats + ns
   messages.success(request, "booking canceled successfully")
   return redirect('home')
