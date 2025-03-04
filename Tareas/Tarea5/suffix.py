class Suffix: 
    def __init__(self,text,position): 
        self.text = text
        self.position = position
    def __lt__(self, other):
        return self.text.lower() < other.text.lower()
    
    def __str__(self):
        return f"({self.position}){self.text}"