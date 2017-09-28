
class Node(object):
    def __init__(self,data = -1,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self,data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)
    #递归实现前序遍历
    def pre_order(self,start):
        node = start
        if node == None:
            return
        print(node.data)
        if node.lchild == None and node.rchild == None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def isEmpty(self):
        return True if self.root.data == -1 else False


if __name__ == '__main__':
    # arr = []
    # for i in range(10):
    #     arr.append(i)
    # print(arr)
    arr = ['case1', '借款成功', "{'Content-Type': 'application/json;charset=utf-8'}", '{"creditorSrcCode":"002",}', '{"returnCode":"0000","returnDesc":"成功","returnContent":null,"canResend":false}']

    tree = BinaryTree()
    for i in arr:
        tree.add(i)

    print('pre_order:')
    tree.pre_order(tree.root)

