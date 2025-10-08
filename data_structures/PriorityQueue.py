from data_structures import Queue

class PriorityQueue(Queue):

    elements = {}
    list_priority = []

    def __init__(self, e, p):
        self.insert(e, p)

    def insert(self, e, p):
        le = len(e)

        if le > 1:
            lp = len(p)

            if le < lp: print('elementi da inserire', le,' < ', lp, 'priorita'); return

            if le > lp: print('elementi da inserire', le, ' > ', lp, 'priorita'); return

            for i in range(le):
                self.elements[e[i]] = p[i]

            self.list_priority.extend(p)

        else: self.elements[e] = p; self.list_priority.append(p)

        self.list_priority.sort(reverse=True)