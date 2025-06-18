from settings import *  # Импортируем все переменные и настройки из файла settings.py
import time  # Импортируем модуль time для работы со временем
import pygame  # Импортируем библиотеку Pygame
import math

def win(player, sc):
    if player.win:  # Проверяем, победил ли игрок
        player.game = False  # Останавливаем игровой процесс
        pygame.mixer.stop()  # Останавливаем все звуки
        sc.fill(BLACK)  # Заполняем экран черным цветом
        gif_pygame.transform.scale(gif_w, (WIDTH, HEIGHT))  # Масштабируем GIF-анимацию победы до размеров экрана
        start_time = time.time()  # Запоминаем время начала анимации
        animation_duration_w = 13  # Продолжительность анимации победы в секундах
        if not pygame.mixer.Channel(5).get_busy():  # Если канал 5 не занят воспроизведением звука
            pygame.mixer.Channel(5).play(player.win_m, loops=0)  # Проигрываем звук победы один раз
        while time.time() - start_time < animation_duration_w:  # Пока не истекло время анимации
            gif_w.render(sc, (0, 0))  # Отображаем текущий кадр GIF-анимации
            pygame.display.flip()  # Обновляем экран
        pygame.mixer.Channel(5).stop()  # Останавливаем звук победы
        player.x = 2650  # Возвращаем игрока на стартовую позицию
        player.y = 1850  # Возвращаем игрока на стартовую позицию
        player.angle = 0  # Обнуляем угол поворота игрока
        player.endurance = 0  # Восстанавливаем выносливость игрока
        player.in_end = True  # Устанавливаем флаг, что игрок находится в начальной локации
        player.loos = False  # Сбрасываем флаг проигрыша
        player.win = False  # Сбрасываем флаг проигрыша
        player.game = True  # Возобновляем игровой процесс

def loos(player, sc):
    if player.loos:  # Проверяем, проиграл ли игрок
        player.game = False  # Останавливаем игровой процесс
        pygame.mixer.stop()  # Останавливаем все звуки
        sc.fill(BLACK)  # Заполняем экран черным цветом
        gif_pygame.transform.scale(gif_l, (WIDTH, HEIGHT))  # Масштабируем GIF-анимацию проигрыша до размеров экрана
        start_time = time.time()  # Запоминаем время начала анимации
        animation_duration_l = 4.46  # Продолжительность анимации проигрыша в секундах

        if not pygame.mixer.Channel(4).get_busy():  # Если канал 4 не занят воспроизведением звука
            pygame.mixer.Channel(4).play(player.die, loops=0)  # Проигрываем звук смерти один раз
        while time.time() - start_time < animation_duration_l:  # Пока не истекло время анимации
            gif_l.render(sc, (0, 0))  # Отображаем текущий кадр GIF-анимации
            pygame.display.flip()  # Обновляем экран
        pygame.mixer.Channel(4).stop()  # Останавливаем звук смерти
        player.x = 2650  # Возвращаем игрока на стартовую позицию
        player.y = 1850  # Возвращаем игрока на стартовую позицию
        player.angle = 0  # Обнуляем угол поворота игрока
        player.endurance = 0  # Восстанавливаем выносливость игрока
        player.in_end = True  # Устанавливаем флаг, что игрок находится в начальной локации
        player.loos = False  # Сбрасываем флаг проигрыша
        player.game = True  # Возобновляем игровой процесс

def loading(sc, player):
    if player.load:  # Проверяем, нужно ли отображать экран загрузки
        pygame.mixer.stop()  # Останавливаем все звуки
        sc.fill(BLACK)  # Заполняем экран черным цветом
        gif_pygame.transform.scale(gif_load, (HEIGHT, HEIGHT))  # Масштабируем GIF-анимацию загрузки до размеров экрана
        start_time = time.time()  # Запоминаем время начала анимации
        animation_duration_w = 1  # Продолжительность анимации загрузки в секундах
        while time.time() - start_time < animation_duration_w:  # Пока не истекло время анимации
            gif_load.render(sc, (HALF_WIDTH - HALF_HEIGHT, 0))  # Отображаем текущий кадр GIF-анимации
            pygame.display.flip()  # Обновляем экран
        player.load = False  # Сбрасываем флаг загрузки
        player.win = False # Сбрасываем флаг победы

def start(sc, player):
    pygame.mixer.stop()
    pygame.mouse.set_visible(True)
    while player.home:  # Пока игрок находится в главном меню
        for event in pygame.event.get():  # Обрабатываем события, такие как нажатия клавиш, закрытие окна и т.д.
            if event.type == pygame.QUIT:  # Если игрок нажал на кнопку закрытия окна.
                player.RunGame = False  # Завершаем игровой цикл.
                player.home = False  # Выходим из главного меню

        if not pygame.mixer.Channel(14).get_busy():  # Если канал 14 не занят воспроизведением звука
            pygame.mixer.Channel(14).play(player.home_screen_m, loops=-1)

        maus_x = pygame.mouse.get_pos()[0]  # Получаем X координату мыши
        maus_y = pygame.mouse.get_pos()[1]  # Получаем Y координату мыши
        gif_bg.render(sc, (0, 0)) # Рендерим фон
        sc.blit(start_button, (HALF_WIDTH - 100, HALF_HEIGHT - 110)) # Отображаем кнопку старта
        sc.blit(settings_button, (HALF_WIDTH - 100, HALF_HEIGHT))  # Отображаем кнопку настроек
        sc.blit(exit_button, (HALF_WIDTH - 100, HALF_HEIGHT + 110))  # Отображаем кнопку выхода
        maus_key = pygame.mouse.get_pressed() # Получаем состояние кнопок мыши

        #button start
        if maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100: # Если мышь находится в области кнопки старта
            if player.maus_in_button_start: # Если мышь только что вошла в область кнопки
                pygame.mixer.Channel(10).play(player.button_m, loops=0) # Проигрываем звук кнопки
            player.maus_in_button_start = False # Устанавливаем флаг, что мышь находится в области кнопки
            start_button1 = pygame.transform.scale(start_button, (210, 110)) # Увеличиваем размер кнопки
            sc.blit(start_button1, (HALF_WIDTH - 105, HALF_HEIGHT - 115)) # Отображаем увеличенную кнопку
            if maus_key[0]: # Если нажата левая кнопка мыши
                sc.blit(start_button_pressed, (HALF_WIDTH - 105, HALF_HEIGHT - 115)) # Отображаем нажатую кнопку
                pygame.mouse.set_visible(False) # Скрываем курсор мыши
                player.home = False # Выходим из главного меню
                player.exit_to_main_menu() # Вызываем функцию выхода в главное меню
        else:
            player.maus_in_button_start = True # Сбрасываем флаг, что мышь находится в области кнопки
        #button exit
        if maus_y >= HALF_HEIGHT + 110 and maus_y <= HALF_HEIGHT + 210 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки выхода
            if player.maus_in_button_exit: # Если мышь только что вошла в область кнопки
                pygame.mixer.Channel(11).play(player.button_exit, loops=0) # Проигрываем звук кнопки
            player.maus_in_button_exit = False # Устанавливаем флаг, что мышь находится в области кнопки
            exit_button1 = pygame.transform.scale(exit_button, (210, 110)) # Увеличиваем размер кнопки
            sc.blit(exit_button1, (HALF_WIDTH - 105, HALF_HEIGHT + 105)) # Отображаем увеличенную кнопку
            if maus_key[0]: # Если нажата левая кнопка мыши
                sc.blit(exit_button_pressed, (HALF_WIDTH - 105, HALF_HEIGHT + 105)) # Отображаем нажатую кнопку
                player.RunGame = False # Завершаем игровой цикл
                player.home = False # Выходим из главного меню
        else:
            player.maus_in_button_exit = True  # Сбрасываем флаг, что мышь находится в области кнопки
        #button settings
        if maus_y >= HALF_HEIGHT and maus_y <= HALF_HEIGHT + 100 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100: # Если мышь находится в области кнопки настроек
            if player.maus_in_button_settings: # Если мышь только что вошла в область кнопки
                pygame.mixer.Channel(12).play(player.button_m, loops=0) # Проигрываем звук кнопки
            player.maus_in_button_settings = False # Устанавливаем флаг, что мышь находится в области кнопки
            settings_button1 = pygame.transform.scale(settings_button, (210, 110)) # Увеличиваем размер кнопки
            sc.blit(settings_button1, (HALF_WIDTH - 105, HALF_HEIGHT - 5)) # Отображаем увеличенную кнопку
            if maus_key[0]: # Если нажата левая кнопка мыши
                pygame.time.wait(150)
                player.in_settings = True # Открываем настройки
        else:
            player.maus_in_button_settings = True # Сбрасываем флаг, что мышь находится в области кнопки
        if player.in_settings: # Если открыты настройки
            settings(sc, player) # Вызываем функцию настроек
        pygame.display.flip() # Обновляем экран

def home_screen(sc, player):
    pygame.mouse.set_visible(False)  # Делаем курсор мыши невидимым.
    pygame.mixer.stop()  # Останавливаем все звуки
    sc.fill(BLACK)  # Заполняем экран черным цветом
    gif_pygame.transform.scale(gif_sc_sv, (HEIGHT, HEIGHT))  # Масштабируем GIF-анимацию заставки до размеров экрана
    start_time = time.time()  # Запоминаем время начала анимации
    animation_duration_w = 4  # Продолжительность анимации заставки в секундах
    gif_pygame.transform.scale(gif_bg_start, (WIDTH, HEIGHT))  # Масштабируем GIF-анимацию начального экрана до размеров экрана
    gif_pygame.transform.scale(gif_bg, (WIDTH, HEIGHT))  # Масштабируем GIF-анимацию фона до размеров экрана
    pygame.mouse.set_visible(True)  # Делаем курсор мыши видимым.
    if not pygame.mixer.Channel(9).get_busy():  # Если канал 9 не занят воспроизведением звука
        pygame.mixer.Channel(9).play(player.start_m, loops=0)  # Проигрываем звук заставки один раз
    while time.time() - start_time < animation_duration_w:  # Пока не истекло время анимации
        for event in pygame.event.get():  # Обрабатываем события, такие как нажатия клавиш, закрытие окна и т.д.
            if event.type == pygame.QUIT:  # Если игрок нажал на кнопку закрытия окна.
                player.RunGame = False  # Завершаем игровой цикл.
                player.home = False  # Выходим из главного меню
                player.in_settings = False  # Выходим из настроек
        gif_sc_sv.render(sc, (HALF_WIDTH - HALF_HEIGHT, 0))  # Отображаем текущий кадр GIF-анимации
        pygame.display.flip()  # Обновляем экран
    start_time = time.time()
    while time.time() - start_time < 3:  # Пока не истекло 3 секунды
        for event in pygame.event.get():  # Обрабатываем события, такие как нажатия клавиш, закрытие окна и т.д.
            if event.type == pygame.QUIT:  # Если игрок нажал на кнопку закрытия окна.
                player.RunGame = False  # Завершаем игровой цикл.
                player.home = False  # Выходим из главного меню
                player.in_settings = False  # Выходим из настроек
        gif_bg_start.render(sc, (0, 0))  # Отображаем текущий кадр GIF-анимации
        pygame.display.flip()  # Обновляем экран

def settings(sc, player):
    copy_volume = player.volume_multiplayer
    copy_sensitivity = player.sensivity
    copy_slider_sensitivity_x = 0
    copy_slider_volume_x = 0
    sens_pos_x = HALF_WIDTH - 95
    volume_pos_x = HALF_WIDTH + 85
    gif_pygame.transform.scale(gif_bg, (WIDTH, HEIGHT))  # Масштабируем GIF-анимацию фона до размеров экрана
    pygame.mouse.set_visible(True)  # Делаем курсор мыши видимым.
    while player.in_settings:  # Пока игрок находится в настройках
        for event in pygame.event.get():  # Обрабатываем события, такие как нажатия клавиш, закрытие окна и т.д.
            if event.type == pygame.QUIT:  # Если игрок нажал на кнопку закрытия окна.
                player.RunGame = False  # Завершаем игровой цикл.
                player.home = False  # Выходим из главного меню
                player.in_settings = False  # Выходим из настроек
        if not pygame.mixer.Channel(14).get_busy():  # Если канал 14 не занят воспроизведением звука
            pygame.mixer.Channel(14).play(player.home_screen_m, loops=-1)
        maus_x = pygame.mouse.get_pos()[0]  # Получаем X координату мыши
        maus_y = pygame.mouse.get_pos()[1]  # Получаем Y координату мыши
        maus_key = pygame.mouse.get_pressed() # Получаем состояние кнопок мыши
        gif_bg.render(sc, (0, 0))  # Рендерим фон
        sc.blit(back_button, (0, 0))  # Отображаем кнопку возврата

        #graphics settings
        if player.graphics_l:
            player.graphics_l = True
            player.graphics_n = False
            player.graphics_h = False
            sc.blit(button_gr_l_off, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            player.graphics_multiplier = 5
            player.NUM_RAYS = WIDTH // 5  # Количество лучей, используемых для рейкастинга (треть ширины экрана)
            player.DIST = player.NUM_RAYS / (2 * math.tan(HALF_FOV))  # Расстояние до проекционной плоскости
            player.PROJ_COEF = 5 * player.DIST * TILE  # Проекционный коэффициент (размер стен)
            player.SCALE = WIDTH // player.NUM_RAYS  # Масштабирующий коэффициент
            player.DELTA_ANGLE = FOV / player.NUM_RAYS  # Угол между лучами
            player.FAKE_RAYS_RANGE = player.NUM_RAYS - 1 + 2 * FAKE_RAY  # Общий диапазон лучей с учетом фейковых
            player.CENTER_RAY = player.NUM_RAYS // 2 - 1  # Индекс центрального луча
        if player.graphics_n:
            player.graphics_l = False
            player.graphics_n = True
            player.graphics_h = False
            sc.blit(button_gr_n_off, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            player.graphics_multiplier = 3
            player.NUM_RAYS = WIDTH // 3  # Количество лучей, используемых для рейкастинга (треть ширины экрана)
            player.DIST = player.NUM_RAYS / (2 * math.tan(HALF_FOV))  # Расстояние до проекционной плоскости
            player.PROJ_COEF = 3 * player.DIST * TILE  # Проекционный коэффициент (размер стен)
            player.SCALE = WIDTH // player.NUM_RAYS  # Масштабирующий коэффициент
            player.DELTA_ANGLE = FOV / player.NUM_RAYS  # Угол между лучами
            player.FAKE_RAYS_RANGE = player.NUM_RAYS - 1 + 2 * FAKE_RAY  # Общий диапазон лучей с учетом фейковых
            player.CENTER_RAY = player.NUM_RAYS // 2 - 1  # Индекс центрального луча
        if player.graphics_h:
            player.graphics_l = False
            player.graphics_n = False
            player.graphics_h = True
            sc.blit(button_gr_h_off, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            player.graphics_multiplier = 1
            player.NUM_RAYS = WIDTH // 1  # Количество лучей, используемых для рейкастинга (треть ширины экрана)
            player.DIST = player.NUM_RAYS / (2 * math.tan(HALF_FOV))  # Расстояние до проекционной плоскости
            player.PROJ_COEF = 1 * player.DIST * TILE  # Проекционный коэффициент (размер стен)
            player.SCALE = WIDTH // player.NUM_RAYS  # Масштабирующий коэффициент
            player.DELTA_ANGLE = FOV / player.NUM_RAYS  # Угол между лучами
            player.FAKE_RAYS_RANGE = player.NUM_RAYS - 1 + 2 * FAKE_RAY  # Общий диапазон лучей с учетом фейковых
            player.CENTER_RAY = player.NUM_RAYS // 2 - 1  # Индекс центрального луча
        if maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
            if player.maus_in_button_graphics: # Если мышь только что вошла в область кнопки
                pygame.mixer.Channel(13).play(player.button_m, loops=0) # Проигрываем звук кнопки
            player.maus_in_button_graphics = False
            if player.graphics_h:
                sc.blit(button_gr_h_on, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            if player.graphics_n:
                sc.blit(button_gr_n_on, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            if player.graphics_l:
                sc.blit(button_gr_l_on, (HALF_WIDTH - 100, HALF_HEIGHT - 110))
            if maus_key[0]:
                player.graphics_s = True
        else:
            player.maus_in_button_graphics = True
        if not(maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100): #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
            if not(maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310):
                if not(maus_y >= HALF_HEIGHT and maus_y <= HALF_HEIGHT + 100 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310):
                    if not(maus_y >= HALF_HEIGHT + 110 and maus_y <= HALF_HEIGHT + 210 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310):
                        if maus_key[0]:
                            player.graphics_s = False
        if player.graphics_s:
            if player.graphics_h:
                sc.blit(button_gr_h_on, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                sc.blit(button_gr_n_off, (HALF_WIDTH + 110, HALF_HEIGHT))
                sc.blit(button_gr_l_off, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                if maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_h_on, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                    if maus_key[0]:
                        player.graphics_h = True
                        player.graphics_n = False
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT and maus_y <= HALF_HEIGHT + 100 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_n_on, (HALF_WIDTH + 110, HALF_HEIGHT))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = True
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT + 110 and maus_y <= HALF_HEIGHT + 210 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_l_on, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = False
                        player.graphics_l = True
            if player.graphics_n:
                sc.blit(button_gr_h_off, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                sc.blit(button_gr_n_on, (HALF_WIDTH + 110, HALF_HEIGHT))
                sc.blit(button_gr_l_off, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                if maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_h_on, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                    if maus_key[0]:
                        player.graphics_h = True
                        player.graphics_n = False
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT and maus_y <= HALF_HEIGHT + 100 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_n_on, (HALF_WIDTH + 110, HALF_HEIGHT))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = True
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT + 110 and maus_y <= HALF_HEIGHT + 210 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_l_on, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = False
                        player.graphics_l = True
            if player.graphics_l:
                sc.blit(button_gr_h_off, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                sc.blit(button_gr_n_off, (HALF_WIDTH + 110, HALF_HEIGHT))
                sc.blit(button_gr_l_on, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                if maus_y >= HALF_HEIGHT - 110 and maus_y <= HALF_HEIGHT - 10 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_h_on, (HALF_WIDTH + 110, HALF_HEIGHT - 110))
                    if maus_key[0]:
                        player.graphics_h = True
                        player.graphics_n = False
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT and maus_y <= HALF_HEIGHT + 100 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_n_on, (HALF_WIDTH + 110, HALF_HEIGHT))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = True
                        player.graphics_l = False
                if maus_y >= HALF_HEIGHT + 110 and maus_y <= HALF_HEIGHT + 210 and maus_x >= HALF_WIDTH + 110 and maus_x <= HALF_WIDTH + 310: #and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:  # Если мышь находится в области кнопки грфики
                    sc.blit(button_gr_l_on, (HALF_WIDTH + 110, HALF_HEIGHT + 110))
                    if maus_key[0]:
                        player.graphics_h = False
                        player.graphics_n = False
                        player.graphics_l = True

        #sensivity settings
        font_sens0 = pygame.font.SysFont('sensivity', 42, bold=False)
        if not player.graphics_s:
            render_p_s_1 = font_sens0.render(str(math.floor(player.sensivity * 10000) / 10), True, WHITE)
            render_p_s_2 = font_sens0.render(str(math.floor(player.sensivity * 10000) / 10), True, BLACK)
            sc.blit(render_p_s_2, (HALF_WIDTH + 110, HALF_HEIGHT + 29))
            sc.blit(render_p_s_1, (HALF_WIDTH + 107, HALF_HEIGHT + 26))
        render = font_sens0.render("sensitivity", True, WHITE)
        render1 = font_sens0.render("sensitivity", True, BLACK)
        sc.blit(render1, (HALF_WIDTH - 240, HALF_HEIGHT + 29))
        sc.blit(render, (HALF_WIDTH - 237, HALF_HEIGHT + 26))
        if player.sensivity < 0.0001:
            player.sensivity = 0.0001
        if player.sensivity > 0.0100:
            player.sensivity = 0.0100
        pygame.draw.rect(sc, BLACK, (HALF_WIDTH - 100, HALF_HEIGHT, 200, 100))
        pygame.draw.rect(sc, RED, (sens_pos_x, HALF_HEIGHT + 5, 10, 90))
        if maus_y >= HALF_HEIGHT + 5 and maus_y <= HALF_HEIGHT + 95 and maus_x > HALF_WIDTH - 100 and maus_x < HALF_WIDTH + 100:
            if maus_key[0] != 0:
                sens_pos_x = copy_slider_sensitivity_x - 5
                if sens_pos_x < HALF_WIDTH - 95:
                    sens_pos_x = HALF_WIDTH - 95
                if sens_pos_x > HALF_WIDTH + 85:
                    sens_pos_x = HALF_WIDTH + 85
                difference = maus_x - copy_slider_sensitivity_x
                player.sensivity += math.floor(difference) / 10000
            copy_slider_sensitivity_x = maus_x
        #exit settings
        if maus_y >= 0 and maus_y <= 70 and maus_x >= 0 and maus_x <= 70:  # Если мышь находится в области кнопки возврата
            if player.maus_in_button_back: # Если мышь только что вошла в область кнопки
                pygame.mixer.Channel(13).play(player.button_m, loops=0) # Проигрываем звук кнопки
            player.maus_in_button_back = False # Устанавливаем флаг, что мышь находится в области кнопки
            back_button1 = pygame.transform.scale(back_button, (80, 80)) # Увеличиваем размер кнопки
            sc.blit(back_button1, (0, 0)) # Отображаем увеличенную кнопку
            if maus_key[0]: # Если нажата левая кнопка мыши
                player.in_settings = False # Закрываем настройки
                player.graphics_s = False
                player.volume_multiplayer = copy_volume
                player.sensivity = copy_sensitivity
        else:
            player.maus_in_button_back = True # Сбрасываем флаг, что мышь находится в области кнопки

        #exit main menu
        if player.is_playing:
            sc.blit(button_exit_main_menu, (HALF_WIDTH - 100, HEIGHT - 180))
            if maus_y >= HEIGHT - 180 and maus_y <= HEIGHT - 60 and maus_x >= HALF_WIDTH - 100 and maus_x <= HALF_WIDTH + 100:
                if player.maus_in_button_settings: # Если мышь только что вошла в область кнопки
                    pygame.mixer.Channel(13).play(player.button_m, loops=0) # Проигрываем звук кнопки
                player.maus_in_button_settings = False # Устанавливаем флаг, что мышь находится в области кнопки
                button_exit_main_menu1 = pygame.transform.scale(button_exit_main_menu, (210, 130)) # Увеличиваем размер кнопки
                sc.blit(button_exit_main_menu1, (HALF_WIDTH - 105, HEIGHT - 185)) # Отображаем увеличенную кнопку
                if maus_key[0]: # Если нажата левая кнопка мыши
                    sc.blit(button_exit_main_menu_pressed, (HALF_WIDTH - 105, HEIGHT - 185))
                    player.volume_multiplayer = copy_volume
                    player.sensivity = copy_sensitivity
                    pygame.time.wait(150)
                    player.in_settings = False # Закрываем настройки
                    player.graphics_s = False
                    player.home = True

        # volume settings
        font_sens0 = pygame.font.SysFont('volume', 42, bold=False)
        if not player.graphics_s:
            render_p_s_1 = font_sens0.render(str(math.floor(player.volume_multiplayer * 100)), True, WHITE)
            render_p_s_2 = font_sens0.render(str(math.floor(player.volume_multiplayer * 100)), True, BLACK)
            sc.blit(render_p_s_2, (HALF_WIDTH + 110, HALF_HEIGHT + 139))
            sc.blit(render_p_s_1, (HALF_WIDTH + 107, HALF_HEIGHT + 136))
        render = font_sens0.render("volume", True, WHITE)
        render1 = font_sens0.render("volume", True, BLACK)
        sc.blit(render1, (HALF_WIDTH - 240, HALF_HEIGHT + 139))
        sc.blit(render, (HALF_WIDTH - 237, HALF_HEIGHT + 136))
        if player.volume_multiplayer < 0:
            player.volume_multiplayer = 0
        if player.volume_multiplayer > 1:
            player.volume_multiplayer = 1
        pygame.draw.rect(sc, BLACK, (HALF_WIDTH - 100, HALF_HEIGHT + 110, 200, 100))
        pygame.draw.rect(sc, RED, (volume_pos_x, HALF_HEIGHT + 115, 10, 90))
        if maus_y >= HALF_HEIGHT + 115 and maus_y <= HALF_HEIGHT + 205 and maus_x > HALF_WIDTH - 100 and maus_x < HALF_WIDTH + 100:
            if maus_key[0] != 0:
                volume_pos_x = copy_slider_volume_x - 5
                if volume_pos_x < HALF_WIDTH - 95:
                    volume_pos_x = HALF_WIDTH - 95
                if volume_pos_x > HALF_WIDTH + 85:
                    volume_pos_x = HALF_WIDTH + 85
                difference_vol = maus_x - copy_slider_volume_x
                player.volume_multiplayer += math.floor(difference_vol) / 100
            copy_slider_volume_x = maus_x

        #apply
        sc.blit(button_apply_no, (WIDTH - 460, HEIGHT - 170))
        if player.volume_multiplayer != copy_volume or player.sensivity != copy_sensitivity:
            sc.blit(button_apply_yes, (WIDTH - 460, HEIGHT - 170))
            if maus_y >= HEIGHT - 170 and maus_y <= HEIGHT - 70 and maus_x >= WIDTH - 460 and maus_x <= WIDTH - 260:
                sc.blit(button_apply_pressed, (WIDTH - 460, HEIGHT - 170))
                if maus_key[0]:
                    copy_volume = player.volume_multiplayer
                    copy_sensitivity = player.sensivity
                    player.music_settings()
                    pygame.mixer.stop()

        #remove
        sc.blit(button_remove_no, (WIDTH - 250, HEIGHT - 170))
        if player.volume_multiplayer != copy_volume or player.sensivity != copy_sensitivity:
            sc.blit(button_remove_yes, (WIDTH - 250, HEIGHT - 170))
            if maus_y >= HEIGHT - 170 and maus_y <= HEIGHT - 70 and maus_x >= WIDTH - 250 and maus_x <= WIDTH - 50:
                sc.blit(button_remove_pressed, (WIDTH - 250, HEIGHT - 170))
                if maus_key[0]:
                    player.volume_multiplayer = copy_volume
                    player.sensivity = copy_sensitivity

        pygame.display.flip() # Обновляем экран