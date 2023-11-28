# This is simple currency converter.
# In this program user can enter choose the currency what they that and what they need.
# By doing this program you can understand - how to assign more string value in list and if, elif, else conditional statement.
# Example- only Nepal and Qatar two country is here. you can review and add more country currency converter as per your requirement.

nepal_name = [
    "NEPAL",
    "Nepal",
    "nepal",
    "NP",
    "Np",
    "np",
    "NEPALI RUPEE",
    "Nepal Rupee",
    "nepali rupee",
    "NEPALI",
    "Nepali",
    "nepali",
]

qatar_name = [
    "QATAR",
    "Qatar",
    "qatar",
    "QTR",
    "Qtr",
    "qtr",
    "QATARI RIYAL",
    "Qatari Riyal",
    "qatari riyal",
    "QATARI",
    "Qatari",
    "qatari",
]

from_curr = str(input("Please enter the currency you have: "))
to_curre = str(input("Please enter the currency you need: "))

if from_curr in qatar_name and to_curre in nepal_name:
    store_qtr = float(input("Enter the Amount: "))
    npr = round(store_qtr * 36.42, 2)
    print("Your total Nepal Rupess is", "NRP.", "{:,}".format(npr))
elif from_curr in nepal_name and to_curre in qatar_name:
    store_npr = float(input("Enter the Amount: "))
    qr = round(store_npr * 0.027, 2)
    print("Your Total Qatari Riyal is", "QAR.", "{:,}".format(qr))
else:
    print("Invaild input, please try again: ")
