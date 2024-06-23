from .models import Director, Movie
from rest_framework import viewsets
from .serializers import DirectorSerializer, MovieSerializer

# ViewSet para peliculas
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]

# ViewSet para directores
class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]