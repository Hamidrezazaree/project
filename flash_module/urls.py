
from django.urls import path

from flash_module.views import CreateProfileApiView, CreateFlashCardApiView, UpdateFlashCardApiView, \
    DeleteFlashCardApiView, ListFlashCardApiView

urlpatterns = [
    path('create-user',CreateProfileApiView.as_view(),name ='create_user'),
    path('create-flash',CreateFlashCardApiView.as_view(),name ='create_flash'),
    path('list-flash/', ListFlashCardApiView.as_view(), name='list_flash'),
    path('update-flash/<id>',UpdateFlashCardApiView.as_view(),name ='update_flash'),
    path('delete-flash/<id>',DeleteFlashCardApiView.as_view(),name ='delete_flash'),
]