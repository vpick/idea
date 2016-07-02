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
        form=MemberForm(request.POST)
        if form.is_valid():
            #member=Member.objects.create(name=name, relation=relation, thought=thought)
            return redirect('member_detail', pk=member.pk)
    else:
        form=MemberForm()
    return render(request, 'cmtbox/display_member.html', {'form':form})

def member_detail(request, pk):
    member=get_object_or_404(Member, pk=pk)
    return render(request, 'cmtbox/member_detail.html',{'member':member})

def display_member(request, pk):
    member=get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form=MemberForm(request.POST, instance=member)
        if form.is_valid():
            #member=Member.objects.create(name=name, relation=relation, thought=thought)
            return redirect('member-info', pk=member.pk)
    else:
        form=MemberForm(instance=member)
    return render(request, 'cmtbox/display_member.html', {'form':form})

    #members=Member.objects.all()
    #return render(request,'cmtbox/display_member.html',{'members':members})