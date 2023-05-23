from django.urls import path
from Mountain.views import SubmitData

urlpatterns = [
    # path('', Readme.as_view()),
    path('submit-data/', SubmitData.as_view(), name='submit-data'),
]
