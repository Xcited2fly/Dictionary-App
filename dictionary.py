import requests
import json
from Tkinter import *
import textwrap

def dictionary():
        # Get your id and key from https://developer.oxforddictionaries.com
        # TODO: replace with your own app_id and app_key
        app_id = ''
        app_key = ''

        language = 'en'
        word_id = e.get()

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

        try :
                r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
                response = json.dumps(r.json())
                res = json.loads(response)
                s = "Definitions -"

                for i in range(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
                        s += "\n{}. {}".format(i+1,textwrap.fill(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions'][0],100))

                l3.configure(text=s)
                
        except ValueError :
                l3.configure(text="No data found of this word!!")

        except IOError :
                l3.configure(text="No Internet")

tk = Tk()
tk.configure(background='cyan')
tk.title('Oxford Dictionary')
tk.geometry('1366x768')
l = Label(tk,text="Oxford Dictionary Interface",bg="cyan",font="Times 25 bold")
l.pack()
l2 = Label(tk,text="Enter word to Search : ",bg="cyan",font="Times 15 bold")
l2.pack()
e = Entry(tk,bd =4)
e.pack()
b1=Button(tk,text="Go",command=dictionary,bg="cyan",activebackground="red",bd=10)
b1.pack()
l3 = Label(tk,text="",bg="cyan",font="Times 15 bold")
l3.pack()
tk.mainloop()
