# normalde pomodoroyu 25dk çalışma + 5 dk mola şeklinde yapıyorlar
# fakat 25 dk bana az geldiği için 1 saat + 15 dk şeklinde yapıyorum
# o yüzden kodu da buna göre ayarladım, siz sürelerini değiştirip kullanabilirsiniz algoritmayı <3

from tkinter import*

window=Tk()
window.geometry("700x700") # ekranın ölçüsünü ayarlıyoruz
window.title("POMODORO") #ekranda çıkacak başlık
bell=True 


def clocksize(m, s): # def ile ihtiyaçlarımıza yönelik func oluşturuyoruz
    mstr = str(m)
    sstr = str(s)
    if m<10:
        mstr="0"+mstr
    if s<10:
        sstr="0"+sstr
    return mstr+":"+sstr

def start_60():
    global conting
    global bell
    start["state"]="disabled"

    if bell:
        window.bell()
        bell=False
    status.config(text="Çalışma Süreci") 
    curr= countdown["text"]  
    m,s =curr.split(":")
    mint,sint=int(m),int(s)
    if sint>0:
        sint-=1
        countdown.config(text=clocksize(mint,sint))
    if sint==0:
        if mint>0:
            sint=59
            mint-=1
            countdown.config(text=clocksize(mint,sint))
        else:
            countdown.config(text=clocksize(5,0))
            bell=True
            start_15()
            return
    conting=window.after(1000, start_60)

def start_15():
    global conting
    global bell

    if bell:
        window.bell()
        bell=False
    status.config(text="Mola")
    curr= countdown["text"]
    m,s= curr.split(":")
    mint,sint= int(m), int(s)

    if sint>0:
        sint-=1
        countdown.config(text=clocksize(mint,sint))
    if sint==0:
        if mint>0:
            sint=59
            mint-=1
            countdown.config(text=clocksize(mint,sint))
        else:
            countdown.config(text=clocksize(25,0))
            bell=True
            start_60()
            return
    conting=window.after(1000, start_15)

def wait():
    start["state"]="active"
    try:
        window.after_cancel(conting)
        status.config(text="Durdu.")
    except NameError:
        return

def reset():
    wait()
    countdown.config(text="60:00")
    status.config(text="Başlatılmadı.")

status=Label(window, text="Başlatılmadı.", font=("Times New Roman",20))
status.pack(pady=15)
countdown=Label(window, text="60:00", font=("Times New Roman",40))
countdown.pack(pady=15)

start=Button(window,text="Başla.", font=("Times New Roman",20),command=start_60)
start.pack(pady=60)
pause=Button(window,text="Durdur.", font=("Times New Roman",20),command=wait)
pause.pack(pady=60)
reset=Button(window,text="Resetle", font=("Times New Roman",20),command=reset)
reset.pack(pady=60)

window.mainloop()