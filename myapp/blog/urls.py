from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='index'),
    path('jayam/', views.jayam, name='jayam'),
    path('detail/<int:post_id>', views.detail, name='detail_with_id'),
    path('old_link/', views.old_link, name='old_link'),
    path('new_link_something/', views.new_link, name='new_link'),
]