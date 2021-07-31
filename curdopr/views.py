from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import VoterForms,Delete,Updates
from .models import Voters

# Create your views here.

def Index(request):
    return render(request,'curdopr/index.html')

def Insert(request):

    v=Voters.objects.all()

    if request.method=='POST':
        forms=VoterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/curdopr/insert')

    else:
        forms=VoterForms()
    return render(request,'curdopr/insert.html',{'forms':forms,'votes':v})

def Deletes(request):
    if request.method=="POST":
        forms=Delete(request.POST)
        if forms.is_valid():

            getsVoter=Voters.objects.filter(email__exact=forms.cleaned_data['email'])
            getsVoter.delete();
            return redirect('/curdopr/insert')
    else:
        forms=Delete()

    return render(request,'curdopr/delete.html',{'forms':forms})


# def Update(request,id):
#     print(id)
#     if request.method=="POST":
#         forms=Updates(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('/curdopr/insert')
#     else:
#         forms=Updates()
#     return render(request,'curdopr/update.html',{'forms':forms})

# Update Method
def Update(request,id):
    item=Voters.objects.get(id=id)
    updateForm=Updates(instance=item)
    if request.method=='POST':
        forms=Updates(request.POST,instance=item)
        if forms.is_valid():
            forms.save()
            return redirect('/curdopr/insert')
    return render(request,'curdopr/update.html',{"forms":updateForm})