frase = list(input("Dame una frase: "))
for i in range(0,len(frase)):
    frase[i] = frase[i].lower()
dic = {"a": "4", "b": "l3","c":"[","d":")","e":"3","f":"|=","g":"&","h":"#","i":"1","j":",_|","k":">|","l":"1","m":"/\/\ ","n":"^/",
       "o":"0","p":"|*","q":"(_,)","r":"I2","s":"5","t":"7","u":"(_)","v":"\/","w":"\/\/","x":"><","y":"j","z":"2"}
frase_new = []
for string in frase:
    if string in dic.keys():
        frase_new += dic[string]
    else:
        frase_new += string
print("".join(frase_new))


    
