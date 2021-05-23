import wikipedia
import os
import pyttsx3
import speech_recognition
from datetime import date

bot_mouth = pyttsx3.init()
voices = bot_mouth.getProperty('voices')
bot_mouth.setProperty('voice', voices[1].id)
bot_ear = speech_recognition.Recognizer()
bot_brain = "How may I help you, Boss?"
today = date.today()
d2 = today.strftime("%B %d, %Y")

print("Bot: " + bot_brain)
bot_mouth.say(bot_brain)
bot_mouth.runAndWait()

while True:

	print("Say one of the following: \n1. Hello \n2. Find (item) \n3. CEO Registration \n4. Ordering coffee \n5. Wikipedia \n6. Say Thank \n7. Today's date \n8. Terminate \n9. Love \n10. Game\n")

	with speech_recognition.Microphone() as mic:
		default = "I'm listening..."
		print ("Bot: " + default)
		bot_ear.adjust_for_ambient_noise(mic,duration=2)
		audio = bot_ear.listen(mic)
		print("Bot: ...")
	try:
		you = bot_ear.recognize_google(audio)
	except:
		you = ""
	
	print("Boss: " + you)
	if you == "":
		bot_brain = "I'm sorry, I can't hear that. Try again, please..."

	elif "find" in you:
		bot_brain = "Alright, I can help you with that."

	elif "CEO" in you:
		bot_brain = "You've just registered to be the CEO"

	elif "hello" in you:
		bot_brain = "Hello Boss. How are you today?"

	elif "coffee" in you:
		bot_brain = "Your coffee will be ready in five minutes. Keep up the great work!"

	elif "look" in you:
		bot_brain = "It's hard to say, but everyone thinks you are handsome."

	elif "today" in you:
		bot_brain = "It's " + d2

	elif "happy" in you:
		bot_brain = "That's great"

	elif you == "thank you":
		bot_brain = "You're welcome!"

	elif "Wikipedia" in you:
		bot_brain = "Starting Wikipedia Search"
		print(bot_brain)
		bot_mouth.say(bot_brain)
		bot_mouth.runAndWait()
		while True:
			ear2 = speech_recognition.Recognizer()
			bot_brain = "What would you like to search for?"
			print("Bot: " + bot_brain)
			bot_mouth.say(bot_brain)
			bot_mouth.runAndWait()
			print("1. (item) \n2. Exit\n")
			with speech_recognition.Microphone() as mic:
				ear2.adjust_for_ambient_noise(mic,duration = 1)
				wiki_input = ear2.listen(mic)
				try:
					wiki = ear2.recognize_google(wiki_input)
					print("Wikipedia: ...")
					print("You: " + wiki)
					if wiki == "exit":
						break
					else:
						try:
							searchresult = wikipedia.summary(wiki, sentences=2, auto_suggest=True, redirect=True)
						except:
							searchresult = "File not found"
						print("Wikipedia: " + searchresult)
						bot_mouth.say(searchresult)
						bot_mouth.runAndWait()
				except:
					print("Searching Unable")
					bot_mouth.say("Searching Unable")
					bot_mouth.runAndWait()

		bot_brain = "End of Wikipedia"
	
	elif you == "terminate" or "bye" in you:
		bot_brain = "Have a nice day! See you next time, Boss."
		print("Bot: " + bot_brain)
		bot_mouth.say(bot_brain)
		bot_mouth.runAndWait()
		break

	elif "love" in you:
		os.system('love.exe')

	elif "game" in you:
		os.system('game.exe')
		
	else:
		bot_brain = "Okay"
	print("Bot: " + bot_brain)
	bot_mouth.say(bot_brain)
	bot_mouth.runAndWait()
	os.system("cls")