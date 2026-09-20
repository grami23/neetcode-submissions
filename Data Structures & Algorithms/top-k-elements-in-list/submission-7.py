class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {} #dict for num: # of times shown
        result = [] # those same numbers but as repeats
        
        for num in nums:
            if not tracker.get(num):
                tracker[num] = 0
            tracker[num] = tracker[num] + 1

        sorted_list = dict(sorted(tracker.items(), key=lambda item: item[1], reverse=True))
        counter = 0

        for key, value in sorted_list.items():
            print(key)
            result.append(key)
            counter = counter + 1
            if counter == k:
                break

        return result
