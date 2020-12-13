import os

def ex():
	keyword = input('\033[95m'+"What information do you wish to see? (if you want to see all press all)"+'\033[0m' + "\n\t-Title \n\t-Encoder \n\t-Duration \n\t-Bitrate \n\t-Video (specifications such as encoder, ratio, etc) \n" +'\033[4m' + "please enter it in lower case:"+ '\033[0m' +" " )
	print()

	all = False
	if keyword == "all":
		all = True
	if keyword == "duration":
		keyword = 'Duration'
	if keyword == "video":
		keyword = "Video: "


	os.system('ffmpeg -i BBB.mp4 2> videoData.txt')
	txt = open('videoData.txt')


	for line in txt:
		if 'Duration' in line and (keyword == 'Duration' or all):
        	    print(line[2:23])
		if 'bitrate' in line and (keyword == 'bitrate' or all):
        	    print('Bitrate: ', line[51:-1])
		if 'encoder' in line and (keyword == 'encoder' or all):
        	    print("Encoder: ", line[22:-1])
		if 'title' in line and (keyword == 'title' or all):
        	    print("Title: ", line[22:-1])
		if 'Video: ' in line and (keyword == 'Video: ' or all):
        	    print("Video specs: ", line[22:-1])	
