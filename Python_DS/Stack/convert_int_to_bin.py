from stack import Stack

stack = Stack()


def convert_int_to_bin(dec_number):

    if dec_number is None:
        return False

    bin_value = ""
    while dec_number > 0:
        rem = dec_number % 2
        stack.push(rem)
        dec_number = dec_number//2

    while not stack.is_empty():
        bin_value += str(stack.pop())
    return bin_value
