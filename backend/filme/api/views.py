from rest_framework import viewsets

from ..models import Filme
from .serializers import FilmeSerializer


class FilmeListView(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer


# class FilmeDetailView(RetrieveAPIView):
#     queryset = Filme.objects.all()
#     serializer_class = FilmeSerializer
