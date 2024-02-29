
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        head2 = self.head
        while head2:
            print(head2.data)
            head2 = head2.next

    def push_ll(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data
        return "Qo'shildi !!!"

    def insert_ll(self, prev_element, new_element):
        if prev_element is None:
            return "Error!!!"

        head2 = self.head
        while head2:
            if head2.data == prev_element:
                new_element = Node(new_element)
                new_element.next = head2.next
                head2.next = new_element
                return "Qo'shildi !!!"
            head2 = head2.next

    def append(self, new_element):

        new_element = Node(new_element)
        if self.head is None:
            self.head = new_element
            return "Linked listda element yaratildi !!!"

        head2 = self.head
        while head2.next:
            head2 = head2.next
        head2.next = new_element
        return "Qo'shildi !!!"


if __name__ == "__main__":

    # Tugun hosil qilish
    x = Node(int(input("Element kiriting: ")))
    y = Node(int(input("Element kiriting: ")))
    a = Node(int(input("Element kiriting: ")))
    b = Node(int(input("Element kiriting: ")))
    c = Node(int(input("Element kiriting: ")))

    # Tugunlarni bog'lash
    a.next = b
    b.next = c
    c.next = x
    x.next = y

    # Linked list obyektini yaratish
    ll = LinkedList()
    ll.head = a
    ll.print_ll()

    # Boshiga element qo'shish
    print("\nBoshiga element qo'shish\n")
    new_el = int(input("new elelemnt: "))
    print(ll.push_ll(new_el))
    ll.print_ll()

    # Istalgan elementdan keyinga qo'shish
    print("\nIstalgan elementdan keyin element qo'shish\n")
    prev_el = int(input("prev element: "))
    new_el = int(input("new element: "))
    print("\n", ll.insert_ll(prev_el, new_el), "\n")
    ll.print_ll()

    # Oxiriga element(tugun) qo'shish
    print("\nOxiriga element qo'shish\n")
    new_el = int(input("new element: "))
    print("\n", ll.append(new_el))
    ll.print_ll()

    """Test qilindi:
        1) x = 2, y = 8, a = 10, b = 0, c = 1
        2) x = 3, y = 5, a = -4, b = 1, c = 9
        3) x = -8, y = 11, a = 6, b = 5, c = 3
        4) x = 0, y = 7, a = 4, b = 23, c = 5
        5) x = 200, y = 10, a = 30, b = 98, c = 1"""
