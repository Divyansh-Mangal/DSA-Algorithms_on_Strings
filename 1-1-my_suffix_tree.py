# python3
# Build suffix trie - Attempt 4
import sys

class Node():
    def __init__(self , value, parent, rank):
        self.parent = parent
        self.value = value
        self.children = []
        self.rank = rank

def addNode(tree, treeNode, pattern, n):
    i = 0
    while treeNode.value[i] == pattern[i]:
        i+=1
        if i == len(pattern) or i == len(treeNode.value):
            break

    if i!=0 and i < len(pattern) and i<len(treeNode.value):

        tree.append(Node(treeNode.value[:i:], treeNode.parent, n))
        treeNode.parent.children.append(tree[n])
        treeNode.parent.children.pop(treeNode.parent.children.index(treeNode))
        treeNode.parent = tree[n]
        tree[n].children.append(treeNode)
        treeNode.value = treeNode.value[i::]
        n+=1
        tree.append(Node(pattern[i::], tree[n-1], n))
        tree[n].parent.children.append(tree[n])
        n+=1


    elif i!=0 and i < len(pattern) and i==len(treeNode.value):
        tree, n = build_trie(tree, pattern[i::], n, treeNode.rank)

    return tree, n

def build_trie(tree, pattern, n, t):
    check = 1
    for child in tree[t].children:
        if child.value[0] == pattern[0]:
            check = 0
            tree, n = addNode(tree, child, pattern, n)
            break

    if check:
        tree.append(Node(pattern, tree[t], n))
        tree[n].parent.children.append(tree[n])
        n+=1

    return tree, n

def build_suffix_tree(text):
    result = []
    patterns = []
    tree = []
    tree.append(Node('root', None , 0))
    tree.append(Node(text, tree[0], 1))
    tree[0].children.append(tree[1])
    n = 2

    for i in range(1,len(text)):
        tree, n = build_trie(tree, text[i::], n, 0)

    for a in tree:
        if a.value != 'root':
            result.append(a.value)

    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    #text = input().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
