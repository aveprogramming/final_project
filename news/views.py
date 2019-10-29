from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# '''a list or a dictionary to which I'll send the scraped posts'''
# posts = [
#     {
#         'headline': 'Donald Trump kills his dog',
#         'content': 'ZZZZZZZ smth happens',
#         'date': '22.10.2019',
#         'category' : 'politics'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'politics'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'politics'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     },
#     {
#         'headline': 'Manchester beats Real Madrid',
#         'content': 'RM is beaten',
#         'date': '23.10.2019',
#         'category': 'sport'
#     }
#
# ]


# def home(request):
#     '''хочу сюда сложить наскрейпленные новости'''
#     context = {
# #        posts : Post.objects.all()
#     }
#     # context = {'posts':
#     # posts}
#     return render(request, 'news/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'news/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


