import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=HEICtoJPG',
    '--onefile',
    '--noconsole',
    'HEICtoJPG.py'
])
