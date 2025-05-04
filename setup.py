from setuptools import setup

APP = ['ordering_run.py']
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'includes': [
        'datetime', 'pytz', 'unicodedata',
        'pandas._libs.tslibs.timestamps',
        'pandas._libs.tslibs.nattype',
        'pandas._libs.tslibs.timezones',
    ],
    'packages': ['pandas', 'openpyxl', 'numpy', 'dateutil'],
    'plist': {
        'CFBundleName': '쭌파일변환기',
        'CFBundleDisplayName': '쭌파일변환기',
        'CFBundleIdentifier': 'com.midnightaxi.jjunconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    },
    # 'iconfile': 'icon.icns',
}

setup(
    app=APP,
    name='쭌파일변환기',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
