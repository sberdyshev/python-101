# 1
print('Task1')
number = int(input('Enter a number: '))
number += 2
print(number)

# 2
print('Task2')
numberBetween0And10 = 0
while numberBetween0And10 <= 0 or numberBetween0And10 >= 10:
    numberBetween0And10 = int(input("Enter a number between 0 and 10: "))
    print('Inserted number - {}'.format(numberBetween0And10))
else:
    numberBetween0And10 **= 2
    print('Result is ', numberBetween0And10)

# 3
print('Task3')
patientFirstName = input("Enter patient's first name: ")
patientSecondName = input("Enter patient's second name: ")
patientAge = int(input("Enter patient's age: "))
patientWeight = int(input("Enter patient's weight: "))

if patientWeight > 50 and patientWeight < 120:
    print("Patient: {} {}. Age {}. Weight {}. Everything is ok.".format(patientFirstName, patientSecondName, patientAge,
                                                                       patientWeight))
elif patientAge > 30 and patientAge < 40:
    print("Patient: {} {}. Age {}. Weight {}. Should excercise more.".format(patientFirstName, patientSecondName,
                                                                            patientAge, patientWeight))
elif patientAge > 40:
    print("Patient: {} {}. Age {}. Weight {}. Should see a doctor.".format(patientFirstName, patientSecondName,
                                                                          patientAge, patientWeight))
else:
    print("Patient: {} {}. Age {}. Weight {}. Consult your GP.".format(patientFirstName, patientSecondName,
                                                                          patientAge, patientWeight))
