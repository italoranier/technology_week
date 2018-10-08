from django.shortcuts import render


def technology_week(request):
    return render(request, 'blog/technology_week.html',{})
