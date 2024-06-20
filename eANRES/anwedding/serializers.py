from rest_framework import serializers
from .models import WeddingService, WeddingHall, BanquetRoom, User, FeedBack, WeddingMenu, WeddingBooking, FoodMenu, \
    FoodItem, HomePage, Staff


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class WeddingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingService
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        req = super().to_representation(instance)
        req['image'] = instance.image.url
        return req


class WeddingHallSerializer(ItemSerializer):
    class Meta:
        model = WeddingHall
        fields = '__all__'


class WeddingMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingMenu
        fields = '__all__'


class WeddingBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingBooking
        fields = '__all__'


class BanquetRoomSerializer(ItemSerializer):
    class Meta:
        model = BanquetRoom
        fields = '__all__'


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class FoodMenuSerializer(ItemSerializer, WeddingMenuSerializer, FoodItemSerializer):
    class Meta:
        model = FoodMenu
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.set_password(user.password)
        user.save()

        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'role', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class FeedBackSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = FeedBack
        fields = ['id', 'content', 'created_date', 'user']