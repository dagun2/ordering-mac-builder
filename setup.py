from setuptools import setup

APP = ['ordering_run.py']
DATA_FILES = []

OPTIONS = {
    'argv_emulation': False
    'emulate_shell_environment': True,
    'redirect_stdout_to_asl': True,
    'includes': [
        'datetime', 'pytz', 'unicodedata', 'cmath'
    ],
    'packages': ['pandas', 'openpyxl', 'numpy', 'dateutil'],
    'excludes': ['tkinter'],  # 충돌 방지용
    'plist': {
        'CFBundleName': '쭌파일변환기',
        'CFBundleDisplayName': '쭌파일변환기',
        'CFBundleIdentifier': 'com.midnightaxi.jjunconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'LSEnvironment': {
            'PYTHONIOENCODING': 'utf-8',
            'LANG': 'en_US.UTF-8',
            'LC_ALL': 'en_US.UTF-8'
        }
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
