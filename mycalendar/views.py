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
		days = DayInfo.objects.values()
		print(days)
		return Response(status=status.HTTP_200_OK, data="CF black")