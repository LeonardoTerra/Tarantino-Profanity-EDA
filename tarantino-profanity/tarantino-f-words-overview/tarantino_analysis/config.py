from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
CSV_NAME = "19_Tarantino_Profanity_Deaths.csv"
LOCAL_CSV_PATH = APP_DIR / CSV_NAME

MOVIE_GENRE = {
    "Reservoir Dogs": "Crime",
    "Pulp Fiction": "Crime",
    "Kill Bill: Vol. 1": "Action",
    "Kill Bill: Vol. 2": "Action",
    "Inglorious Basterds": "War",
    "Django Unchained": "Western",
    "Jackie Brown": "Crime",
}

CURSOR_LIGHT = {
    "page": "#F8F8F8",
    "surface": "#FFFFFF",
    "header": "#F3F3F3",
    "row_alt": "#FAFAFA",
    "border": "#E5E5E5",
    "text": "#3B3B3B",
    "text_muted": "#616161",
    "grid": "#E5E5E5",
    "code_bg": "#F3F3F3",
    "bar_primary": "#8b7355",
    "bar_secondary": "#5c6b7a",
}

PAPER_CHART = {
    "background": CURSOR_LIGHT["page"],
    "text": CURSOR_LIGHT["text"],
    "tick": CURSOR_LIGHT["text_muted"],
    "grid": CURSOR_LIGHT["grid"],
    "spine": CURSOR_LIGHT["border"],
    "bar_primary": CURSOR_LIGHT["bar_primary"],
    "bar_secondary": CURSOR_LIGHT["bar_secondary"],
}
