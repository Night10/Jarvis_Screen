import pygame


def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = [x.lower().replace(' ', '') for x in fonts]
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)


_cached_weather_fonts = {}


def get_weather_font(font_weather_icons, size):
    global _cached_weather_fonts
    key = str(font_weather_icons) + '|' + str(size)
    font = _cached_weather_fonts.get(key, None)
    if font is None:
        font = make_font(font_weather_icons, size)
        _cached_weather_fonts[key] = font
    return font

_cached_standard_fonts = {}


def get_standard_font(font_standard, size):
    global _cached_standard_fonts
    key = str(font_standard) + '|' + str(size)
    font = _cached_standard_fonts.get(key, None)
    if font is None:
        font = make_font(font_standard, size)
        _cached_standard_fonts[key] = font
    return font

_cached_weather_text = {}


def create_weather_text(text, fonts, size, color):
    global _cached_weather_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_weather_text.get(key, None)
    if image is None:
        font = get_weather_font(fonts, size)
        image = font.render(text, True, color)
        _cached_weather_text[key] = image
    return image

_cached_standard_text = {}


def create_standard_text(text, fonts, size, color):
    global _cached_standard_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_standard_text.get(key, None)
    if image is None:
        font = get_standard_font(fonts, size)
        image = font.render(text, True, color)
        _cached_standard_text[key] = image
    return image