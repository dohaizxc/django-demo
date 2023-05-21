from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Course, Topic
from .forms import CourseForm
from django.http import JsonResponse
import random

# Create your views here.
def get_home(request):
    topic = request.GET.get('topic') if request.GET.get('topic') != None else ''
    courses = Course.objects.filter(Q(topic__name__icontains=topic) | Q(name__icontains=topic) | Q(description__icontains=topic))
    topics = Topic.objects.all()
    context = {'courses': courses, 'topics': topics}
    return render(request, 'home.html', context)

def get_course(request, pk):
    course = Course.objects.get(id=pk)
    context = {'course': course}
    return render(request, 'course.html', context)

def get_topic(request, pk):
    topic = Topic.objects.get(id=pk)
    context = {'topic': topic}
    return render(request, 'topic.html', context)

def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'course_form.html', context)

def update_course(request, pk):
    course = course.objects.get(id=pk)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'course_form.html', context)

def delete_course(request, pk):
    course = course.objects.get(id=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('/')        

    context = {'obj': course}
    return render(request, 'delete_course.html', context)


def pie_chart(request):
    labels = []
    data = []
    colors = []

    topics = Topic.objects.all()
    for topic in topics:
        labels.append(topic.name)
        courses = Course.objects.filter(topic__name__icontains=topic.name)
        data.append(courses.count())
        colors.append('#{:06x}'.format(random.randint(0, 256**3)))

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
        'colors': colors,
    })

def bar_chart(request):
    labels = []
    data = []
    colors = []

    topics = Topic.objects.all()
    for topic in topics:
        labels.append(topic.name)
        courses = Course.objects.filter(topic__name__icontains=topic.name)
        data.append(courses.count())
        colors.append('#{:06x}'.format(random.randint(0, 256**3)))
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'colors': colors,
    })

def get_bar_chart(request):
    return render(request, 'bar_chart.html')

