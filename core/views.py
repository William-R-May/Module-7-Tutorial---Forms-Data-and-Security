from django.shortcuts import render
from datetime import datetime

def home(request):
    items = ["Checking Account", "Savings Account", "Certificate of Deposit"]
    context = {
        "page_title": "Welcome",
        "items": items,
        "now": datetime.now(),
    }
    return render(request, "home.html", context)
