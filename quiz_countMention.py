class Solution(object):
    def countMentions(self, numberOfUsers, events):
        # Sort events by timestamp.
        # Tie-breaker: Process OFFLINE (priority 0) before MESSAGE (priority 1).
        # This ensures that if a user goes offline at time T, they are considered offline
        # for any messages occurring at exactly time T.
        parsed_events = []
        for type_str, ts, data in events:
            # priority: OFFLINE=0, MESSAGE=1
            priority = 0 if type_str == "OFFLINE" else 1
            parsed_events.append((int(ts), priority, type_str, data))
            
        parsed_events.sort()
        
        mentions = [0] * numberOfUsers
        # online_time[i] stores the timestamp when user i comes back online.
        # Initially 0 (everyone is online).
        online_time = [0] * numberOfUsers
        
        for ts, _, type_str, data in parsed_events:
            if type_str == "OFFLINE":
                user_id = int(data)
                # User stays offline for 60 units.
                # If they go offline at ts, they return at ts + 60.
                online_time[user_id] = ts + 60
            else:
                # MESSAGE
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        # User is online if current time >= time they are back online
                        if ts >= online_time[i]:
                            mentions[i] += 1
                else:
                    # Specific ids, e.g., "id0 id1"
                    ids = data.split()
                    for id_str in ids:
                        # Parse "id123" -> 123
                        uid = int(id_str[2:])
                        mentions[uid] += 1
                        
        return mentions
