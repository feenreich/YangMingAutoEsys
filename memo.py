print("xdd")
wait = input("PRESS ENTER TO CONTINUE.")
exec(open('E1.py',encoding='utf-8').read())
time.sleep(5.5)
pyinstaller -F --add-binary "C:\Users\pcclass\Desktop\AutoEsys\chromedriver.exe";"." F1.py
python interactive_runner.py python testGG.py 0 -- python GG.py