import math  # Импортируем модуль math для математических операций
import gif_pygame  # Импортируем модуль gif_pygame для работы с GIF-анимациями
import ctypes
import os  # Импортируем модуль os для работы с операционной системой
import pygame


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
WIDTH = user32.GetSystemMetrics(0)  # Находим ширину экрана по горизонтали и сохраняем в переменной WIDTH
HEIGHT = user32.GetSystemMetrics(1)

# MATH
PENTA_HEIGHT = 3 * HEIGHT  # Вычисляем высоту игрового мира (в 5 раз больше высоты экрана)
HALF_WIDTH = WIDTH // 2  # Вычисляем центр экрана по горизонтали
HALF_HEIGHT = HEIGHT // 2  # Вычисляем центр экрана по вертикали
TILE = 100  # Размер одного тайла (квадрата) в игровом мире

# ray casting
FOV = 1  # Угол обзора (в радианах)
HALF_FOV = FOV / 2  # Половина угла обзора
MAX_LINE = 100  # Максимальная дальность луча

# player
player_pos = (2850, 450)  # Начальная позиция игрока
speed = 2  # Скорость игрока
speed_angle = 0.04  # Скорость поворота
player_angle = 4.73  # Начальный угол поворота игрока
FPS = 60  # Максимальный FPS (влияет на скорость игры)

# sprite
pi = math.pi  # Число пи
DUBLE_PI = pi * 2  # Двойное число пи
FAKE_RAY = 100  # Количество "фейковых" лучей для обработки спрайтов по краям экрана
DUBLE_HEIGHT = 2 * HEIGHT  # Двойная высота экрана

# RGB
WHITE = (255, 255, 255)  # Белый цвет
BLACK = (0, 0, 0)  # Черный цвет
RED = (255, 0, 0)  # Красный цвет
GREEN = (0, 255, 0)  # Зеленый цвет
BLUE = (0, 0, 255)  # Синий цвет
BETON = (50, 50, 50)  # Цвет пола
YELLOW = (234, 255, 0)  # Желтый цвет
ORANGE = (255, 160, 0)  # Ораньжевый цвет

# settings textures
TEXTURE_WIGHT = 1200  # Ширина текстуры
TEXTURE_HEIGHT = 1200  # Высота текстуры
TEXTURE_SCALE = TEXTURE_WIGHT // TILE  # Масштаб текстуры
HALF_TEXTURE_HEIGHT = TEXTURE_HEIGHT // 2  # Половина высоты текстуры

# textures/img
glitch = os.path.abspath('img/textures/sprite/monstor/monstor.png')  # Путь к изображению спрайта монстра
stena = os.path.abspath('img/textures/environment/wall.jpg')  # Путь к изображению текстуры стены
endurance_point = os.path.abspath('img/textures/sprite/endurance_point/be178df8659744d2c07c3f23e07fa2c6qN8be18p0Ax1M4QQ-0.png')
point_anim = os.path.abspath('img/textures/sprite/endurance_point/animation')
trap = os.path.abspath('img/textures/sprite/monstor/trap/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-0.png')
trap_anim = os.path.abspath('img/textures/sprite/monstor/trap/animation')
wall_go = os.path.abspath('img/textures/environment/wall_go.jpg')  # Путь к изображению стены "идти"
wall_run = os.path.abspath('img/textures/environment/wall_run.jpg')  # Путь к изображению стены "бежать"
wall_escape = os.path.abspath('img/textures/environment/wall_escape.jpg')  # Путь к изображению стены "убегать"
wall_restart = os.path.abspath('img/textures/environment/wall_restart.jpg')  # Путь к изображению стены "перезапуск"
wall_interaction = os.path.abspath('img/textures/environment/wall_interaction.jpg')  # Путь к изображению стены "взаимодействие"
freedom = os.path.abspath('img/textures/environment/freedom.jpg')  # Путь к изображению стены "свобода"
wall_tg = os.path.abspath('img/textures/environment/wall_tg.jpg') # Путь к изображению рекламы тг
anim_glitch = os.path.abspath('img/textures/sprite/monstor/animation')  # Путь к папке с анимацией монстра
icon = os.path.abspath('img/icon/icon.png')  # Путь к изображению иконки
cover = os.path.abspath('img/textures/cover/cover.jpg')
return_t = os.path.abspath('img/textures/sprite/go/press_e_to_return.png')
restart = os.path.abspath('img/textures/sprite/go/press_e_to_restart.png')
exit_to_main_memu = os.path.abspath('img/textures/sprite/go/press_e_to_go_to_main_menu.png')
exit = os.path.abspath('img/textures/sprite/go/press_e_to_exit.png')
start = os.path.abspath('img/textures/sprite/go/press_e_to_start.png')  # Путь к изображению "нажмите E для старта"

# keys
key1s = os.path.abspath('img/textures/sprite/keys/key1/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-0.png')  # Путь к изображению ключа 1
key2s = os.path.abspath('img/textures/sprite/keys/key2/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-1.png')  # Путь к изображению ключа 2
key3s = os.path.abspath('img/textures/sprite/keys/key3/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-2.png')  # Путь к изображению ключа 3
key4s = os.path.abspath('img/textures/sprite/keys/key4/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-3.png')  # Путь к изображению ключа 4
key5s = os.path.abspath('img/textures/sprite/keys/key5/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-4.png')  # Путь к изображению ключа 5
key6s = os.path.abspath('img/textures/sprite/keys/key6/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-5.png')  # Путь к изображению ключа 6
key7s = os.path.abspath('img/textures/sprite/keys/key7/7fa9e8aa16f245b8caca8f4d09779c03lcC4ijOz6601J4Zj-6.png')  # Путь к изображению ключа 7
number_of_keys = 0  # Начальное количество собранных ключей

# dorrs
door1 = os.path.abspath('img/textures/sprite/doors/door1/animation/0-Picsart-BackgroundRemover.png')  # Путь к изображению двери 1
door1anim = os.path.abspath('img/textures/sprite/doors/door1/animation')  # Путь к папке с анимацией двери 1
door2 = os.path.abspath('img/textures/sprite/doors/door2/animation/0-Picsart-BackgroundRemover.png')  # Путь к изображению двери 2
door2anim = os.path.abspath('img/textures/sprite/doors/door2/animation/')  # Путь к папке с анимацией двери 2
door3 = os.path.abspath('img/textures/sprite/doors/door3/a1d04099c0c14ed2f3fa86a7aa4c0b42bjCIGDAmHELU2hRQ-2.png')  # Путь к изображению двери 3
door3anim = os.path.abspath('img/textures/sprite/doors/door3/animation')  # Путь к папке с анимацией двери 3
door4 = os.path.abspath('img/textures/sprite/doors/door4/animation/0.png')  # Путь к изображению двери 4
door4anim = os.path.abspath('img/textures/sprite/doors/door4/animation')  # Путь к папке с анимацией двери 4
door5 = os.path.abspath('img/textures/sprite/doors/door5/animation/0-Picsart-BackgroundRemover.png')  # Путь к изображению двери 5
door5anim = os.path.abspath('img/textures/sprite/doors/door5/animation')  # Путь к папке с анимацией двери 5
door6 = os.path.abspath('img/textures/sprite/doors/door6/animation/0-Picsart-BackgroundRemover.png')  # Путь к изображению двери 6
door6anim = os.path.abspath('img/textures/sprite/doors/door6/animation')  # Путь к папке с анимацией двери 6
door7 = os.path.abspath('img/textures/sprite/doors/door7/animation/0.png')  # Путь к изображению двери 7
door7anim = os.path.abspath('img/textures/sprite/doors/door7/animation')  # Путь к папке с анимацией двери 7

# win/loos/load/start
win = os.path.abspath('img/textures/win/win1.gif')  # Путь к GIF-анимации победы
gif_w = gif_pygame.load(win)  # Загрузка GIF-анимации победы
loos = os.path.abspath('img/textures/loos/loos.gif')  # Путь к GIF-анимации проигрыша
gif_l = gif_pygame.load(loos)  # Загрузка GIF-анимации проигрыша
load = os.path.abspath('img/textures/loading/load.gif')
gif_load = gif_pygame.load(load)
screen_saver = os.path.abspath('img/icon/gw.gif')
gif_sc_sv = gif_pygame.load(screen_saver)

# начальный экран
back_button = os.path.abspath('img/home_screen/buttons/in_settings/back/back.png')
back_button = pygame.image.load(back_button)
back_button = pygame.transform.scale(back_button, (70, 70))
back_button_pressed = os.path.abspath('img/home_screen/buttons/in_settings/back/back_pressed.png')
back_button_pressed = pygame.image.load(back_button_pressed)
back_button_pressed = pygame.transform.scale(back_button_pressed, (80, 80))
start_button = os.path.abspath('img/home_screen/buttons/in_main_menu/start/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-0.png')
start_button_pressed = os.path.abspath('img/home_screen/buttons/in_main_menu/start/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-1.png')
start_button = pygame.image.load(start_button)
start_button = pygame.transform.scale(start_button, (200, 100))
start_button_pressed = pygame.image.load(start_button_pressed)
start_button_pressed = pygame.transform.scale(start_button_pressed, (210, 110))
settings_button = os.path.abspath('img/home_screen/buttons/in_main_menu/settings/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-4.png')
settings_button_pressed = os.path.abspath('img/home_screen/buttons/in_main_menu/settings/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-5.png')
settings_button = pygame.image.load(settings_button)
settings_button = pygame.transform.scale(settings_button, (200, 100))
settings_button_pressed = pygame.image.load(settings_button_pressed)
settings_button_pressed = pygame.transform.scale(settings_button_pressed, (210, 110))
exit_button = os.path.abspath('img/home_screen/buttons/in_main_menu/exit/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-2.png')
exit_button_pressed = os.path.abspath('img/home_screen/buttons/in_main_menu/exit/6ffcf0643211454fe15d689322d738bb3PCW7Hhi4H0MivU5-3.png')
exit_button = pygame.image.load(exit_button)
exit_button = pygame.transform.scale(exit_button, (200, 100))
exit_button_pressed = pygame.image.load(exit_button_pressed)
exit_button_pressed = pygame.transform.scale(exit_button_pressed, (210, 110))
bg_start = os.path.abspath('img/home_screen/background/bg_start.gif')
gif_bg_start = gif_pygame.load(bg_start)
bg = os.path.abspath('img/home_screen/background/bg.gif')
gif_bg = gif_pygame.load(bg)
button_m = os.path.abspath('music/button/button.mp3')
button_click = os.path.abspath('music/button/button-click.mp3')
button_exit = os.path.abspath('music/button/exit.mp3')
button_gr_h_off = os.path.abspath('img/home_screen/buttons/in_settings/graphics/hard/6d00d3bb-1c9b-4470-bba9-28433ae821a9-0.png')
button_gr_h_off = pygame.image.load(button_gr_h_off)
button_gr_h_off = pygame.transform.scale(button_gr_h_off, (200, 100))
button_gr_h_on = os.path.abspath('img/home_screen/buttons/in_settings/graphics/hard/6d00d3bb-1c9b-4470-bba9-28433ae821a9-1.png')
button_gr_h_on = pygame.image.load(button_gr_h_on)
button_gr_h_on = pygame.transform.scale(button_gr_h_on , (200, 100))
button_gr_n_off = os.path.abspath('img/home_screen/buttons/in_settings/graphics/normal/6d00d3bb-1c9b-4470-bba9-28433ae821a9-2.png')
button_gr_n_off = pygame.image.load(button_gr_n_off)
button_gr_n_off = pygame.transform.scale(button_gr_n_off, (200, 100))
button_gr_n_on = os.path.abspath('img/home_screen/buttons/in_settings/graphics/normal/6d00d3bb-1c9b-4470-bba9-28433ae821a9-3.png')
button_gr_n_on = pygame.image.load(button_gr_n_on)
button_gr_n_on = pygame.transform.scale(button_gr_n_on , (200, 100))
button_gr_l_off = os.path.abspath('img/home_screen/buttons/in_settings/graphics/low/6d00d3bb-1c9b-4470-bba9-28433ae821a9-4.png')
button_gr_l_off = pygame.image.load(button_gr_l_off)
button_gr_l_off = pygame.transform.scale(button_gr_l_off, (200, 100))
button_gr_l_on = os.path.abspath('img/home_screen/buttons/in_settings/graphics/low/6d00d3bb-1c9b-4470-bba9-28433ae821a9-5.png')
button_gr_l_on = pygame.image.load(button_gr_l_on)
button_gr_l_on = pygame.transform.scale(button_gr_l_on , (200, 100))
button_exit_main_menu = os.path.abspath('img/home_screen/buttons/in_settings/exit_to_main_menu/exit_to_main_menu.png')
button_exit_main_menu = pygame.image.load(button_exit_main_menu)
button_exit_main_menu = pygame.transform.scale(button_exit_main_menu, (200, 120))
button_exit_main_menu_pressed = os.path.abspath('img/home_screen/buttons/in_settings/exit_to_main_menu/exit_to_main_menu_pressed.png')
button_exit_main_menu_pressed = pygame.image.load(button_exit_main_menu_pressed)
button_exit_main_menu_pressed = pygame.transform.scale(button_exit_main_menu_pressed, (210, 130))
button_apply_yes = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/apply/apply_yes.png')
button_apply_yes = pygame.image.load(button_apply_yes)
button_apply_yes = pygame.transform.scale(button_apply_yes, (200, 100))
button_apply_pressed = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/apply/apply_pressed.png')
button_apply_pressed = pygame.image.load(button_apply_pressed)
button_apply_pressed = pygame.transform.scale(button_apply_pressed, (200, 100))
button_apply_no = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/apply/apply_no.png')
button_apply_no = pygame.image.load(button_apply_no)
button_apply_no = pygame.transform.scale(button_apply_no, (200, 100))
button_remove_yes = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/remove/remove_yes.png')
button_remove_yes = pygame.image.load(button_remove_yes)
button_remove_yes = pygame.transform.scale(button_remove_yes, (200, 100))
button_remove_pressed = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/remove/remove_pressed.png')
button_remove_pressed = pygame.image.load(button_remove_pressed)
button_remove_pressed = pygame.transform.scale(button_remove_pressed, (200, 100))
button_remove_no = os.path.abspath('img/home_screen/buttons/in_settings/apply_or_remove/remove/remove_no.png')
button_remove_no = pygame.image.load(button_remove_no)
button_remove_no = pygame.transform.scale(button_remove_no, (200, 100))


# music
shagi = os.path.abspath('music/player/shagi.mp3')  # Путь к музыкальному файлу шагов игрока
glitch_speech_start = os.path.abspath("music/sprite/glich/glitch's_speech.mp3")  # Путь к музыкальному файлу речи глюка (начало)
glitch_speech = os.path.abspath("music/sprite/glich/glitch's_speech_next.mp3")  # Путь к музыкальному файлу речи глюка (продолжение)
environment = os.path.abspath('music/environment/environment.mp3')  # Путь к музыкальному файлу окружения
die = os.path.abspath('music/player/die.mp3')  # Путь к музыкальному файлу смерти игрока
win_m = os.path.abspath('music/player/win_m.mp3') # Путь к музыкальному файлу победы игрока
take_the_key = os.path.abspath('music/player/take_the_key.mp3')
open_door = os.path.abspath('music/sprite/doors/open_door.mp3')
close_door = os.path.abspath('music/sprite/doors/closed_door.mp3')
trap_m = os.path.abspath('music/sprite/glich/trap.mp3')
start_m = os.path.abspath('music/start/extract-audio-online.com_1748184100_1_gwmp4-1748178894271-_JoTRQn6r.mp3')
home_screen_m = os.path.abspath('music/start/bg_music.mp3')

# complexity
easy = os.path.abspath('img/textures/sprite/complexity/70b296d87e7c450e9939201664800645ohUTjyMC7xT4g5Q2-1.png')  # Путь к изображению сложности "легко"
normal = os.path.abspath('img/textures/sprite/complexity/70b296d87e7c450e9939201664800645ohUTjyMC7xT4g5Q2-0.png')  # Путь к изображению сложности "нормально"
hard = os.path.abspath('img/textures/sprite/complexity/70b296d87e7c450e9939201664800645ohUTjyMC7xT4g5Q2-2.png')  # Путь к изображению сложности "сложно"