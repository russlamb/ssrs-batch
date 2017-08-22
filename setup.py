import sys
from cx_Freeze import setup, Executable


includefiles = ["config.json"]
packages = ["requests","requests_ntlm"]
build_exe_options = {
	"include_msvcr":True,
	'include_files':includefiles,
	'packages':packages
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [ Executable('ssrs_batch.py', icon="094 Gengar.ico") ]
setup(name="SSRS_Batch",
      version='0.1',
      description="Automate SSRS downloads",
      options = {"build_exe": build_exe_options},
      executables=executables)
