from cx_Freeze import *

includefiles = ["icon.ico"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "i              Translator",
     "TARGETDIR",
     "[TARGETDIR]\Translator.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}


bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="My Translator",
    author="Himanshu Sahu",
    name="iTranslate",
    options={'build_exe': {'include_files':includefiles},'bdist_msi':bdist_msi_options, },
    executables=[
        Executable(
            script="Translator.py",
            base=base,
            icon='icon.ico',
        )
    ]
)