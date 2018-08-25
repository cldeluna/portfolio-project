from django.shortcuts import render

from .models import Job
# Create your views here.

# django will automatically look in app/templates directory for template files
def home(request):

    jobs = Job.objects
    print(jobs)
    return render(request, 'jobs/home.html', {'jobs': jobs})
