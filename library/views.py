from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm

# View to list all books
def view_books(request):
    books = Book.objects.all()
    return render(request, 'library/view_books.html', {'books': books})

# View to add a new book
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")  # Success message
            return redirect('add_book')  # Redirect back to the same page to show the message
    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})

# View to edit a book's details
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('edit_book', pk=book.pk)

    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form})

# View to delete a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('view_books')
    return render(request, 'library/delete_book.html', {'book': book})
