"""
node.py
Represents a Node in a singly linked list
"""

class Node():

    def __init__(self, value, next=None):
        self.__value = value   
        self.__next_node = next  

    

    
    def is_first(self):
        return self.__next_node == None

    
    def get_value(self):
        return self.__value 
    
   
    def get_next_node(self):
        return self.__next_node
    
   
    def set_value(self, new_value):
        self.__value = new_value 

    
    def set_next_node(self, new_next):
       
        if self.__check_valid_node(new_next):
            self.__next_node = new_next 

    def __check_valid_node(self, node):
        if type(node) != Node and node != None:
            raise Exception("Error: Input must be a valid Node or None")
        return True
    
   
    def __str__(self):
        return str(self.get_value())
    
if __name__ == "__main__":
    pass
