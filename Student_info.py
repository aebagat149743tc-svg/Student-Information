print("==========================================")
print("           STUDENT INFORMATION            ")
print("==========================================")
print("Name: Alexis James P. Ebagat")

print("Age: 19")

print("course: BSIT")

print("Year Level: 2")

print("School: University of Mindanao Tagum College")

print("==========================================")
print("              QUIZ RESULTS                ")
print("==========================================")
print("")

grade = 0 
score =[85,90,95]
total = 0

print("Quiz 1:", score[0])
print("Quiz 2:", score[1])
print("Quiz 3:", score[2])

for totalScore in score:
    total += totalScore

grade = total /3
print("Total Score:", total)
print("Average Score:", grade)

personalIntroduction = ["Alexis James P. Ebagat", 19,"BSIT",2,"University of Mindanao Tagum College"]
print("hello! My name is", personalIntroduction[0])
print("I am", personalIntroduction[1],"years old")
print("I am Currently Studying", personalIntroduction[2])
print("My year level is",personalIntroduction[3])
print("I Study at",personalIntroduction[4] +".")
print("Welcome to my first python project")

print("==========================================")
print("           ARITHMETIC OPERATIONS          ")
print("==========================================")


num1 = 20
num2 = 5

print("First Number:", num1)
print("Second Number:", num2)
print("Addition:", (num1 + num2))
print("Substraction:", (num1 - num2))
print("Multiplication:",(num1 * num2))
print("Divisiom:", (num1 / num2))



