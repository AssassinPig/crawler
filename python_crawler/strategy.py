class Strategy(object):
    visited_list = None 
    todo_list = None 

    dsf = 0 
    bsf = 1 

    strategy = 0

    def __init__(self, strategy):
        self.visited_list = list() 
        self.todo_list = list() 
        self.strategy = strategy

    def append(self,elem):
        if self.strategy == 0:
            #dsf
            self.todo_list.append(elem)
        elif self.strategy == 1: 
            # bsf
            # add to head 
            self.todo_list.insert(0, elem)


    def pop(self):
        return self.todo_list.pop()

    def make_visited(self, url):
        self.visited_list.append(url)
        if url in self.todo_list:
            self.todo_list.remove(url)

    def todo_count(self):
        return len(self.todo_list)

    def extend_list(self, url_list):
        #1.add 'http' prefix
        #2.reject duplicate item
        for e in self.visited_list:
            if e in url_list:
                url_list.remove(e)

        self.todo_list.extend(url_list)
