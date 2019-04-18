import time, traceback, os, telepot
from tkinter import *
import cv2, youtube_dl # pip install opencv-python; pip install --upgrade 
youtube_dl
from PIL import Image, ImageTk #
from io import BytesIO # io
from ffpyplayer.player import MediaPlayer # pip install ffpyplayer
from pytube import YouTube
import vlc

_name_ = os.path.basename(os.path.realpath(__file__))
_path_ = os.path.realpath(__file__).replace(_name_, '')

class Screen(Frame):
    '''
        Screen widget: Embedded video player from local or youtube
    '''
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg = 'black')
        self.settings = { # Inizialazing dictionary settings
            "width" : 1024,
            "height" : 576
        }
        self.settings.update(kwargs) # Changing the default settings
        # Open the video source |temporary
        self.video_source ='D:\jjh\project\project1_moviesite\avergers.mp4'
    
        # Canvas where to draw video output
        self.canvas = Canvas(self, width = self.settings['width'], height = self.settings['height'], bg = "black", highlightthickness = 0)
        self.canvas.pack()
    
        # Creating VLC player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def update(self):
        '''
            Function: Start the player and keeps drawing the canvas 
        '''
        if not self.vid or not self.aux: # If Audio or Video is missing stop everything
            self.stop()
            return None

        # Get the frames and if video and audio are running
        ret, frame = self.get_frame()
        audio_frame, val = self.aux.get_frame()

        # Drawing frames on canvas
        if self.fb == 1: # Check if it's the first cycle, trying to make the audio start with the video
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame).resize((self.settings['width'], self.settings['height'])))
            self.canvas.create_image(0,0, image = self.photo, anchor = 'nw')
            self.fb = 0
            self.aux.set_pause(False) # Starting the audio
        elif ret and val != 'eof':
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame).resize((self.settings['width'], self.settings['height'])))
            self.canvas.create_image(0,0, image = self.photo, anchor = 'nw')

        self.after(self.delay, self.update) # Update for single frame, need to sync

    def get_frame(self):
        '''
            Function: Draws the frames
        '''
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)

    def youTube(self, ID):
        '''
            Function: Gets the youtube video and starts it 
        '''
        print("(TO REPLACE) : Downloading")
        yt = YouTube("https://www.youtube.com/watch?v=" + ID)
        stream = yt.streams.filter(progressive=True).first() # SEE THE POSSIBLE THINGS TO DOWNLOAD
        stream.download(_path_, 'test')
        print("(TO REPLACE) : Finished")
        self.start(_path_+'\\test.mp4')

    def start(self, _source):
        '''
            Function: Starts the player when gets input from keyboard(temporal) or Telegram
        '''
        try: # Stopping player if is already playing for a new video
            self.stop()
        except:
            None

        ff_opts = {'paused' : True} # Audio options
        self.fb = 1 # Setting first cycle

        if _source == 'local': # Checking which source use
            self.vid = cv2.VideoCapture(self.video_source)
            self.aux = MediaPlayer(self.video_source, ff_opts=ff_opts)
        else:
            self.vid = cv2.VideoCapture(_source)
            self.aux = MediaPlayer(_source, ff_opts=ff_opts)

        if not self.vid.isOpened():
            raise ValueError("Unable to open video source")

        self.update() # Starting the player

    def stop(self):
        '''
            Function: Release and stop Video and Audio
        '''
        try: # Stopping video
            self.vid.release()
            self.vid = None
        except:
            pass
        try: # Stopping audio
            self.aux.toggle_pause()
            self.aux = None
        except:
            pass
        self.canvas.delete('all') # Resetting canvas

    def __del__(self):
        '''
            Function: Release the video source when the object is destroyed
        '''
        if self.vid.isOpened():
            self.vid.release()

class Mirror:
    '''
        Mainframe: Display where to put the widgets
    '''
    def __init__(self):
        self.tk = Tk() # Creating the window
        self.tk.configure(background = 'black')
        self.tk.update()

        # Setting up the FRAMES for widgets
        self.bottomFrame = Frame(self.tk, background = 'black')
        self.bottomFrame.pack(side = BOTTOM, fill = BOTH, expand = YES)

        # Bindings and fullscreen setting
        self.fullscreen = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

        # Screen, BOT
        print("Inizializing Screen...")
        self.screen = Screen(self.bottomFrame)
        self.screen.pack(side = TOP)

        self.tk.bind("<Key>", self.key) # Get inputs from keyboard

    def key(self, event):
        pressed = repr(event.char).replace("'", '')
        if pressed == 's':
            self.screen.stop()
        elif pressed == 'a':
            self.screen.start('local')
        else:
            print('fail')

    def toggle_fullscreen(self, event = None):
        self.fullscreen = True
        self.tk.attributes("-fullscreen", self.fullscreen)

    def end_fullscreen(self, event = None):
        self.fullscreen = False
        self.tk.attributes("-fullscreen", self.fullscreen)

    def on_chat_message(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        message = str(msg.get('text'))

        if 'https://youtu.be/' in message:
            URL_VIDEO = message.split('https://youtu.be/')[1]
            Mir.screen.youTube(URL_VIDEO)       
        elif 'stop' == message.lower():
            Mir.screen.stop()

if __name__ == '__main__':
    Mir = Mirror()
    #bot = telepot.Bot(TELEGRAM_TOKEN)
    #bot.message_loop(on_chat_message)
    Mir.tk.mainloop()
    #while 1:
        #time.sleep(10)