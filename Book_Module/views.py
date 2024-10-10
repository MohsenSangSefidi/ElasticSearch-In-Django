from django.shortcuts import render
from django.views import View
from .documents import BookDocument


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        info = request.POST.get('info')
        books = BookDocument.search().query('match', title=info).to_queryset()
        print(books)
        if books:
            return render(request, 'index.html', {
                'books': books,
            })

        return render(request, 'index.html', {
            'error': True
        })