import json

def calculateBMI(height, weight):
    if weight == 0:
        print("wrong weight")
    if height == 0:
        print("wrong height")
    bmi = weight/height
    return bmi


def get_input():
        student_roll_number = input("Enter student's roll number:")
        student_details = {}
        student_details['name'] = input("Enter the name of the student")
        student_details['height'] = input("Enter the height of the student")
        student_details['weight'] = input("Enter the weight of the student")
        student_details['bmi'] = calculateBMI(student_details["height"], student_details["weight"])
        return (student_roll_number,student_details)

def update_user():
    student_roll_number = input(("ENter roll number of student whose details you want to update"))
    student_detail_name = input("enter detail name which you want to update") 
    student_detail = input("enter detail you want to update")
    
    with open("student.json", "r") as file:
        information = json.load(file)

    information[student_roll_number].append({
        student_detail_name: student_detail
    })

    with open("student.json", 'w') as fp:
        json.dump(information, fp, indent=2)



if __name__ == "__main__":
    adddetails = {}
    while True:
        exit = input("Do you want to add an input (y/n)?")
        if exit.lower() == 'n':
            break
        elif exit.lower() == 'y':
            name, details = get_input()

            adddetails[name] = details
        else:
            print("Wrong answer, Try again!!")
    
    with open('student.json','w') as f:
        json.dump(adddetails, f, indent=2)

    while True:
        exit = input("Do you want to update student detail (y/n)?")
        if exit.lower() == 'n':
            break
        elif exit.lower() == 'y':
            update_user()
        else:
            print("Wrong answer, Try again!!")