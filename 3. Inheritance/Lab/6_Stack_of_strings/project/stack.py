class Stack:
    data = []

    def push(self,element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data
    def __str__(self):
        result = ", ".join(x for x in reversed(self.data))
        return f"[{result}]"



