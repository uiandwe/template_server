from django.shortcuts import render

# Create your views here.


def show_templates(request, template_name):

    if template_name is not None:
        return render(request, template_name+'/index.html')
