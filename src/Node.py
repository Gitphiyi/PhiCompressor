class Node:
    def __init__(self, let = None, val = None, l = None, r = None):
        self.let = let
        self.val = val 
        self.l = l
        self.r = r
        
    def __lt__(self, other):
        return self.val < other.val
        
    def __repr__(self):
        return f"Node({self.let}, {self.val})"