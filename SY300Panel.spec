# -*- mode: python -*-
from kivy.deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal,get_deps_all, hookspath, runtime_hooks

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Elliot and Sharon\\PycharmProjects\\sand_box'],
             binaries=[],
             datas=[('SY300logo64.png', '.'), ('osc_panel.kv', '.')],
             #hiddenimports=[],
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             #excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
             **get_deps_minimal(video=None, audio=None, spelling=None, camera=None))
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SY300Panel',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='SY300logo_icon.ico')
coll = COLLECT(exe, Tree('C:\\Users\\Elliot and Sharon\\PycharmProjects\\sand_box\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='SY300Panel')
