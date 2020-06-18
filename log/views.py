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

from .models import Log

@permission_classes([IsAuthenticated])
class Add(APIView):
	def post(self, request):
		text = request.data.get("text")
		important = request.data.get("important")
		category = request.data.get("category").upper()
		args = {"text": text, "important": important, "category": Log.Category[category]}
		try:
			Log.objects.create(**args)
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		return Response(status=status.HTTP_200_OK, data="Codeforces red koi")

@permission_classes([IsAuthenticated])
class Delete(APIView):
	def post(self, request):
		id = request.data.get("id")
		try:
			Log.objects.get(id=id).delete()
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		return Response(status=status.HTTP_200_OK, data="Log: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class GetAll(APIView):
	def get(self, request):
		logs = Log.objects.values()
		ret = []
		for log in logs:
			cur = log
			cur["time"] = str(log["date"]) + " => " + str(log["time"]).split(".")[0]
			ret.append(cur)
		ret.reverse()
		return Response(status=status.HTTP_200_OK, data=ret)