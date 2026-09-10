print("<<<===IF ELSE===>>>")

import random
some_num = random.randint(10, 100)
print("some_num", some_num, sep='-->>')

if some_num >=50:  #86>=50
    result = some_num**2/45
    print('result in if block', result, sep=':')
    print('end of if block')
else:  
    cal_val = ((some_num*5) + 45)/10
    print('cal val in else block:', cal_val)
    print('end of else block')
print('i am done with my program')

print("<<<===IF - ELIF -- ELSE===>>>")
pushpa2 = random.randint(100, 800)
print("pushpa2", pushpa2, sep='-->>')
#<=100 : normal
#100 to 300 : hit
#300 to 500 : super hit
# >500: blockbuster

if pushpa2 <= 100:   #109<=100 --> False
    print('Its normal movie')
elif pushpa2 > 100 and pushpa2 <= 300:   #109 > 100 and 109 <=300  --> True and True --> True
    print('Its HIT movie')
elif pushpa2 > 300 and pushpa2 <= 500:   #752 > 300 and 752 <= 500 --> True and False --> False
    print('Its Super HIT movie')
elif pushpa2 > 500 and pushpa2 <=700:                      #752 > 500 -> True
    print('its blockbuster movie.')
else:
    print('We cant estimate the success of this movie.')    
    
print('this is my analysis of pushpa2 movie.')