from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import CodeforcesTree, RuleTree, EconTree

@permission_classes([IsAuthenticated])
class CodeforcesAdd(APIView):
	def post(self, request):
		name = request.data.get("name")
		# attributes = request.data.get("attributes")
		parent_id = request.data.get("parent_id")

		args = {
			"name": name, 
			"parent_id": parent_id,
		}
		try:
			CodeforcesTree.objects.create(**args)
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Codeforces: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class CodeforcesUpdate(APIView):
	def post(self, request):
		id = request.data.get("id")
		name = request.data.get("name")
		node = CodeforcesTree.objects.filter(id=id)[0]
		print(node)
		node.name = name
		try:
			node.save()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="CodeforcesTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class CodeforcesDelete(APIView):
	def post(self, request):
		id = request.data.get("id")
		print(id)
		try:
			CodeforcesTree.objects.filter(id=id).delete()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="CodeforcesTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class CodeforcesGet(APIView):
	def get(self, request):
		tree = CodeforcesTree.objects.values()
		for node in tree:
			node["children"] = []
			node["attributes"] = {"id": node["id"]}
			node["_collapsed"] = True
		tree.reverse()
		# print(tree)
		new_tree = []
		for node in tree:
			new_tree.append(node)
			for node_par in tree:
				if node_par["id"] == node["parent_id"]:
					node_par["children"].append(node)
					new_tree.remove(node)
		new_tree[0]["_collapsed"] = False
		# print(new_tree)
		return Response(status=status.HTTP_200_OK, data=new_tree)

@permission_classes([IsAuthenticated])
class RulesAdd(APIView):
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
		return Response(status=status.HTTP_200_OK, data="RuleTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class RulesUpdate(APIView):
	def post(self, request):
		id = request.data.get("id")
		name = request.data.get("name")
		node = RuleTree.objects.filter(id=id)[0]
		print(node)
		node.name = name
		try:
			node.save()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="RuleTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class RulesDelete(APIView):
	def post(self, request):
		id = request.data.get("id")
		print(id)
		try:
			RuleTree.objects.filter(id=id).delete()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="RuleTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class RulesGet(APIView):
	def get(self, request):
		tree = RuleTree.objects.values()
		for node in tree:
			node["children"] = []
			node["attributes"] = {"id": node["id"]}
			node["_collapsed"] = True
		tree.reverse()
		# print(tree)
		new_tree = []
		for node in tree:
			new_tree.append(node)
			for node_par in tree:
				if node_par["id"] == node["parent_id"]:
					node_par["children"].append(node)
					new_tree.remove(node)
		new_tree[0]["_collapsed"] = False
		print(new_tree)
		return Response(status=status.HTTP_200_OK, data=new_tree)

@permission_classes([IsAuthenticated])
class EconAdd(APIView):
	def post(self, request):
		name = request.data.get("name")
		# attributes = request.data.get("attributes")
		parent_id = request.data.get("parent_id")

		args = {
			"name": name,
			"parent_id": parent_id,
		}
		try:
			EconTree.objects.create(**args)
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="EconTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class EconUpdate(APIView):
	def post(self, request):
		id = request.data.get("id")
		name = request.data.get("name")
		node = EconTree.objects.filter(id=id)[0]
		print(node)
		node.name = name
		try:
			node.save()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="EconTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class EconDelete(APIView):
	def post(self, request):
		id = request.data.get("id")
		print(id)
		try:
			EconTree.objects.filter(id=id).delete()
		except Exception as e:
			print(str(e))
			print("-------------------------------------------------------")
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="EconTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class EconGet(APIView):
	def get(self, request):
		tree = EconTree.objects.values()
		for node in tree:
			node["children"] = []
			node["attributes"] = {"id": node["id"]}
			node["_collapsed"] = True
		tree.reverse()
		# print(tree)
		new_tree = []
		for node in tree:
			new_tree.append(node)
			for node_par in tree:
				if node_par["id"] == node["parent_id"]:
					node_par["children"].append(node)
					new_tree.remove(node)
		new_tree[0]["_collapsed"] = False
		print(new_tree)
		return Response(status=status.HTTP_200_OK, data=new_tree)