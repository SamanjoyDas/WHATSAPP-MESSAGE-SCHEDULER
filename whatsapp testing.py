import pywhatkit as kit
number = input('+country_code Receiver_Phone_Number')

kit.sendwhatmsg(number, 'message', 15,41)
#HERE 15 DENOTES THE HOUR AND 41 DENOTES THE TIME IN 24 HOUR CLOCK FORMAT
