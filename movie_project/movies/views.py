from rest_framework import status
from rest_framework import  generics, permissions, authentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .models import Director, Movie
from .serializers import DirectorSerializer, MovieSerializer



# Vistas genéricas para Director
class DirectorListView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]

class DirectorDetailView(generics.RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]

class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    #permission_classes = [permissions.DjangoModelPermissions]



# Vista basada en función para obtener películas por director
@api_view(['GET'])
@authentication_classes([authentication.SessionAuthentication, authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def movies_by_director(request, director_id):
    try:
        director = Director.objects.get(pk=director_id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    movies = director.movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


#Vistas añadidas para cumplir con los requisitos de la entrega

class DirectorUpdateView(generics.UpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDeleteView(generics.DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    
class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
class MovieDeleteView(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer