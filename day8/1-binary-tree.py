class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree():
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(node)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    def preorder_traversal(self, root: Node):
        if root == None:
            return
        print(root.elem, end=' ')
        self.preorder_traversal(root.lchild)
        self.preorder_traversal(root.rchild)

    def inorder_traversal(self, root: Node):
        if root == None:
            return
        self.inorder_traversal(root.lchild)
        print(root.elem, end=' ')
        self.inorder_traversal(root.rchild)

    def postorder_traversal(self, root: Node):
        if root == None:
            return
        self.preorder_traversal(root.lchild)
        self.preorder_traversal(root.rchild)
        print(root.elem, end=' ')

    def level_traversal(self, root):
        if root == None:
            return
        node = root
        myQueue = []
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem, end=' ')
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(10):
        tree.add(i)

    print('先序：')
    tree.preorder_traversal(tree.root)
    print('\n中序：')
    tree.inorder_traversal(tree.root)
    print('\n后序：')
    tree.postorder_traversal(tree.root)
    print('\n层序：')
    tree.level_traversal(tree.root)
