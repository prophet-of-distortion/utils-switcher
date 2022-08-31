from turtle import width
import pystray
import pywintypes
import win32api
import win32con
from tkinter import *
from PIL import Image
from pystray import MenuItem as item


def on_set_resolution(width: int, height: int, frequency: int = 60):
  devmode = pywintypes.DEVMODEType()
  devmode.PelsWidth = width
  devmode.PelsHeight = height
  devmode.DisplayFrequency = frequency

  devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT | win32con.DM_DISPLAYFREQUENCY

  win32api.ChangeDisplaySettings(devmode, 0)


def on_quit():
  icon.visible = False
  icon.stop()


def on_custom_resolution():
  root = Tk()
  width = 300
  height = 150

  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  x = (screen_width/2) - (width/2)
  y = (screen_height/2) - (height/2)

  root.geometry(f"{width}x{height}+{x:.0f}+{y:.0f}")



  frame = Frame(root)
  frame.pack()
  root.title("Custom Resolution")
  root.resizable(False, False)
  root.mainloop()


if __name__ == "__main__":
  image = Image.open('tray-icon.png')
  menu = (
    item('Dota 2', lambda: on_set_resolution(2560, 1440, 120)),
    item('Dev', lambda: on_set_resolution(3840, 2160)),
    item('Custom', on_custom_resolution),
    item('Quit', on_quit)
  )

  icon = pystray.Icon("Switcher", image, "Switcher", menu)
  icon.run()


