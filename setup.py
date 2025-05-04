from setuptools import setup

APP = ['ordering_run.py']  # 메인 파이썬 파일명
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'includes': [
        'cmath', 'datetime', 'pytz', 'tkinter',
        'pandas._libs.tslibs.timestamps',
        'pandas._libs.tslibs.nattype',
        'pandas._libs.tslibs.timezones'
    ],
    'packages': ['pandas', 'openpyxl', 'tkinter'],
    'plist': {
        'CFBundleName': '쭌파일변환기',
        'CFBundleDisplayName': '쭌파일변환기',
        'CFBundleIdentifier': 'com.yourdomain.jjunconverter',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    },
    #'iconfile': 'icon.icns',  # 아이콘 파일 필요 시 사용, 없으면 제거 가능
}

setup(
    app=APP,
    name='쭌파일변환기',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
