#imprting time module 

import time
import random as randd
na = ""
na = input("what is your name ")
print(na)
#dictnary = { 6 : ["mad max","popeye","The fly","avatar","aliens","Batman","Escape"],7: ["Robocop","Titaic","Rain man","Tangled"],8 : []
li = {1 : ["joker","once upon a time in Hollywood","Deadpool","spiderman"],
2 : ["money heist","stranger things","13 reasons why","Peaky blinders","Breaking bad"]
}

usr_chs = int(input("1.movies \n2.series "))
while usr_chs > 2 :
	print("error try again!")
	usr_chs = int(input("enter either 1 or 2 \n"))
Gword = ""
temp = ""


def pre_word():
	global Gword
	global temp
	Gword = randd.choice(li[usr_chs])
	print("word  =   " + Gword)
	word_count = 4
	for x in Gword:
		if x in "AEIOUaeiou":
			temp = temp + x 
			word_count = word_count-1
		elif x == " ":
			temp = temp + " "
		else :
			temp = temp + "#"
	print("player word   : "+ temp)
	

def check_letter(char,gct):
		global Gword 
		global temp
		k = list(temp)
		for i in range(len(temp)):
				if (Gword[i] == char.lower() or Gword[i] == char.upper() )and temp[i] =="#":
						k[i] = Gword[i]
		if k == list(temp):
			gct = gct - 1
		print("k = ")
		print(k)
		k1 = ""
		for i in k :
    			k1= k1+i
		print("k1  = "+k1)
		temp = k1

		return(gct)

def game_stats(g_ct,g_wrd):
		print(" GAME STATUS\n curr_word : "+g_wrd)
		print("guess left: "+str(g_ct)+"\n")
	
def play_wor():
		count = 10
		global temp
		game_stats(count,temp)
		char=""
		while count > 0 :
			char = input("guess : ")			#exeption 
			count=check_letter(char,count)
			game_stats(count,temp)
			print("character :  "+ char)

pre_word()
play_wor()











#-------------------------------------------> GAME STARTS <----------------------------------------------------------------------------------------------------------------------------------


#print(	"\t\t\t\t\t\t LET's PLAY\n\t\t\t\t\t\t============")


#def lets_play ():










