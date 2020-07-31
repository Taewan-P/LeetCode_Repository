class UndergroundSystem:

    def __init__(self):
        """
        Database Structure
        { id : [("stationName", time, "in/out"), ("stationName", time, "in/out")] }
        """
        self.db = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        t_log = (stationName, t, "i")
        
        if self.verifyUser(id):
            # If user exists
            self.db[id].append(t_log)
            
        else:
            self.createUser(id)
            self.db[id].append(t_log)
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        t_log = (stationName, t, "o")
        
        if self.verifyUser(id):
            # If user exists
            self.db[id].append(t_log)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        db = self.db.values()
        parsed = []
        
        for record in db:
            for i in range(0, len(record)-1, 2):
                # Compare i, i+1 since i is "in" and i+1 is "out".
                if record[i][0] == startStation and record[i+1][0] == endStation:
                    parsed.append(record[i+1][1] - record[i][1])
                    
        if parsed:
            return sum(parsed)/len(parsed)
        else:
            return 0.0
                

    def verifyUser(self, id: int) -> bool:
        return True if self.db.get(id) else False
    
    def createUser(self, id: int) -> None:
        self.db[id] = []
    
    
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)