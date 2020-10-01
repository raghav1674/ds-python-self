class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:

    __size = 0

    def __init__(self):
        self.head = None

    def push_front(self, data):
        List.__size += 1
        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def push_back(self, data):
        List.__size += 1
        new_node = Node(data)
        temp = self.head
        if self.head is None:
            self.head = new_node
        else:

            while(temp.next is not None):
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def __node_at(self, index):
        num = 0
        if self.head is not None:
            temp = self.head
            while(num != index):
                temp = temp.next
                num += 1
            return temp
        return None

    def insert(self, index, data):
        List.__size += 1
        new_node = Node(data)
        prev_node = self.__node_at(index)

        if prev_node is not None:

            new_node.next = prev_node.next
        if prev_node.next is not None:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node

    def pop_back(self):

        temp = self.head

        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            List.__size -= 1
        else:
            prev_node = None

            while(temp.next is not None):
                prev_node = temp
                temp = temp.next
            temp = None
            prev_node.next = temp
            List.__size -= 1

    def pop_front(self):

        temp = None
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            List.__size -= 1
        else:
            temp = self.head
            temp.next.prev = None
            self.head = self.head.next
            temp = None
            List.__size -= 1

    def remove(self, data):

        prev_node = None
        if self.head is not None:
            temp = self.head
            try:
                while(temp.data != data):
                    prev_node = temp
                    temp = temp.next
                if temp == self.head:
                    self.pop_front()
                elif temp.next is None:
                    self.pop_back()
                else:
                    prev_node.next = temp.next
                    temp.next.prev = prev_node
                    temp = None
                    List.__size -= 1
            except Exception as e:
                print(e)

    def index(self, data):
        num = 0
        if self.head is not None:
            temp = self.head
            try:
                while(temp.data != data):

                    temp = temp.next
                    num += 1

                return num
            except Exception as e:
                pass

        return -1

    def display(self):
        if self.head is None:
            return
        temp = self.head
        while(temp is not None):
            print(temp.data, end=" ")
            temp = temp.next


    def count(self, data):
        num = 0
        item_count =0
        if self.head is not None:
            temp = self.head

            while(num < List.__size):
                if(temp.data == data):
                     item_count+=1
                temp = temp.next
                num += 1

            return item_count
    
    @classmethod 
    def __len__(cls):
        return cls.__size


myll = List()
myll.push_back(10)
myll.push_back(2)
myll.push_back(1)
myll.push_front(3)
myll.push_front(10)
# myll.pop_back()
# myll.pop_back()
# myll.pop_back()
# myll.pop_front()
# myll.pop_back()
# myll.remove(3)

print(myll.index(10))



print(myll.count(10))

print(len(myll))
myll.display()
