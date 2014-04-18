import time
now = time.localtime()
def main():
	if now.tm_hour < 12:
		print("Good morning.")
	elif (now.tm_hour >= 12) and (now.tm_hour <= 16):
		print("Good Aftermoon")
	elif (now.tm_hour > 16) and (now.tm_hour < 24):
		print("Good Evening.")

main()
