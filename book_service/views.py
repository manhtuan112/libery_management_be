from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, BookResponseSerializer, BookItemResponseSerializer
from .models import Book, Category
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.


# ### Cách 1: tạo đối tượng không dùng Serializer không cần custom hàm create trong class BookSerializer,  ######
# @api_view(["POST"])
# def create_book(request):
#     category_data = {
#         "name": request.data.get('category'),
#     }
#     category = None
#     category_serializer = CategorySerializer(data=category_data)
#     if category_serializer.is_valid():
#         category, created = Category.objects.get_or_create(
#             name=category_serializer.validated_data['name'])
#     else:
#         return Response({
#             'success': False,
#             'code': 400,
#             "message_field_error": 'category',
#             "message": category_serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)


#     book = Book.objects.create(title=request.data.get('title'),
#                                author=request.data.get('author'),
#                                category=category,
#                                public_date=request.data.get('public_date'),
#                                page_num=request.data.get('page_num'),
#                                description=request.data.get('description'),
#                                image_url=request.data.get('image_url'))
#     if (book):
#         book = BookResponseSerializer(book, many=False)
#         return Response({
#             'success': True,
#             'code': 200,
#             "message": "add book successful",
#             "data": book.data
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response({
#             'success': False,
#             'code': 400,
#             "message": book.errors
#         }, status=status.HTTP_400_BAD_REQUEST)


####### Cách 2: Tạo đối tượng dùng Serializer (phải thêm hàm create cho class Serializer) ###########
@api_view(["POST"])
def create_book(request):

    category_data = {
        "name": request.data.get('category'),
    }
    category_serializer = CategorySerializer(data=category_data)
    if category_serializer.is_valid():

        book_data = {
            'title': request.data.get('title'),
            'author': request.data.get('author'),
            'category': category_serializer.data,
            'public_date': request.data.get('public_date'),
            'page_num': request.data.get('page_num'),
            'description':  request.data.get('description'),
            'image_url': request.data.get('image_url'),
        }

        book = BookResponseSerializer(data=book_data)
        if book.is_valid():
            book.save()
            return Response({
                'success': True,
                'code': 200,
                "message": "add book successful",
                "data": book.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'code': 400,
                "message": book.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message_field_error": 'category',
            "message": category_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_book(request, **kwargs):
    # Tìm sách
    id_book = kwargs.get('id')
    try:
        book = get_object_or_404(Book, id=id_book)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

    # Sửa thông tin sách
    category_data = {
        "name": request.data.get('category'),
    }
    category_serializer = CategorySerializer(data=category_data)
    if category_serializer.is_valid():

        book_data = {
            'title': request.data.get('title'),
            'author': request.data.get('author'),
            'category': category_serializer.data,
            'public_date': request.data.get('public_date'),
            'page_num': request.data.get('page_num'),
            'description':  request.data.get('description'),
            'image_url': request.data.get('image_url'),
        }

        book = BookResponseSerializer(book, data=book_data)
        if book.is_valid():
            book.save()
            return Response({
                'success': True,
                'code': 200,
                "message": "update book successful",
                "data": book.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'success': False,
                'code': 400,
                "message": book.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({
            'success': False,
            'code': 400,
            "message_field_error": 'category',
            "message": category_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_book(request, **kwargs):
    # Tìm sách
    id_book = kwargs.get('id')
    try:
        book = get_object_or_404(Book, id=id_book)

    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

    # tạo serilizer không cần dùng hàm is_valid() như khi dùng data=resquest.data
    book_serializer = BookResponseSerializer(book)
    return Response({
        'success': True,
        'code': 200,
        "message": "get book data successful",
        "data": book_serializer.data
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_all_book(request):
    # Tìm sách
    book = Book.objects.all()
    # tạo serilizer không cần dùng hàm is_valid() như khi dùng data=resquest.data
    book_serializer = BookItemResponseSerializer(book, many=True)
    return Response({
        'success': True,
        'code': 200,
        "message": "get book data successful",
        "data": book_serializer.data
    }, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_book(request, **kwargs):
    # Tìm sách
    id_book = kwargs.get('id')
    try:
        book = get_object_or_404(Book, id=id_book)
        book.delete()
        return Response({
            'success': True,
            'code': 200,
            "message": "Delete book successful"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'success': False,
            'code': 400,
            "message": str(e)
        }, status=status.HTTP_404_NOT_FOUND)

        

    