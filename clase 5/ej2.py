import os 
import webbrowser
resp =1 
while resp !=0:
    print("paint(1)")
    print("chrome (2)")
    print("pagar pc en 2 hs (3)")
    print("salir(0)")
    resp=int(input("selecione: "))
    if(resp==1):
        os.system("mspaint")
    elif(resp==2):
       webbrowser.open_new("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    elif(resp==3):
        os.system("shutdown -s -t 7200")
    else:
        print("no entiendo esa orden ._.")
