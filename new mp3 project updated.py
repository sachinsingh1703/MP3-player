from tkinter import *
import mysql.connector as sql
import tkinter.messagebox
from tkinter import filedialog
import pygame
from pygame import mixer
import os
import time
import random
import threading
import PIL.Image, PIL.ImageTk
from mutagen.mp3 import MP3
from tkinter import ttk

pygame.mixer.init()
mixer.init()

######################################################################################################################################################################

mycon = sql.connect(host='localhost',user='root',password='dhoni777',database='songs')
cursor=mycon.cursor()

def fetch():
    global choose_music
    choose_music=cursor.fetchone()

######################################################################################################################################################################

def hin_1():
    cursor.execute("select song_name from songs where sid=1")
    fetch()

def hin_2():
    cursor.execute("select song_name from songs where sid=2")
    fetch()
      
def hin_3():
    cursor.execute("select song_name from songs where sid=3")
    fetch()

def hin_4():
    cursor.execute("select song_name from songs where sid=4")
    fetch()

def hin_5():
    cursor.execute("select song_name from songs where sid=5")
    fetch()

def hin_6():
    cursor.execute("select song_name from songs where sid=6")
    fetch()

def hin_7():
    cursor.execute("select song_name from songs where sid=7")
    fetch()

def hin_8():
    cursor.execute("select song_name from songs where sid=8")
    fetch()

def hin_9():
    cursor.execute("select song_name from songs where sid=9")
    fetch()

def hin_10():
    cursor.execute("select song_name from songs where sid=10")
    fetch()

def hin_11():
    cursor.execute("select song_name from songs where sid=11")
    fetch()
    
def hin_12():
    cursor.execute("select song_name from songs where sid=12")
    fetch()
    
def hin_13():
    cursor.execute("select song_name from songs where sid=13")
    fetch()
    
def hin_14():
    cursor.execute("select song_name from songs where sid=14")
    fetch()
    
def hin_15():
    cursor.execute("select song_name from songs where sid=15")
    fetch()
    
def hin_16():
    cursor.execute("select song_name from songs where sid=16")
    fetch()
    
def hin_17():
    cursor.execute("select song_name from songs where sid=17")
    fetch()
    
def hin_18():
    cursor.execute("select song_name from songs where sid=18")
    fetch()
    
def hin_19():
    cursor.execute("select song_name from songs where sid=19")
    fetch()
    
def hin_20():
    cursor.execute("select song_name from songs where sid=20")
    fetch()

#######################################################################################################################################################################

def tam_1():
    cursor.execute("select song_name from songs where sid=101")
    fetch()

def tam_2():
    cursor.execute("select song_name from songs where sid=102")
    fetch()

def tam_3():
    cursor.execute("select song_name from songs where sid=103")
    fetch()

def tam_4():
    cursor.execute("select song_name from songs where sid=104")
    fetch()
    
def tam_5():
    cursor.execute("select song_name from songs where sid=105")
    fetch()
    
def tam_6():
    cursor.execute("select song_name from songs where sid=106")
    fetch()
    
def tam_7():
    cursor.execute("select song_name from songs where sid=107")
    fetch()
    
def tam_8():
    cursor.execute("select song_name from songs where sid=108")
    fetch()
    
def tam_9():
    cursor.execute("select song_name from songs where sid=109")
    fetch()
    
def tam_10():
    cursor.execute("select song_name from songs where sid=110")
    fetch()

def tam_11():
    cursor.execute("select song_name from songs where sid=111")
    fetch()

def tam_12():
    cursor.execute("select song_name from songs where sid=112")
    fetch()

def tam_13():
    cursor.execute("select song_name from songs where sid=113")
    fetch()

def tam_14():
    cursor.execute("select song_name from songs where sid=114")
    fetch()
    
def tam_15():
    cursor.execute("select song_name from songs where sid=115")
    fetch()
    
def tam_16():
    cursor.execute("select song_name from songs where sid=116")
    fetch()
    
def tam_17():
    cursor.execute("select song_name from songs where sid=117")
    fetch()
    
def tam_18():
    cursor.execute("select song_name from songs where sid=118")
    fetch()
    
def tam_19():
    cursor.execute("select song_name from songs where sid=119")
    fetch()
    
def tam_20():
    cursor.execute("select song_name from songs where sid=120")
    fetch()
    
###################################################################################################################################################################### 

def eng_1():
    cursor.execute("select song_name from songs where sid=201")
    fetch()

def eng_2():
    cursor.execute("select song_name from songs where sid=202")
    fetch()
    
def eng_3():
    cursor.execute("select song_name from songs where sid=203")
    fetch()
    
def eng_4():
    cursor.execute("select song_name from songs where sid=204")
    fetch()
    
def eng_5():
    cursor.execute("select song_name from songs where sid=205")
    fetch()
    
def eng_6():
    cursor.execute("select song_name from songs where sid=206")
    fetch()
    
def eng_7():
    cursor.execute("select song_name from songs where sid=207")
    fetch()
    
def eng_8():
    cursor.execute("select song_name from songs where sid=208")
    fetch()
    
def eng_9():
    cursor.execute("select song_name from songs where sid=209")
    fetch()
    
def eng_10():
    cursor.execute("select song_name from songs where sid=210")
    fetch()

def eng_11():
    cursor.execute("select song_name from songs where sid=211")
    fetch()

def eng_21():
    cursor.execute("select song_name from songs where sid=212")
    fetch()
    
def eng_13():
    cursor.execute("select song_name from songs where sid=213")
    fetch()
    
def eng_14():
    cursor.execute("select song_name from songs where sid=214")
    fetch()
    
def eng_15():
    cursor.execute("select song_name from songs where sid=215")
    fetch()
    
def eng_16():
    cursor.execute("select song_name from songs where sid=216")
    fetch()
    
def eng_17():
    cursor.execute("select song_name from songs where sid=217")
    fetch()
    
def eng_18():
    cursor.execute("select song_name from songs where sid=218")
    fetch()
    
def eng_19():
    cursor.execute("select song_name from songs where sid=219")
    fetch()
    
def eng_20():
    cursor.execute("select song_name from songs where sid=220")
    fetch()
    
#######################################################################################################################################################################
def music():
    a=(r"C:\Users\Sachin\Music\'Tu Jo Mila' VIDEO Song - K.K.Salman Khan, Nawazuddin, HarshaaliBajrangi Bhaijaan.mp3")
    b=(r"C:\Users\Sachin\Music\Naina - Dangal Aamir Khan Arijit Singh Pritam Amitabh Bhattacharya New Song 2017.mp3")
    c=(r"C:\Users\Sachin\Music\Give Me Some Sunshine.mp3")
    d=(r"C:\Users\Sachin\Music\Jaane Nahin Denge Tujhe.mp3")
    _songs = [a,b,c,d]
    _currently_playing_song = None
    next_song = random.choice(_songs)
    element = _songs.index(next_song)
    deleted=_songs.pop(element)
    while(next_song == _currently_playing_song):
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()
    
def random_songs():
    while True:
        music()
        while pygame.mixer.music.get_busy():
            continue
        threading.Thread(target = music , args =(_currently_playing_song,)).start()
def show_details_other(play_song):
   
    file_data=os.path.splitext(play_song)
    audio=MP3(play_song)
    total_length=audio.info.length
    mins,secs=divmod(total_length,60)
    mins=round(mins)
    secs=round(secs)
    timeformat='{:02d}:{:02d}'.format(mins,secs)
    lengthlabel['text']='TOTAL LENGTH -'+timeformat
    
    threading.Thread(target = start_count , args =(total_length,)).start()
        
def show_details(play_song):
    global total_length
    audio=MP3(play_song)
    total_length=audio.info.length
    mins,secs=divmod(total_length,60)
    mins=round(mins)
    secs=round(secs)
    timeformat='{:02d}:{:02d}'.format(mins,secs)
    lengthlabel['text']='TOTAL LENGTH -'+timeformat
    
    threading.Thread(target = start_count , args =(total_length,)).start()

def start_count(t):
    global paused
    
    while t and mixer.music.get_busy():
        if(paused):
            continue
        else:
            mins,secs=divmod(t,60)
            mins=round(mins)
            secs=round(secs)
            timeformat='{:02d}:{:02d}'.format(mins,secs)
            currenttimelabel['text']='CURRENT TIME -' + timeformat
            time.sleep(1) 
            t=t-1

def play_music():
    global paused
    
    if(paused):
        mixer.music.unpause()
        paused=False
    else:
        music =  ''.join(choose_music)
        mixer.music.load(music)
        mixer.music.play()
        show_details(music)
        musicpage.mainloop()


def play_other_music():
    global paused

    if(paused):
        mixer.music.unpause()
        paused=False
    else:
        stop_music()
        time.sleep(1)
        selected_song = playlistbox.curselection()
        selected_song=int(selected_song[0])
        play_it=playlist[selected_song]
        mixer.music.load(play_it)
        mixer.music.play()
        show_details_other(play_it)            
        
def stop_music():
    global stop
    stop=True
    mixer.music.stop()

paused=False

def pause_music():
    global paused
    paused=True
    mixer.music.pause()
    
def sound_control(val):
    soundcotrol=True
    volume=float(val)/100
    mixer.music.set_volume(volume)

def project():
    tkinter.messagebox.showinfo('-----DESCRIPTION-----','''   ---IT'S A MUSIC ALBUM WITH MUSIC PLAYER---
    -------ONLY MP3 FILES-------
    ------CONTAIN 20 HINDI,TAMIL,ENGLISH SONGS--------
    -------YOUR OWN FILES CAN ALSO BE PLAYED-------''')
def about_us():
    tkinter.messagebox.showinfo('-----MUSIC ALBUM-----',""" ----------Python Tkinter----------
    by ----------SACHIN----------""")

playlist = []

def choose_song():
    global filename
    filename=filedialog.askopenfilename()
    add_to_playlist(filename)

def del_song():
    selected_song = playlistbox.curselection()
    selected_song=int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)
    

def add_to_playlist(f):
    f=os.path.basename(f)
    index = 0
    playlistbox.insert(index, f)
    playlist.insert(index, filename)
    index += 1

def on_closing():
    stop_music()
    root.destroy()

def while_closing():
    stop_music()
    frame.destroy()

######################################################################################################################################################################
def random_page():
    ran_page=Tk()

    topframe=Frame(ran_page)
    topframe.pack(padx=15,side=TOP,pady=20)
    bottomframe=Frame(ran_page)
    bottomframe.pack(padx=15,side=BOTTOM,pady=20)
    rightframe=Frame(bottomframe)
    rightframe.pack(padx=15,side=LEFT,pady=30)
    leftframe=Frame(bottomframe)
    leftframe.pack(padx=15,side=RIGHT,pady=30)

    #play_photo=PhotoImage(file=r'C:\Users\Sachin\OneDrive\Pictures\video (1).png')
    play_button=ttk.Button(topframe,text='play_image',command=random_songs)
    play_button.grid(row=0,column=0,padx=30)
    
    #pause_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\pause.png')
    pause_button=ttk.Button(topframe,text='pause_photo',command=pause_music)
    pause_button.grid(row=0,column=1,padx=30)

    #lengthlabel = ttk.Label(rightframe,text='TOTAL LENGTH - --:--',relief=GROOVE,font='Times 10 italic')
    #lengthlabel.grid(pady=5)

    #currenttimelabel = ttk.Label(rightframe,text='CURRENT TIME - --:--',relief=GROOVE,font='Times 10 italic')
    #currenttimelabel.grid(pady=10)

    volume_control=ttk.Scale(leftframe,from_=0,to_=100,orient=HORIZONTAL,command=sound_control)
    volume_control.set(70)
    mixer.music.set_volume(0.7)
    volume_control.grid(row=4,column=3,padx=20)
    ran_page.mainloop()
    
    
def music_page():
    global musicpage
    global lengthlabel
    global currenttimelabel
    musicpage=Tk()
    musicpage.title('WELCOME TO MUSIC PLAYER')
    musicpage.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')

    topframe=Frame(musicpage)
    topframe.pack(padx=15,side=TOP,pady=20)
    bottomframe=Frame(musicpage)
    bottomframe.pack(padx=15,side=BOTTOM,pady=20)
    rightframe=Frame(bottomframe)
    rightframe.pack(padx=15,side=LEFT,pady=30)
    leftframe=Frame(bottomframe)
    leftframe.pack(padx=15,side=RIGHT,pady=30)
    
    #play_photo=PhotoImage(file=r'C:\Users\Sachin\OneDrive\Pictures\video (1).png')
    play_button=ttk.Button(topframe,text='play_image',command=play_music)
    play_button.grid(row=0,column=0,padx=30)

    #stop_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\stop-button.png')
    stop_button=ttk.Button(topframe,text='stop_photo',command=stop_music)
    stop_button.grid(row=0,column=1,padx=30)
    
    #pause_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\pause.png')
    pause_button=ttk.Button(topframe,text='pause_photo',command=pause_music)
    pause_button.grid(row=0,column=2,padx=30)

    lengthlabel = ttk.Label(rightframe,text='TOTAL LENGTH - --:--',relief=GROOVE,font='Times 10 italic')
    lengthlabel.grid(pady=5)

    currenttimelabel = ttk.Label(rightframe,text='CURRENT TIME - --:--',relief=GROOVE,font='Times 10 italic')
    currenttimelabel.grid(pady=10)

    volume_control=ttk.Scale(leftframe,from_=0,to_=100,orient=HORIZONTAL,command=sound_control)
    volume_control.set(70)
    mixer.music.set_volume(0.7)
    volume_control.grid(row=4,column=3,padx=20)
    
######################################################################################################################################################################

def hinmusic():
    global hinmusic
    hinpage=Tk()
    hinpage.geometry('1200x600')
    hinpage.title('HINDI MUSICS')
    hinpage.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')
    
    #music_image=PhotoImage(file="C:\\Users\\Sachin\\OneDrive\\Pictures\\enable-sound.png")

    h_1=ttk.Button(hinpage,text='music_image',command=lambda:[music_page(),hin_1()])
    h_1.pack()
    h_2=ttk.Button(hinpage,text='Chaar Kadam',command=lambda:[music_page(),hin_2()])
    h_2.pack()
    h_3=ttk.Button(hinpage,text='Rakta Charitra- Mila To Marega',command=lambda:[music_page(),hin_3()])
    h_3.pack()
    h_4=ttk.Button(hinpage,text='Tujhe Kitna Chahne Lage ',command=lambda:[music_page(),hin_4()])
    h_4.pack()
    h_5=ttk.Button(hinpage,text='Dil Bechara',command=lambda:[music_page(),hin_5()])
    h_5.pack()
    h_6=ttk.Button(hinpage,text='Tera Yaar Hoon Main',command=lambda:[music_page(),hin_6()])
    h_6.pack()
    h_7=ttk.Button(hinpage,text='Tum Hi Aana',command=lambda:[music_page(),hin_7()])
    h_7.pack()
    h_8=ttk.Button(hinpage,text='Teri Mitti',command=lambda:[music_page(),hin_8()])
    h_8.pack()
    h_9=ttk.Button(hinpage,text='KAUN TUJHE',command=lambda:[music_page(),hin_9()])
    h_9.pack()
    h_10=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_10()])
    h_10.pack()
    h_11=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_11()])
    h_11.pack()
    h_12=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_12()])
    h_12.pack()
    h_13=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_13()])
    h_13.pack()
    h_14=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_14()])
    h_14.pack()
    h_15=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_15()])
    h_15.pack()
    h_16=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_16()])
    h_16.pack()
    h_17=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_17()])
    h_17.pack()
    h_18=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_18()])
    h_18.pack()
    h_19=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_19()])
    h_19.pack()
    h_20=ttk.Button(hinpage,text='KHAIRIYAT',command=lambda:[music_page(),hin_20()])
    h_20.pack()

######################################################################################################################################################################

def tammusic():
    tampage=Tk()
    tampage.geometry('1200x600')
    tampage.title('TAMIL MUSICS')
    tampage.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')
    
    t_1=ttk.Button(tampage,text='1st_song',command=lambda:[music_page(),tam_1()])
    t_1.pack()  
    t_2=ttk.Button(tampage,text='2nd_song',command=lambda:[music_page(),tam_2()])
    t_2.pack()
    t_3=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_3()])
    t_3.pack()
    t_4=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_4()])
    t_4.pack()
    t_5=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_5()])
    t_5.pack()
    t_6=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_6()])
    t_6.pack()
    t_7=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_7()])
    t_7.pack()
    t_8=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_8()])
    t_8.pack()
    t_9=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_9()])
    t_9.pack()
    t_10=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_10()])
    t_10.pack()
    t_11=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_11()])
    t_11.pack()
    t_12=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_12()])
    t_12.pack()
    t_13=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_13()])
    t_13.pack()
    t_14=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_14()])
    t_14.pack()
    t_15=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_15()])
    t_15.pack()
    t_16=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_16()])
    t_16.pack()
    t_17=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_17()])
    t_17.pack()
    t_18=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_18()])
    t_18.pack()
    t_19=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_19()])
    t_19.pack()
    t_20=ttk.Button(tampage,text='3rd_song',command=lambda:[music_page(),tam_20()])
    t_20.pack()

######################################################################################################################################################################

def engmusic():
    engpage=Tk()
    engpage.geometry('1200x600')
    engpage.title('ENGLISH MUSICS')
    engpage.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')
    
    e_1=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_1()])
    e_1.pack()
    e_2=ttk.Button(engpage,text='2nd_song',command=lambda:[music_page(),eng_2()])
    e_2.pack()
    e_3=ttk.Button(engpage,text='3rd_song',command=lambda:[music_page(),eng_3()])
    e_3.pack()
    e_4=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_4()])
    e_4.pack()
    e_5=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_5()])
    e_5.pack()
    e_6=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_6()])
    e_6.pack()
    e_7=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_7()])
    e_7.pack()
    e_8=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_8()])
    e_8.pack()
    e_9=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_9()])
    e_9.pack()
    e_10=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_10()])
    e_10.pack()
    e_11=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_11()])
    e_11.pack()
    e_12=ttk.Button(engpage,text='2nd_song',command=lambda:[music_page(),eng_12()])
    e_12.pack()
    e_13=ttk.Button(engpage,text='3rd_song',command=lambda:[music_page(),eng_13()])
    e_13.pack()
    e_14=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_14()])
    e_14.pack()
    e_15=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_15()])
    e_15.pack()
    e_16=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_16()])
    e_16.pack()
    e_17=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_17()])
    e_17.pack()
    e_18=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_18()])
    e_18.pack()
    e_19=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_19()])
    e_19.pack()
    e_20=ttk.Button(engpage,text='1st_song',command=lambda:[music_page(),eng_20()])
    e_20.pack()

######################################################################################################################################################################
def hindi_random_page():
    hin_page=Tk()

    random_button=ttk.Button(hin_page,text='RANDOM_SONGS',command=random_page)
    random_button.grid(row=0,column=0,padx=30,pady=30)

    music_button=ttk.Button(hin_page,text='SELECT_SONGS',command=hinmusic)
    music_button.grid(row=0,column=1,padx=30,pady=30)
def othermusic():

    global frame
    global playlistbox
    global lengthlabel
    global currenttimelabel
    frame = Tk()
    frame.title('----MUSIC--PLAYER----')
    frame.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')

    rightframe=Frame(frame)
    rightframe.pack(padx=15,side=RIGHT,pady=30)

    topframe=Frame(rightframe)
    topframe.pack()

    bottomframe=Frame(rightframe)
    bottomframe.pack(padx=20,pady=20)

    bottomleftframe=Frame(bottomframe)
    bottomleftframe.pack(side=LEFT,padx=30)

    leftframe=Frame(frame)
    leftframe.pack(side=LEFT,padx=30,pady=30)

    playlistbox=Listbox(leftframe)
    playlistbox.pack()


    add_btn=ttk.Button(leftframe,text='ADD',command=choose_song)
    add_btn.pack(side=LEFT)
    del_btn=ttk.Button(leftframe,text='DELETE',command=del_song)
    del_btn.pack(side=LEFT)

    #play_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\video (1).png')
    #print(play_photo)
    play_button=ttk.Button(topframe,command=play_other_music,text='play_photo')
    play_button.grid(row=0,column=0,padx=20)

    #stop_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\stop-button.png')
    stop_button=ttk.Button(topframe,command=stop_music,text='stop_photo')
    stop_button.grid(row=0,column=1,padx=20)

    #pause_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\pause.png')
    pause_button=ttk.Button(topframe,command=pause_music,text='pause_photo')
    pause_button.grid(row=0,column=2,padx=20)

    lengthlabel = ttk.Label(bottomframe,text='TOTAL LENGTH - --:--',relief=GROOVE,font='Times 10 italic')
    lengthlabel.pack(pady=10)

    currenttimelabel = ttk.Label(bottomframe,text='CURRENT TIME - --:--',relief=GROOVE,font='Times 10 italic')
    currenttimelabel.pack(pady=10)


    volume_control=ttk.Scale(bottomleftframe,from_=0,to_=100,orient=HORIZONTAL,command=sound_control)
    volume_control.set(70)
    mixer.music.set_volume(0.7)
    volume_control.pack(pady=10)

    menu_bar=Menu(frame)
    frame.config(menu=menu_bar)

    sub_menu=Menu(menu_bar,tearoff=0)
    menu_bar.add_cascade(label='FILE',menu=sub_menu)
    sub_menu.add_command(label="PROJECT DESCRIPTION",command=project)
    sub_menu.add_command(label="ABOUT US",command=about_us)

    
    frame.protocol('WM_DELETE_WINDOW',while_closing)
    frame.mainloop()
    

#################################################################################################################################################################
root = Tk()
root.title('MUSIC FILE')
root.geometry('1200x600')
root.iconbitmap('C:\\Users\\Sachin\\OneDrive\\Pictures\\play_fv0_icon.ico')

label=ttk.Label(root,text='CHOOSE--A--LANGUAGE--YOU--WANT--TO--LISTEN',font=('Times',17,'italic bold'),relief = RIDGE,borderwidth=4,width=47)
label.place(x=250,y=0)
label.pack(side=TOP)

topframe=Frame(root)
topframe.pack()

bottomframe=Frame(root)
bottomframe.pack()

#play_photo=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\video (1).png')



hindi=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\hindi image.png')
hinlabel2=ttk.Label(topframe,text='')
hinbtn=ttk.Button(topframe,image=hindi,command=hindi_random_page)
hinlabel1=ttk.Label(topframe,text='')
hinlabel2.grid(row=0,column=0,pady=10)
hinbtn.grid(row=1,column=0,padx=30)
hinlabel1.grid(row=3,column=0,pady=10)

tamil=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\tamil image.png')
tamlabel2=ttk.Label(topframe,text='')
tambtn=ttk.Button(topframe,image=tamil,command=tammusic)
tamlabel1=ttk.Label(topframe,text='')
tamlabel2.grid(row=0,column=1,pady=10)
tambtn.grid(row=1,column=1,padx=30)
tamlabel1.grid(row=3,column=1,pady=10)

english=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\english image.png')
englabel2=ttk.Label(topframe,text='')
engbtn=ttk.Button(topframe,image=english,command=engmusic)
englabel1=ttk.Label(topframe,text='')
englabel2.grid(row=0,column=2,pady=10)
engbtn.grid(row=1,column=2,padx=30)
englabel1.grid(row=3,column=2,pady=10)

other=PhotoImage(file='C:\\Users\\Sachin\\OneDrive\\Pictures\\other.png')
othlabel2=ttk.Label(bottomframe,text='')
othbtn=ttk.Button(bottomframe,image=other,command=othermusic)
othlabel1=ttk.Label(bottomframe,text='')
othlabel2.grid(row=0,column=3,pady=10)
othbtn.grid(row=1,column=3,padx=30)
othlabel1.grid(row=3,column=3,pady=10)


menu_bar=Menu(root)
root.config(menu=menu_bar)
sub_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='FILE',menu=sub_menu)
sub_menu.add_command(label="ABOUT US",command=about_us)
sub_menu.add_command(label="PROJECT DESCRIPTION",command=project)
sub_menu.add_command(label='EXIT',command=root.destroy)

label=ttk.Label(root,text='*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*',font='Times 17 italic')
label.pack(side=BOTTOM)


root.protocol('WM_DELETE_WINDOW',on_closing)
root.mainloop()




