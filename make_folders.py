#This script takes a directory of multiple files and makes a new folder, within that given directory, for each file and 
#its sidecar metadata file using the same name as the file itself with '_folder' added on the end ex. 'unv_speech_AudP_folder'. The result is a separate container/folder for each 
#data file and metadata file combo with the purpose of organizing files before bagging them for long term preservation with the LoC's Bagger or BagIt.
#Originaly created 5/24/2018 for WCFTR The Wisconsin Center for Film and Theater Research, for Windows 7 and Python 2.7
#Built to work with all future operating systems and python versions
#@author: https://github.com/LauraPoplett

#setup environment
import os
import shutil

#define functions
def get_dir():
	#This function gets the name of the directory as input from the user and tests to ensrue it is an actual directory.
	#If not a true directory, the user is prompted to re-enter the directory name. This was done recursively and within 
	#a function in order to allow for repetitive path entry on the misspelling of directory names. It is recommended, however, 
	#to simply drag and drop the file path into the terminal window, in order to prevent this from occurning.
	directory = raw_input('Please enter file path of the folder containing all files for processing:')
	if not os.path.isdir(directory):
		print 'The given file is not a directory'
		get_dir()
	return directory
def make_folders(directory):
	#This function creates a new folder/directory for each separate data file within the given directory, using the same
	#name as the file itself.
	try:
		os.chdir(directory)
	except: print 'Could not change directory. Please try again.'
	try:
		file_names = os.listdir(directory)#Get list of all file names in directory
	except IOError: print 'could not read folder/directory'
	names =[] #Variable to hold base filenames without the extension. 
	folder_names =[]
	for i in range(len(file_names)): #Change the list of all files in directory to cut off any file extensions and include base file names only. Save in a new list called 'names'
		name = file_names[i].split('.')[0]
		if name not in names and not os.path.isdir(os.path.join(directory, name)): #ensures folder by that name doesn't already exist
		#Only adds the basename to the list called 'names' if it is not already there. This ensures that 
		#data files and their metadata files, which have the same name and will be in the same folder, are only represented once.
			names.append(name)
	
	for i in range(len(names)): 
		#Loops through the base file name list and appends '_folder' to the end of each name. 
		folder_names.append(names[i] + '_folder')
			
	for name in folder_names: #Makes a new folder for each file name(plus '_folder') in the same main directory using the above created list of names
		#this simplifies issues that come from making a folder name the same as a file name in certain operating systems rather than using exist_ok with
		#makdirs() which only works in python 3 etc...
		p = os.path.join(directory, name)
		if not os.path.isdir(p): #Checks that the directory does not already exist.
			os.mkdir(p)		
	
	return names
def move_files(directory):
	#This function moves the data files and their associated metadata files from the main directory into their 
	#newly created individual folders.
	make_folders(directory)
	all = os.listdir(directory)
	dirs = []
	files = []
	for f in all:#get list of all files and directories in main directory given
		if os.path.isdir(f):
			dirs.append(f)
		else:
			files.append(f)
	for name in files:#move each file to appropriate folder
		src_path = os.path.normpath(os.path.join(directory, name))#path where folder is now i.e. source path
		no_ext = name.split('.')[0]
		to_folder = no_ext + '_folder'
		if to_folder in dirs and no_ext in to_folder:
			full_name = os.path.join(to_folder,name)
			dest_path = os.path.normpath(os.path.join(directory, full_name))#target/destination folder
			shutil.move(src_path, dest_path)#move fodler from source path to destination path

#execute functions
move_files(get_dir()) 	
