""" Implementation of a simple Linked List in Python. """


class Node:
    def __init__(self, dataval: int=None) -> None:
        self.dataval: int = dataval
        self.nextval: Node = None
    
    def set_nextval(self, nextval) -> None:
        self.nextval = nextval

    def return_val(self) -> int:
        return self.dataval


class SLinkedList:
    def __init__(self) -> None:
        self.headval: Node = None

    def set_headval(self, headval: Node) -> None:
        self.headval = headval


if __name__ == "__main__":
    list1 = SLinkedList()
    list1.set_headval(Node(1))
    list1.headval.set_nextval(Node(2))
    list1.headval.nextval.set_nextval(Node(3))
    print(list1)
    print(list1.headval.return_val())
    print(list1.headval.nextval.return_val())
    print(list1.headval.nextval.nextval.return_val())