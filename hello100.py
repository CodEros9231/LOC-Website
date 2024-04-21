#!/usr/bin/python3

print("Content-Type: text/html\n\n")


print("""

<!DOCTYPE HTML>
<head>
<title>  Hello Program </title>
      <link rel='stylesheet' href='style.css'>
      </head>
      <body>
      <h1>Output of my first program </h1>


     """ )
# Student names and grades
name1 = "Minnie Mouse"
grade1 = 100

name2 = "Mickie Mouse"
grade2 = 50

name3 = "Tom"
grade3 = 99

# average formula
average_grade = (grade1 + grade2 + grade3) / 3

# # printing the results
# print("Name:", name1)
# print("Grade:", grade1)
# print("<br>")

# print("Name:", name2)
# print("Grade:", grade2)
# print("<br>")

# print("Name:", name3)
# print("Grade:", grade3)
# print("<br>")

#print("Average grade:", average_grade)
print(f"""<div class="container">
        <h2> Student Grades </h2>
        <div class="row">
            <p> Name: {name1} </p>
            <p> Grade: {grade1} </p>
        </div>
        <div class="row">
            <p> Name: {name2} </p>
            <p> Grade: {grade2} </p>
        </div>
        <div class="row">
            <p> Name: {name3} </p>
            <p> Grade: {grade3} </p>
        </div>
        <h3> Average: {average_grade} </h3>
    </div>
      """)

print("""
      </body>
      </html> """)