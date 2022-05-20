"""


To start we will gather the grades from the Final.txt file and 
catputure users input for each grade. Each time we capture the users input,
we append the number to the list. once we have three highest number in the list, 
we sum them up and divide by 3 and output a message to the user.
We will display the number of grades, the average grade, 
and a calculate_percent_above_average to calculate the percentage 
of grades that are above the average grade.


"""

"""
Start

     Open file "Final.txt" in read mode

     Declare list grades

     For num in file:

         Append num to grades

     End loop

     total = sum(grades)

     totalNumberOfGrades = len(grades)

     Divide total by totalNumberOfGrades to get avg

     Initialise numberOfGradeAboveAvg to 0

     For num in grades:

          If num > avg

              Increase numberOfGradeAboveAvg value by 1.

     End loop

     Multiply numberOfGradeAboveAvg by 100 and then divide the result by totalNumberOfGrades  to                                   percentOfGradeAboveAvg

     Display totalNumberOfGrades, avg, percentOfGradeAboveAvg

End

"""


def main():
    # reading the file
    file = open("Final.txt", "r")
    # varibles to store the values
    grades = []
    # looping over file
    for num in file:
        grades.append(int(num))
    # finding sum of grades and total number of grades
    total = sum(grades)
    totalNumberOfGrades = len(grades)
    # finding the average
    avg = total / totalNumberOfGrades
    # finding numbe of grades abpver average
    numberOfGradeAboveAvg = 0
    for num in grades:
        if num > avg:
            numberOfGradeAboveAvg += 1
    percentOfGardeAboveAvg = numberOfGradeAboveAvg*100 / totalNumberOfGrades
    # printing the result
    print("Number of grades:", totalNumberOfGrades)
    print("\nAverage grade:", avg)
    print(f"\nPercentage of grades above average: {round(percentOfGardeAboveAvg,2)}%")

# method invocation
main()





