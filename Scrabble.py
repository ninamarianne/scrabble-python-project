#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Scrabble_2935581.py

from Tkinter import *
import random, re, letters


def main(value=None):

	l_one = random.choice(letters.buchstabenliste)
	l_two = random.choice(letters.buchstabenliste)
	l_three = random.choice(letters.buchstabenliste)
	l_four = random.choice(letters.buchstabenliste)
	l_four = random.choice(letters.buchstabenliste)
	l_five = random.choice(letters.buchstabenliste)
	l_six = random.choice(letters.buchstabenliste)
	l_seven = random.choice(letters.buchstabenliste)
	selected_letters =  l_one, l_two, l_three, l_four, l_five, l_six, l_seven  
	buchstabenauswahl = list(selected_letters)


	def button_action():
		'''wird ausgeführt, wenn der User auf den Ergebnis-Button klickt'''

		letone = letter_one.get()
		lettwo = letter_two.get()
		letthree = letter_three.get()
		letfour = letter_four.get()
		letfive = letter_five.get()
		letsix = letter_six.get()
		letseven = letter_seven.get()
		wort = str(letone.upper()+lettwo.upper()+letthree.upper()+letfour.upper()+
					   letfive.upper()+letsix.upper()+letseven.upper())

		def check_word(value_x = wort, value_y = letters.wortsammlung):
			'''nimmt ein Wort entgegen, wandelt alle Buchstaben in Kleinbuchstaben um, ersetzt das Wort,
			falls es in der Datei nur zusammen mit einem Satzzeichen bzw. überhaupt vorkommt, durch das 
			reine Wort und prüft dann, ob das Wort in der neuen Datei vorkommt'''

			lower = wort.lower()
			changed_file = re.sub(r'(\s+'+lower+r'(,|\?|\.|;|:|!)?\s+)', r'\n'+lower+r'\n', str(letters.wortsammlung))
			if lower in changed_file.split():
				return True
			else:
				return False

		def check_letters(value_x = wort):
			'''geht die einzelnen Buchstaben eines Wortes durch, prüft, ob die Buchstaben in der
			Buchstabenauswahlliste vorhanden sind oder nicht und löscht die bereits benutzten Buchstaben
			aus der Buchstabenauswahlliste'''
			for letter in wort:
				if letter in buchstabenauswahl:
					buchstabenauswahl.remove(letter)
				else:
					return False


		def get_points(value_x = wort, value_y = letters.punktzahl):
			'''geht die einzelnen Buchstaben eines Wortes durch, prüft, ob die Buchstaben in dem Punktzahldictionary
			vorkommen, sucht den passenden Zahlwert für die Buchstaben raus, fügt die Zahlen in eine Liste ein
			und summiert diese Liste auf'''
			spieler_punkte = []
			for letter in wort:
				if letter in letters.punktzahl:
					punkte = letters.punktzahl[letter]
					spieler_punkte.append(punkte)
					gesamtpunktzahl = sum(spieler_punkte)
				
			return gesamtpunktzahl
			
		def points_for_place(value = letters.buchstabenliste):
			'''geht die sieben Eingabefelder für die Buchstaben durch und prüft, ob eine Eingabe vorhanden ist, 
			also ob die Eingabe in der Buchstabenliste zu finden ist, wenn das der Fall ist fügt sie einer Liste
			eine angegebene Zahl hinzu, wenn nicht, dann wird der Liste der Wert 0 hinzugefügt, 
			dann addiert sie die Liste'''
			place_points = []
			if letone.upper() in letters.buchstabenliste:
				place_points.append(1)
			else:
				place_points.append(0)
			if lettwo.upper() in letters.buchstabenliste:
				place_points.append(1)
			else:
				place_points.append(0)
			if letthree.upper() in letters.buchstabenliste:
				place_points.append(1)
			else:
				place_points.append(0)
			if letfour.upper() in letters.buchstabenliste:
				place_points.append(2)
			else:
				place_points.append(0)
			if letfive.upper() in letters.buchstabenliste:
				place_points.append(2)
			else:
				place_points.append(0)
			if letsix.upper() in letters.buchstabenliste:
				place_points.append(4)
			else:
				place_points.append(0)
			if letseven.upper() in letters.buchstabenliste:
				place_points.append(6)
			else:
				place_points.append(0)
			all_points = sum(place_points)
			
			return all_points
			

		def check_word_with_variable(value_w = wort, value_x = letters.wortsammlung):
			'''ersetzt das Blankoelement eines Wortes durch einen Buchstaben und macht dann dasselbe, wie check_word()
			und check_letters()'''

			neue_buchstabenauswahl = re.sub('_', user_letter, str(buchstabenauswahl))
			new_word = re.sub('_', user_letter, wort)
			new_lower = new_word.lower()
			second_changed_file = re.sub(r'(\s+'+new_lower+r'(,|\?|\.|;|:|!)?\s+)', r'\n'+new_lower+r'\n', str(letters.wortsammlung))
			if new_lower in second_changed_file.split():
				for letter in new_word:
					if letter in neue_buchstabenauswahl:
						list(neue_buchstabenauswahl).remove(letter)
					else:
						return False
			else:
				return 2


		if check_word() == 1:
			if check_letters() == 0:
				checkword.config(text='Du hast falsche Buchstaben benutzt! ')
			else:
				get_points()
				checkword.config(text=str(get_points()+points_for_place())+' Punkte')

		elif '_' in wort:
			if '_' not in buchstabenauswahl:
				checkword.config(text='Du hast falsche Buchstaben benutzt! ')
			else:
				user_letter = user_let.get()
				try:
					if check_word_with_variable() == 0:
						checkword.config(text='Du hast falsche Buchstaben benutzt! ')
					elif check_word_with_variable() == 2:
						checkword.config(text='Diese Eingabe ist ungültig. Versuche es nochmal!')
					else:
						get_points()
						checkword.config(text=str(get_points()+points_for_place())+' Punkte')
				except AttributeError:
					checkword.config(text='Du hast falsche Buchstaben benutzt! ')

		else:
			checkword.config(text='Diese Eingabe ist ungültig. Versuche es nochmal!')
			
	########################################################################################################   

	fenster = Tk()
	fenster.title("Mein Scrabble")
	fenster.config(bg='light coral')

	# Label und Buttons erstellen.
	continue_button = Button(fenster, text='Neustart', bg='red', command=lambda:[fenster.destroy(), main()])

	exit_button = Button(fenster, text="Beenden", bg='red', command=fenster.destroy)
	wordcheck_button = Button(fenster, text='Ergebnis:', bg='red', command=button_action)

	info_label = Label(fenster, text='Deine Buchstaben:', bg='light coral')
	another_info = Label(fenster, text='''\
Buchstabe für
Blankostelle:''', bg='orange red')
	your_letters = Label(fenster, text=selected_letters, bg='light coral', font='arial 15 bold')
	checkword = Label(fenster, bg='light coral', font='comic 10 bold')

	field_one = Label(fenster, text='1 Punkt', bg='light coral')
	field_two = Label(fenster, text='1 Punkt', bg='light coral')
	field_three = Label(fenster, text='1 Punkt', bg='light coral')
	field_four = Label(fenster, text='2 Punkte', bg='light coral')
	field_five = Label(fenster, text='2 Punkte', bg='light coral')
	field_six = Label(fenster, text='4 Punkte', bg='light coral')
	field_seven = Label(fenster, text='6 Punkte', bg='light coral')
	welcome_label = Label(fenster, text= '''\
	
Willkommen zum virtuellen Scrabble!

Vorab ein paar Spielregeln:
Du bekommst eine zufällige Auswahl an Buchstaben.
Aus diesen Buchstaben sollst Du ein Wort der deutschen Sprache bilden.
Eigennamen sind nicht erlaubt! Das Wort sollte so lang wie möglich sein, 
wobei Du aber jedes Buchstabenvorkommen nur einmal benutzen darfst!
Wenn Du ein Blankoelement hast, dann darfst Du dafür einen Buchstaben 
Deiner Wahl einsetzen. Die Buchstaben müssen in der richtigen Reihen-
folge gesetzt werden, dürfen aber in beliebige Felder geschrieben werden.
		
Viel Spaß und los geht's! 

		''', bg='orange red', font='comic 11')

	instruction_label = Label(fenster, text='''\
Nenne 
ein Wort:''', bg='orange red')
	letter_one = Entry(fenster, font='arial 15 bold', justify="center")
	letter_two = Entry(fenster, font='arial 15 bold', justify="center")
	letter_three = Entry(fenster, font='arial 15 bold', justify="center")
	letter_four = Entry(fenster, font='arial 15 bold', justify="center")
	letter_five = Entry(fenster, font='arial 15 bold', justify="center")
	letter_six = Entry(fenster, font='arial 15 bold', justify="center")
	letter_seven = Entry(fenster, font='arial 15 bold', justify="center")
	user_let = Entry(fenster, font='arial 15 bold', justify="center")

	#Größe des Fensters
	fenster.geometry("700x650")

	#Größe der Komponenten
	info_label.place(x = 80, y = 285)
	your_letters.place(x = 250, y = 280)
	checkword.place(x = 150, y = 605)

	welcome_label.place(x = 50, y = 0, width=600, height=250)
	exit_button.place(x = 550, y = 600, width=150, height=50) 
	instruction_label.place(x = 20, y = 370)
	another_info.place(x = 20, y = 500)
	wordcheck_button.place(x = 20, y = 600, width=110, height=30)
	continue_button.place(x = 550, y = 540, width=150, height=50)

	field_one.place(x = 80, y = 420, width=80, height=40)
	field_two.place(x = 160, y = 420, width=80, height=40)
	field_three.place(x = 240, y = 420, width=80, height=40)
	field_four.place(x = 320, y = 420, width=80, height=40)
	field_five.place(x = 400, y = 420, width=80, height=40)
	field_six.place(x = 480, y = 420, width=80, height=40)
	field_seven.place(x = 560, y = 420, width=80, height=40)

	letter_one.place(x = 100, y = 370, width=40, height=40 )
	letter_two.place(x = 180, y = 370, width=40, height=40 )
	letter_three.place(x = 260, y = 370, width=40, height=40 )
	letter_four.place(x = 340, y = 370, width=40, height=40 )
	letter_five.place(x = 420, y = 370, width=40, height=40 )
	letter_six.place(x = 500, y = 370, width=40, height=40 )
	letter_seven.place(x = 580, y = 370, width=40, height=40 )
	user_let.place(x=180, y = 500, width=40, height=40)

	# In der Ereignisschleife auf Eingabe des Benutzers warten.

	fenster.mainloop()
	
	
main()
