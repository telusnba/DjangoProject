from django.shortcuts import render


def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Lorem', 'Ipsum', 'Dolor', 'Sit', 'Ammet']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
