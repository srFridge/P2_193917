import os
def ex():
	filename = input("What file do you wish to change? (add the extension)")
	width = int(input("Select the desired width of the resolution"))
	height = int(input("Select the desired height of the resolution"))
	function = "ffmpeg -i " + filename +" -vf scale="+str(width)+":"+str(height)+" resizedBBB.mp4"
	os.system(function)


