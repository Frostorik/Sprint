from django.urls import path
from Mountain.views import SubmitData, PerevalAddedDetail, PerevalAddedUpdate

urlpatterns = [
    path('submit-data/', SubmitData.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', PerevalAddedDetail.as_view(), name='pereval-detail'),
    path('submitData/<int:pk>/update/', PerevalAddedUpdate.as_view(), name='pereval-update'),
]
