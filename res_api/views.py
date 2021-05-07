from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from library.models import Book
from .serializers import BookSerializer


@api_view(['GET', 'POST'])
def get_post_book(request):
    if request.method == "GET":
        book = Book.objects.all()
        return Response(BookSerializer(book, many=True).data,
                        status=status.HTTP_200_OK)

    elif request.method == "POST":
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
def get_update_delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)

    except:
        return Response({"error": "Not Found!"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = BookSerializer(book)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        if book.owner == request.user:
            ser = BookSerializer(book, data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=status.HTTP_200_OK)
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        if book.owner == request.user:
            book.delete()
        else:
            return Response("errors", status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_book(request):
    book = Book.objects.filter(title=request.query_params['title'])
    if book:
        ser = BookSerializer(book, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)