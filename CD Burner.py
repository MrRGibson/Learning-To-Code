numberOfTrack = int(input('How many tracks are to be burned?'))
while numberOfTrack <1 or numberOfTrack >20:
    print('You entered an invalid number of tracks')
    numberOfTrack = int(input('How many tracks are to be burned?'))

print('The number of tracks are ' + str(numberOfTrack))

titleOfTrack =[None]*numberOfTrack
lengthOfTrack =[None]*numberOfTrack

for i in range(numberOfTrack):
    titleOfTrack[i] = input('What is the title of the track?')
    print('The title of the track is ' + titleOfTrack[i])
    lengthOfTrack[i] = int(input('What is the length of the track?'))
    print(lengthOfTrack[i])

cdr = 0

for j in range(numberOfTrack):
    cdr = cdr + lengthOfTrack[j]

print(cdr)
