class NodeList:

    def __init__(self, value, ptr=None):
        self.value = value
        self.next = ptr


def print_list(head):

    print()

    current = head

    while current is not None:

        print(current.value, end=" >> ")

        current = current.next

    print("NULL")


def reverse_part(head):

    prev = None
    current = head

    while current is not None:

        nxt = current.next

        current.next = prev

        prev = current
        current = nxt

    return prev


def process(head):

    if head is None or head.next is None:
        return head

    # ======================
    # Ищем середину
    # ======================

    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:

        slow = slow.next
        fast = fast.next.next

    # slow = середина

    second_half = slow.next
    slow.next = None

    second_half = reverse_part(second_half)

    first = head
    second = second_half

    while second is not None:

        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2

    return head


if __name__ == "__main__":

    print(
        "Введите числа списка.\n"
        "Ctrl+D / Ctrl+Z для конца ввода.\n"
    )

    values = []

    try:

        while True:
            values.append(int(input()))

    except EOFError:
        pass

    if not values:
        exit()

    head = NodeList(values[0])

    current = head

    for value in values[1:]:

        current.next = NodeList(value)

        current = current.next

    process(head)

    print_list(head)