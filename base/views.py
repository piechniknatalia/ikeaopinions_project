from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from .models import Opinion, Comment, Product
from .forms import OpinionForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
    context={'page':page }
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'login_register.html', {'form':form})

def home(request):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    products = Product.objects.all()
    print(products)
    opinions = Opinion.objects.all().order_by('-created')
    opinion_count = opinions.count()
    context = {'opinions': opinions, 'opinion_count': opinion_count, 'product_names': product_names, 'products': products}
    return render(request, 'home.html', context)

def opinions_by_name(request, nm):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    opinions = Opinion.objects.filter(user__username=nm)
    opinion_count = opinions.count()
    last_opinion = Opinion.objects.filter(user__username=nm).values_list('created', flat=True).order_by('-created')[0]
    context = {'opinions':opinions, 'name':nm, 'product_names': product_names, 'opinion_count': opinion_count, 'last_opinion': last_opinion}
    return render(request, 'opinions_by_name.html', context) 

def opinion(request, pk):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    opinion = Opinion.objects.get(id=pk)
    comments = opinion.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            opinion=opinion,
            body=request.POST.get('body')
        )
        return redirect('opinion', pk=opinion.id)

    return render(request, 'opinion.html', {'opinion':opinion, 'product_names': product_names, 'comments':comments})

def opinions_by_product(request, pn):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    opinions = Opinion.objects.filter(product__name=pn)
    opinion_count = opinions.count()
    context = {'opinions':opinions, 'product': pn, 'product_names': product_names, 'opinion_count': opinion_count}
    return render(request, 'opinions_by_product.html', context) 

@login_required(login_url='login')
def createOpinion(request):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    form = OpinionForm()
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.user = request.user
            opinion.save()
            return redirect('home')
    context = {'form': form, 'product_names': product_names}
    return render(request, 'opinion_form.html', context)

@login_required(login_url='login')
def deleteOpinion(request, pk):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    opinion = Opinion.objects.get(id=pk)
    if request.method == 'POST':
        opinion.delete()
        return redirect('home')   
    return render(request, 'delete.html', {'obj': opinion, 'product_names': product_names})

@login_required(login_url='login')
def deleteComment(request, pko, pkc):
    product_names = Opinion.objects.values_list('product', flat=True).distinct()
    comment = Comment.objects.get(id=pkc)
    if request.method == 'POST':
        comment.delete()
        return redirect('opinion', pk=pko)   
    return render(request, 'delete.html', {'obj': comment, 'product_names': product_names})