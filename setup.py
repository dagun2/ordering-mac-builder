from setuptools import setup

APP = ['ordering_run.py']  # ✅ 실행할 메인 스크립트 파일명
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pandas'],
    'plist': {
        'CFBundleName': '쭌파일변환기',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'com.yourname.jjunapp',
    },
    'iconfile': 'icon.icns',  # ❌ 아이콘 파일이 없으면 이 줄은 지워도 됩니다.
}

setup(
    app=APP,
    name='쭌파일변환기',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
