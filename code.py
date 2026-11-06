import terminalio
from adafruit_display_text import label
import supervisor
import time
import board
import displayio

display=board.DISPLAY
board.DISPLAY.width
board.DISPLAY.height

supervisor.status_bar.display = False #obere Statusleiste(WLAN usw) ausblenden
print("\033[2J\033[H", end="") #Bildschirm leeren

bitmap = displayio.Bitmap(320,170,1)
#print(board.DISPLAY.width , board.DISPLAY.height) #um Displaygröße herauszufinden
palette = displayio.Palette(1) #erzeugt eine Paletette mit einem Farbplatz
palette[0] = 0xFFC0CB # füllt Platz mir rosa
rechteck = displayio.TileGrid(bitmap, pixel_shader=palette, x= 0 ,y=0 )

gruppe = displayio.Group()
gruppe.append(rechteck)
display.root_group = gruppe

text = label.Label(
    terminalio.FONT,          # eingebaute Schrift
    text= "My Linkedin: selinameusel",               # mein text
    color=0x6F3250,           # Textfarbe
    scale=4,                # Textgröße
)

gruppe.append(text)
text.x= 320
text.y= display.height//2
textbreite = text.bounding_box[2] * text.scale      # Breite des Textes in Pixeln
while True:
    text.y = 85
    text.x = text.x - 1      # wie viele Pixel pro Frame
    if text.x < -textbreite:           # wann ist der Text komplett links raus
        text.x = display.width           # wo soll er wieder starten
    time.sleep(0.01)            # wie lange pro Frame
