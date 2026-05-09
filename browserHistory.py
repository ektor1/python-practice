# Browser History
class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    # Browser history where the first url is stored at the beginning. Implementation with double linked list
    # has to be of max length = capacity

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_capacity = capacity 
        # create two dummy nodes for head and tail
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.currently_viewing = self.tail 
        # hash map to access nodes for deletion in constant time O(1)
        self.node_map = {}

    def visit(self, url: str) -> None:
        if url in self.node_map:
            self.remove(url)
            self.insert(url)
            return

        self.insert(url)
        if self.cur_capacity > 0:
            self.cur_capacity += 1

        else:
            url_to_remove = self.tail.prev.url
            self.remove(url_to_remove)

    def insert(self, url: str) -> None:
        new_node = Node(url)
        if self.currently_viewing != self.head.next:
            prev, cur, next = self.currently_viewing, new_node, self.tail 
        else:
            prev, cur, next = self.head, new_node, self.head.next
        
        prev.next = cur
        next.prev = cur
        cur.prev = prev
        cur.next = next
        self.node_map[url] = new_node
        self.currently_viewing = new_node

    def remove(self, url: str) -> None:
        to_remove = self.node_map[url]
        prev, next = to_remove.prev, to_remove.next
        prev.next = next
        next.prev = prev
        del self.node[url]

    def get_current_url(self):
        if self.currently_viewing != self.tail:
            return self.currently_viewing.url 
        else:
            return "Browser history is empty"

    def back(self):
        if self.currently_viewing.next != self.tail:
            self.currently_viewing = self.currently_viewing.next
            return self.currently_viewing.url
        else:
            return "No history beyond this point"    
            
    def forward(self):
        if self.currently_viewing.prev != self.head:
            self.currently_viewing = self.currently_viewing.prev
            return self.currently_viewing.url
        else:
            return "No history beyond this point"

    def print_history(self) -> list[str]:
        history = [] 
        cur = self.head.next

        while cur != self.tail:
            history.append(cur.url) 
            cur = cur.next

        return history




