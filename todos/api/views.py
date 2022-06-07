from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from todos.models import Todo
from .serializers import TodoSerializer
from .permissions import IsUserOrIsAdmin,IsAdmin


class TodoListView(APIView):
    """ List API view for all todos """
    permission_classes = (IsUserOrIsAdmin,)

    def get(self, request):
        todos = Todo.objects.all()
        serializers = TodoSerializer(todos, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class CreateTodoView(APIView):
    """Todo Create API view definition """
    permission_classes = (IsAdmin,)

    @swagger_auto_schema(request_body=TodoSerializer)
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response({'message': 'Todo item added successfully !!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class TodoDetailsView(APIView):
    """Todo API details view where you can get,update and delete specific todo by its ID"""
    permission_classes = (IsAdmin,)

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'error': 'Not found !!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TodoSerializer)
    def put(self, request, pk):
        todo = Todo.objects.get(pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({'error': 'Not found !!'}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response({'message': 'Deleted successfully !!'}, status=status.HTTP_204_NO_CONTENT)
