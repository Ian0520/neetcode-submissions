class TimeMap:
    # [(1, "happy"), (6, "sad"), ...] for each key
    time_stamp_maps = {}
    def __init__(self):
        # time_stamps["key"] -> list[(timestamp, value)]
        self.time_stamp_maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # to a certain timestamp, map[key] = value
        if key not in self.time_stamp_maps:
            self.time_stamp_maps[key] = [(timestamp, value)]
        self.time_stamp_maps[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_stamp_maps:
            return ""
        time_stamp_map = self.time_stamp_maps[key]
        left = 0
        right = len(time_stamp_map)
        value = -1
        while left < right:
            mid = (left + right) // 2
            if timestamp < time_stamp_map[mid][0]:
                right = mid
            else:
                value = max(mid, value)
                left = mid + 1
        if value == -1:
            return ""
        return time_stamp_map[value][1]
        