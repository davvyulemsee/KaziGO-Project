from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import requests
from .forms import GigForm
from .models import Gig
from django.contrib import messages
from .models import TaskRequest
from .forms import TaskRequestForm


# Create your views here.

# def all_gigs(request):
#     query = request.GET.get('q')
#     if query:
#         gigs = Gig.objects.filter(title__icontains=query)
#     else:
#         gigs = Gig.objects.all()
#     return render(request, 'giglandingpage.html', {'gigs': gigs})

def all_gigs(request):
    category = request.GET.get('category')
    query = request.GET.get('q')

    gigs = Gig.objects.all()
    if category:
        gigs = gigs.filter(category=category)
    if query:
        gigs = gigs.filter(title__icontains=query)

    return render(request, 'giglandingpage.html', {
        'gigs': gigs,
        'selected_category': category,
        'categories': dict(Gig.CATEGORY_CHOICES)
    })


def create_gig(request):
    if request.method == 'POST':
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.seller = request.user
            gig.save()
            return redirect('gigs:all_gigs')
    else:
        form = GigForm()
    return render(request, 'creategigpage.html', {'form': form})

def gig_detail(request, slug):
    gig = get_object_or_404(Gig, slug=slug)
    return render(request, 'gigpage.html', {'gig': gig})




# Example category dictionary (you can move this to settings or a model)
CATEGORIES = {
        'WD': 'Web Development',
        'GD': 'Graphic Design',
        'WR': 'Writing & Translation',
        'DM': 'Digital Marketing',
        'VA': 'Virtual Assistant',
        'VO': 'Voice Over',
        'SE': 'SEO',
        'DA': 'Data Analysis',
}

def submit_task(request, category_code, seller_id):
    category_name = CATEGORIES.get(category_code)
    seller = get_object_or_404(User, id=seller_id)

    if not category_name:
        messages.error(request, "Invalid category selected.")
        return redirect('gigs:all_gigs')

    if request.method == 'POST':
        form = TaskRequestForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.category = category_code
            task.seller = seller
            task.save()
            messages.success(request, "Your task request has been submitted!")
            return redirect('gigs:all_gigs')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TaskRequestForm()

    return render(request, 'submit_task.html', {
        'form': form,
        'category_code': category_code,
        'category_name': category_name,
        'seller': seller
    })


def gigs_by_category(request, code):
    gigs = Gig.objects.filter(category=code)
    category_name = dict(Gig.CATEGORY_CHOICES).get(code, 'Unknown Category')
    return render(request, 'gigs_by_category.html', {
        'gigs': gigs,
        'category_code': code,
        'category_name': category_name
    })

def seller_dashboard(request):
    tasks = request.user.task_requests.all()
    return render(request, 'seller_dashboard.html', {'tasks': tasks})