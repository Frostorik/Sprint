from django.urls import path
from Mountain.views import SubmitData, PerevalAddedDetail, PerevalAddedUpdate, PerevalAddedList

urlpatterns = [
    path('SubmitData/create', SubmitData.as_view(), name='submit-data'),
    path('SubmitData/<int:pk>/', PerevalAddedDetail.as_view(), name='pereval-detail'),
    path('SubmitData/<int:pk>/update/', PerevalAddedUpdate.as_view(), name='pereval-update'),
    path('SubmitData/list/', PerevalAddedList.as_view(), name='pereval-list'),
]
