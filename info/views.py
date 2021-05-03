from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from info.models import Contact, Project


def index(request):
    projects = Project.objects.order_by('-created_date').filter(is_published=True) #arrival_date from the model
    context = {
        'projects': projects
    }
    return render(request, 'pages/index.html',context)


def about(request):
    return render(request, 'pages/about.html')

def portfolio(request):
    projects = Project.objects.order_by('-created_date').filter(is_published=True) #arrival_date from the model
    context = {
        'projects': projects
    }
    return render(request, 'pages/portfolio.html', context)



def contact(request):
    #form contact
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact( first_name = first_name, last_name = last_name, email=email, message=message )

        contact.save()

        #send an email function
        send_mail(
            'Hi! ' + first_name + ' Thank you for your message', #subject person´s name
            message, #message
            email, #from email
           ['esti.codes@gmail.com'], #to email
        )


        return render(request, 'pages/contact.html', {'first_name': first_name})
    
    else:
        return render(request, 'pages/contact.html')




def project(request, project_id):
    one_project = get_object_or_404(Project, pk=project_id) #check if exist or gives error

    context = {
        'one_project': one_project
    }

    return render(request, 'pages/project.html', context)
