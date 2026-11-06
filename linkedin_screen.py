import terminalio
from adafruit_display_text import label
import supervisor
import time
import board
import displayio
import adafruit_miniqr


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
textbreite = text.bounding_box[2] * text.scale
text.y = display.height // 2# Breite des Textes in Pixeln

qr = adafruit_miniqr.QRCode()
qr.add_data(b"https://www.linkedin.com/in/selinameusel")
qr.make()
matrix = qr.matrix          # das Raster: matrix[x, y] ist True (schwarz) oder False (weiß)
# 2. Bitmap mit Rand bauen
rand = 4                                  # weißer Rand in Modulen, sonst scannt das Handy schlecht
groesse = matrix.width + 2 * rand
qr_bitmap = displayio.Bitmap(groesse, groesse, 2)

qr_palette = displayio.Palette(2)
qr_palette[0] = 0xFFC0CB                  # Farbe 0 = rosa
qr_palette[1] = 0x6F3250 # Farbe 1 = Textfarbe Beere

qr_tile = displayio.TileGrid(qr_bitmap, pixel_shader=qr_palette)
qr_gruppe = displayio.Group(scale=4, x=172, y=11)
qr_gruppe.append(qr_tile)
gruppe.append(qr_gruppe)

# 3. Raster übertragen
for y in range(matrix.height):
    for x in range(matrix.width):
        if matrix[x, y]:
            qr_bitmap[x + rand, y +rand] = 1

while True:
    text.y = 85
    text.x = text.x - 1      # wie viele Pixel pro Frame
    if text.x < -textbreite:           # wann ist der Text komplett links raus
        text.x = display.width           # wo soll er wieder starten
    time.sleep(0.01)            # wie lange pro Frame
