import re
text = "Kristijan 512 caliB"
pattern = "^K.*\s.*[0-5].*B$"
result = re.search(pattern,text)
if result:
    print("Ima podudaranje: ",result)
else:
    print("Nema podudaranja.")
