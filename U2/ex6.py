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
reservations = [(1,2),(2,9),(3,4),(5,6),(9,12),(9,12)]
result = courts(reservations)
print(f"Minimum number of courts required: {result}")




        
        
        