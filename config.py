key_binds_txt = """ 
s - set start point
n - new path point
c - change path point
m - move point(work only when point selected)
"""

APP_STATES = {
    0: "Режим: ничего",
    1: "Режим: установка стартовой точки",
    2: "Режим: установка путевой точки",
    3: "Режим: изменение точки пути"
}

CACHE_DIR = "static/cached"
