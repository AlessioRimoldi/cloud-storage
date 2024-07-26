from django.db import models

from .decorators import execute



# Create your models here.
class Experiment(models.Model):
    owner = models.ForeignKey('auth.User', related_name = 'experiments', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default = '')
    code = models.TextField()
    related_results = models.OneToOneField('Results', related_name = 'experiment', on_delete=models.CASCADE, null = True)

    class Meta:
        ordering = ['created']

    def run(self):
        data = {'output': '', 'duration': 0, 'errors': ''}
        try:
            data.update(execute(self.code))
        except Exception as e:
            data['errors'] = str(e)
        return data

class Results(models.Model):
    owner = models.ForeignKey('auth.User', related_name='results', on_delete=models.CASCADE)
    related_experiment = models.OneToOneField('Experiment', related_name='results', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField()
    output = models.TextField(null = True)
    errors = models.TextField(null=True)

    class Meta:
        ordering = ['created']
