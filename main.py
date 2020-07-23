from window import Window
import os
	
def main():
	try:
		FILE = open("address.txt", 'r+')
	except:
		FILE = open("address.txt",'w+')
		FILE.writelines(["IP", "\n", "Authorization"])
	finally:	
		FILE.close()
		
		
	frame = Window()
	frame.start()

if __name__ == "__main__":
	main()