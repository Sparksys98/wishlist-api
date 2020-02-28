from django.contrib.auth.models import User
from rest_framework import serializers
from items.models import Item ,FavoriteItem
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = ['user']
class ItemListSerializer(serializers.ModelSerializer):
    added_by =  UserSerializer()
    favourited  = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )
    class Meta:
        model = Item
        fields = ['id','name','added_by','detail','favourited']

    def get_favourited (self , obj):
        return obj.favoriteitem_set.count()


class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['name' , 'image', 'description' , 'favourited_by']
    def get_favourited_by(self, obj):
        return FavoriteSerializer(obj.favoriteitem_set.all(), many=True).data
