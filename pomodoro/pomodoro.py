# normalde pomodoroyu 25dk çalışma + 5 dk mola şeklinde yapıyorlar
# fakat 25 dk bana az geldiği için 1 saat + 15 dk şeklinde yapıyorum
# o yüzden kodu da buna göre ayarladım, siz sürelerini değiştirip kullanabilirsiniz algoritmayı <3

from tkinter import*

window=Tk()
window.geometry("400x400") # ekranın ölçüsünü ayarlıyoruz
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

def start_60(): #çalışma süresi func'u
    global counting
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
        sint-=1 # geriye doğru saymasını istediğimiz için
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
    counting=window.after(1000, start_60)

def start_15(): #mola func'u
    global counting
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
    counting=window.after(1000, start_15)

def wait(): #durdurma func'u
    start["state"]="active"
    try:
        window.after_cancel(counting)
        status.config(text="Durdu.")
    except NameError:
        return

def reset(): # timer'ı resetlemek için func
    wait()
    countdown.config(text="60:00")
    status.config(text="Başlat.")

status=Label(window, text="Başlat.", font=("Times New Roman",20)) #default
status.pack(pady=15)
countdown=Label(window, text="60:00", font=("Times New Roman",40))
countdown.pack(pady=15)

start=Button(window,text="Başla.", font=("Times New Roman",20),command=start_60)
start.pack(pady=10) 

# pady, tkinter kütüphanesinn bir şeysisi. y ekseninde alınacak pikseli belirtiyor. 
# eğer 700x700lük bir window açacaksanız bence pady değerinin 60 olması ideal,
# ben 400x400lük açmak istediğim ve daha kompakt bir görünüm sevdiğim için 10 yaptım :p

pause=Button(window,text="Durdur.", font=("Times New Roman",20),command=wait)
pause.pack(pady=10)

reset=Button(window,text="Resetle.", font=("Times New Roman",20),command=reset)
reset.pack(pady=10)


window.mainloop()
