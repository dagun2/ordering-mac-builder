from setuptools import setup

APP = ['ordering_run.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pandas', 'openpyxl'],
    'plist': {
        'CFBundleName': '발주자동기입기',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleIdentifier': 'com.midnightaxi.orderingapp',
    },
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
