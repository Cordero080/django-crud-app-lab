from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workouts/', views.workout_index, name='workout-index'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout-detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workout-create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout-update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout-delete'),
    
    # Exercise routes
    path('workouts/<int:workout_id>/add-exercise/', views.ExerciseCreate.as_view(), name='exercise-create'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercise-update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercise-delete'),
    
    # Equipment routes
    path('equipment/', views.EquipmentList.as_view(), name='equipment-list'),
    path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment-create'),
    path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment-update'),
    path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment-delete'),
    
    # Associate/unassociate equipment
    path('workouts/<int:workout_id>/add-equipment/<int:equipment_id>/', views.associate_equipment, name='associate-equipment'),
    path('workouts/<int:workout_id>/remove-equipment/<int:equipment_id>/', views.unassociate_equipment, name='unassociate-equipment'),
    
    # Auth routes
    path('accounts/signup/', views.signup, name='signup'),
]