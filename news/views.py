from django.shortcuts import render
from .models import Post


'''a list or a dictionary to which I'll send the scraped posts'''
posts = [
    {
        'headline': 'Donald Trump kills his dog',
        'content': 'ZZZZZZZ smth happens',
        'date': '22.10.2019'
    },
    {
        'headline': 'Manchester beats Real Madrid',
        'content': 'RM is beaten',
        'date': '23.10.2019'
    }

]


def home(request):
    context = {
        '''хочу сюда сложить наскрейпленные новости'''
        'posts': Post.objects.all()
    }
    return render(request, 'news/home.html', context)


def about(request):
    return render(request, 'news/about.html', {'title': 'About'})
