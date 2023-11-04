from rest_framework import serializers

from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"
        # fields = ("id", "name", "category", "channels")
        # read_only_fields = ("id", "category", "channels")
        # depth = 1

    def create(self, validated_data):
        server = Server.objects.create(**validated_data)
        return server
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def get(self, instance):
        return instance

    def get_all(self):
        return Server.objects.all()
    
    def get_by_id(self, id):
        return Server.objects.get(id=id)
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"
        # fields = ("id", "name", "category", "channels")
        # read_only_fields = ("id", "category", "channels")
        # depth = 1

    def create(self, validated_data):
        server = Server.objects.create(**validated_data)
        return server
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance

    def get(self, instance):
        return instance

    def get_all(self):
        return Server.objects.all()
    
    def get_by_id(self, id):
        return Server.objects.get(id=id)

