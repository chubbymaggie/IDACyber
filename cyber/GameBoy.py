from PyQt5.QtGui import qRgb
from idacyber import ColorFilter
from ida_bytes import get_item_size

class GameBoy(ColorFilter):
    name = "GameBoy"
    highlight_cursor = True
    help =  None

    def render_img(self, buf, addr, mouse_offs):
        #Bit    7  6  5  4  3  2  1  0
        #Data   R  R  R  G  G  G  B  B
        colors = []
        for c in buf:           
            c = ord(c)
            red = c & 0xE0
            green = (c << 3) & 0xE0
            blue = (c << 6) & 0xC0
            gray = red * 0.3 + green * 0.59 + blue * 0.11
            colors.append(qRgb(gray, gray, gray))
        return colors

    def get_tooltip(self, addr, mouse_offs):
        return "%X: item size %d" % (addr, get_item_size(addr + mouse_offs))
    
def FILTER_ENTRY():
    return GameBoy()
