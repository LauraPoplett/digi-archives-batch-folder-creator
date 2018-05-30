# digi-archives-batch-folder-creator

This script was created for digital archive purposes.  It takes a directory of multiple files and makes a new folder, within that given directory, for each file (or group of files) with the same basename. The new folder will be named with the same basename as its intended files, but with '_folder' added to the end of the name. The purpose of this functionality is to group data files together with their related metadata files, for archival preservation. 

Example: If you have two folders in a main directory called:

'unv_speech_aud.wav' 
'unv_speech_aud.wave.mediainfo.xml'  
(The extension for both does not matter as long as the basename is the same for both files.)

The resulting folder within the main directory will be named 'unv_speech_aud_folder'. 

Both files are then moved from the main directory into their new, and appropriately named, directory. The result is a separate container/folder for each data file/group and metadata file combo. The original purpose was to organize the files before bagging them for long term preservation with the Library of Congress Bagger software, however, it may be used in any event where separate folders are needed for each file item or group.

Requirements for Use:
1)The data files and their corresponding metadata files must have the same base filename apart from the file extension. 
2)The main directory that you wish to operate on my not have a space in its name.

Instructions for Use: 
1)Click on the executable file
2)Drag or type the main directory path you wish to operate on into the terminal window when prompted. 
