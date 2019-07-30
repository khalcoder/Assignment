import random
month = int(input('Enter a month'))
day = int(input('Enter a day'))
horoscope = ["you will have a good day", "you will have an awesone day", "you will have a terrific day"]

if month == 1:
    if day<=19:
        print('you are Capricorn')
    else:
        print('you are Aquarius')
            
if month==2:
    if day<=18:
        print('you are Aquarius')
    else:
        print('you are Pisces')       
if month==3:
    if day<=20:
        print('you are Pisces')
    else:
        print('you are Aries')
            
            
if month==4:
    if day<=19:
        print('you are Aries')
    else:
        print('you are Taurus')
  
            
          
if month==5:
    if day<=20:
        print('you are Taurus')
    else:
        print('you are Gemini')
            
            
if month==6:
    if day<=20:
        print('you are Gemini')
    else:
        print('you are Cancer')
            
if month==7:
    if day<=22:
        print('you are Cancer')
    else:
        print('you are Leo')
            
            
if month==8:
    if day<=22:
        print('you are Leo')
    else:
        print('you are Virgo')
            
            
if month==9:
    if day<=22:
        print('you are Virgo')
    else:
        print('you are Libra')
            
if month==10:
    if day<=22:
        print('you are Libra')
    else:
        print('you are Scorpio')
            
if month==11:
    if day<=21:
        print('you are Scorpio')
    else:
        print('you are Sagittarius')
            
    
if month==12:
    if day<=21:
        print('you are Sagittarius')
    else:
        print('you are Capricorn')
            
print(random.choice(horoscope))
            

    

    
    
    
