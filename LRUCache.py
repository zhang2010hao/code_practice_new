
class DlinkNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = DlinkNode()
        self.tail = DlinkNode()
        self.size = 0

        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.movetohead(node)

            return node.value



    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.cache[key] = node
            self.movetohead(node)
        else:
            node = DlinkNode(key, value)
            self.cache[key] = node
            self.addtohead(node)
            self.size += 1

            if self.size > self.capacity:
                removenode = self.removetail()
                self.cache.pop(removenode.key)
                self.size -= 1


    def addtohead(self, node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removenode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def movetohead(self, node):
        # 先刪除
        self.removenode(node)
        # 再加到头部
        self.addtohead(node)

    def removetail(self):
        node = self.tail.pre
        self.removenode(node)

        return node