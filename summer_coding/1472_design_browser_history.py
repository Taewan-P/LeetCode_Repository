class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited = 1
        self.max_visited = 1
        self.history = dict()
        self.history[1] = homepage
        

    def visit(self, url: str) -> None:
        if self.visited == self.max_visited:
            self.visited += 1
            self.max_visited += 1
        else:
            for r in range(self.visited+1, self.max_visited+1):
                self.history.pop(r)
            self.visited += 1
            self.max_visited = int(self.visited)
        
        self.history[self.visited] = url
        

    def back(self, steps: int) -> str:
        if steps >= self.visited:
            self.visited = 1
        else:
            self.visited -= steps
            
        return self.history.get(self.visited, "")
        

    def forward(self, steps: int) -> str:
        if self.visited + steps >= self.max_visited:
            self.visited = int(self.max_visited)
        else:
            self.visited += steps
            
        return self.history.get(self.visited, "")
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)