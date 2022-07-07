class SLList:
    def __init__(self):
        self.head = None            # start of the list location
    
    def add_to_front(self, val):	# added this line, takes a value
        new_node = SLNode(val)      # create a new instance of our Node class using the given value
        current_head = self.head    # saves the current head in a variable (for later use)
        new_node.next = current_head # SET the new nodes next TO the lists current head
        self.head = new_node        # SET the list's head TO the new node we created at the start of this method
        return self

    def add_to_back(self, val):
        # use add_to_front if list is empty
        if self.head == None:
            self.add_to_front(val)
            return self

        # if list is not empty continue on
        new_node = SLNode(val)
        runner = self.head          # set iterator to the start of the list
        while (runner.next != None):
            runner = runner.next    # this will eventually become the last node in the list and exit the loop
        runner.next = new_node      # now set that previously last node next from "none" to the new_node
        return self

    # traversing through a linked list! via iterating using a "pointer"
    def print_values(self):
        runner = self.head          # a pointer to the list's first node
        while (runner != None):     # says "keep going until we get to a node that has no next (ie end of the linked list)"
            print(runner.value)     # prints the current nodes value
            runner = runner.next    # set the runner to its next neighbor
        return self                 # returning self just to allow chaining
    


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None



#testing
my_list = SLList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()


