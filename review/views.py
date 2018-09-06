from django.shortcuts import render, redirect
from .forms import NewProfileForm, NewLawFirmForm, NewDemandLetterForm, NewAfidavitForm
from .models import Profile, DemandLetter
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .email import email_doc
import qrcode
from . utility import generateUniqueKey
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

# Create your views here.
def home(request):
    # NewProfileForm=form
    return render(request, 'index.html', locals())
#
#
def new_profile(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user_id=current_user)
    form = NewProfileForm()

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = current_user
            user_profile.save()
            return redirect('index')
    else:
        form = NewProfileForm()
    return render(request, 'forms/new_profile.html', {"form": form})

def new_firm(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewLawFirmForm(request.POST, request.FILES)
        if form.is_valid():
            lawfirm = form.save(commit=False)
            lawfirm.user = current_user
            lawfirm.save()
            return redirect('home')
    else:
        form = NewLawFirmForm()
    return render(request, 'forms/new_firm.html', {"form": form})

def new_demand(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewDemandLetterForm(request.POST, request.FILES)
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = current_user.profile
            demand.uniquekey = generateUniqueKey()
            demand.save()
            # firstname = form.cleaned_data['firstname']
            # sirname = form.cleaned_data['sirname']
            # othernames = form.cleaned_data['othernames']
            # idnumber = form.cleaned_data['idnumber']
            # boxnumber = form.cleaned_data['boxnumber']
            # town = form.cleaned_data['town']
            # email = form.cleaned_data['email']
            inputs = form.cleaned_data
            email_doc(inputs)
            return redirect('new_demand_temp')
    else:
        form = NewDemandLetterForm(initial={
           'firstname': request.user.profile.firstname,
           'sirname': request.user.profile.sirname,
           'othernames': request.user.profile.othernames,
           'idnumber': request.user.profile.idnumber,
           'boxnumber': request.user.profile.boxnumber,
           'town': request.user.profile.town,
           'email': request.user.profile.email,
           })
    return render(request, 'forms/demand_letter.html', {"form": form})

def doc_email(request):
    if request.method == 'POST':
        form = NewDemandLetterForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            sirname = form.cleaned_data['sirname']
            othernames = form.cleaned_data['othernames']
            idnumber = form.cleaned_data['idnumber']
            boxnumber = form.cleaned_data['boxnumber']
            town = form.cleaned_data['town']
            email = form.cleaned_data['email']
            recipient = DocumentRecepients(firstname = firstname, sirname = sirname, othernames = othernames, idnumber = idnumber, boxnumber = boxnumber, town = town, email = email)
            recepient.save()
            email_doc(firstname,sirname,othernames,idnumber,boxnumber,town)
            HttpResponseRedirect('demand_tmp')

    return render(request, 'documents/demand_letter_doc.html', locals())


def new_aff(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewAfidavitForm(request.POST, request.FILES)
        if form.is_valid():
            affidavit = form.save(commit=False)
            affidavit.user = current_user
            affidavit.save()
            return redirect('home')
    else:
        form = NewAfidavitForm()
    return render(request, 'forms/affidavit.html', {"form": form})

def profile(request, profile_id):
    profile = Profile.objects.filter(user_id=profile_id).first()
    return render(request, 'profile.html', locals())

def demand_tmp(request):
    affs = request.user.profile.legals.all()
    return render(request, 'documents/demand_letter_doc.html', locals())

def qrcodes(request):

   return render(request, 'qrcode.html')


def africa_talking(request):
    # Specify your login credentials
    username = "Max_.h"
    apikey   = "cd06068afc592bedeed691307b41fe44e003f68e6521fa37614afdbc9b5a39ac"
    # username = "sandbox"
    # apikey   = "54a2cd06ea9b6118b691567a856ab4b92eeb3621e1b753e5f26815c967f44072"
    # Specify the numbers that you want to send to in a comma-separated list
    # Please ensure you include the country code (+254 for Kenya)
    
    to      = "+254716280403,+254724401515"
    # And of course we want our recipients to know what we really do
    
    message = "random txt"
    # Create a new instance of our awesome gateway class
    gateway = AfricasTalkingGateway(username, apikey, "sandbox")
    #*************************************************************************************
    #  NOTE: If connecting to the sandbox:
    #
    #  1. Use "sandbox" as the username
    #  2. Use the apiKey generated from your sandbox application
    #     https://account.africastalking.com/apps/sandbox/settings/key
    #  3. Add the "sandbox" flag to the constructor
    #
    #  gateway = AfricasTalkingGateway(username, apiKey, "sandbox");
    #**************************************************************************************
    # Any gateway errors will be captured by our custom Exception class below,
    # so wrap the call in a try-catch block
    try:
        # Thats it, hit send and we'll take care of the rest.

        results = gateway.sendMessage(to, message)
        print(results)

        for recipient in results:
            # status is either "Success" or "error message"
            print('number= %s;status= %s;statusCode= %s;messageId= %s;cost= %s' % (recipient['number'], recipient['status'], recipient['statusCode'], recipient['messageId'], recipient['cost']))
    except AfricasTalkingGatewayException as e:
        print('Encountered an error while sending: %s' % str(e))

    return HttpResponse("message succesfully sent")