# Python 3 code to rename multiple
# files in a directory or folder

# importing os module
import os
import random

# Function to rename multiple files
def main():

	folder = '../cowry-sample/'
	for count, filename in enumerate(os.listdir(folder)):
		# dst = f"{str(count)}_Cowries_Samples_{random.random()}.jpg"
		dst = f"cowry_{str(count)}.jpg"
		src =f"{folder}/{filename}" # foldername/filename, if .py file is outside folder
		dst =f"{folder}/{dst}"
		
		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':
	# Calling main() function
	main()
