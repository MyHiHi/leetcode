class node:
    def __init__(self, value=-1):
        self.val = value
        self.next = None


def create(s):
    p = node()
    head = p
    for i in s.split(" "):
        n = node(int(i))
        p.next = n
        p = n
    return head


def merge(one, two):
    res = node()
    head = res
    while one.next and two.next:
        val = 0
        p1, p2 = one.next, two.next
        if p1.val < p2.val:
            val = p1.val
            one = one.next
        else:
            val = p2.val
            two = two.next
        p = node(val)
        res.next = p
        res = p
    res.next = one.next if one.next else two.next
    return head


def seeMe(n):
    while n.next:
        print(n.next.val, end=" ")
        n = n.next


s1, s2 = input(), input()
one, two = create(s1), create(s2)
res = merge(one, two)
seeMe(res)
