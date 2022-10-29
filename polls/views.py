from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions,Choices

# Create your views here.
def question(request):
    ques=Questions.objects.all()

    return render(request,'questions.html',{'ques':ques})


def question_choices(request,pk):
    choices=Choices.objects.filter(question__id=pk)

    if request.method=="POST":
        c=request.POST.get("a")

        for choice in choices:
            if request.user in choice.replier.all():
                choice.replier.remove(request.user)
                choice.count=choice.count-1
                choice.save()
                print("YaSSSSSSSSSS")
   
        Choice=Choices.objects.get(id=c)
        Choice.replier.add(request.user)
        Choice.count=Choice.count + 1
        Choice.save()
        choicess=Choices.objects.filter(question__id=pk)
        return render(request,'choices_count.html',{'choicess':choicess})

        
        
        

    
    return render(request,'choices.html',{'choices':choices})


