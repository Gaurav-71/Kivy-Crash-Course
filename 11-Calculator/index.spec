from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['index.py'],
             pathex=['/Users/gauravv/Desktop/Development/Python/Crash Course/Kivy-Crash-Course/11-Calculator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='index',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

a.datas += [('Code/Design.kv','/Users/gauravv/Desktop/Development/Python/Crash Course/Kivy-Crash-Course/11-Calculator','DATA')]

app = BUNDLE(exe,
             name='index.app',
             icon=None,
             bundle_identifier=None)

coll = COLLECT(exe, Tree('/Users/gauravv/Desktop/Development/Python/Crash Course/Kivy-Crash-Course/11-Calculator/'),a.binaries, a.zipfiles, a.datas,*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)], strip=False, upx=True, upx_exclude=[], name='index')
