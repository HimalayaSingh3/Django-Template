from django.shortcuts import render
from django.http import HttpResponse

# Sample users list (Fixed: age as integers)
users = [
    {"username": "Himalaya Singh", "age": 20},
    {"username": "Himalaya Singh", "age": 14},
    {"username": "Himalaya Singh", "age": 40},
    {"username": "Himalaya Singh", "age": 17},
]

def home(request):
    return render(request, 'home/index.html', {'users': users})
