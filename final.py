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
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

sort the list, then splice out the two lowest number

print message to user

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





