from django.db import models
from django.contrib.auth.models import User

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'equipment'

class Workout(models.Model):
  name = models.CharField(max_length=100)
  workout_type = models.CharField(max_length=50)
  duration = models.IntegerField()
  date = models.DateField()
  notes = models.TextField(blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  equipment = models.ManyToManyField(Equipment, blank=True)
    
  def __str__(self):
      return f"{self.name} - {self.date}"

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.name} - {self.sets}x{self.reps}"    