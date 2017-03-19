# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyqt_ui.pyw'],
             pathex=['d:\\Sync\\PythonProjects\\CopyPaste\\Distr'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyCopyPaste',
          debug=False,
          strip=False,
          upx=True,
          icon='d:\Sync\PythonProjects\CopyPaste\Distr\Icon.ico',
          console=False )
