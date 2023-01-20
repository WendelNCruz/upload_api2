from django.urls import path
from .views import simple_upload
#from uploadapp.views import simple_upload
from . import views


app_name = 'uploadapp'

urlpatterns = [
    #path("", views.homepage, name="homepage"),
    #path("upload", simple_upload, name="upload"),
    #path('', simple_upload, name='upload-view'),
]