def frontRoot(n,tree,root):
    leftChild = 2*root+1
    if leftChild < len(tree): # 先序遍历的逻辑：如果有 X 子树，就遍历，没有就算了
        n = frontRoot(n,tree,leftChild)
        n += 1

    tree[root] = n  

    rightChild = 2*root+2
    if rightChild < len(tree): # 右子树就不需要特殊的判断了
        n = frontRoot(n+1,tree,rightChild)


    return n

l = [1,2,3,4,5,6,7]
print(frontRoot(0,l,0))
print(l)
