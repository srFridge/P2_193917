import os

def ex():
	oldname = input('\033[95m'+"What file do you wish to rename? (if no file is selected BBB will be used)"+'\033[0m' +" ")
	newname = input('\033[95m'+"What do you want the new name to be? (if no name is selected a name derived from the specs will be selected)"+'\033[0m' +" ")
	print()

	if oldname == '':
		oldname = 'BBB'
	if newname == '':
		os.system('ffmpeg -i BBB.mp4 2> videoData.txt')
		txt = open('videoData.txt')
		for line in txt:
			if 'Video: ' in line :
	            		newname = "BBB_" + line[82:92]
	oldname = oldname + ".mp4"
	newname = newname + ".mp4"
	
	
	os.rename(oldname, newname)
