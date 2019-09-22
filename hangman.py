#imprting time module 
#important input changes to raw in put in python 2  and input in python3 inrder to run opengl python2 is used hence the program is changesd to python 2  fromat 
import time
import random as randd
na = ""
na = raw_input("what is your name ")
print(na)
#dictnary = { 6 : ["mad max","popeye","The fly","avatar","aliens","Batman","Escape"],7: ["Robocop","Titaic","Rain man","Tangled"],8 : []
li = {1 : ["joker","once upon a time in Hollywood","Deadpool","spiderman"],
2 : ["money heist","stranger things","13 reasons why","Peaky blinders","Breaking bad"]
}
dif_lvl = input("1.east\n 2. medium \n 3.ultra Hard")
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
	
def play_wor(count):
		global temp
		game_stats(count,temp)
		char=""
		while count > 0 :
			char = raw_input("guess : ")			#exeption 
			count=check_letter(char,count)
			game_stats(count,temp)
			print("character :  "+ char)
pre_word()

if dif_lvl == 3 :
	play_wor(1)
elif dif_lvl in (1,2):
	play_wor(dif_lvl*5)













#-------------------------------------------> GAME STARTS <----------------------------------------------------------------------------------------------------------------------------------


#print(	"\t\t\t\t\t\t LET's PLAY\n\t\t\t\t\t\t============")


#def lets_play ():










