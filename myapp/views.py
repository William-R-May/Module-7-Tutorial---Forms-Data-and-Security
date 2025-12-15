from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from books.models import Book
from .forms import CommentForm, ProfileForm

@login_required
def dashboard(request):
    books = Book.objects.all()[:10]
    return render(request, 'myapp/dashboard.html', {'books': books})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            return redirect('myapp:profile')
    else:
        form = ProfileForm(initial={'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    return render(request, 'myapp/profile.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.select_related('user').order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                return redirect('login')
            comment.book = book
            comment.save()
            return redirect('myapp:book_detail', pk=book.pk)
    else:
        form = CommentForm()
    return render(request, 'myapp/book_detail.html', {'book': book, 'comments': comments, 'form': form})
