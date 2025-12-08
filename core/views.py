from django.shortcuts import render
from datetime import datetime

def home(request):
    items = ["Apples", "Bread", "Milk"]
    return render(request, "home.html", {"items": items, "now": datetime.now()})
