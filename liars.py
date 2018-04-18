
# My approach to solve this problem consisted of reverse engineering the logic
# that produces the given Sample Output. I used this strategy although I doubt that
# produces the actual number of liars with the given data. For instance, room 4 is said to have
# exactly 4 liars, based on the fact that the third student has the most Truth-Speaker 
# denominations. However, this student's thesis is that all four other students are liars. Thus,
# when validating him as the source of truth, we also repudiate the worth of the answers from  
# the other four students, and thus his own as well. 

# I used object oriented programming to solve the problem, but it wasn't necessary.
# I could've had the findmajority function defined globally, and initiate a majdata object
# inside of it. OOP could've been more interesting if students were also made into objects.



# Define a room class to store the current students data
class Room:
    # Initalize a room instance with an object storing data related to the answers
    def __init__(self, students):
        self.Students = students
        self.majdata =  { 'current': 0, # No of students who labeled the current student as a Truth-Speaker
            'index': 0, # index of latest student who has the majority of Truth-Speaker tags
            'high': 0, # Highest No of Truth-Speaker tags for one student
            'count': 0, # No of students with highest No of Truth-Speaker tags
            'numofLiars':0, # Number of liars the current student believes there are
            'paradoxical': False # Is the room paradoxical
                }
        print(self.Students)

    # Find the source of truth to determine the number of liars in encapsulating room
    def findmajority(self, students):
        currentnumofLiars = 0

        # O(n^2) :(
        for i in range(len(students)):
            for j in range(len(students)):
                # Store the liars' count according to student i
                if students[i][j] == 'L':
                    currentnumofLiars += 1
                # Count how many students believe student i is a Truth-Speaker
                if students[j][i] == 'T':
                    self.majdata['current'] += 1

            # If i student has the majority of T tags, store:
            if self.majdata['current'] > self.majdata['high']:
                # Number of liars according to student i
                self.majdata['numofLiars'] = currentnumofLiars
                # Reset paradoxical to False
                self.majdata['paradoxical'] = False
                # Reset count
                self.majdata['count'] = 1
                # Set highest amount of T tags to current
                self.majdata['high'] = self.majdata['current']
                # Store index of current student
                self.majdata['index'] = i

            # If the current student has the same amount of T tags as existing majority
            elif self.majdata['current'] == self.majdata['high']:
                # Increment the count of sources of truth
                self.majdata['count'] += 1
                # If the current number of liars is different from the one that the previous
                # source of truth stated, the room is paradoxical
                if currentnumofLiars != self.majdata['numofLiars']: 
                    self.majdata['paradoxical'] = True 
            # Reset before next iteration
            self.majdata['current'] = 0
            currentnumofLiars = 0
        
# Populate students array with input answers
def populateanswers(numberofstudents):
    students = []
    for i in range(numberofstudents):
        students.append(['']*numberofstudents)
        for j in range(numberofstudents):
            students[i][j] = input('What does student {}  think about student {} ? '.format(i+1, j+1))
        print("Next Row")
    return students

# Output amount of liars in room for current test case based on room instance data
def findliars(room, T, Ti):
    liarslower = 0
    liarsupper = 0
    if room.majdata['paradoxical'] == True :
        print("Class Room#"+str(Ti-T+1)+" is paradoxical")
        
    else:  
        if room.majdata['count'] == 1:
            liarsupper = room.majdata['numofLiars']
            liarslower = room.majdata['numofLiars']

        if room.majdata['count'] > 1:
            liarslower = room.majdata['numofLiars']
            liarsupper = len(room.Students[0])
        
        print("Class Room#" + str(Ti-T+1) +" contains atleast "+str(liarslower)+" and atmost "+str(liarsupper)+" liars")


def main():
    T = int(input('Enter number of test cases '))
    Ti = T 

    # Go over number of test cases
    while T>0: 
        numberofstudents = int(input('Enter total number of students '))
        students = populateanswers(numberofstudents)
        
        # Make a room instance with the inputted answers and find majority truth speaker(s)
        room = Room(students)
        room.findmajority(students)
        findliars(room, T, Ti)
        T -= 1
        numberofstudents += 1
    
main()