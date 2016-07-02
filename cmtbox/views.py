from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Member
from .forms import MemberForm
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("hi, i am varsha nd u r in cmtbox index.")

def member_list(request):
    members=Member.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'cmtbox/member_list.html', {'members':members})

def new_member(request):   
    if request.method == "POST":
    	print request.POST
        form=MemberForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data['name']
            n2=form.cleaned_data['relation']
            n3=form.cleaned_data['thought']
            member=Member.objects.create(name=n1, relation=n2, thought=n1)
            return redirect('display_member', {'member':member})
    else:
        form=MemberForm()
    return render(request, 'cmtbox/contact_form.html', {'form':form})

def member_detail(request, pk):
    member=get_object_or_404(Member, pk=pk)
    return render(request, 'cmtbox/member_detail.html',{'member':member})

def display_member(request, pk=None):
    print "in this view", pk
    member=get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form=MemberForm(request.POST, instance=member)
        if form.is_valid():
            n1=form.cleaned_data['name']
            n2=form.cleaned_data['relation']
            n3=form.cleaned_data['thought']
            member=Member.objects.create(name=n1, relation=n2, thought=n1)
            return redirect('display_member',{'member':member})
    else:
        form=MemberForm(instance=member)
    return render(request, 'cmtbox/display_member.html', {'form':form})

    #members=Member.objects.all()
    #return render(request,'cmtbox/display_member.html',{'members':members})