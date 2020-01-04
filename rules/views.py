from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import RuleTree
from .serializers import RuleTreeSerializer

@permission_classes([IsAuthenticated])
class Add(APIView):
	def post(self, request):
		name = request.data.get("name")
		# attributes = request.data.get("attributes")
		parent_id = request.data.get("parent_id")

		args = {
			"name": name, 
			"parent_id": parent_id,
		}
		try:
			RuleTree.objects.create(**args)
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Rule: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class GetAll(APIView):
	def get(self, request):
		rule_tree = RuleTreeSerializer(RuleTree.objects.all(), many=True)
		tree = RuleTree.objects.values()
		for node in tree:
			node["children"] = []
			node["attributes"] = {"id": node["id"]}
		tree.reverse()
		# print(tree)
		new_tree = []
		for node in tree:
			new_tree.append(node)
			for node_par in tree:
				if node_par["id"] == node["parent_id"]:
					node_par["children"].append(node)
					new_tree.remove(node)
		# print(new_tree)
		return Response(status=status.HTTP_200_OK, data=new_tree)