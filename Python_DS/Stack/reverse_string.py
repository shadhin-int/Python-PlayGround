from stack import Stack


def reverse_string(stack, stra):
    for char in range(len(stra)):
        stack.push(stra[char])
    rev_string = ''
    while not stack.is_empty():
        rev_string += stack.pop()
    return rev_string


stack = Stack()
input_string = "!evitacudE ot emocleW"
print(reverse_string(stack, input_string))
