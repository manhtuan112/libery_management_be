
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class BookResponseSerializer(serializers.ModelSerializer):
    # thêm thuộc tính (read_only=True nếu dùng cách 1)
    category = CategorySerializer(many=False)

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ("id",
                  "title",
                  "author",
                  "public_date",
                  "page_num",
                  "description",
                  "image_url",
                  "category")


    # tất cả các hàm bên dưới phục vụ cho việc tạo đối tượng bằng data json còn tạo bằng đối tượng thì không cần
    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):  # thêm hàm create nếu dùng cách 2

        category_data = validated_data.pop('category')

        category, created = Category.objects.get_or_create(
            name=category_data.get("name"))  # Trả về đối tượng category (nếu không tồn tại thì sẽ tạo mới vào csdl)

        book = Book.objects.create(category=category, **validated_data)

        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.public_date = validated_data.get(
            'public_date', instance.public_date)
        instance.page_num = validated_data.get('page_num', instance.page_num)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.image_url = validated_data.get(
            'image_url', instance.image_url)

        # Update the nested Category instance if it exists in the validated data
        category_data = validated_data.get('category')
        if category_data:
            category_serializer = CategorySerializer(
                instance.category, data=category_data)
            if category_serializer.is_valid():
                category_serializer.save()

        instance.save()
        return instance


class BookItemResponseSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=False)

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ("id", "title", "author", "category", "public_date", "page_num")
