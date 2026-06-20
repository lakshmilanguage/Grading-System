name = input("Enter student name:")
telugu = float(input("Enter telugu marks:"))
hindi = float(input("Enter hindi marks:"))
english = float(input("Enrer english marks:"))
maths = float(input("Enter maths marks:"))
science = float(input("Enter science marks:"))
social = float(input("Enter social marks:"))
if telugu<35 or hindi<35 or english<35 or maths<35 or science<35 or social<35:
    print("result: failed")
else:
    total = telugu+hindi+english+maths+science+social
    percentage = (total/600)*100
if percentage>=90:
    print("A+ grade")
elif percentage>=80:
    print("A grade")
elif percentage>=70:
    print("B+ grade")
elif percentage>=60:
    print("B grade")
elif percentage>=50:
    print("C grade")
else:
    print("D grade")
    print("percentage is:",percentage)
    print("result:passed")