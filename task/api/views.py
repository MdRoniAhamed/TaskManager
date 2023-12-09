from .serializers import Task, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class manage(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields = ['create_date','start_date','end_date','priority','complete']  
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    