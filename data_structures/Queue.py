class Queue:

    elements = []

    def __init__(self, element):
        self.insert(self, element)

    def insert(self, element, *elements):
        self.elements.append(element)

        if len(elements) > 0: self.elements.extend(elements)

    def remove(self):
        return self.elements.remove(0)

    def isEmpty(self):
        return self.elements == []