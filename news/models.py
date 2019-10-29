from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''a list or a dictionary to which I'll send the scraped posts'''
    posts = [
        {
            'headline': 'Donald Trump kills his dog',
            'content': 'ZZZZZZZ smth happens',
            'date': '22.10.2019',
            'category' : 'politics'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'politics'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'politics'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        },
        {
            'headline': 'Manchester beats Real Madrid',
            'content': 'RM is beaten',
            'date': '23.10.2019',
            'category': 'sport'
        }

    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()
    category = models.TextField()

    # def __str__(self):
    #     return self.title

