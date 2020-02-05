from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsAdminUserOrReadOnly
from rest_framework.response import Response

from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer, BookInfoSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('is_online', 'price')
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_staff:
            return queryset.filter(is_online=True)

        return queryset

    def get_serializer_class(self):
        if not self.request.user.is_staff:
            return BookInfoSerializer

        return super().get_serializer_class()
    # @action(['get'], False, 'all', 'all')
    # def all_books(self, request):
    #     books = Book.objects.all()
    #     serializer = BookSerializer(books, many=True)
    #     return Response(serializer.data)
