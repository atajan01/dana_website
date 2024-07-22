from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *



# ======================== Getting data from Database ========================
course_list = Course.objects.all()
groups = Group.objects.all()

data = {
    'courses': course_list,
    'groups':groups,
}

# ======================== Rendering HTML files ========================
def home(request):
    return render(request, "index.html", data)

def about(request):
    return render(request, "about.html")


def courses(request):
    return render(request, 'courses.html', data)


def blog(request):
    blogs = Blog.objects.all()
    p = Paginator(Blog.objects.all(), 6)
    page = request.GET.get('page')
    blogs_pagination = p.get_page(page)

    return render(request, 'blog.html', 
                {'blogs':blogs, 
                 'blogs_pagination': blogs_pagination,
                })
    

def contact(request):
    return render(request, 'contact.html', data)

def group_spec(request, id):
    group = Group.objects.get(id = id)
    courses = Course.objects.filter(group = group)
    return render(request, 'courses.html', {'courses' : courses})


def save_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        phone = request.POST['phone']
        email = request.POST['email']
        group_course = request.POST['courses']
        message = request.POST['message']

        Feedback.objects.create(name=name, surname=surname, phone=phone, email=email, group_course = group_course, message=message)
    return redirect ('/contact/', {'groups': groups})

