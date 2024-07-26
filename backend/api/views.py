from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import Experiment, Results
from api.permissions import IsOwner
from api.serializers import ExperimentSerializer, ResultsSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        ''' 
        Instantiates and returns the lists of permissions based on the action
        '''
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        if self.action == 'list':
            permission_classes = [IsOwner | permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save()
    
    def list(self, request):
        users = self.queryset.filter(id = request.user.id)
        serializer = self.get_serializer(users, many = True)
        return Response(serializer.data)
        
class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    def get_permissions(self):
        
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner | permissions.IsAdminUser]
        
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    
    def list(self, request):
        experiments = self.queryset.filter(owner = request.user)
        serializer = self.get_serializer(experiments, many = True)
        return Response(serializer.data)
    
    @action(detail = True, renderer_classes = [renderers.JSONRenderer], methods = ['post','get'])
    def run(self, request, pk=None):
        experiment = self.get_object()
        try:
            data = experiment.run()
            results = Results.objects.create(owner = self.request.user,related_experiment = experiment ,**data)
            experiment.related_results = results
            experiment.save()
            return Response({'results': results.id}, status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    def get_serializer(self, *args, **kwargs):
        
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
    def get_serializer_context(self):
        
        return {'request': self.request,
                'format': self.format_kwarg,
                'view': self,
                }
        
class ResultsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner | permissions.IsAdminUser]
        
        return [permission() for permission in permission_classes]

    def list(self, request):
        results = self.queryset.filter(owner = request.user)
        serializer = self.get_serializer(results, many = True)
        return Response(serializer.data)

    def get_serializer(self, *args, **kwargs):
        
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
    def get_serializer_context(self):
        
        return {'request': self.request,
                'format': self.format_kwarg,
                'view': self,
                }
