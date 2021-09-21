from setuptools import setup
import packaging
import packaging.version
import packaging.specifiers
import packaging.requirements

APP = ["moonu_phases.py"]
DATA_FILES = []
OPTIONS = {
    'argv_emulation' :True,
    'iconfile' : 'CFE.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'numpy', 'py2app'],
}

setup(
    app = APP,
    name = "Moonu-Phases",
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app']
)


