#მოსწავლეს შეეკითხეთ მის მიერ მიღებული ქულა,თუ ქულა უდრის 100-ს მაშინ გამოუტანეთ "A Group),თუ იქნება 80-დან 99-მდე მაშინ გამოიტანეთ "B Group",თუ იქნება 40-დან 70-მდე მაშინ "C Group",დანარჩენ შემთხვევაში კი "D Group

qula = input("enter your number")
if qula >= 100:
    print("A group")
elif qula <= 99:
    print("B class")
elif qula <= 70:
    print("C class")
elif qula <= 39:
    print("D class")