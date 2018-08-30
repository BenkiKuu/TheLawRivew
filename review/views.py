from django.shortcuts import render, redirect
from .forms import NewProfileForm, NewLawFirmForm, NewDemandLetterForm, NewAfidavitForm
from .models import Profile

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
            demand.save()
            return redirect('new_demand_temp')
    else:
        form = NewDemandLetterForm(initial={
            'firstname': request.user.profile.first_name,
            'sirname': request.user.profile.last_name,
            'idnumber': request.user.profile.id_number,
        })
    return render(request, 'forms/demand_letter.html', {"form": form})

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
