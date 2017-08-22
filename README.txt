This script takes in a configuration file and username/password to download a bunch of ssrs files to a shared location

To run this script:
python ssrs_batch.py [username] [optional: config file] [optional: password]

if you don't input a configuration file path it will default to "config.json".
If you don't input a password, you will be prompted to enter it securely (no terminal echo)

To compile this script:
You need the Microsoft Visual C++ Runtime installed on the build machine.  The necessary DLL is copied to the output.

For installed python:
1. Type the build command (below)

If running from WinPython 3.4 Zero (https://sourceforge.net/projects/winpython/files/WinPython_3.4/3.4.4.6/)

1. Open the winpython folder.  
2. Start the command prompt from the WinPython folder shortcut "WinPython Command Prompt.exe"
3. Type the build command (below) 

Build command:

python setup.py build
