from library.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.shortcuts import render
from library.models import Book
from django.contrib.humanize.templatetags.humanize import naturaltime
from library.utils import dump_queries
from django.db.models import Q
class BookListView(OwnerListView):
    model = Book
    template_name = "library/book_list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(description__icontains=strval), Q.OR)
            objects = Book.objects.filter(query).select_related().order_by('-publish_date')[:10]
        else :
            objects = Book.objects.all().order_by('-publish_date')[:10]

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.publish_date)

        ctx = {'book_list' : objects, 'search': strval}
        retval = render(request, self.template_name, ctx)

        dump_queries()
        return retval
    # By convention:
    # template_name = "myarts/article_list.html"


class BookDetailView(OwnerDetailView):
    model = Book


class BookCreateView(OwnerCreateView):
    model = Book
    fields = '__all__'

class BookUpdateView(OwnerUpdateView):
    model = Book
    fields = '__all__'


class BookDeleteView(OwnerDeleteView):
    model = Book


