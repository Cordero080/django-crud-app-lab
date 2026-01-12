from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Workout, Exercise, Equipment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Home view 
def home(request):
    return render(request, 'home.html')

# Index view - list of workouts (only user's workouts)
@login_required
def workout_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})

# Detail view - show single workout
@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)

    equipment_not_in_workout = Equipment.objects.exclude(id__in=workout.equipment.all().values_list('id'))
    
    # Handle adding equipment
    if request.method == 'POST':
        equipment_id = request.POST.get('equipment')
        if equipment_id:  # Only add if equipment was selected
            workout.equipment.add(equipment_id)
        return redirect('workout-detail', workout_id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout, 'all_equipment': equipment_not_in_workout})

# Create view - form to add new workout
class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name', 'workout_type', 'duration', 'date', 'notes']
    success_url = '/workouts/'
    
    # Auto-set the user when creating workout
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Update view (edit)
class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['name', 'workout_type', 'duration', 'date', 'notes']
    success_url = '/workouts/'

# Delete view - confirm and delete workout
class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'

# Exercise Create - adds exercise to a specific workout
class ExerciseCreate(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ['name', 'sets', 'reps']
    
    # Automatically link exercise to workout from URL
    def form_valid(self, form):
        form.instance.workout_id = self.kwargs['workout_id']
        return super().form_valid(form)
    
    # Redirect back to workout detail after creating
    def get_success_url(self):
        return f'/workouts/{self.kwargs["workout_id"]}/'

# Exercise Update - edit existing exercise
class ExerciseUpdate(LoginRequiredMixin, UpdateView):
    model = Exercise
    fields = ['name', 'sets', 'reps']
    
    # Redirect back to workout detail after updating
    def get_success_url(self):
        return f'/workouts/{self.object.workout.id}/'

# Exercise Delete - remove exercise
class ExerciseDelete(LoginRequiredMixin, DeleteView):
    model = Exercise
    
    # Redirect back to workout detail after deleting
    def get_success_url(self):
        return f'/workouts/{self.object.workout.id}/'

# Signup view - creates new user account
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('workout-index')
        else:
            error_message = 'Invalid sign up - try again'
    else:
        form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
# Equipment CRUD views
class EquipmentList(LoginRequiredMixin, ListView):
    model = Equipment

class EquipmentCreate(LoginRequiredMixin, CreateView):
    model = Equipment
    fields = ['name']
    success_url = '/equipment/'

class EquipmentUpdate(LoginRequiredMixin, UpdateView):
    model = Equipment
    fields = ['name']
    success_url = '/equipment/'

class EquipmentDelete(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = '/equipment/'

# Associate/Unassociate equipment with workout
@login_required
def associate_equipment(request, workout_id, equipment_id):
    Workout.objects.get(id=workout_id).equipment.add(equipment_id)
    return redirect('workout-detail', workout_id=workout_id)

@login_required
def unassociate_equipment(request, workout_id, equipment_id):
    Workout.objects.get(id=workout_id).equipment.remove(equipment_id)
    return redirect('workout-detail', workout_id=workout_id)