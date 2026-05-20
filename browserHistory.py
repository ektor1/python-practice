class Node:
    def __init__(self, val, prev=None, next=None):
        self.data = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """
    Implementation of browser history with LRU cache
    No dupe URLs allowed. Nodes are stored in a hash map for O(1) lookup time
    Once we reach capacity we pop FIFO
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.n_visited = 0
        self.urls_visited = {}
        self.head = None
        self.tail = None


    def visit(self, url: str) -> None:
        """
        (1) If we have capacity and haven't visited that url before, increment n_visisted. Else FIFO
        (2) Always insert the new node
        """
        if self.n_visited == self.capacity:
            self.remove(self.head.data)
        elif url not in self.urls_visited:
            self.n_visited += 1
        
        self.insert(url) 


    def insert(self, url: str) -> None:
        """
        (1) If url has been visited before get the node from hash map. Else create a new node
        (2) If list is empty set both head and tail equal to that node
            Else add node to tail
        """
        if self.get_current_url == url:
            return 
        
        if url in self.urls_visited:
            self.remove(url)
            node = self.urls_visited[url]
        else:
            node = Node(url)

        if self.head is None:
            self.head = node
            self.tail = node

        elif self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            prev, cur = self.tail, node
            prev.next = node
            cur.prev = prev
            self.tail = cur

        self.urls_visited[url] = node


    def remove(self, url: str) -> None:
        node = self.urls_visited[url]
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None

        else:
            prev, cur, next = node.prev, node, node.next
            prev.next = next
            next.prev = prev


    def get_current_url(self) -> Node | str:
        if self.tail is not None:
            return self.tail.data
        return "History is empty"


    def back(self):
        pass
            

    def forward(self):
        pass


    def print_history(self) -> Node | str:
        if self.tail is not None:
            cur = self.tail
            while cur is not None:
                print(cur.data)
                cur = cur.prev
        else:
            return "History is empty"



if __name__ == '__main__':
    session = BrowserHistory(10)
    session.print_history()
    for url in ['youtube.com', 'bloomberg.com', 'investopedia.com', 'google.com']:
        session.visit(url)
    session.print_history()
    session.visit('youtube.com')
    session.print_history()
