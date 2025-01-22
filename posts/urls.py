from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('create_photo_post/', views.CreatePhotoPostView.as_view() , name='create_photo_post'),
    path('create_text_post/', views.CreateTextPostView.as_view() , name='create_text_post'),
]
