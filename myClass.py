class mymy:
    def __init__(self):
        self.seq =''
        self.gc =0.0
        print("class mymy created!")

    def calcGC(self):
        c = self.count('C')
        g = self.count('G')
        self.gc = float(c+g)/len(seq)

