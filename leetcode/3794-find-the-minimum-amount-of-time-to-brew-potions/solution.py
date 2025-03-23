class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        prefix_skill = [0 for _ in range(n)]
        time = [0 for _ in range(n)]

        for i in range(n):
            if i == 0:
                time[i]= skill[i] * mana[0]
            else:
                time[i]= time[i - 1] + skill[i] * mana[0]
                prefix_skill[i] = prefix_skill[i - 1] + skill[i - 1]
        
        # print(prefix_skill, time)

        for j in range(1, m):
            start_time = max([time[i] - prefix_skill[i] * mana[j] for i in range(n)])
            # print(start_time)
            # print(time)
            for i in range(n):
                if i == 0:
                    time[i] = start_time + skill[i] * mana[j]
                else:
                    time[i] = time[i - 1] + skill[i] * mana[j]
        return time[-1]

