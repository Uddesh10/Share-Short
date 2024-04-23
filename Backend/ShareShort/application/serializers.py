from rest_framework import serializers
from .models import Profile, ExtraLinks, Store , User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
    

class ExtraLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraLinks
        fields = "__all__"

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class PublicDataSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    extralinks = ExtraLinksSerializer(many=True , read_only=True ,source = 'extralinks_set')
    store = StoreSerializer(many=True , read_only=True, source = 'store_set')
    class Meta:
        model = User
        fields = ('profile' , 'extralinks' , 'store')