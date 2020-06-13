from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Freet
from .serializers import FreetSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class FreetViewSet(viewsets.ModelViewSet):
    queryset = Freet.objects.all()
    serializer_class = FreetSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def list(self, request):
        queryset = self.get_queryset()
        author = request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(owner__username=author)
        serializer = FreetSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk):
        qs = Freet.objects.filter(id=pk)
 
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()

        obj.likes.add(request.user)
        serializer = FreetSerializer(obj)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk):
        qs = Freet.objects.filter(id=pk)
 
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()

        obj.likes.remove(request.user)
        serializer = FreetSerializer(obj)
        return Response(serializer.data, status=200)

    
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def refreet(self, request, pk):
        qs = Freet.objects.filter(id=pk)
 
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()

        new_freet = Freet.objects.create(owner=request.user, source_freet=obj, content=obj.content)
        serializer = FreetSerializer(new_freet)
        return Response(serializer.data, status=201)

    
# class FreetListAPI(generics.ListCreateAPIView):
#     queryset = Freet.objects.all()
#     serializer_class = FreetSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = FreetSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(request, *args, **kwargs):

    
# class FreetDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FreetSerializer