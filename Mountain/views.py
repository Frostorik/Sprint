from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PerevalAddedSerializer
from .models import PerevalAdded


class SubmitData(generics.CreateAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class PerevalAddedDetail(generics.RetrieveAPIView):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class PerevalAddedUpdate(APIView):
    def patch(self, request, pk):
        try:
            per_obj = PerevalAdded.objects.get(pk=pk)
        except PerevalAdded.DoesNotExist:
            return Response({'state': 0, 'message': 'Запись не найдена.'})

        if per_obj.status != 'new':
            return Response({'state': 0, 'message': 'Запись не в статусе "новая".'})

        serializers = PerevalAddedSerializer(per_obj, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'state': 1})
        return Response({'state': 0, 'message': serializers.errors})


class PerevalAddedList(generics.ListAPIView):
    serializer_class = PerevalAddedSerializer

    def get_queryset(self):
        email = self.request.query_params.get('user__email', None)
        if email is not None:
            return PerevalAdded.objects.filter(user__email=email)
        else:
            return PerevalAdded.objects.all()
