# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ( 'config/config.py', 'config'),
    ( 'gamemap/gamemap.py', 'gamemap'),
    ('player/player.py', 'player')
    ]

datafiles = [
    ( 'maps/*.json', 'maps'),
    ( 'pics/*.png', 'pics')
    ]

a = Analysis(['CaseysRPG.py'],
             pathex=['C:\\Users\\Student\\PycharmProjects\\RPG'],
             binaries=added_files,
             datas=datafiles,
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
          [],
          exclude_binaries=True,
          name='CaseysRPG',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='CaseysRPG')
