class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []

        self.data[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        values = self.data[key]
        left = 0 
        right = len(values) - 1

        result = ""

        while left <= right:
            middle = (left + right) // 2

            if values[middle][1] == timestamp:
                return values[middle][0]
            
            elif values[middle][1] < timestamp:
                result = values[middle][0]
                left = middle + 1

            else: 
                right = middle - 1
        
        return result