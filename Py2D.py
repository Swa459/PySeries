import tkinter as tk
import time
from datetime import datetime
import math
from PIL import Image, ImageTk
import os

# --- Utility Functions ---
def RGBformatter(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

Colors = {
    # --- REDS & PINKS ---
    "red": RGBformatter(255, 0, 0),
    "firebrick": RGBformatter(178, 34, 34),
    "darkred": RGBformatter(139, 0, 0),
    "crimson": RGBformatter(220, 20, 60),
    "indianred": RGBformatter(205, 92, 92),
    "lightcoral": RGBformatter(240, 128, 128),
    "salmon": RGBformatter(250, 128, 114),
    "darksalmon": RGBformatter(233, 150, 122),
    "lightsalmon": RGBformatter(255, 160, 122),
    "pink": RGBformatter(255, 192, 203),
    "lightpink": RGBformatter(255, 182, 193),
    "hotpink": RGBformatter(255, 105, 180),
    "deeppink": RGBformatter(255, 20, 147),
    "palevioletred": RGBformatter(219, 112, 147),
    "mediumvioletred": RGBformatter(199, 21, 133),
    # Additional reds and pinks
    "brickred": RGBformatter(203, 65, 84),
    "carnation": RGBformatter(255, 166, 201),
    "cherryred": RGBformatter(222, 49, 99),
    "coralred": RGBformatter(255, 64, 64),
    "flamingo": RGBformatter(252, 142, 172),
    "fuchsiapink": RGBformatter(255, 119, 255),
    "magentarose": RGBformatter(255, 0, 175),
    "persianrose": RGBformatter(254, 40, 162),
    "raspberryred": RGBformatter(227, 11, 92),
    "rose": RGBformatter(255, 0, 127),
    "rosewood": RGBformatter(101, 0, 11),
    "ruby": RGBformatter(224, 17, 95),
    "scarlet": RGBformatter(255, 36, 0),
    "shockingpink": RGBformatter(252, 15, 192),
    "strawberry": RGBformatter(252, 90, 141),
    "watermelon": RGBformatter(254, 127, 156),
    "wine": RGBformatter(114, 47, 55),
    
    # --- ORANGES & YELLOWS ---
    "orangered": RGBformatter(255, 69, 0),
    "tomato": RGBformatter(255, 99, 71),
    "coral": RGBformatter(255, 127, 80),
    "darkorange": RGBformatter(255, 140, 0),
    "orange": RGBformatter(255, 165, 0),
    "gold": RGBformatter(255, 215, 0),
    "yellow": RGBformatter(255, 255, 0),
    "lightyellow": RGBformatter(255, 255, 224),
    "lemonchiffon": RGBformatter(255, 250, 205),
    "papayawhip": RGBformatter(255, 239, 213),
    "moccasin": RGBformatter(255, 228, 181),
    "peachpuff": RGBformatter(255, 218, 185),
    "palegoldenrod": RGBformatter(238, 232, 170),
    "khaki": RGBformatter(240, 230, 140),
    "darkkhaki": RGBformatter(189, 183, 107),
    # Additional oranges and yellows
    "amber": RGBformatter(255, 191, 0),
    "apricot": RGBformatter(251, 206, 177),
    "brass": RGBformatter(181, 166, 66),
    "bronze": RGBformatter(205, 127, 50),
    "buff": RGBformatter(240, 220, 130),
    "butterscotch": RGBformatter(224, 169, 69),
    "canary": RGBformatter(255, 255, 153),
    "caramel": RGBformatter(255, 213, 154),
    "champagne": RGBformatter(247, 231, 206),
    "citrine": RGBformatter(228, 208, 10),
    "copper": RGBformatter(184, 115, 51),
    "cream": RGBformatter(255, 253, 208),
    "dandelion": RGBformatter(240, 225, 48),
    "ecru": RGBformatter(194, 178, 128),
    "fawn": RGBformatter(229, 170, 112),
    "flax": RGBformatter(238, 220, 130),
    "gamboge": RGBformatter(228, 155, 15),
    "honey": RGBformatter(235, 174, 52),
    "jasmine": RGBformatter(248, 222, 126),
    "lemon": RGBformatter(255, 247, 0),
    "maize": RGBformatter(251, 236, 93),
    "marigold": RGBformatter(234, 162, 33),
    "mustard": RGBformatter(255, 219, 88),
    "ocher": RGBformatter(204, 119, 34),
    "peach": RGBformatter(255, 229, 180),
    "pumpkin": RGBformatter(255, 117, 24),
    "saffron": RGBformatter(244, 196, 48),
    "sand": RGBformatter(194, 178, 128),
    "straw": RGBformatter(228, 217, 111),
    "tangerine": RGBformatter(242, 133, 0),
    
    # --- PURPLES ---
    "lavender": RGBformatter(230, 230, 250),
    "thistle": RGBformatter(216, 191, 216),
    "plum": RGBformatter(221, 160, 221),
    "violet": RGBformatter(238, 130, 238),
    "orchid": RGBformatter(218, 112, 214),
    "fuchsia": RGBformatter(255, 0, 255),
    "magenta": RGBformatter(255, 0, 255),
    "mediumorchid": RGBformatter(186, 85, 211),
    "mediumpurple": RGBformatter(147, 112, 219),
    "blueviolet": RGBformatter(138, 43, 226),
    "darkviolet": RGBformatter(148, 0, 211),
    "darkorchid": RGBformatter(153, 50, 204),
    "darkmagenta": RGBformatter(139, 0, 139),
    "purple": RGBformatter(128, 0, 128),
    "indigo": RGBformatter(75, 0, 130),
    "slateblue": RGBformatter(106, 90, 205),
    "darkslateblue": RGBformatter(72, 61, 139),
    # Additional purples
    "amethyst": RGBformatter(153, 102, 204),
    "byzantium": RGBformatter(112, 41, 99),
    "eggplant": RGBformatter(97, 64, 81),
    "grape": RGBformatter(111, 45, 168),
    "heliotrope": RGBformatter(223, 115, 255),
    "iris": RGBformatter(90, 79, 207),
    "lilac": RGBformatter(200, 162, 200),
    "mauve": RGBformatter(224, 176, 255),
    "mulberry": RGBformatter(197, 75, 140),
    "palatinate": RGBformatter(103, 26, 76),
    "pansy": RGBformatter(120, 24, 74),
    "periwinkle": RGBformatter(204, 204, 255),
    "puce": RGBformatter(204, 136, 153),
    "royal": RGBformatter(120, 81, 169),
    "wisteria": RGBformatter(201, 160, 220),
    
    # --- GREENS ---
    "greenyellow": RGBformatter(173, 255, 47),
    "chartreuse": RGBformatter(127, 255, 0),
    "lawngreen": RGBformatter(124, 252, 0),
    "lime": RGBformatter(0, 255, 0),
    "limegreen": RGBformatter(50, 205, 50),
    "palegreen": RGBformatter(152, 251, 152),
    "lightgreen": RGBformatter(144, 238, 144),
    "mediumspringgreen": RGBformatter(0, 250, 154),
    "springgreen": RGBformatter(0, 255, 127),
    "mediumseagreen": RGBformatter(60, 179, 113),
    "seagreen": RGBformatter(46, 139, 87),
    "forestgreen": RGBformatter(34, 139, 34),
    "green": RGBformatter(0, 128, 0),
    "darkgreen": RGBformatter(0, 100, 0),
    "yellowgreen": RGBformatter(154, 205, 50),
    "olivedrab": RGBformatter(107, 142, 35),
    "olive": RGBformatter(128, 128, 0),
    "darkolivegreen": RGBformatter(85, 107, 47),
    "mediumaquamarine": RGBformatter(102, 205, 170),
    "darkseagreen": RGBformatter(143, 188, 139),
    "lightseagreen": RGBformatter(32, 178, 170),
    "darkcyan": RGBformatter(0, 139, 139),
    "teal": RGBformatter(0, 128, 128),
    # Additional greens
    "apple": RGBformatter(141, 182, 0),
    "asparagus": RGBformatter(135, 169, 107),
    "avocado": RGBformatter(181, 195, 107),
    "celadon": RGBformatter(172, 225, 175),
    "celery": RGBformatter(184, 212, 120),
    "emerald": RGBformatter(80, 200, 120),
    "fern": RGBformatter(113, 188, 120),
    "jade": RGBformatter(0, 168, 107),
    "juniper": RGBformatter(106, 150, 130),
    "kelly": RGBformatter(76, 187, 23),
    "malachite": RGBformatter(11, 218, 81),
    "mantis": RGBformatter(116, 195, 101),
    "mint": RGBformatter(152, 255, 152),
    "moss": RGBformatter(138, 154, 91),
    "myrtle": RGBformatter(33, 66, 30),
    "neon": RGBformatter(57, 255, 20),
    "parakeet": RGBformatter(3, 192, 74),
    "pear": RGBformatter(209, 226, 49),
    "pistachio": RGBformatter(147, 197, 114),
    "sage": RGBformatter(188, 184, 138),
    "seafoam": RGBformatter(147, 223, 184),
    "shamrock": RGBformatter(0, 158, 96),
    "verdigris": RGBformatter(67, 179, 174),
    "viridian": RGBformatter(64, 130, 109),
    
    # --- BLUES & CYANS ---
    "aqua": RGBformatter(0, 255, 255),
    "cyan": RGBformatter(0, 255, 255),
    "lightcyan": RGBformatter(224, 255, 255),
    "paleturquoise": RGBformatter(175, 238, 238),
    "aquamarine": RGBformatter(127, 255, 212),
    "turquoise": RGBformatter(64, 224, 208),
    "mediumturquoise": RGBformatter(72, 209, 204),
    "darkturquoise": RGBformatter(0, 206, 209),
    "cadetblue": RGBformatter(95, 158, 160),
    "steelblue": RGBformatter(70, 130, 180),
    "lightsteelblue": RGBformatter(176, 196, 222),
    "powderblue": RGBformatter(176, 224, 230),
    "lightblue": RGBformatter(173, 216, 230),
    "skyblue": RGBformatter(135, 206, 235),
    "lightskyblue": RGBformatter(135, 206, 250),
    "deepskyblue": RGBformatter(0, 191, 255),
    "dodgerblue": RGBformatter(30, 144, 255),
    "cornflowerblue": RGBformatter(100, 149, 237),
    "royalblue": RGBformatter(65, 105, 225),
    "blue": RGBformatter(0, 0, 255),
    "mediumblue": RGBformatter(0, 0, 205),
    "darkblue": RGBformatter(0, 0, 139),
    "navy": RGBformatter(0, 0, 128),
    "midnightblue": RGBformatter(25, 25, 112),
    # Additional blues
    "airforce": RGBformatter(93, 138, 168),
    "alice": RGBformatter(240, 248, 255),
    "azure": RGBformatter(0, 127, 255),
    "babyblue": RGBformatter(137, 207, 240),
    "capri": RGBformatter(0, 191, 255),
    "cerulean": RGBformatter(0, 123, 167),
    "cobalt": RGBformatter(0, 71, 171),
    "denim": RGBformatter(21, 96, 189),
    "egyptianblue": RGBformatter(16, 52, 166),
    "electricblue": RGBformatter(125, 249, 255),
    "iceblue": RGBformatter(153, 217, 234),
    "lapislazuli": RGBformatter(38, 97, 156),
    "neonblue": RGBformatter(70, 102, 255),
    "oxfordblue": RGBformatter(0, 33, 71),
    "peacock": RGBformatter(51, 161, 201),
    "persianblue": RGBformatter(28, 57, 187),
    "prussian": RGBformatter(0, 49, 83),
    "sapphire": RGBformatter(15, 82, 186),
    "tiffany": RGBformatter(10, 186, 181),
    "ultramarine": RGBformatter(63, 0, 255),
    
    # --- BROWNS & WHITES ---
    "cornsilk": RGBformatter(255, 248, 220),
    "blanchedalmond": RGBformatter(255, 235, 205),
    "bisque": RGBformatter(255, 228, 196),
    "navajowhite": RGBformatter(255, 222, 173),
    "wheat": RGBformatter(245, 222, 179),
    "burlywood": RGBformatter(222, 184, 135),
    "tan": RGBformatter(210, 180, 140),
    "rosybrown": RGBformatter(188, 143, 143),
    "sandybrown": RGBformatter(244, 164, 96),
    "goldenrod": RGBformatter(218, 165, 32),
    "darkgoldenrod": RGBformatter(184, 134, 11),
    "peru": RGBformatter(205, 133, 63),
    "chocolate": RGBformatter(210, 105, 30),
    "saddlebrown": RGBformatter(139, 69, 19),
    "sienna": RGBformatter(160, 82, 45),
    "brown": RGBformatter(165, 42, 42),
    "maroon": RGBformatter(128, 0, 0),
    "white": RGBformatter(255, 255, 255),
    "snow": RGBformatter(255, 250, 250),
    "honeydew": RGBformatter(240, 255, 240),
    "mintcream": RGBformatter(245, 255, 250),
    "aliceblue": RGBformatter(240, 248, 255),
    "ghostwhite": RGBformatter(248, 248, 255),
    "whitesmoke": RGBformatter(245, 245, 245),
    "seashell": RGBformatter(255, 245, 238),
    "beige": RGBformatter(245, 245, 220),
    "oldlace": RGBformatter(253, 245, 230),
    "floralwhite": RGBformatter(255, 250, 240),
    "ivory": RGBformatter(255, 255, 240),
    "antiquewhite": RGBformatter(250, 235, 215),
    "linen": RGBformatter(250, 240, 230),
    "lavenderblush": RGBformatter(255, 240, 245),
    "mistyrose": RGBformatter(255, 228, 225),
    # Additional browns and whites
    "almond": RGBformatter(239, 222, 205),
    "beaver": RGBformatter(159, 129, 112),
    "biscuit": RGBformatter(255, 228, 196),
    "brunette": RGBformatter(77, 40, 0),
    "camel": RGBformatter(193, 154, 107),
    "chestnut": RGBformatter(149, 69, 53),
    "cinnamon": RGBformatter(210, 105, 30),
    "cocoa": RGBformatter(135, 84, 45),
    "coffee": RGBformatter(111, 78, 55),
    "cognac": RGBformatter(159, 56, 0),
    "desert": RGBformatter(193, 154, 107),
    "espresso": RGBformatter(97, 62, 35),
    "hazel": RGBformatter(139, 117, 0),
    "mahogany": RGBformatter(192, 64, 0),
    "mocha": RGBformatter(135, 84, 45),
    "oak": RGBformatter(128, 84, 43),
    "russet": RGBformatter(128, 70, 27),
    "sepia": RGBformatter(112, 66, 20),
    "tawny": RGBformatter(205, 87, 0),
    "terracotta": RGBformatter(226, 114, 91),
    "umber": RGBformatter(99, 81, 71),
    "walnut": RGBformatter(119, 63, 26),
    
    # --- GRAYS & BLACKS ---
    "gainsboro": RGBformatter(220, 220, 220),
    "lightgray": RGBformatter(211, 211, 211),
    "silver": RGBformatter(192, 192, 192),
    "darkgray": RGBformatter(169, 169, 169),
    "gray": RGBformatter(128, 128, 128),
    "dimgray": RGBformatter(105, 105, 105),
    "lightslategray": RGBformatter(119, 136, 153),
    "slategray": RGBformatter(112, 128, 144),
    "darkslategray": RGBformatter(47, 79, 79),
    "black": RGBformatter(0, 0, 0),
    # Additional grays and blacks
    "ash": RGBformatter(178, 190, 181),
    "battleship": RGBformatter(132, 132, 130),
    "carbon": RGBformatter(50, 50, 50),
    "charcoal": RGBformatter(54, 69, 79),
    "dove": RGBformatter(109, 109, 109),
    "ebony": RGBformatter(85, 93, 80),
    "graphite": RGBformatter(56, 63, 69),
    "gunmetal": RGBformatter(42, 52, 57),
    "iron": RGBformatter(90, 92, 106),
    "lead": RGBformatter(33, 34, 36),
    "nickel": RGBformatter(114, 116, 114),
    "pewter": RGBformatter(150, 168, 161),
    "platinum": RGBformatter(229, 228, 226),
    "smoke": RGBformatter(115, 130, 118),
    "steel": RGBformatter(67, 70, 75),
    "tin": RGBformatter(127, 127, 127),
    
    # --- ADDITIONAL NAMED COLORS ---
    "burgundy": RGBformatter(128, 0, 32),
    "cardinal": RGBformatter(196, 30, 58),
    "carmine": RGBformatter(150, 0, 24),
    "cerise": RGBformatter(222, 49, 99),
    "claret": RGBformatter(127, 23, 52),
    "garnet": RGBformatter(115, 54, 53),
    "pomegranate": RGBformatter(192, 57, 43),
    "vermilion": RGBformatter(227, 66, 52),
    
    "aqua2": RGBformatter(127, 255, 212),
    "beryl": RGBformatter(217, 242, 221),
    "caribbean": RGBformatter(0, 204, 153),
    "lagoon": RGBformatter(4, 123, 141),
    "ocean": RGBformatter(0, 119, 190),
    "seawater": RGBformatter(61, 89, 171),
    
    "burgundy2": RGBformatter(144, 0, 32),
    "clover": RGBformatter(56, 118, 29),
    "emerald2": RGBformatter(1, 121, 111),
    "forest2": RGBformatter(11, 102, 35),
    "hunter": RGBformatter(53, 94, 59),
    "jungle": RGBformatter(41, 171, 135),
    "pine": RGBformatter(1, 121, 111),
    
    "aubergine": RGBformatter(58, 0, 41),
    "boysenberry": RGBformatter(135, 50, 96),
    "lavenderblue": RGBformatter(204, 204, 255),
    "mauveine": RGBformatter(224, 176, 255),
    "orchid2": RGBformatter(175, 115, 179),
    "violetred": RGBformatter(247, 83, 148),
    
    "bay": RGBformatter(166, 106, 60),
    "brandy": RGBformatter(135, 65, 63),
    "brick": RGBformatter(156, 102, 31),
    "burnt": RGBformatter(138, 54, 15),
    "ginger": RGBformatter(176, 101, 0),
    "leather": RGBformatter(150, 112, 89),
    "rust": RGBformatter(183, 65, 14),
    "teak": RGBformatter(177, 148, 105),
    
    # --- METALLIC COLORS ---
    "antiquegold": RGBformatter(133, 109, 46),
    "chromeyellow": RGBformatter(255, 167, 0),
    "copperrose": RGBformatter(153, 102, 102),
    "goldleaf": RGBformatter(212, 175, 55),
    "metallicgold": RGBformatter(212, 175, 55),
    "metallicsilver": RGBformatter(170, 169, 173),
    "oldbronze": RGBformatter(111, 78, 55),
    "oldgold": RGBformatter(207, 181, 59),
    "rosegold": RGBformatter(183, 110, 121),
    
    # --- NEON COLORS ---
    "neongreen": RGBformatter(57, 255, 20),
    "neonpink": RGBformatter(255, 16, 240),
    "neonorange": RGBformatter(255, 95, 31),
    "neonyellow": RGBformatter(255, 255, 51),
    "neonpurple": RGBformatter(188, 19, 254),
    
    # --- PASTEL COLORS ---
    "pastelblue": RGBformatter(174, 198, 207),
    "pastelgreen": RGBformatter(119, 221, 119),
    "pastellavender": RGBformatter(222, 165, 164),
    "pastelorange": RGBformatter(255, 179, 71),
    "pastelpink": RGBformatter(255, 209, 220),
    "pastelpurple": RGBformatter(179, 158, 181),
    "pastelred": RGBformatter(255, 105, 97),
    "pastelyellow": RGBformatter(253, 253, 150),
}

def AddColor(name, r, g, b):
    Colors[name.lower()] = RGBformatter(r, g, b)

def Wait(value, unit, freezeProcess=True, root=None):
    if freezeProcess:
        if unit == "milli":
            time.sleep(float(value) / 1000)
        elif unit == "secs":
            time.sleep(float(value))
        elif unit == "mins":
            time.sleep(float(value) * 60)
        elif unit == "hrs":
            time.sleep(float(value) * 3600)
    else:
        delay = 0
        if unit == "milli":
            delay = int(value)
        elif unit == "secs":
            delay = int(value * 1000)
        elif unit == "mins":
            delay = int(value * 60 * 1000)
        elif unit == "hrs":
            delay = int(value * 3600 * 1000)
        if root is not None:
            root.after(delay, lambda: None)

def CurrentTime():
    return datetime.now().strftime("%H:%M:%S")

def CurrentDate():
    return datetime.now().strftime("%d/%m/%Y")

# --- Window Class ---
class Window:
    def __init__(self, geometry="1000x600", title="Py2D Version 1.1", master=None):
        self.listKeys = []
        
        if master is None:
            self.root = tk.Tk()
        else:
            self.root = tk.Toplevel(master)
            self.root.transient(master)
            self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.title(title)
        self.root.geometry(geometry)

        self.area: tk.Canvas = tk.Canvas(self.root, bg="white")
        self.area.pack(fill="both", expand=True)

    def Geometry(self, geometry):
        self.root.geometry(geometry)
    
    def Title(self, title):
        self.root.title(title)
    
    def BackgroundColor(self, color):
        self.area.config(bg=Colors.get(str(color).lower(), color))
    
    def Transparency(self, value):
        self.root.attributes("-alpha", value)
    
    def FullScreen(self):
        self.root.attributes("-fullscreen", True)
    
    def BgImg(self, path: str):
        ext = os.path.splitext(path)[1].lower()
        if ext != '.svg':
            raise ValueError("Only SVG images are supported for BgImg.")
        self.bg_path = path
        self._render_bg()

        # Re-render on resize
        self.area.bind("<Configure>", lambda e: self._render_bg())

    def _render_bg(self):
        import cairosvg
        png_path = os.path.splitext(self.bg_path)[0] + "_bgtemp.png"
        cairosvg.svg2png(
            url=self.bg_path,
            write_to=png_path,
            output_height=self.area.winfo_height(),
            output_width=self.area.winfo_width()
        )
        self.bg_image = Imagetk.PhotoImage(Image.open(png_path))
        self.area.create_image(0, 0, image=self.bg_image, anchor="nw")
        
    def Settings(self, characteristic, value):
        characteristic = str(characteristic).lower()
        if characteristic == "geometry":
            self.root.geometry(value)
        elif characteristic == "title":
            self.root.title(value)
        elif characteristic == "bg":
            self.area.config(bg=Colors.get(value.lower(), value))
        elif characteristic == "transparency":
            self.root.attributes("-alpha", value)
        elif characteristic == "fullscreen":
            self.root.attributes("-fullscreen", value)
        elif characteristic == "topmost":
            self.root.attributes("-topmost", value)
    
    def Return(self, characteristic):
        characteristic = str(characteristic).lower()
        if characteristic == "geometry":
            return self.root.wm_geometry()
        elif characteristic == "title":
            return self.root.wm_title()
        elif characteristic == "bg":
            return self.area.cget("bg")
        elif characteristic == "transparency":
            return self.root.attributes("-alpha")
        elif characteristic == "fullscreen":
            return self.root.attributes("-fullscreen")
        elif characteristic == "topmost":
            return self.root.attributes("-topmost")
    
    def PrintKeys(self, end="", start=""):
        def key(event):
            print(start + event.keysym, end=end)
        self.root.bind("<Key>", key)

    def IsKey(self, key, func):
        self.root.bind(key, func)

    def SeriesKey(self, listofKeys=None):
        def key(event):
            if isinstance(listofKeys, list):
                listofKeys.append(event.keysym)
            elif listofKeys is None:
                self.listKeys.append(event.keysym)
        self.root.bind("<Key>", key)

    def FirstKey(self, termination=False):
        try:
            return self.listKeys[0]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, No keys were pressed.\033[0m")
            return None if not termination else exit(1)

    def SecondKey(self, termination=False):
        try:
            return self.listKeys[1]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, 2 keys weren't pressed.\033[0m")
            return None if not termination else exit(1)

    def ThirdKey(self, termination=False):
        try:
            return self.listKeys[2]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, 3 keys weren't pressed.\033[0m")
            return None if not termination else exit(1)

    def PrevKey(self, termination=False):
        try:
            return self.listKeys[-1]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, No keys were pressed.\033[0m")
            return None if not termination else exit(1)

    def SecondLastKey(self, termination=False):
        try:
            return self.listKeys[-2]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, 2 keys weren't pressed.\033[0m")
            return None if not termination else exit(1)

    def ThirdLastKey(self, termination=False):
        try:
            return self.listKeys[-3]
        except IndexError:
            print("\033[38;2;255;165;0mSorry, 3 keys weren't pressed.\033[0m")
            return None if not termination else exit(1)
    
    def After(self, value, unit, job, freezeProcess=True):
        unit = str(unit).lower()
        if unit == "milli":
            delay = int(value)
        elif unit == "secs":
            delay = int(value * 1000)
        elif unit == "mins":
            delay = int(value * 60 * 1000)
        elif unit == "hrs":
            delay = int(value * 3600 * 1000)
        else:
            raise ValueError("Unit must be one of: 'milli', 'secs', 'mins', 'hrs'")

        if freezeProcess:
            time.sleep(delay / 1000.0)
            job()
        else:
            self.root.after(delay, job)

    def run(self):
        self.root.mainloop()

class Score:
    def __init__(self, window: Window, x=None, y=None, anchor="n"):
        window.root.update_idletasks()
        self.canvas: tk.Canvas = window.area
        self.value = 0

        self.x = int(self.canvas.winfo_reqwidth() / 2) if x is None else x
        self.y = 30 if y is None else y

        self.text_id = self.canvas.create_text(
            self.x, self.y,
            text=str(self.value),
            font=("Arial", 36),
            fill=Colors.get("scoretext", Colors.get("darkblue", "#000001")),
            anchor=anchor
        )

    def Add(self, points):
        self.value += points
        self.canvas.itemconfig(self.text_id, text=str(self.value))

    def Subtract(self, points):
        self.value -= points
        self.canvas.itemconfig(self.text_id, text=str(self.value))

    def Multiply(self, points):
        self.value *= points
        self.canvas.itemconfig(self.text_id, text=str(self.value))

    def Divide(self, points):
        self.value /= points
        self.canvas.itemconfig(self.text_id, text=str(self.value))
    
    def Reset(self):
        self.value = 0
        self.canvas.itemconfig(self.text_id, text=str(self.value))
        
    def Preview(self, x=None, y=None, value=None,
                font=("Arial", 36, "bold"), color="#010426", anchor="n"):
        px = self.x if x is None else x
        py = self.y if y is None else y
        pv = self.value if value is None else value

        self.canvas.create_text(
            px, py,
            text=str(pv),
            font=font,
            fill=Colors.get(str(color).lower(), color),
            anchor=anchor
        )
    
    def Above(self):
        self.canvas.tag_raise(self.text_id)
    def Below(self):
        self.canvas.tag_lower(self.text_id)

# -- Label --
class Label:
    def __init__(self, window, x=None, y=30, anchor="n", font=("Arial", 14), fill="black"):
        window.root.update_idletasks()
        self.screen: tk.Canvas = window.area
        self.x = int(self.screen.winfo_reqwidth() / 2) if x is None else x
        self.y = y
        self.anchor = anchor
        self.font = font
        self.fill = fill
        self.label_id = None

    def Text(self, text):
        if self.label_id:
            self.screen.itemconfig(self.label_id, text=text)
        else:
            self.label_id = self.screen.create_text(
                self.x, self.y,
                text=text,
                anchor=self.anchor,
                font=self.font,
                fill=self.fill
            )
    
    def Add(self, pos=None, text=None):
        if self.label_id is None:
            return

        current = self.screen.itemcget(self.label_id, "text")

        if text is None:
            return current

        if pos is None:
            pos = len(current)

        new_text = current[:pos] + text + current[pos:]
        self.screen.itemconfig(self.label_id, text=new_text)
        return new_text
    
    def Remove(self, entity=None):
        if self.label_id is None:
            return

        current: str = self.screen.itemcget(self.label_id, "text")

        if entity is None:
            new = ""
        elif entity == "clear":
            new = ""
        else:
            new = current.replace(entity, "")

        self.screen.itemconfig(self.label_id, text=new)
        return new
        
    def Above(self):
        if self.label_id:
            self.screen.tag_raise(self.label_id)
    def Below(self):
        if self.label_id:
            self.screen.tag_lower(self.label_id)
    
    def IsClicked(self, func):
        if self.label_id:
            self.screen.tag_bind(self.label_id, "<Button-1>", func)

class StopWatch:
    def __init__(self, window: "Window", x=None, y=None, anchor="n",
                 fontcolor="#000001", fontsize=36, fontname="Arial"):
        window.root.update_idletasks()
        self.screen: tk.Canvas = window.area
        self.x = int(self.screen.winfo_reqwidth() / 2) if x is None else x
        self.y = 30 if y is None else y

        self.timer = 0.0
        self.start_time = None
        self.timer_id = None

        self.fc = fontcolor
        self.fs = fontsize
        self.fn = fontname

        self.pfc = fontcolor
        self.pfs = fontsize
        self.pfn = fontname

        self.sw_id = self.screen.create_text(
            self.x, self.y,
            text=str(self.timer) + "s",
            font=(self.fn, self.fs),
            fill=Colors.get("timertext", Colors.get("darkblue", self.fc)),
            anchor=anchor
        )

    def Trigger(self):
        if self.start_time is None:
            self.start_time = time.time()

        def i():
            self.timer = time.time() - self.start_time
            self.screen.itemconfig(self.sw_id, text=f"{self.timer:.1f}s")
            self.timer_id = self.screen.after(100, i)

        i()

    def Stop(self):
        if self.start_time is not None:
            self.timer = time.time() - self.start_time
            self.screen.itemconfig(self.sw_id, text=f"{self.timer:.1f}s")
        if self.timer_id is not None:
            self.screen.after_cancel(self.timer_id)
            self.timer_id = None

    def Reset(self):
        self.start_time = time.time()
        self.timer = 0.0
        self.screen.itemconfig(self.sw_id, text="0.0s")

    def Above(self):
        if self.sw_id:
            self.screen.tag_raise(self.sw_id)

    def Below(self):
        if self.sw_id:
            self.screen.tag_lower(self.sw_id)
    
    def Font(self, fontname=None, fontsize=None, fontcolor=None):
        self.fn = self.pfn if fontname is None else fontname
        self.fs = self.pfs if fontsize is None else fontsize
        self.fc = self.pfc if fontcolor is None else fontcolor

        self.pfn, self.pfs, self.pfc = self.fn, self.fs, self.fc

        self.screen.itemconfig(self.sw_id,
                            fill=self.fc,
                            font=(self.fn, self.fs))

class TextBox:
    def __init__(self, Window, X=10, Y=10, Height=5, Width=40, 
                 Bg="white", Fg="black", Font=("Arial", 12), 
                 BorderWidth=0, Relief="solid", Status="multi-liner"):
        Window.root.update_idletasks()
        self.Height = Height
        self.Width = Width
        self.X = X
        self.Y = Y
        self.Bg = Bg
        self.Fg = Fg
        self.Font = Font
        self.BorderWidth = BorderWidth
        self.Relief = Relief
        self.Screen: tk.Canvas = Window.area

        if Status == "multi-liner":
            self.Entity = tk.Text(
                self.Screen, 
                height=self.Height, 
                width=self.Width, 
                bg=self.Bg, 
                fg=self.Fg, 
                font=self.Font, 
                bd=self.BorderWidth, 
                relief=self.Relief
            )
        elif Status == "single-liner":
            self.Entity = tk.Entry(
                self.Screen, 
                width=self.Width, 
                bg=self.Bg, 
                fg=self.Fg, 
                font=self.Font, 
                bd=self.BorderWidth, 
                relief=self.Relief
            )
        else:
            raise ValueError("Status must be 'multi-liner' or 'single-liner'")

        self.Entity.place(x=self.X, y=self.Y)

    def SetText(self, Text: str):
        if isinstance(self.Entity, tk.Text):
            self.Entity.delete("1.0", tk.END)
            self.Entity.insert(tk.END, Text)
        elif isinstance(self.Entity, tk.Entry):
            self.Entity.delete(0, tk.END)
            self.Entity.insert(0, Text)

    def GetText(self) -> str:
        if isinstance(self.Entity, tk.Text):
            return self.Entity.get("1.0", tk.END).strip()
        elif isinstance(self.Entity, tk.Entry):
            return self.Entity.get().strip()

    def Clear(self):
        if isinstance(self.Entity, tk.Text):
            self.Entity.delete("1.0", tk.END)
        elif isinstance(self.Entity, tk.Entry):
            self.Entity.delete(0, tk.END)

    def Configure(self, **kwargs):
        self.Entity.configure(**kwargs)

    def Move(self, X: int, Y: int):
        self.X, self.Y = X, Y
        self.Entity.place(x=self.X, y=self.Y)

    def BindEvent(self, Event: str, Callback):
        self.Entity.bind(Event, Callback)

    def SetAlignment(self, Align="left"):
        if isinstance(self.Entity, tk.Entry):
            self.Entity.configure(justify=Align)

# --- Sprite Class ---
class Sprite:
    def __init__(self, window: Window):
        window.root.update_idletasks()
        self.canvas: tk.Canvas = window.area
        self.sprite = None
        self.drawing = False
        self.pencolor = "black"
        self.draggable = False
        self.dragging = False
        self.offset_x = 0
        self.offset_y = 0
        self._drag_callback = None

    def Figure(self, x=100, y=100, l=8, h=4, shape="square",
               fillcolor="lime", outlinecolor="", outlinethickness=0):
        l *= 10; h *= 10
        def star_points(x, y, outer_r, inner_r, vertices):
            points = []
            angle_step = 360 / (vertices * 2)
            for i in range(vertices * 2):
                angle = math.radians(90 + i * angle_step)
                r = outer_r if i % 2 == 0 else inner_r
                px = x + r * math.cos(angle)
                py = y + r * math.sin(angle)
                points.extend([px, py])
            return points
        fcolor = Colors.get(fillcolor.lower(), fillcolor)
        olcolor = Colors.get(outlinecolor.lower(), outlinecolor)

        if outlinethickness == 0:
            olcolor = ""

        if shape == "square":
            points = [x, y, x+l, y, x+l, y+h, x, y+h]
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "equilateral-triangle":
            # Equilateral triangle pointing up
            points = [
                x + l/2, y,           # top
                x + l, y + h,         # bottom right
                x, y + h              # bottom left
            ]
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "right-triangle":
            # Right triangle (right angle at bottom left)
            points = [
                x, y,                 # top left
                x, y + h,             # bottom left
                x + l, y + h          # bottom right
            ]
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "circle":
            self.sprite = self.canvas.create_oval(
                x, y, x+l, y+h, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "paralellogram":
            points = [x,y, x+(l/2),y+(h/2), x,y+h, x-(l/2),y-(h/2)]
            self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "trapezium":
            points = [
                x, y,                 # top left
                x + l, y,             # top right
                x + int(0.75*l), y+h, # bottom right (shorter)
                x + int(0.25*l), y+h  # bottom left (shorter)
            ]
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        elif shape == "pentagon":
            points = []
            for i in range(5):
                angle = math.radians(90 + i * 72)
                px = x + l * math.cos(angle)
                py = y + h * math.sin(angle)
                points.extend([px, py])
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )

        elif shape == "hexagon":
            points = []
            for i in range(6):
                angle = math.radians(90 + i * 60)
                px = x + l * math.cos(angle)
                py = y + h * math.sin(angle)
                points.extend([px, py])
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )

        elif shape == "heptagon":
            points = []
            for i in range(7):
                angle = math.radians(90 + i * (360/7))
                px = x + l * math.cos(angle)
                py = y + h * math.sin(angle)
                points.extend([px, py])
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )

        elif shape == "octagon":
            points = []
            for i in range(8):
                angle = math.radians(90 + i * 45)
                px = x + l * math.cos(angle)
                py = y + h * math.sin(angle)
                points.extend([px, py])
            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )
        
        elif shape.startswith("stairs"):
            try:
                steps = int(shape.replace("stairs", ""))
            except:
                steps = 3

            step_w = l // steps
            step_h = h // steps

            points = [x, y+h]

            for i in range(steps):
                points.extend([x + i*step_w, y + (steps - i - 1)*step_h])
                points.extend([x + (i+1)*step_w, y + (steps - i - 1)*step_h])

            points.extend([x+l, y])
            points.extend([x+l, y+h])

            self.sprite = self.canvas.create_polygon(
                points, fill=fcolor, outline=olcolor, width=outlinethickness
            )

        elif shape == "star4":
            points = star_points(x, y, l, l/2, 4)
            self.sprite = self.canvas.create_polygon(points, fill=fcolor, outline=olcolor, width=outlinethickness)

        elif shape == "star5":
            points = star_points(x, y, l, l/2, 5)
            self.sprite = self.canvas.create_polygon(points, fill=fcolor, outline=olcolor, width=outlinethickness)

        elif shape == "star8":
            points = star_points(x, y, l, l/2, 8)
            self.sprite = self.canvas.create_polygon(points, fill=fcolor, outline=olcolor, width=outlinethickness)
        
        else:
            raise ValueError(f"Unknown shape: {shape}")
    
    def CreateShape(self, points, fill, outline, outlinethickness, x, y, l, h):
        scaled_points = []
        for px, py in points:
            sx = x + px * l
            sy = y + py * h
            scaled_points.append((sx, sy))

        flat_points = [coord for point in scaled_points for coord in point]

        self.sprite = self.canvas.create_polygon(
            flat_points,
            fill=Colors.get(str(fill).lower(), fill),
            outline=Colors.get(str(outline).lower(), outline),
            width=outlinethickness
        )

    def Resize(self, scale=1.0):
        if not self.sprite:
            return
        coords = self.canvas.coords(self.sprite)
        if not coords or len(coords) < 2:
            return
        # Find center of all points
        xs = coords[::2]
        ys = coords[1::2]
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)
        self.canvas.scale(self.sprite, cx, cy, scale, scale)

    def HeadsAt(self, side, angle, pivot="center"):
        coords = self.canvas.coords(self.sprite)
        points = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]

        xs = [p[0] for p in points]
        ys = [p[1] for p in points]

        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # Pivot logic
        if pivot == "left-end":
            cx, cy = points[0]   # literal first point
        elif pivot == "right-end":
            cx, cy = points[-1]  # literal last point
        elif pivot == "left":
            cx, cy = min_x, (min_y + max_y) / 2
        elif pivot == "right":
            cx, cy = max_x, (min_y + max_y) / 2
        else:  # "center"
            cx, cy = (min_x + max_x) / 2, (min_y + max_y) / 2

        # Adjust angle based on side
        if side == "left":
            angle = -angle

        rad = math.radians(angle)

        rotated = []
        for x, y in points:
            dx, dy = x - cx, y - cy
            rx = cx + dx * math.cos(rad) - dy * math.sin(rad)
            ry = cy + dx * math.sin(rad) + dy * math.cos(rad)
            rotated.extend([rx, ry])

        self.canvas.coords(self.sprite, *rotated)
    
    def Rotate(self, side, angle, pivot="center", steps=30, delay=8):
        increment = angle / steps
        if side == "left":
            increment = -increment

        def step(count=0):
            if count >= steps:
                return
            self.HeadsAt("right", increment, pivot)
            self.canvas.after(delay, lambda: step(count+1))

        step()

    def Teleport(self, x, y):
        if not self.sprite:
            return

        coords = self.canvas.coords(self.sprite)
        if coords:
            current_x, current_y = coords[0], coords[1]
            dx, dy = x - current_x, y - current_y

            # If drawing mode is active, leave a trail
            if getattr(self, "drawing", False):
                self.canvas.create_line(current_x, current_y, x, y, fill="black")

            # Move the sprite
            self.canvas.move(self.sprite, dx, dy)
    
    def Glide(self, direction, speed=5, steps=None):
        moved = {"pixels": 0}
        if speed <= 0:
            speed = 1

        dx = 0
        dy = 0
        if "e" in direction:
            dx += speed
        if "w" in direction:
            dx -= speed
        if "s" in direction:
            dy += speed
        if "n" in direction:
            dy -= speed

        def step():
            if not self.sprite:
                return

            # Current position before moving
            coords = self.canvas.coords(self.sprite)
            if coords:
                x1, y1 = coords[0], coords[1]  # take first point as reference
            else:
                x1, y1 = 0, 0

            # Move the sprite
            self.canvas.move(self.sprite, dx, dy)

            # New position after moving
            coords_new = self.canvas.coords(self.sprite)
            if coords_new:
                x2, y2 = coords_new[0], coords_new[1]
            else:
                x2, y2 = x1 + dx, y1 + dy

            # If drawing mode is active, leave a trail
            if getattr(self, "drawing", False):
                self.canvas.create_line(x1, y1, x2, y2, fill=Colors.get("black", "black"))

            moved["pixels"] += abs(dx) + abs(dy)
            if steps is None or moved["pixels"] < steps:
                self.canvas.after(17, step)

        step()
    
    def Jump(self, view="front", key="<space>", jumpHeight=100, bounciness="mid"):
        def do_jump(event=None):
                # Physics parameters
                initial_velocity = jumpHeight / 10  # Initial upward velocity
                gravity = 0.5  # Gravity constant
                bounce_dampening = {"low": 0.3, "mid": 0.5, "high": 0.7}
                dampen = bounce_dampening.get(bounciness, 0.5)
                
                # Get current position
                coords = self.canvas.coords(self.sprite)
                if not coords:
                    return
                
                # For shapes (polygons), take the first point as reference
                start_y = coords[1]
                
                # Animation state
                state = {
                    "velocity": initial_velocity,
                    "position_y": 0,  # Relative position from start
                    "ground_y": 0,
                    "bounces": 0,
                    "max_bounces": {"low": 1, "mid": 2, "high": 3}[bounciness]
                }
                
                def animate_bounce():
                    # Update velocity with gravity
                    state["velocity"] -= gravity
                    state["position_y"] -= state["velocity"]
                    
                    # Check if hit ground
                    if state["position_y"] >= state["ground_y"]:
                        # Snap to ground
                        dy = state["ground_y"] - state["position_y"]
                        self.canvas.move(self.sprite, 0, dy)
                        state["position_y"] = state["ground_y"]
                        
                        # Bounce back up
                        if state["bounces"] < state["max_bounces"] and abs(state["velocity"]) > 1:
                            state["velocity"] = abs(state["velocity"]) * dampen
                            state["bounces"] += 1
                            self.canvas.after(16, animate_bounce)  # ~60 FPS
                        else:
                            # Stop bouncing - ensure we're exactly at ground
                            state["velocity"] = 0
                    else:
                        # Move sprite by velocity
                        self.canvas.move(self.sprite, 0, -state["velocity"])
                        # Continue animation
                        self.canvas.after(16, animate_bounce)  # ~60 FPS
                
                # Start the animation
                animate_bounce()
                        
        self.canvas.bind_all(key, do_jump)

    def Fly(self, view="front", key="<space>", speed=4, bounciness="mid", flyHeight=40):
        def start_fly(event=None):
            if view == "front":
                self.Glide(direction="n", speed=speed, steps=flyHeight)
                if bounciness == "mid":
                    self.Glide(direction="s", speed=speed, steps=flyHeight//2)
                    self.Glide(direction="n", speed=speed, steps=flyHeight//2)
                elif bounciness == "high":
                    self.Glide(direction="s", speed=speed, steps=flyHeight//2)
                    self.Glide(direction="n", speed=speed, steps=flyHeight//2)
                    self.Glide(direction="s", speed=speed, steps=flyHeight//4)
                    self.Glide(direction="n", speed=speed, steps=flyHeight//4)
            elif view == "top":
                self.Resize(scale=1.2)

        def stop_fly(event=None):
            if view == "front":
                self.Glide(direction="s", speed=speed, steps=flyHeight)
            elif view == "top":
                self.Resize(scale=1.0)

        self.canvas.bind_all(key, start_fly)
        key_name = key[1:-1] if key.startswith('<') and key.endswith('>') else key
        self.canvas.bind_all(f"<KeyRelease-{key_name}>", stop_fly)
    
    def Pendown(self):
        self.drawing = True
    def Penup(self):
        self.drawing = False
    
    def Circle(self, radius, amount=360, speed=5):
        if not self.sprite:
            return

        coords = self.canvas.coords(self.sprite)
        if not coords or len(coords) < 2:
            return

        xs = coords[::2]
        ys = coords[1::2]
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)

        steps = amount
        angle_step = 2 * math.pi / steps

        prev_x, prev_y = None, None

        delay = max(1, int(50 / speed))

        def step(i=0):
            nonlocal prev_x, prev_y
            if i > steps:
                return

            angle = i * angle_step
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)

            # Move the shape by the offset from its current center to the new (x, y)
            current_coords = self.canvas.coords(self.sprite)
            if not current_coords or len(current_coords) < 2:
                return
            xs = current_coords[::2]
            ys = current_coords[1::2]
            curr_cx = sum(xs) / len(xs)
            curr_cy = sum(ys) / len(ys)
            dx = x - curr_cx
            dy = y - curr_cy
            self.canvas.move(self.sprite, dx, dy)

            if getattr(self, "drawing", False):
                if prev_x is not None and prev_y is not None:
                    self.canvas.create_line(prev_x, prev_y, x, y, fill=Colors.get("black", "black"))
                prev_x, prev_y = x, y

            self.canvas.after(delay, lambda: step(i + 1))

        step()
    
    def CollidesWith(self, other):
        if not self.sprite or not other.sprite:
            return False
        coords1 = self.canvas.bbox(self.sprite)
        coords2 = self.canvas.bbox(other.sprite)
        if not coords1 or not coords2:
            return False
        x1_min, y1_min, x1_max, y1_max = coords1
        x2_min, y2_min, x2_max, y2_max = coords2
        return not (x1_max < x2_min or x1_min > x2_max or y1_max < y2_min or y1_min > y2_max)

    def ImageSprite(self, imgPath, x=50, y=50, anchor="nw", sizex=None, sizey=None):
        ext = os.path.splitext(imgPath)[1].lower()
        if ext != ".svg":
            raise ValueError("Only SVG images are supported for ImageSprite.")
        import cairosvg
        base_name = os.path.splitext(imgPath)[0]
        size_tag = f"_{sizex or 'orig'}x{sizey or 'orig'}"
        cache_path = base_name + size_tag + "_sprite.png"
        if not os.path.exists(cache_path):
            cairosvg.svg2png(
                url=imgPath,
                write_to=cache_path,
                output_width=sizex if sizex else None,
                output_height=sizey if sizey else None
            )
        pil_img = Image.open(cache_path)
        self.image = Imagetk.PhotoImage(pil_img)
        self.sprite = self.canvas.create_image(x, y, image=self.image, anchor=anchor)
    
    def IsClicked(self, func):
        if self.sprite:
            self.canvas.tag_bind(self.sprite, "<Button-1>", func)
    
    def SetDraggable(self, boolean: bool):
        self.draggable = boolean
        if boolean:
            self.canvas.tag_bind(self.sprite, "<ButtonPress-1>", self._on_click)
            self.canvas.tag_bind(self.sprite, "<B1-Motion>", self._on_drag)
            self.canvas.tag_bind(self.sprite, "<ButtonRelease-1>", self._on_release)
        else:
            self.canvas.tag_unbind(self.sprite, "<ButtonPress-1>")
            self.canvas.tag_unbind(self.sprite, "<B1-Motion>")
            self.canvas.tag_unbind(self.sprite, "<ButtonRelease-1>")

    def WhenDraggedTo(self, callback):
        """Register a callback function to run whenever the sprite is dragged.
        The callback must accept (x, y, event)."""
        self._drag_callback = callback

    def _on_click(self, event):
        if self.draggable:
            self.dragging = True
            coords = self.canvas.coords(self.sprite)
            self.offset_x = event.x - coords[0]
            self.offset_y = event.y - coords[1]

    def _on_drag(self, event):
        if self.dragging and self.draggable:
            coords = self.canvas.coords(self.sprite)
            width = coords[2] - coords[0]
            height = coords[3] - coords[1]
            x1 = event.x - self.offset_x
            y1 = event.y - self.offset_y
            self.canvas.coords(self.sprite, x1, y1, x1+width, y1+height)

            if self._drag_callback:
                self._drag_callback(x1, y1, event)

    def _on_release(self, event):
        self.dragging = False

__all__ = ["Window", "Sprite", "Score", "StopWatch", "Label", "TextBox"]
Window = Window
Sprite = Sprite
Score = Score
StopWatch = StopWatch
Label = Label
TextBox = TextBox
