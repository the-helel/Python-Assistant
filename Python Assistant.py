import os
import pyttsx3 as tts

tts.speak("Welcome I am Your Personal Assistant")
print("------------------------------------------------------------------")
print("Welcome I am Your Personal Assistant Note:- use run <option>")
print("------------------------------------------------------------------")

while True:
	print("What Do You Want : " , end='')
	p=input()

	if(("run" in p) and ("edge" in p) or ("microsoftedge" in p) or ("browser" in p)):
		tts.speak("Opening Microsoft Edge")
		os.system("msedge")
	elif(("run" in p) and ("notepad" in p) or ("texteditor" in p) or ("editor" in p)):
		tts.speak("Opening Notepad")
		os.system("notepad")
	elif("calculator" in p):
		tts.speak("Opening Calculator")
		os.system("calc")
	elif(("run" in p) and ("paint" in p) or ("drawing software" in p)):
		tts.speak("Opening Paint")
		os.system("mspaint")
	elif(("run" in p) and ("excel" in p) or ("msexcel" in p) or ("microsoftexcel" in p)):
		tts.speak("Opening Microsoft Excel")
		os.system("excel")
	elif(("run" in p) and ("word" in p) or ("msword" in p) or ("microsoftword" in p)):
		tts.speak("Opening Microsoft Word")
		os.system("winword")
	elif(("run" in p) and ("ppt" in p) or ("powerpoint" in p) or ("microsoftpowerpoint" in p)):
		tts.speak("Opening Microsoft Power Point")
		os.system("powerpnt")
	elif(("run" in p) and ("sublime text" in p) or ("sublimetext" in p) or ("sublime" in p)):
		tts.speak("Opening Sublime Text 3")
		os.system("sublime_text")
	elif(("run" in p) and ("anydesk" in p)):
		tts.speak("Opening AnyDesk")
		os.system("AnyDesk")
	elif(("run" in p) and ("onenote" in p) or ("msnote" in p) or ("microsoftnot" in p)):
		tts.speak("Opening Microsoft One Note")
		os.system("onenote")
	elif("exit" in p):
		tts.speak("Thanku")
		os.system("exit()")
		break;