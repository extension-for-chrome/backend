from rest_framework import serializers


class ApiRootsSerializer(serializers.Serializer):
	root = serializers.CharField()
