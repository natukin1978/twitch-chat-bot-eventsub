# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['twitch_chat_bot.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

b = Analysis(
    ['id_checker.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

MERGE( (a, 'TwitchChatBot', 'TwitchChatBot'), (b, 'IdChecker', 'IdChecker') )

pyz_a = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe_a = EXE(
    pyz_a,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TwitchChatBot',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

pyz_b = PYZ(b.pure, b.zipped_data, cipher=block_cipher)
exe_b = EXE(
    pyz_b,
    b.scripts,
    [],
    exclude_binaries=True,
    name='IdChecker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe_a,
    a.binaries,
    a.zipfiles,
    a.datas,
    exe_b,
    b.binaries,
    b.zipfiles,
    b.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='myapp_dist',
)
