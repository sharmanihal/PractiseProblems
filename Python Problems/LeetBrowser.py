
class BrowserHistory:
    
    stack=[]
    currentIndex=-1
    def __init__(self, homepage: str):
        self.stack.clear()
        self.stack.append(homepage)
        self.currentIndex=self.currentIndex+1

    def visit(self, url: str) -> None:
        del self.stack[self.currentIndex+1:len(self.stack)]
        self.stack.append(url)
        self.currentIndex=self.currentIndex+1

    def back(self, steps: int) -> str:
        if steps> self.currentIndex:
            self.currentIndex=0
            return self.stack[0]
        else: 
            set= self.stack[self.currentIndex-steps]
            self.currentIndex=self.currentIndex-steps
            return set

    def forward(self, steps: int) -> str:
        if steps> len(self.stack)-1-self.currentIndex:
            return self.stack[len(self.stack)-1]
        else:
            self.currentIndex=self.currentIndex+steps;
            return self.stack[self.currentIndex]


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory('zav.com')

obj.visit('kno.com')

param_2 = obj.back(7)
param_3 = obj.back(7)
param_4 = obj.forward(5)
param_5 = obj.forward(1)
obj.visit("pwwrrbnw.com")
obj.visit("mosohif.com")

param_6 = obj.back(9)

print(param_2,param_3,param_4,param_5,param_6)

["BrowserHistory","visit","back","back","back","forward","forward","visit","visit","visit","visit","visit","visit","visit","visit","back","visit","forward","back","back","forward","visit","visit","visit","back","visit","forward","visit","visit","visit","visit","back","back","visit","forward","back","visit","visit","back","forward","forward"]
[["vvlf.com"],["rwrjffk.com"],[9],[6],[10],[6],[5],["af.com"],["jjuulz.com"],["vqthh.com"],["viw.com"],["mvvxuo.com"],["sezid.com"],["ncbnmr.com"],["qehugwp.com"],[7],["wg.com"],[9],[6],[4],[2],["foy.com"],["szi.com"],["yqxprn.com"],[9],["pmgoa.com"],[3],["dkik.com"],["mxlcs.com"],["mvs.com"],["uuto.com"],[4],[1],["mdhkz.com"],[9],[9],["zwcc.com"],["afsdng.com"],[6],[1],[3]]
