class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        offline = [0] * numberOfUsers

        events = sorted(events, key=lambda event:(int(event[1]), event[0] == "MESSAGE") )
        print(events)

        for event, time, msg in events:

            if event == "MESSAGE":
                if msg == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif msg == "HERE":
                    for i in range(numberOfUsers):
                        mentions[i] += 1 if offline[i] <= int(time) else 0
                else:
                    ids = msg.split("id")
                    print(ids)
                    for i in range(1, len(ids)):
                        mentions[int(ids[i])] += 1 # if offline[int(ids[i])] <= int(time) else 0

            else:
                offline[int(msg)] = int(time) + 60

        return mentions
                
        
