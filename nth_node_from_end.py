from linklist import linkList

def nth_node_from_end(root, n):
    t = root
    for i in range(n):
        t = t.next

    s = root
    if(not t):
        return
    while(t):
        t = t.next
        s = s.next

    return s.data


l = linkList()
l.createList()
print(nth_node_from_end(l.head,2))
