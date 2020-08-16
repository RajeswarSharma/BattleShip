import cx_Freeze

executables = [cx_Freeze.Executable("BattleShip.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame","random","math"],
                           "include_files":["Bubblegum.ttf","bullets.png","enemy2.png","icon.png","spaceship.png"]}},
    executables = executables
    )
