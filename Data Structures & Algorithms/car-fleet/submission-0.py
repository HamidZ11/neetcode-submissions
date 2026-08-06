class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, reverse = True)
        carstack = []
        for position, speed in cars:
            time = (target - position) / speed
            if not carstack:
                carstack.append(time)
            else:
                if time > carstack[-1]:
                    carstack.append(time)
        
        return len(carstack)