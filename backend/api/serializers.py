from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Experiment, Results

class UserSerializer(serializers.HyperlinkedModelSerializer):
    experiments = serializers.HyperlinkedRelatedField(many= True, view_name = 'experiment-detail', read_only = True)
    results = serializers.HyperlinkedRelatedField(many = True, view_name = 'results-detail', read_only = True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password','experiments', 'results']

class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    related_results = serializers.HyperlinkedRelatedField(many = False, view_name = 'results-detail', read_only = True)

    class Meta:
        model = Experiment
        fields = ['url', 'id', 'owner', 'created', 'title', 'code', 'related_results']

class ResultsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    related_experiment = serializers.HyperlinkedRelatedField(many = False, view_name = 'experiment-detail', read_only = True)

    class Meta:
        model = Results
        fields = ['url', 'id', 'owner', 'related_experiment', 'created', 'duration', 'output', 'errors']
        
