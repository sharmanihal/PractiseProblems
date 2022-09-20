class SeatManager:
    res=0
    def __init__(self, n: int):
        i=1
        while(n!=0):
            self.unreserve.append(i)
            i=i+1
            n=n-1



        
# ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
# [[5], [], [], [2], [], [], [], [], [5]]
# Output
# [null, 1, 2, null, 2, 3, 4, 5, null]

ans=SeatManager(5)
print(ans.reserve())
print(ans.reserve())
print(ans.unreserve(2))
print(ans.reserve())
print(ans.reserve())
print(ans.reserve())
print(ans.reserve())
print(ans.unreserve(5))


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)