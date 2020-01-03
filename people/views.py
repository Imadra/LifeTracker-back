from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import Person

@permission_classes([IsAuthenticated])
class Add(APIView):
	def post(self, request):
		name = request.data.get("name")
		commentary = request.data.get("commentary")
		strengths = request.data.get("strengths")
		weaknesses = request.data.get("weaknesses")
		happyness = request.data.get("happyness")
		img = request.data.get("img")

		args = {
			"name": name, 
			"commentary": commentary, 
			"strengths": strengths, 
			"weaknesses": weaknesses, 
			"happyness": happyness,
			"img": img
		}
		try:
			Person.objects.create(**args)
		except Exception as e:
			# print(str(e))
			# print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Person: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class GetAll(APIView):
	def get(self, request):
		people = Person.objects.values()
		# ret = []
		# for person in people:
		# 	cur = {}
		# 	cur["name"] = person["name"]
		# 	cur["important"] = log["important"]
		# 	cur["category"] = log["category"]
		# 	ret.append(cur)
		# ret.reverse()
		return Response(status=status.HTTP_200_OK, data=people)