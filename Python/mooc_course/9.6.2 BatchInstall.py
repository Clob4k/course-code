# 9.6.2 BatchInstall.py

import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", \
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy", \
        "pyinstaller", "django", "flask", "werobot", "pyqt5", \
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame", \
        "wordcloud", "PyMuPDF", "pytesseract"}
try :
    total = len(libs)
    count = 0
    for lib in libs:
        os.system("pip install " + lib + " -i https://pypi.tuna.tsinghua.edu.cn/simple")
        count += 1
        print("="*20)
        print("Installed " + lib)
        print("progress: " + str(count) + "/" + str(total))
        print("="*20)
    print("All libraries installed.")
except:
    print("Error: pip install failed.")  