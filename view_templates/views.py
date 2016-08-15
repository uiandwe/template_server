from django.shortcuts import render

# Create your views here.


def show_templates(request, template_name):
    if template_name is not None:
        print(template_name)
        return render(request, 'template/'+template_name+'/index.html')
