"""
Given a set of paddle tennis court reservations, each with a start time and an end time,
design an algorithm that calculates the minimum number of courts required so that all
reservations can be carried out without schedule conflicts.
For this purpose, we have a list of time intervals, where each interval is represented by a
start time and an end time for the reservation
Example:
    Inbound: [(10, 12),(9, 11),(11, 13)] Outbound: 2.
Explanation:
    • The reservation from 9 to 11 occupies one track.
    • The second reservation from 10 to 12 needs a new track because it overlaps with the first one.
    • The third reservation from 11 to 13 can use the same track as the first one after it
ends.
"""
def courts(reservations):
    n = len(reservations)
    reservations= sorted(reservations) #sort the reservations by start time
    courtsInUse=[] #list to keep track of the courts in use
    for i in range(n):
        if len(courtsInUse) == 0:
            courtsInUse.append(reservations[i])
        else:
            for j in range(len(courtsInUse)):
                if reservations[i][0] >= courtsInUse[j][1]:#if the reservation starts after the end of the last one
                    courtsInUse[j] = reservations[i] #replace the last reservation with the new one
                    break
            else:
                courtsInUse.append(reservations[i]) # if no court is available, add a new one
        
    return len(courtsInUse)

# Example usage
reservations = [(10, 12), (9, 11), (11, 13)]
result = courts(reservations)
print(f"Minimum number of courts required: {result}")

#other example trying edge cases
reservations = [(10, 12), (9, 23), (11, 13), (12, 14), (13, 15)]
result = courts(reservations)
print(f"Minimum number of courts required: {result}")




        
        
        