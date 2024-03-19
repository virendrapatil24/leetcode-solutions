class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash_map = {}
        for task in tasks:
            hash_map[task] = hash_map.get(task, 0) + 1
        sorted_hash_map = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)
        max_count = sorted_hash_map[0][1]
        count_max_count = 0
        for counts in sorted_hash_map:
            if counts[1] == max_count:
                count_max_count += 1
            else:
                break
        return max((max_count - 1) * (n + 1) + count_max_count, len(tasks))
        
