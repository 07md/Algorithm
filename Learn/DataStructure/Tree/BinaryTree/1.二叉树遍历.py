class TreeNode:
    def __init__(self, value=None):
        self.value, self.left, self.right = value, None, None

    def preOrderRecursive(self):
        if self is None:
            return
        print(self.value, end=' ')
        if self.left:
            self.left.preOrderRecursive()
        if self.right:
            self.right.preOrderRecursive()

    def inOrderRecursive(self):
        if self is None:
            return
        if self.left:
            self.left.inOrderRecursive()
        print(self.value, end=' ')
        if self.right:
            self.right.inOrderRecursive()

    def posOrderRecursive(self):
        if self is None:
            return
        if self.left:
            self.left.posOrderRecursive()
        if self.right:
            self.right.posOrderRecursive()
        print(self.value, end=' ')

    def preOrderLoop(self):
        stack = [self]
        while stack:
            temp = stack.pop()
            print(temp.value, end=' ')
            if temp.right is not None:
                stack.append(temp.right)
            if temp.left is not None:
                stack.append(temp.left)

    def inOrderLoop(self):
        if self is not None:
            stack, temp = [], self
            while stack or temp is not None:
                if temp is not None:
                    stack.append(temp)
                    temp = temp.left
                else:
                    temp = stack.pop()
                    print(temp.value, end=' ')
                    temp = temp.right

    def posOrderLoop(self):
        """
        前序遍历的次序是：中左右
        后续遍历的次序是：左右中
        相当于将前序遍历中左右的顺序颠倒再倒着打印
        """
        stack1 = []
        if self is not None:
            stack2 = [self]
            while stack2:
                temp = stack2.pop()
                stack1.append(temp)
                if temp.left is not None:
                    stack2.append(temp.left)
                if temp.right is not None:
                    stack2.append(temp.right)
        while stack1:
            print(stack1.pop().value, end=' ')


if __name__ == '__main__':
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)

    print("==============recursive==============")
    print("pre order recursive: ", end='')
    head.preOrderRecursive()
    print()
    print("in order recursive: ", end='')
    head.inOrderRecursive()
    print()
    print("pos order recursive: ", end='')
    head.posOrderRecursive()
    print()

    print("============no recursive=============")
    print("pre order loop: ", end='')
    head.preOrderLoop()
    print()
    print("in order loop: ", end='')
    head.inOrderLoop()
    print()
    print("pos order loop: ", end='')
    head.posOrderLoop()
    print()
