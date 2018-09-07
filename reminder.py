try:
	import schedule
	import time
	import sys
	import random
	from playsound import playsound
	from gtts import gTTS

	colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
	normal=('\033[1;m')
	
except:
	print('Missing Package')
	import os
	os.system('pip install schedule')
	os.system('pip install playsound')
	os.system('pip install gTTS')
	sys.exit()

print('*'*80)
print(random.choice(colour)+'Created by Pierce2r'+normal).center(100)
print(random.choice(colour)+'Reminder vs 1.0'+normal).center(100)
print('*'*80)

try:
	def job():
		print(random.choice(colour)+'Reminder: '+str(text)+normal)	
		msg=('You set a reminder for '+str(text))
		tts=gTTS(text=msg,lang='en')
		tts.save('/root/reminder.mp3')
		playsound('/root/reminder.mp3')
		print('')
		sys.exit()
			

	text=raw_input(random.choice(colour)+'\nWould you like me to remind you of something:'+normal)
	clock=raw_input(random.choice(colour)+'At what time in the day [e.g:1:30] : '+normal)
	sch=schedule.every().day.at(clock).do(job)
	run=schedule.run_pending
	while True:
		run()
		time.sleep(1)
		
	
except KeyboardInterrupt:
	print('\nInvalid character. Exitting....')
	sys.exit()
