from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view
# from .serializers import UserSerializer, TokenSerializer
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings

from .models import DayInfo


@permission_classes([IsAuthenticated])
class GetInfo(APIView):
	def get(self, request):
		year = request.GET.get("year")
		month = request.GET.get("month")
		day = request.GET.get("day")
		# print(year)
		# print(month)
		# print(day)
		days = DayInfo.objects.filter(year=year, month=month, day=day).values()
		if len(days) == 0:
			return Response(status=status.HTTP_200_OK, data=None)
		else:
			return Response(status=status.HTTP_200_OK, data=days[0])

@permission_classes([IsAuthenticated])
class AddDay(APIView):
	def post(self, request):
		year = request.data.get("year")
		month = request.data.get("month")
		day = request.data.get("day")
		mood = request.data.get("mood")
		note = request.data.get("note").upper()
		args = {"year": text, "month": important, "mood": DayInfo.Mood[mood], "note": note}
		try:
			DayInfo.objects.create(**args)
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="CF black shygar")