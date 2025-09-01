class Node:
    def __init__(self, value: int = 0, p: "Node" = None):
        self.value = value
        self.p = p
    
    @classmethod
    def new(cls, value: int = 0, p: "Node" = None):
        return cls(value=value, p=p)

class Fila:
    def __init__(self, data: "Node" = None, top: "Node" = None):
        self.data = data
        self.top = top

    @classmethod
    def new_fila(cls, value: int = 0):
        obj = Node.new(value=value)
        return cls(data=obj, top=obj)

    def push(self, value: int = 0, node: "Node" = None):
        obj = Node.new(value=value, p=node)
        self.top.p = obj
        self.top = obj
    
    def print_fila(self, node: "Node" = None):
        if node == None:
            obj = self.data
            print(f"\n{obj.value}")
            if obj.p != None:
                self.print_fila(obj.p)
        else:
            obj = node
            if obj.p != None:
                print(f"{obj.value}")
                self.print_fila(obj.p)
            else:
                print(f"{obj.value}")
    
    def pop(self):
        if self.data != None:
            temp = self.data 
            self.data = self.data.p
            temp.p = None
            del temp
        else:
            raise IndexError("fila está vazia")