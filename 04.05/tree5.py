

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


class ListNode:

	def __init__(self, value, nextNode):
		self.value = value
		self.nextNode = nextNode

	def display(self):
		print(str(self.value), end = "")
		if self.nextNode != None:
			print(", ", end = "")
			self.nextNode.display()


def ReadTree():
	val = input()


	if val != "N":
		Node = TreeNode(val, ReadTree(), ReadTree())
	elif val == "N":
		return None
	else:
		print("Шо за такое ты написал?")

	return Node

def ReadList():
	val = input()

	if val != "N":
		Node = ListNode(val, ReadList())
	elif val == "N":
		return None
	else:
		print("Шо за такое ты написал?")

	return Node


def process(Head, Tree):
	if ((Head.nextNode == None) and (Head.value == Tree.value)):
		return 1

	if Head.nextNode == None:
		return 0

	if (Head.value == Tree.value):
		return (process(Head.nextNode, Tree.left) or process(Head.nextNode, Tree.right))

	return 0



# print("List input: ")

A = ReadList()

# print("Tree input: ")

B = ReadTree()

print("List:")
A.display()
print()
print()
print("Tree:")
B.display()
print()
print()

print("result: " + str(process(A, B)))