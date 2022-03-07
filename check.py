import pyinputplus as pyip

response=pyip.inputInt("enter a integer: ",min=4)


response1 = pyip.inputNum('Enter num: ', greaterThan=4)

response = pyip.inputNum('>', min=4, lessThan=6)



response = pyip.inputNum('Enter num: ')

response = pyip.inputNum(blank=True)

response = pyip.inputNum(limit=2)
response = pyip.inputNum(timeout=10)
response = pyip.inputNum(limit=2, default='N/A'
response = pyip.inputNum(blockRegexes=[r'[02468]$'])