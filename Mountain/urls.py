from django.urls import path
from Mountain.views import SubmitData, PerevalAddedDetail, PerevalAddedUpdate, PerevalAddedList

urlpatterns = [
    path('submitData/', SubmitData.as_view(), name='submit-data'),
    path('submitData/<int:pk>/', PerevalAddedDetail.as_view(), name='pereval-detail'),
    path('submitData/<int:pk>/update/', PerevalAddedUpdate.as_view(), name='pereval-update'),
    path('submitData/email/', PerevalAddedList.as_view(), name='pereval-list'),
]
