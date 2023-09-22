from rest_framework import serializers
from education_system_api.models import Lesson, User, Product, View


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class ViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = View
#         fields = '__all__'
