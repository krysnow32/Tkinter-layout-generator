class SimpleIter():
    def __init__(self):
        self.iter = 0

    
    def next(self) -> int:
        self.iter += 1
        return self.iter - 1
    

    def restart(self) -> None:
        self.iter = 0
