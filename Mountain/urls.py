from django.urls import path
from Mountain import views

urlpatterns = [
    # path('', Readme.as_view()),
    path('submit-data/', views.SubmitData, name='submit-data'),
]
