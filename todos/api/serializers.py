from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Model serializer definition of todos """
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
