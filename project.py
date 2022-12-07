# your task is to find name of student with max marks after updation in marks and jump in the  students rank previous rank and current rank
names = input("Enter list of  Names: ").split(',')
marks = input("Enter list of Marks: ").split(',')
updates = input("Enter List of updated marks").split(',')
n = len(marks) #length of marks list
def nameRank(names, marks, updates, n):# bracket inside parameters
    x = [[0 for j in range(3)] for i in range(n)] #list comprehension , n number of lists with three zeros each inside a list
    for i in range(n):
        x[i][0] = names[i]  # Store the name of the student
        x[i][1] = marks[i] + updates[i]  # Update the marks of the student
        x[i][2] = i + 1  # Store the current rank of the student
    highest = x[0] #gives 1st list
    for j in range(1, n):
        if (x[j][1] >= highest[1]):
            highest = x[j]
    print("Name: ", highest[0], ", Jump: ", abs(highest[2] - 1), sep="")
nameRank(names, marks, updates, n)
