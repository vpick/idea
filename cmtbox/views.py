from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Member
from .forms import MemberForm
#from django.http import HttpResponse


#def index(request):
    #return HttpResponse("hi, i am varsha nd u r in cmtbox index.")

def member_list(request):
    members=Member.objects.filter(post_date__lte=timezone.now()).order_by('post_date')
    return render(request, 'cmtbox/member_list.html', {'members':members})

def new_member(request):
    form=MemberForm()
    return render(request, 'cmtbox/contact_form.html', {'form':form})

def member_detail(request,pk):
	member=get_object_or_404(Member,pk=pk)
	return render(request, 'cmtbox/member_detail.html',{'member':member})

def display_member(request):
	members=Member.objects.filter(post_date__lte=timezone.now())
	return render(request,'cmtbox/display_member.html',{'members':members})