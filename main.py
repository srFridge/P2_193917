import os
import data
import rename 
import resize as rs
import recode

#This menu will redirect you to each exercise, it just uses if statements inside a loop
loop = 1
allExes = False
while loop == 1:
	exercise = input('\033[96m'+"Which exercise would you like to try? (1-4, type exit to quit and all to execute them all)"+ '\033[0m')
	
	if exercise == "all":
		allExes = True
		exercise = "1"
		
	if exercise == "1":
		data.ex()
		if allExes:
			exercise = "2"
		
	if exercise =="2":
		rename.ex()
		if allExes:
			exercise = "3"
		
	if exercise =="3":
		rs.ex()
		if allExes:
			exercise = "4"
		
	if exercise =="4":
		recode.ex()
		
		
	elif exercise == "exit":
		loop = 0
		
	allExes=False	
	print()
