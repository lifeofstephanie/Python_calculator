from cx_Freeze import setup, Executable

base = None    

executables = [Executable("calculator.py", base=base)]

packages = ["idna", "tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "calculator",
    options = options,
    version = "2.8",
    description = 'My first calculator',
    executables = executables
)