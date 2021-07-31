from django.urls import path
from . import views
urlpatterns =[
    path('',views.Index,name="indexcurdopr"),
    path('insert',views.Insert,name="insert"),
    path('deletes',views.Deletes,name="delete"),
    path('updates/<int:id>',views.Update,name="updates")
  ]