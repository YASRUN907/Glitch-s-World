from settings import *  # Импорт настроек из файла settings.py
from map import collision_walls, world_map  # Импорт данных о стенах для коллизий из map.py
import keyboard  # Импорт библиотеки keyboard для обработки нажатий клавиш (не Pygame)
import random

pygame.mixer.init()  # Инициализация микшера Pygame для работы со звуком

walk_sound = pygame.mixer.Sound(shagi)  # Загрузка звукового файла шагов из переменной shagi (предположительно, путь к файлу)
walk_sound.set_volume(0.5)  # Установка громкости звука шагов на 50%

class Player:  # Определение класса Player
    def __init__(self, sprites):  # Конструктор класса, принимает спрайты объектов на карте
        self.speed = speed  # Скорость движения игрока (берется из файла settings.py)
        self.speed_angle = speed_angle  # Скорость поворота игрока (берется из файла settings.py)
        self.sprites = sprites  # Спрайты объектов на карте (передаются при создании экземпляра класса)
        self.speed_run = 2.5  # Скорость бега игрока
        self.x, self.y = player_pos  # Начальная позиция игрока (x, y) (берется из файла settings.py)
        self.angle = player_angle  # Начальный угол поворота игрока (берется из файла settings.py)
        self.RunGame = True  # Флаг, определяющий, продолжается ли игра
        self.sensivity = 0.0005  # Чувствительность мыши для поворота
        self.number_of_keys = 0  # Количество собранных ключей
        self.side = 25  # Размер стороны квадрата, представляющего игрока
        self.rect = pygame.Rect(player_pos, (self.side, self.side))  # Прямоугольник игрока для коллизий
        self.endurance = 100 #выносливость
        self.endurance_point = 0
        self.endurance_x = random.randint(250, 2250)
        self.endurance_y = random.randint(250, 2250)
        self.game = True #игра
        self.win = False #выйграл
        self.loos = False #проиграл
        self.run = False #бежит
        self.collision_sprite = [pygame.Rect(obj.pos, (obj.side, obj.side)) for obj in
                                    self.sprites.list_of_object if obj.blocked]  # Прямоугольники для коллизий из спрайтов
        self.collision_list = collision_walls + self.collision_sprite  # Объединение всех прямоугольников для коллизий
        self.Mouving = True #движется
        self.restarting = False #перезапуск
        self.nps_on = False #нпс вкл
        self.visible = False #видит
        self.music = 0
        self.start_e = False #легкий уровень
        self.start_n = False #средний уровень
        self.start_h = False #тяжелый уровень
        self.speed_multiplier = 300
        self.r_x = random.randint(850, 2000)
        self.r_y = random.randint(600, 1700)
        self.load = False
        self.point_pos = True
        self.trap1 = False
        self.trap2 = False
        self.trap3 = False
        self.trap4 = False
        self.trap5 = False
        self.in_traping = False
        self.spawn_trap = False
        self.in_end = False
        self.from_the_player = False
        self.traps = 0
        self.home = True
        self.maus_in_button_start = True
        self.maus_in_button_settings = True
        self.maus_in_button_exit = True
        self.maus_in_button_back = True
        self.maus_in_button_graphics = True
        self.in_settings = False
        self.graphics_h = False
        self.graphics_n = True
        self.graphics_l = False
        self.graphics_s = False
        self.graphics_multiplier = 3
        self.is_playing = False
        self.volume_multiplayer = 1

        # настройки отвечающие за графику
        self.NUM_RAYS = WIDTH // self.graphics_multiplier  # Количество лучей, используемых для рейкастинга (треть ширины экрана)
        self.DIST = self.NUM_RAYS / (2 * math.tan(HALF_FOV))  # Расстояние до проекционной плоскости
        self.PROJ_COEF = self.graphics_multiplier * self.DIST * TILE  # Проекционный коэффициент (размер стен)
        self.SCALE = WIDTH // self.NUM_RAYS  # Масштабирующий коэффициент
        self.DELTA_ANGLE = FOV / self.NUM_RAYS  # Угол между лучами
        self.FAKE_RAYS_RANGE = self.NUM_RAYS - 1 + 2 * FAKE_RAY  # Общий диапазон лучей с учетом фейковых
        self.CENTER_RAY = self.NUM_RAYS // 2 - 1  # Индекс центрального луча

        #music
        self.shagi_sound = pygame.mixer.Sound(shagi)  # Звук шагов игрока
        self.shagi_sound.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.environment_sound = pygame.mixer.Sound(environment)
        self.environment_sound.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.glich_start_sound = pygame.mixer.Sound(glitch_speech_start)
        self.glich_start_sound.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.glich_next_sound = pygame.mixer.Sound(glitch_speech)
        self.glich_next_sound.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.die = pygame.mixer.Sound(die)
        self.die.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.win_m = pygame.mixer.Sound(win_m)
        self.take_the_key = pygame.mixer.Sound(take_the_key)
        self.take_the_key.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.take_the_key.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.open_door = pygame.mixer.Sound(open_door)
        self.open_door.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.close_door = pygame.mixer.Sound(close_door)
        self.close_door.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.trap_m = pygame.mixer.Sound(trap_m)
        self.start_m = pygame.mixer.Sound(start_m)
        self.start_m.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_m = pygame.mixer.Sound(button_m)
        self.button_m.set_volume(1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_click = pygame.mixer.Sound(button_click)
        self.button_click.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_exit = pygame.mixer.Sound(button_exit)
        self.button_exit.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.home_screen_m = pygame.mixer.Sound(home_screen_m)
        self.home_screen_m.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)

    def music_settings(self):
        self.shagi_sound = pygame.mixer.Sound(shagi)  # Звук шагов игрока
        self.shagi_sound.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.environment_sound = pygame.mixer.Sound(environment)
        self.environment_sound.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.glich_start_sound = pygame.mixer.Sound(glitch_speech_start)
        self.glich_start_sound.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.glich_next_sound = pygame.mixer.Sound(glitch_speech)
        self.glich_next_sound.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.die = pygame.mixer.Sound(die)
        self.die.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.win_m = pygame.mixer.Sound(win_m)
        self.take_the_key = pygame.mixer.Sound(take_the_key)
        self.take_the_key.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.take_the_key.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.open_door = pygame.mixer.Sound(open_door)
        self.open_door.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.close_door = pygame.mixer.Sound(close_door)
        self.close_door.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.trap_m = pygame.mixer.Sound(trap_m)
        self.start_m = pygame.mixer.Sound(start_m)
        self.start_m.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_m = pygame.mixer.Sound(button_m)
        self.button_m.set_volume(1 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_click = pygame.mixer.Sound(button_click)
        self.button_click.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.button_exit = pygame.mixer.Sound(button_exit)
        self.button_exit.set_volume(0.5 * math.floor(self.volume_multiplayer * 100) / 100)
        self.home_screen_m = pygame.mixer.Sound(home_screen_m)
        self.home_screen_m.set_volume(0.1 * math.floor(self.volume_multiplayer * 100) / 100)

    @property
    def pos(self):  # Декоратор property: позволяет обращаться к методу как к атрибуту
        return (self.x, self.y)  # Возвращает текущую позицию игрока (x, y)

    def detected_collision(self, dx, dy):  # Метод для обнаружения столкновений
        # Обнаружение столкновений при движении на dx и dy
        next_rect = self.rect.copy()  # Создаем копию прямоугольника игрока для проверки столкновений
        next_rect.move_ip(dx, dy)  # Перемещаем копию прямоугольника на dx и dy
        hit_indexes = next_rect.collidelistall(self.collision_list)  # Получаем индексы всех прямоугольников, с которыми столкнулась копия

        if len(hit_indexes):  # Если есть столкновения
            delta_x, delta_y = 0, 0  # Инициализируем переменные для хранения смещений
            for hit_index in hit_indexes:  # Перебираем все индексы столкновений
                hit_rect = self.collision_list[hit_index]  # Получаем прямоугольник, с которым произошло столкновение
                if dx > 0:  # Если движение по X положительное (вправо)
                    delta_x += next_rect.right - hit_rect.left  # Вычисляем величину перекрытия по X
                else:  # Если движение по X отрицательное (влево)
                    delta_x += hit_rect.right - next_rect.left  # Вычисляем величину перекрытия по X
                if dy > 0:  # Если движение по Y положительное (вниз)
                    delta_y += next_rect.bottom - hit_rect.top  # Вычисляем величину перекрытия по Y
                else:  # Если движение по Y отрицательное (вверх)
                    delta_y += hit_rect.bottom - next_rect.top  # Вычисляем величину перекрытия по Y

            if abs(delta_x - delta_y) < 10:  # Если разница между перекрытиями по X и Y небольшая
                dx, dy = 0, 0  # Останавливаем движение по обеим осям
            elif delta_x > delta_y:  # Если перекрытие по X больше перекрытия по Y
                dy = 0  # Останавливаем движение по Y
            elif delta_y > delta_x:  # Если перекрытие по Y больше перекрытия по X
                dx = 0  # Останавливаем движение по X
        self.x += dx  # Обновляем позицию игрока по X
        self.y += dy  # Обновляем позицию игрока по Y\

    def mouvement(self):  # Метод для обработки движения игрока
        self.keys_control()  # Обработка нажатий клавиш
        self.moues_control()  # Обработка движения мыши
        self.rect.center = self.x, self.y  # Обновление позиции прямоугольника игрока
        self.angle %= DUBLE_PI  # Нормализация угла поворота (от 0 до 2*PI)

    def keys_control(self):  # Метод для обработки нажатий клавиш
        sin_a = math.sin(self.angle)  # Синус угла поворота
        cos_a = math.cos(self.angle)  # Косинус угла поворота
        keys = pygame.key.get_pressed()  # Получение информации о нажатых клавишах
        self.moving = False  # Флаг движения

        # Обработка движения
        if keys[pygame.K_d]:  # Если нажата клавиша 'D' (вправо)
            self.moving = True  # Устанавливаем флаг движения
            dx = -self.speed * sin_a  # Вычисляем смещение по X (вправо)
            dy = self.speed * cos_a  # Вычисляем смещение по Y (вниз)
            self.detected_collision(dx, dy) #проверка коллизии
        if keys[pygame.K_a]:  # Если нажата клавиша 'A' (влево)
            self.moving = True
            dx = self.speed * sin_a  # Вычисляем смещение по X (влево)
            dy = -self.speed * cos_a  # Вычисляем смещение по Y (вверх)
            self.detected_collision(dx, dy) #проверка коллизии
        if keys[pygame.K_w] or keys[pygame.K_UP]:  # Если нажата клавиша 'W' или стрелка вверх (вперед)
            self.moving = True
            dx = self.speed * cos_a  # Вычисляем смещение по X (вперед)
            dy = self.speed * sin_a  # Вычисляем смещение по Y (вперед)
            self.detected_collision(dx, dy) #проверка коллизии
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  # Если нажата клавиша 'S' или стрелка вниз (назад)
            self.moving = True
            dx = -self.speed * cos_a  # Вычисляем смещение по X (назад)
            dy = -self.speed * sin_a  # Вычисляем смещение по Y (назад)
            self.detected_collision(dx, dy) #проверка коллизии

        if keys[pygame.K_LEFT]:  # Если нажата клавиша стрелка влево (поворот влево)
            self.angle -= self.speed_angle  # Уменьшаем угол поворота
        if keys[pygame.K_RIGHT]:  # Если нажата клавиша стрелка вправо (поворот вправо)
            self.angle += self.speed_angle  # Увеличиваем угол поворота

        if keys[pygame.K_a] and keys[pygame.K_d]:  # Если нажаты клавиши 'A' и 'D' одновременно
            self.moving = False  # Отключаем движение
        if keys[pygame.K_w] and keys[pygame.K_s]:  # Если нажаты клавиши 'W' и 'S' одновременно
            self.moving = False  # Отключаем движение

        if self.start_e and self.endurance <= -1: # Если начался легкий уровень и выносливость закончилась
            self.endurance = 300 #устанавливаем выносливость
            self.speed_multiplier = 60 #скорость

        if self.start_n and self.endurance <= -1: # Если начался средний уровень и выносливость закончилась
            self.endurance = 200 #устанавливаем выносливость
            self.speed_multiplier = 80 #скорость

        if self.start_h and self.endurance <= -1: # Если начался тяжелый уровень и выносливость закончилась
            self.endurance = 200 #устанавливаем выносливость
            self.speed_multiplier = 100 #скорость

        if not self.start_e and not self.start_n and not self.start_h: # Если уровни не начались
            self.endurance = -1 #выносливость

        if (self.endurance > 0 and (self.start_e or self.start_n or self.start_h)) or self.endurance == -1: # Если выносливость есть
            if (keys[pygame.K_w] or keys[pygame.K_UP]) and keys[
                pygame.K_c]:  # Если нажаты клавиши 'W'/'UP' и 'C'(ускорение)
                self.moving = True
                dx = self.speed_run * cos_a  # Вычисляем смещение по X (вперед)
                dy = self.speed_run * sin_a  # Вычисляем смещение по Y (вперед)
                self.detected_collision(dx, dy) #проверка коллизии
                self.endurance -= 1 #уменьшение выносливости
                self.run = True #бежит
        else:
            self.run = False #не бежит

        if self.endurance == 0: #выносливость закончилась
            self.run = False #не бежит

        # Управление звуками
        if self.moving:  # Если игрок двигается
            if not pygame.mixer.Channel(0).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(0).play(self.shagi_sound, loops=-1)  # Запускаем звук шагов в цикле
        else:  # Если игрок не двигается
            pygame.mixer.Channel(0).stop()  # Останавливаем звук шагов

        # Фоновый звук
        if not pygame.mixer.Channel(1).get_busy():  # Если фоновый звук не проигрывается
            pygame.mixer.Channel(1).play(self.environment_sound, loops=-1)  # Запускаем фоновый звук в цикле

    def moues_control(self):  # Метод для обработки движения мыши
        if pygame.mouse.get_focused():  # Если окно игры в фокусе
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH  # Вычисляем разницу между текущей позицией мыши и центром экрана
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))  # Устанавливаем позицию мыши в центр экрана
            self.angle += difference * math.floor(self.sensivity * 10000) / 10000  # Изменяем угол поворота игрока в зависимости от разницы и чувствительности

    def exit(self):  # Метод для выхода из игры
        if keyboard.is_pressed('esc'):  # Если нажат ESC
            self.in_settings = True
        if keyboard.is_pressed('r'):  # Если нажата R
            if self.start_e or self.start_n or self.start_h:
                self.angle = 0.0000001
                self.endurance = 0
                self.in_end = True
                self.loos = False
                self.game = True
                self.x = 2650
                self.y = 1750
        if not self.in_end and not (((self.x // TILE) * TILE, (self.y // TILE) * TILE) in world_map):
            self.c_x = self.x
            self.c_y = self.y
            self.c_angle = self.angle
            self.c_endurance = self.endurance
        if self.in_end:
            self.speed_multiplier = 0
        elif self.start_e:  # Если начался легкий уровень и выносливость закончилась
            self.speed_multiplier = 60  # скорость
        elif self.start_n:  # Если начался средний уровень и выносливость законwчилась
            self.speed_multiplier = 80  # скорость
        elif self.start_h:  # Если начался тяжелый уровень и выносливость закончилась
            self.speed_multiplier = 100  # скорость
        if ((self.x // TILE) * TILE, (self.y // TILE) * TILE) in world_map:
            self.x, self.y = self.c_x, self.c_y

    def restart_game(self):
        # Сброс всех параметров игры к начальному состоянию
        if self.start_e or self.start_n or self.start_h or self.in_end:
            for sprite in self.sprites.list_of_object:
                sprite.reset(self)
            self.r_x = random.randint(850, 2000)
            self.r_y = random.randint(600, 1700)
            self.x, self.y = 250, 250  # Возвращаем игрока в начальную позицию
            self.angle = 0.01  # Сбрасываем угол поворота
            if self.start_e:  # Если начался легкий уровень
                self.endurance = 300  # устанавливаем выносливость
                self.speed_multiplier = 60  # скорость
            if self.start_n:  # Если начался средний уровень
                self.endurance = 200  # устанавливаем выносливость
                self.speed_multiplier = 80  # скорость
            if self.start_h:  # Если начался тяжелый уровень
                self.endurance = 200  # устанавливаем выносливость
                self.speed_multiplier = 100  # скорость
            self.number_of_keys = 0  # Сброс количества ключей
            self.rect.center = self.x, self.y  # Обновляем позицию прямоугольника игрока
            self.point_pos = True
            self.trap1 = False
            self.trap2 = False
            self.trap3 = False
            self.trap4 = False
            self.trap5 = False
            self.in_traping = 100
            self.loos = False
            self.win = False
            self.game = True
            self.in_end = False
            # Останавливаем все звуки
            pygame.mixer.stop()

    def return_game(self):
        self.x = self.c_x
        self.y = self.c_y
        self.angle = self.c_angle
        self.endurance = self.c_endurance
        self.in_end = False

    def exit_to_main_menu(self):
        # Сброс всех параметров игры к начальному состоянию
        for sprite in self.sprites.list_of_object:
            sprite.reset(self)
        self.x, self.y = player_pos  # Возвращаем игрока в начальную позицию
        self.angle = player_angle  # Сбрасываем угол поворота
        self.game = True  # Игра запущена
        self.win = False  # Сброс победы
        self.loos = False  # Сброс проигрыша
        self.run = False  # Не бежит
        self.Mouving = True  # Движение включено
        self.restarting = False  # Перезапуск завершен
        self.nps_on = False  # NPC выключены
        self.visible = False  # Не видит
        self.music = 0  # Сброс музыки
        self.start_e = False  # Легкий уровень не начат
        self.start_n = False  # Средний уровень не начат
        self.start_h = False  # Тяжелый уровень не начат
        self.speed_multiplier = 300  # Сброс множителя скорости
        self.endurance = 100  # Сброс выносливости
        self.number_of_keys = 0 # Сброс количества ключей
        self.rect.center = self.x, self.y  # Обновляем позицию прямоугольника игрока
        self.endurance_x = random.randint(250, 2250)
        self.endurance_y = random.randint(250, 2250)
        self.r_x = random.randint(850, 2000)
        self.r_y = random.randint(600, 1700)
        self.point_pos = True
        self.trap1 = False
        self.trap2 = False
        self.trap3 = False
        self.trap4 = False
        self.trap5 = False
        self.in_traping = 100
        self.in_end = False
        # Останавливаем все звуки
        pygame.mixer.stop()

    def chens(self, world_map):
        self.ch = [2, 1, 1, 1, 1]
        self.result = random.choice(self.ch)
        if self.result == 2:
            self.spawn_trap = True
        elif self.result == 1:
            self.r_x = random.randint(850, 2000)
            self.r_y = random.randint(600, 1700)
            if (self.r_x, self.r_y) in world_map:
                self.r_x = random.randint(850, 2000)
                self.r_y = random.randint(600, 1700)