
class TreeNode:
    def __init__(self,k = None,v = None, height = 0, parent = None):
        self.k = k
        self.v = v
        self.height = height
        self.parent = parent
        self.left_child = None
        self.right_child = None


class SimpleBST:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, k):

        curr = self._root
        while curr:
            if curr.k == k:
                return curr.v
            elif curr.k < k:
                curr = curr.left_child
            else:
                curr = curr.right_child
        raise KeyError("Key not present")

    def __setitem__(self, k, v):
        if not self._root:
            self._root = TreeNode(k, v)
        curr = self._root
        while curr:
            if curr.k == k:
                curr.v = v
                return
            elif k <  curr.k:
                if curr.left_child:
                    curr = curr.left_child
                else:
                    curr.left_child = TreeNode(k,v,parent= curr)
                    return
            else:
                if curr.right_child:
                    curr = curr.right_child
                else:
                    curr.right_child = TreeNode(k,v,parent=curr)
                    return
