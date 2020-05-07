import re

phoneRegex = re.compile(r'''

# +8801830736470, 8801830736470, 01830736470, 1830736470
([+]?[\d]+)

''',re.VERBOSE)

emailRegex = re.compile(r'''

[a-zA-z0-9_.+-]+@[a-zA-z0-9_.+-]+

''',re.VERBOSE)

text = "My phone number is +8801830736470 and my mother phone number is 01670565389 and my father number is 1671691541, another one is 8801971685693"
text1 = "My email id is saminyeaser1@gmail.com and my father email id is Mosharof.hossain123-@gmaul.com"
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text1)
print(extractedPhone)
print(extractedEmail)