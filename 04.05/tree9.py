

class TreeNode:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

	def display(self):
		print("(" + str(self.value) + ": ", end = "")

		if self.left != None:
			self.left.display()
			print(", ", end = "")
		else:
			print("(None, ", end = "")


		if self.right != None:
			self.right.display()
			print(")", end = "")
		else:
			print("None)", end = "")


def ReadTree():
	val = input()

	if val != "N":
		Node = TreeNode(val, ReadTree(), ReadTree())
	elif val == "N":
		return None
	else:
		print("Шо за такое ты написал?")


	return Node

def Ind(pPtr, qPtr, Tree, index, p, q):
	# p = None
	# q = None

	if index == qPtr:
		# print("Hi")
		q = Tree

	if index == pPtr:
		p = Tree

	index+=1
	if Tree.left != None:
		index, p, q = Ind(pPtr, qPtr, Tree.left, index, p, q)
	if Tree.right != None:
		index, p, q = Ind(pPtr, qPtr, Tree.right, index, p, q)
	return index, p, q


def process(Tree, p, q):
	if Tree == None:
		return None

	if(Tree == p or Tree == q):
		return Tree

	Left = process(Tree.left, p, q)
	Right = process(Tree.right, p, q)

	if (Left != None and Right != None):
		return Tree

	if (Left != None):
		return Left
	else:
		return Right

A = ReadTree()

# A.display()

pPtr = int(input())
qPtr = int(input())

p = None
q = None

p = Ind(pPtr, qPtr, A, 1, p, q)[1]
q = Ind(pPtr, qPtr, A, 1, p, q)[2]

process(A, p, q).display()
print()
# p = int(input())

# q = int(input())