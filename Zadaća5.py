import re
email = "^([a-zA-Z]+\.[a-zA-Z]+@fpmoz.sum.ba)$"
eduID = "^([a-zA-Z]+\d?@sum.ba)$"
while 1:
    unos1 = input("Unesite vas email: ")
    unos2 = input("Unesite vas eduID: ")
    result1 = re.match(email,unos1)
    reuslt2 = re.match(eduID,unos2)
    if result1==True and result2==True:
        print("Ispravan unos!")
        break
    else:
        print("Neispravan unos!")
    
