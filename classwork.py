
#this is number where it begins
student_name ="ngwuchukwu kenechukwu"
student_age = int(18)
student_height = float(6.5)
is_registered = True

selected_courses =()
has_paid_fees = True
minimum_age =int(18)

print(student_name)
print(student_age)
print(student_height)
print(is_registered)

print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(is_registered))

#this is number 2
print(student_age + student_height)
print(student_age - student_height)
print(student_age * student_height)
print(student_age / student_height)
print(student_age // student_height)
print(student_age % student_height)
print(student_age ** student_height)

#this is number 3
print(student_age == minimum_age)
print(student_age != minimum_age)
print(student_age > minimum_age)
print(student_age < minimum_age)
print(student_age >= minimum_age)
print(student_age <= minimum_age)

#this is number 4
print(is_registered and has_paid_fees)
print(is_registered or has_paid_fees)
print(is_registered is not has_paid_fees)

#this is number 5
student_courses =[ "english", "math",
                "physics","chemistry","agric"]
print(selected_courses in student_courses)
print(selected_courses not in student_courses)

#this is number 6
first_score=(85)
second_score=(85)
print(first_score is second_score)
print(first_score is not second_score)

#this is number 7
first_name ="ngwuchukwu"
last_name =" kenechukwu"
print(f"my name is {first_name} {last_name}")

# this is number 8
student_name ="ken"
student_age ="14"
school_name ="nanocode"
course="python"
hobby="coding"
state_of_origin="enugu state"

student_bio = (f"The name's {student_name} im currently {student_age } years old, i am from {state_of_origin} ,i attend {school_name} in nsukka, where i study {course}, my hobby is {hobby}.")
print(student_bio)





