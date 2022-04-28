from tkinter import *
from turtle import color

# Colour palette
white = "#D3DCF1"
light_blue = "#315B9B"
blue = "#264573"
dark_blue = "#17202A"
gray = "#0D1726"
black = "#000000"

# Font family
fontFam = "Corbel"

# Labels
def Header1(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 18", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 18", fg=black, bg=white, **kw)

def Header2(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 14", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 14", fg=black, bg=white, **kw)

def Header3(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 12", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 12", fg=black, bg=white, **kw)

def Header1B(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 14 bold", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 14 bold", fg=black, bg=white, **kw)

def Header2B(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 14 bold", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 14 bold", fg=black, bg=white, **kw)

def Header3B(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 12 bold", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 12 bold", fg=black, bg=white, **kw)

def Description(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 10 bold", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 10 bold", fg=black, bg=white, **kw)

def Quote(window, darkmode = False, config={}, **kw):
    if(darkmode):
        return Label(window, config, font = fontFam + " 10 italic", fg=white, bg=dark_blue, **kw)
    return Label(window, config, font = fontFam + " 10 italic", fg=black, bg=white, **kw)

# Text
def MessageConsole(window, config={}, **kw):
    return Text(window,  config, bg = dark_blue, fg = white, font = fontFam + " 14", **kw)

# Text fields
def TextField(window, config={}, **kw):
    return Entry(window, config, bg = gray, fg = white, font = fontFam + " 14", **kw)

def MultiLineTextFiled(window, config={}, **kw):
    return Entry(window, config, bg = gray, fg = white, font = fontFam + " 14", **kw)

# Buttons
def CustomButton(window, config={}, **kw):
    return Button(window, config, font = fontFam + " 14", fg=white, bg = gray, **kw)

