from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import Skill

@permission_classes([IsAuthenticated])
class Add(APIView):
	def post(self, request):
		name = request.data.get("name")
		commentary = request.data.get("commentary")
		field = request.data.get("field")
		comprehense = request.data.get("comprehense")
		importance = request.data.get("importance")

		args = {
			"name": name, 
			"commentary": commentary, 
			"field": field, 
			"comprehense": comprehense, 
			"importance": importance,
		}
		try:
			Skill.objects.create(**args)
		except Exception as e:
			# print(str(e))
			# print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Skill: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class Delete(APIView):
	def post(self, request):
		id = request.data.get("id")
		print(id)
		try:
			Skill.objects.filter(id=id).delete()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Skill: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class GetAll(APIView):
	def get(self, request):
		people = Skill.objects.values()
		return Response(status=status.HTTP_200_OK, data=people)