import os
from pathlib import Path

__version__ = "0.5.0"

# If we are on Windows, Python 3.8+ then we need to add a DLL search path
# The libraries are located relative to this init file.
if os.name == "nt":
    pymsis_dir = None
    # add folder to Windows DLL search paths
    pymsis_dir = Path(__file__).resolve().parent
    print("INIT DIR:", pymsis_dir)
    for p in pymsis_dir.iterdir():
        print(p)
    os.add_dll_directory(pymsis_dir)

    os.environ["PATH"] = f"{pymsis_dir};" f"{os.environ['PATH']}"
    del pymsis_dir
