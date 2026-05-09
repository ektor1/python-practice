class TubeTimes:
    def __init__(self):
        self.hash_map = {}
        self.tap_in_map = {}
        pass

    def tap_in(self, customer_id: int, time: float, location: str):
        self.tap_in_map[customer_id] = [time, location]

    def tap_out(self, customer_id: int, time: float, location: str):
        if customer_id not in self.tap_in_map:
            return
        
        start_time = self.tap_in_map[customer_id][0]
        start_station = self.tap_in_map[customer_id][1]
        key = start_station + "_" + location
        
        if key not in self.hash_map:
            self.hash_map[key] = [0.0, 0]

        self.hash_map[key][0] += time - start_time
        self.hash_map[key][1] += 1

        del self.tap_in_map[key]

    def get_average_time(self, start_location: str, end_location: str) -> float | None:
        key = start_location + "_" + end_location
        if key not in self.hash_map:
            return None
        
        data = self.hash_map[key]
        average =  data[0] / data[1]
        return average


tt = TubeTimes()
tt.tap_in(0, 4, "westSilvertown")
tt.tap_out(0, 10, "Bank")
tt.get_average_time("westSilvertown","Bank")

