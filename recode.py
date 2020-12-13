import os
#This exercise can be completed with the line 'ffmpeg -i oldname.mp4 newname.mpeg' but in order to make take a little bit more from it we now have a code that just changes the extension of a file taking the same name as before
def ex():
	oldname = input('\033[95m'+"What file do you wish to change? (add also the extension)"+'\033[0m' +" ")
	newname = input('\033[95m'+"What extension do you want for it"+'\033[0m' +" ")

	for i in range(len(oldname)):#We check at which point the extension starts
		if oldname[i] =='.':
			break
		
	newname = oldname[:i+1] + newname #We copy the name and add a +1 to also copy the '.' 

	function = 'ffmpeg -i ' + oldname+ ' ' + newname
	os.system(function)


