from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes, api_view

from .models import Tree

@permission_classes([IsAuthenticated])
class AddNode(APIView):
	def post(self, request):
		node = request.data.get("node")
		parent_id = request.data.get("parent_id")
		tree = request.data.get("tree")

		print(parent_id)
		if parent_id != -1:
			try:
				parent = Tree.objects.get(id=parent_id)
			except Exception as e:
				print(str(e))
				return Response(status=status.HTTP_403_FORBIDDEN, data="No such parent id")
			if parent.tree != tree:
				return Response(status=status.HTTP_403_FORBIDDEN, data="Parent is not in the same tree")
		else:
			parent_id = None

		args = {
			"node": node,
			"parent_id": parent_id,
			"tree": tree,
		}
		try:
			Tree.objects.create(**args)
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data="Error")
		return Response(status=status.HTTP_200_OK, data="Codeforces: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class UpdateNode(APIView):
	def post(self, request):
		id = request.data.get("id")
		name = request.data.get("name")
		tree = request.data.get("tree")
		try:
			node = Tree.objects.get(id=id)
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		if node.tree != tree:
			return Response(status=status.HTTP_403_FORBIDDEN, data="Node is not in the same tree")
		node.node = name
		try:
			node.save()
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		return Response(status=status.HTTP_200_OK, data="CodeforcesTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class DeleteNode(APIView):
	def post(self, request):
		id = request.data.get("id")
		tree = request.data.get("tree")
		try:
			node = Tree.objects.get(id=id)
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		if node.tree != tree:
			return Response(status=status.HTTP_403_FORBIDDEN, data="Node is not in the same tree")
		try:
			node.delete()
		except Exception as e:
			print(str(e))
			return Response(status=status.HTTP_403_FORBIDDEN, data=str(e))
		return Response(status=status.HTTP_200_OK, data="CodeforcesTree: Codeforces redblack koi")

@permission_classes([IsAuthenticated])
class GetTree(APIView):
	def get(self, request):
		tree_name = request.GET.get('tree')
		tree = Tree.objects.filter(tree=tree_name).values()
		for node in tree:
			node["children"] = []
			node["name"] = node["node"]
			node["attributes"] = {"id": node["id"]}
			node["_collapsed"] = True
		tree.reverse()
		new_tree = []
		for node in tree:
			new_tree.append(node)
			for node_par in tree:
				if node_par["id"] == node["parent_id"]:
					node_par["children"].append(node)
					new_tree.remove(node)
		if len(new_tree):
			new_tree[0]["_collapsed"] = False
		return Response(status=status.HTTP_200_OK, data=new_tree)

@permission_classes([IsAuthenticated])
class GetAllTrees(APIView):
	def get(self, request):
		trees = Tree.objects.values()
		resp = []
		for el in trees:
			if el["tree"] not in resp:
				resp.append(el["tree"])
		return Response(status=status.HTTP_200_OK, data=resp)