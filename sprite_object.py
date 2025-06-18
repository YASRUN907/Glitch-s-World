from settings import *
from collections import deque
import keyboard
import random

class Sprite:
    def __init__(self):
        self.sprate_parameters = {
            'sprite_glitch': {
                'sprite': pygame.image.load(glitch).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 0.9,
                'animation': deque(
                    [pygame.image.load(anim_glitch + '/gh' + str(i) + '.png').convert_alpha() for i in range(1, 6)]),
                'animation_dist': 100000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': True,
                'speed_n': 2,
                'type': 'nps',
                'to_open': None,
                'attack_dist': 50,
                'used': False,
                'turn': None,
            },
            'glitch': {
                'sprite': pygame.image.load(glitch).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 0.9,
                'animation': deque(
                    [pygame.image.load(anim_glitch + '/gh' + str(i) + '.png').convert_alpha() for i in range(1, 6)]),
                'animation_dist': 100000,
                'animation_speed': 6,
                'blocked': False,
                'is_nps': False,
                'speed_n': 2,
                'type': 'scarecrow',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'start': {
                'sprite': pygame.image.load(start).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_s',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'return': {
                'sprite': pygame.image.load(return_t).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_ret',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'restart': {
                'sprite': pygame.image.load(restart).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_res',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'exit_m_m': {
                'sprite': pygame.image.load(exit_to_main_memu).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_exit_m_m',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'exit': {
                'sprite': pygame.image.load(exit).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_exit',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key1': {
                'sprite': pygame.image.load(key1s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key2': {
                'sprite': pygame.image.load(key2s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key3': {
                'sprite': pygame.image.load(key3s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key4': {
                'sprite': pygame.image.load(key4s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key5': {
                'sprite': pygame.image.load(key5s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key6': {
                'sprite': pygame.image.load(key6s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'key7': {
                'sprite': pygame.image.load(key7s).convert_alpha(),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.3,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'key',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': None,
            },
            'door1': {
                'sprite': pygame.image.load(door1).convert_alpha(),
                'viewing_angles': [pygame.image.load(door1anim + '/' + str(i) + '-Picsart-BackgroundRemover.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 1,
                'attack_dist': None,
                'used': False,
                'turn': False,
            },
            'door2': {
                'sprite': pygame.image.load(door2).convert_alpha(),
                'viewing_angles': [pygame.image.load(door2anim + '/' + str(i) + '-Picsart-BackgroundRemover.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 2,
                'attack_dist': None,
                'used': False,
                'turn': False,
            },
            'door3v': {
                'sprite': pygame.image.load(door3).convert_alpha(),
                'viewing_angles': [pygame.image.load(door3anim + '_v/' + str(i) + '-Picsart-BackgroundRemover.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 3,
                'attack_dist': None,
                'used': False,
                'turn': False,
            },
            'door3h': {
                'sprite': pygame.image.load(door3).convert_alpha(),
                'viewing_angles': [pygame.image.load(door3anim + '_h/' + str(i) + '.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 3,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'door4': {
                'sprite': pygame.image.load(door4).convert_alpha(),
                'viewing_angles': [pygame.image.load(door4anim + '/' + str(i) + '.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 4,
                'attack_dist': None,
                'used': False,
                'turn': False,
            },
            'door5': {
                'sprite': pygame.image.load(door5).convert_alpha(),
                'viewing_angles': [pygame.image.load(door5anim + '/' + str(i) + '-Picsart-BackgroundRemover.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 5,
                'attack_dist': None,
                'used': False,
                'turn': False,
            },
            'door6': {
                'sprite': pygame.image.load(door6).convert_alpha(),
                'viewing_angles': [pygame.image.load(door6anim + '/' + str(i) + '-Picsart-BackgroundRemover.png').convert_alpha()
                                   for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door',
                'to_open': 6,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'door7': {
                'sprite': pygame.image.load(door7).convert_alpha(),
                'viewing_angles': [pygame.image.load(door7anim + '/' + str(i) + '.png').convert_alpha()
                                    for i in range(12)],
                'shift': -0.1,
                'scale': 1.2,
                'animation': False,
                'animation_dist': 100,
                'animation_speed': 0,
                'blocked': True,
                'is_nps': False,
                'speed_n': 0,
                'type': 'door_ex',
                'to_open': 7,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'easy': {
                'sprite': pygame.image.load(easy).convert_alpha(),
                'viewing_angles': None,
                'shift': 0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 99,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_easy',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'normal': {
                'sprite': pygame.image.load(normal).convert_alpha(),
                'viewing_angles': None,
                'shift': 0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 99,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_normal',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'hard': {
                'sprite': pygame.image.load(hard).convert_alpha(),
                'viewing_angles': None,
                'shift': 0,
                'scale': 0.5,
                'animation': False,
                'animation_dist': 99,
                'animation_speed': 0,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'button_hard',
                'to_open': None,
                'attack_dist': None,
                'used': False,
                'turn': True,
            },
            'endurance_point': {
                'sprite': pygame.image.load(endurance_point),
                'viewing_angles': None,
                'shift': 0.8,
                'scale': 0.1,
                'animation': deque(
                    [pygame.image.load(point_anim + '/be178df8659744d2c07c3f23e07fa2c6qN8be18p0Ax1M4QQ-' + str(i) + '.png').convert_alpha() for i in range(0, 12)]),
                'animation_dist': 10000,
                'animation_speed': 2,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': 'point',
                'to_open': None,
                'attack_dist': 50,
                'used': False,
                'turn': None,
            },
            'trap1': {
                'sprite': pygame.image.load(trap),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(trap_anim + '/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-' + str(i) + '.png').convert_alpha() for i in range(0, 3)]),
                'animation_dist': 10000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': '1trap',
                'to_open': None,
                'attack_dist': 80,
                'used': False,
                'turn': None,
            },
            'trap2': {
                'sprite': pygame.image.load(trap),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(trap_anim + '/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-' + str(i) + '.png').convert_alpha() for i in range(0, 3)]),
                'animation_dist': 10000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': '2trap',
                'to_open': None,
                'attack_dist': 80,
                'used': False,
                'turn': None,
            },
            'trap3': {
                'sprite': pygame.image.load(trap),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(trap_anim + '/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-' + str(i) + '.png').convert_alpha() for i in range(0, 3)]),
                'animation_dist': 10000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': '3trap',
                'to_open': None,
                'attack_dist': 80,
                'used': False,
                'turn': None,
            },
            'trap4': {
                'sprite': pygame.image.load(trap),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(trap_anim + '/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-' + str(i) + '.png').convert_alpha() for i in range(0, 3)]),
                'animation_dist': 10000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': '4trap',
                'to_open': None,
                'attack_dist': 80,
                'used': False,
                'turn': None,
            },
            'trap5': {
                'sprite': pygame.image.load(trap),
                'viewing_angles': None,
                'shift': 0.3,
                'scale': 0.4,
                'animation': deque(
                    [pygame.image.load(trap_anim + '/b1316f10845740a3a9e46097dd0979fcjXxKzk1TASyEiiW5-' + str(i) + '.png').convert_alpha() for i in range(0, 3)]),
                'animation_dist': 10000,
                'animation_speed': 3,
                'blocked': False,
                'is_nps': False,
                'speed_n': 0,
                'type': '5trap',
                'to_open': None,
                'attack_dist': 80,
                'used': False,
                'turn': None,
            },
        }
        self.list_of_object = [
            SpriteObject(self.sprate_parameters['sprite_glitch'], (15.0, 12.5)), # глич(монстр)
            SpriteObject(self.sprate_parameters['glitch'], (30.5, 17.5)), # глич(чучело)
            SpriteObject(self.sprate_parameters['glitch'], (30.5, 19.5)), # глич(чучело)
            SpriteObject(self.sprate_parameters['restart'], (30.5, 16.5)), # кнопка возвращения в игру
            SpriteObject(self.sprate_parameters['return'], (30.5, 18.5)), # кнопка перезапуска игры
            SpriteObject(self.sprate_parameters['exit_m_m'], (30.5, 20.5)), # кнопка выхода в главное меню
            SpriteObject(self.sprate_parameters['start'], (29.5, 6.5)), # кнопка начала игры
            SpriteObject(self.sprate_parameters['glitch'], (28.5, 6.5)), # глич(чучело)
            SpriteObject(self.sprate_parameters['exit'], (27.5, 6.5)), # выйти из игры
            SpriteObject(self.sprate_parameters['endurance_point'], (30.0, 30.0)), # сфера энергии
            SpriteObject(self.sprate_parameters['trap1'], (30.5, 30.5)), # ловушка 1
            SpriteObject(self.sprate_parameters['trap2'], (30.5, 30.5)), # ловушка 2
            SpriteObject(self.sprate_parameters['trap3'], (30.5, 30.5)), # ловушка 3
            SpriteObject(self.sprate_parameters['trap4'], (30.5, 30.5)), # ловушка 4
            SpriteObject(self.sprate_parameters['trap5'], (30.5, 30.5)), # ловушка 5
            # ключи
            SpriteObject(self.sprate_parameters['key1'], (2.5, 3.5)),
            SpriteObject(self.sprate_parameters['key2'], (9.5, 18.5)),
            SpriteObject(self.sprate_parameters['key3'], (7.5, 11.5)),
            SpriteObject(self.sprate_parameters['key4'], (23.5, 2.5)),
            SpriteObject(self.sprate_parameters['key5'], (23.5, 18.5)),
            SpriteObject(self.sprate_parameters['key6'], (4.5, 5.5)),
            SpriteObject(self.sprate_parameters['key7'], (22.5, 23.5)),
            # двери
            SpriteObject(self.sprate_parameters['door1'], (4.5, 2.5)),
            SpriteObject(self.sprate_parameters['door2'], (8.5, 14.5)),
            SpriteObject(self.sprate_parameters['door3h'], (17.5, 5.5)),
            SpriteObject(self.sprate_parameters['door3v'], (11.5, 3.5)),
            SpriteObject(self.sprate_parameters['door4'], (21.5, 9.5)),
            SpriteObject(self.sprate_parameters['door4'], (20.5, 15.5)),
            SpriteObject(self.sprate_parameters['door5'], (5.5, 7.5)),
            SpriteObject(self.sprate_parameters['door6'], (4.5, 19.5)),
            SpriteObject(self.sprate_parameters['door6'], (16.5, 19.5)),
            SpriteObject(self.sprate_parameters['door6'], (22.5, 19.5)),
            SpriteObject(self.sprate_parameters['door7'], (2.5, 1.5)),
            # кнопки сложности
            SpriteObject(self.sprate_parameters['easy'], (26.5, 8.5)),
            SpriteObject(self.sprate_parameters['normal'], (28.5, 8.5)),
            SpriteObject(self.sprate_parameters['hard'], (30.5, 8.5)),
        ]

class SpriteObject:
    def __init__(self, parameters, pos):
        # Инициализация параметров спрайта из словаря parameters
        self.object = parameters['sprite']             # Текстура спрайта
        self.viewing_angles = parameters['viewing_angles'] # Углы обзора спрайта (если есть)
        self.shift = parameters['shift']               # Сдвиг спрайта по вертикали
        self.scale = parameters['scale']               # Масштаб спрайта
        self.animation = parameters['animation']         # Кадры анимации (если есть)
        self.animation_dist = parameters['animation_dist'] # Расстояние, на котором начинается анимация
        self.animation_speed = parameters['animation_speed']# Скорость анимации
        self.blocked = parameters['blocked']             # Блокирует ли спрайт проход
        self.is_nps = parameters['is_nps']                 # Является ли спрайт NPC
        self.speed_n = parameters['speed_n']           # Скорость NPC
        self.type = parameters['type']                   # Тип спрайта (ключ, дверь, и т.д.)
        self.to_open = parameters['to_open']             # Количество ключей для открытия
        self.attack_dist = parameters['attack_dist']     # Дистанция атаки NPC
        self.used = parameters['used']                   # Использован ли объект
        self.turn = parameters['turn']                   # Повернут ли объект

        self.side = 100                                  # Размер стороны спрайта
        self.animation_count = 0                        # Счетчик кадров анимации
        self.x, self.y = pos[0] * TILE, pos[1] * TILE    # Координаты спрайта в игровом мире
        self.pos = self.x - self.side // 2, self.y - self.side // 2 # Позиция спрайта
        self.initial_x, self.initial_y = pos[0] * TILE, pos[1] * TILE
        self.initial_pos = (self.initial_x - self.side // 2, self.initial_y - self.side // 2)
        self.open_door_turn = False
        self.closed_door_turn = False
        self.open_door_not_turn = False
        self.closed_door_not_turn = False
        self.to_open_door = 0
        self.openes_doors = 0

        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 13)) for i in range(0, 360, 30)] # Углы обзора для спрайта
            self.sprite_positions = {angle: pos for angle, pos in zip(self.sprite_angles, self.viewing_angles)} # Позиции спрайта в зависимости от угла

    def object_locate(self, player, world_map):
        # Вычисление расстояния до спрайта
        dx, dy = self.x - player.x, self.y - player.y
        self.distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        if self.type == 'point' and not self.used:
            xm, ym = (player.endurance_x // TILE) * TILE, (player.endurance_y // TILE) * TILE
            if player.point_pos:
                if (xm, ym) in world_map:
                    player.endurance_x = random.randint(250, 2250)
                    player.endurance_y = random.randint(250, 2250)
                else:
                    player.point_pos = False
            else:
                self.x, self.y = player.endurance_x, player.endurance_y

        if player.start_e:
            if self.type == 'point' and self.attack_dist >= self.distance_to_sprite:
                if keyboard.is_pressed('e'):
                    if 300 - player.endurance <= 100:
                        self.x += 1000000
                        player.endurance = 300
                        self.used = True
                    else:
                        player.endurance += 100
                        self.x += 1000000
                        self.used = True

        if player.start_n:
            if self.type == 'point' and self.attack_dist >= self.distance_to_sprite:
                if keyboard.is_pressed('e'):
                    self.x += 1000000
                    if 200 - player.endurance <= 100:
                        player.endurance = 200
                        self.used = True
                    else:
                        player.endurance += 100
                        self.used = True

        if player.start_h:
            if self.type == 'point' and self.attack_dist >= self.distance_to_sprite:
                if keyboard.is_pressed('e'):
                    self.x += 1000000
                    if 200 - player.endurance <= 80:
                        player.endurance = 200
                        self.used = True
                    else:
                        player.endurance += 80
                        self.used = True

        # Обработка открытия с горизонтальной двери
        if self.type == 'door' and self.distance_to_sprite < self.animation_dist and self.turn:
            if keyboard.is_pressed('e'):
                if player.number_of_keys >= self.to_open:
                    if not self.used and not self.open_door_turn:
                        # Открываем дверь
                        if not pygame.mixer.Channel(6).get_busy():  # Если звук шагов не проигрывается
                            pygame.mixer.Channel(6).play(player.open_door, loops=0)  # Запускаем звук шагов в цикле
                        self.open_door_turn = True
                        self.animation_dist += 25
                        self.original_collision_rect = next(
                            rect for rect in player.collision_list if rect.topleft == self.pos)
                    # Обработка закрытия вертикальной двери
                    elif self.used and not self.closed_door_turn:
                        # Закрываем дверь
                        if not pygame.mixer.Channel(7).get_busy():  # Если звук шагов не проигрывается
                            pygame.mixer.Channel(7).play(player.close_door, loops=0)  # Запускаем звук шагов в цикле
                        self.closed_door_turn = True
                        self.animation_dist -= 25

        if self.open_door_turn and self.type == 'door' and not self.used:
            self.x += 1
            if self.initial_x + 100 == self.x:
                self.used = True
                self.open_door_turn = False
            # Удаляем коллизию двери
            player.collision_list = [rect for rect in player.collision_list if
                                     rect.topleft != self.pos]
        if self.closed_door_turn and self.type == 'door' and self.used:
            self.x -= 1
            if self.x == self.initial_x:
                self.used = False
                self.closed_door_turn = False
                if hasattr(self, 'original_collision_rect'):
                    player.collision_list.append(self.original_collision_rect)

        # Обработка открытия вертикальной двери
        if self.type == 'door' and self.distance_to_sprite < self.animation_dist and not self.turn:
            if keyboard.is_pressed('e'):
                if player.number_of_keys >= self.to_open:
                    if not self.used and not self.open_door_not_turn:
                        # Открываем дверь
                        if not pygame.mixer.Channel(6).get_busy():  # Если звук шагов не проигрывается
                            pygame.mixer.Channel(6).play(player.open_door, loops=0)  # Запускаем звук шагов в цикле
                        self.original_collision_rect = next(
                            rect for rect in player.collision_list if rect.topleft == self.pos)
                        self.open_door_not_turn = True
                        self.animation_dist += 25
                    # Обработка закрытия вертикальной двери
                    elif self.used and not self.closed_door_not_turn:
                        # Закрываем дверь
                        self.closed_door_not_turn = True
                        if not pygame.mixer.Channel(7).get_busy():  # Если звук шагов не проигрывается
                            pygame.mixer.Channel(7).play(player.close_door, loops=0)  # Запускаем звук шагов в цикле
                        self.animation_dist -= 25

        if self.open_door_not_turn and self.type == 'door' and not self.used:
            self.y += 1
            if self.initial_y + 100 == self.y:
                self.used = True
                self.open_door_not_turn = False
                self.to_open_door = 0
            # Удаляем коллизию двери
            player.collision_list = [rect for rect in player.collision_list if
                                     rect.topleft != self.pos]
        if self.closed_door_not_turn and self.type == 'door' and self.used:
            self.y -= 1
            if self.y == self.initial_y:
                self.used = False
                self.closed_door_not_turn = False
                if hasattr(self, 'original_collision_rect'):
                    player.collision_list.append(self.original_collision_rect)

        if self.type == 'door_ex' and self.animation_dist >= self.distance_to_sprite:
            if self.to_open <= player.number_of_keys:
                if keyboard.is_pressed('e'):
                    player.win = True

        # Обработка взаимодействия с кнопкой
        if self.type == 'button_s' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.x, player.y = 2750, 1250
                player.angle = 4.7300001

        if self.type == 'button_easy' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.start_e = True
                player.x, player.y = 250, 250
                player.angle = 0.000001
                player.load = True

        if self.type == 'button_normal' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.start_n = True
                player.x, player.y = 250, 250
                player.angle = 0
                player.load = True

        if self.type == 'button_hard' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.start_h = True
                player.x, player.y = 250, 250
                player.angle = 0
                player.load = True

        if self.type == 'button_res' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.restart_game()
        if self.type == 'button_ret' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.return_game()
        if self.type == 'button_exit_m_m' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.load = True
                player.home = True
        if self.type == 'button_exit' and self.distance_to_sprite < self.animation_dist:
            if keyboard.is_pressed('e'):
                player.home = True

        if player.spawn_trap:
            if player.traps == 0:
                if self.type == '1trap':
                    if player.start_e:
                        player.in_traping = 100
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_n:
                        player.in_traping = 200
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_h:
                        player.in_traping = 250
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
            if player.traps == 1:
                if self.type == '2trap':
                    if player.start_e:
                        player.in_traping = 100
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_n:
                        player.in_traping = 200
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_h:
                        player.in_traping = 250
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
            if player.traps == 2:
                if self.type == '3trap':
                    if player.start_e:
                        player.in_traping = 100
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_n:
                        player.in_traping = 200
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_h:
                        player.in_traping = 250
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
            if player.traps == 3:
                if self.type == '4trap':
                    if player.start_e:
                        player.in_traping = 100
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_n:
                        player.in_traping = 200
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
                    if player.start_h:
                        player.in_traping = 250
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps += 1
                        player.spawn_trap = False
            if player.traps == 4:
                if self.type == '5trap':
                    if player.start_e:
                        player.in_traping = 100
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps = 0
                        player.spawn_trap = False
                    if player.start_n:
                        player.in_traping = 200
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps = 0
                        player.spawn_trap = False
                    if player.start_h:
                        player.in_traping = 250
                        self.x = player.r_x
                        self.y = player.r_y
                        player.r_x = random.randint(850, 2000)
                        player.r_y = random.randint(600, 1700)
                        player.traps = 0
                        player.spawn_trap = False

        if self.type == '1trap' and self.attack_dist > self.distance_to_sprite:
            player.trap1 = True
        if self.type == '2trap' and self.attack_dist > self.distance_to_sprite:
            player.trap2 = True
        if self.type == '3trap' and self.attack_dist > self.distance_to_sprite:
            player.trap3 = True
        if self.type == '4trap' and self.attack_dist > self.distance_to_sprite:
            player.trap4 = True
        if self.type == '5trap' and self.attack_dist > self.distance_to_sprite:
            player.trap5 = True

        if player.trap1:
            player.r_x = player.x
            player.r_y = player.y
            if not pygame.mixer.Channel(8).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(8).play(player.trap_m, loops=-1)  # Запускаем звук шагов в цикле
            if keyboard.is_pressed('i'):
                player.in_traping -= 1
            else:
                if player.start_e:
                    player.in_traping = 100
                if player.start_n:
                    player.in_traping = 200
                if player.start_h:
                    player.in_traping = 250
            if player.in_traping <= 0:
                pygame.mixer.Channel(8).stop()
                if self.type == '1trap':
                    self.x += 1000000
                player.trap1 = False
        if player.trap2:
            player.r_x = player.x
            player.r_y = player.y
            if not pygame.mixer.Channel(8).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(8).play(player.trap_m, loops=-1)  # Запускаем звук шагов в цикле
            if keyboard.is_pressed('i'):
                player.in_traping -= 1
            else:
                if player.start_e:
                    player.in_traping = 100
                if player.start_n:
                    player.in_traping = 200
                if player.start_h:
                    player.in_traping = 250
            if player.in_traping <= 0:
                if self.type == '2trap':
                    self.x += 1000000
                pygame.mixer.Channel(8).stop()
                player.trap2 = False
        if player.trap3:
            player.r_x = player.x
            player.r_y = player.y
            if not pygame.mixer.Channel(8).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(8).play(player.trap_m, loops=-1)  # Запускаем звук шагов в цикле
            if keyboard.is_pressed('i'):
                player.in_traping -= 1
            else:
                if player.start_e:
                    player.in_traping = 100
                elif player.start_n:
                    player.in_traping = 200
                elif player.start_h:
                    player.in_traping = 250
            if player.in_traping <= 0:
                if self.type == '3trap':
                    self.x += 1000000
                pygame.mixer.Channel(8).stop()
                player.trap3 = False
        if player.trap4:
            player.r_x = player.x
            player.r_y = player.y
            if not pygame.mixer.Channel(8).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(8).play(player.trap_m, loops=-1)  # Запускаем звук шагов в цикле
            if keyboard.is_pressed('i'):
                player.in_traping -= 1
            else:
                if player.start_e:
                    player.in_traping = 100
                if player.start_n:
                    player.in_traping = 200
                if player.start_h:
                    player.in_traping = 250
            if player.in_traping <= 0:
                if self.type == '4trap':
                    self.x += 1000000
                pygame.mixer.Channel(8).stop()
                player.trap4 = False
        if player.trap5:
            player.r_x = player.x
            player.r_y = player.y
            if not pygame.mixer.Channel(8).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(8).play(player.trap_m, loops=-1)  # Запускаем звук шагов в цикле
            if keyboard.is_pressed('i'):
                player.in_traping -= 1
            else:
                if player.start_e:
                    player.in_traping = 100
                if player.start_n:
                    player.in_traping = 200
                if player.start_h:
                    player.in_traping = 250
            if player.in_traping <= 0:
                if self.type == '5trap':
                    self.x += 1000000
                pygame.mixer.Channel(8).stop()
                player.trap5 = False

            if player.in_end:
                player.in_traping = 0

        # Вычисление угла между игроком и спрайтом
        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += DUBLE_PI

        # Определение номера луча, в который попадает спрайт
        delta_rays = int(gamma / player.DELTA_ANGLE)
        current_ray = player.CENTER_RAY + delta_rays
        self.distance_to_sprite *= math.cos(HALF_FOV - current_ray * player.DELTA_ANGLE)

        # Преобразование номера луча в индекс
        fake_ray = current_ray + FAKE_RAY
        if 0 <= fake_ray <= player.FAKE_RAYS_RANGE and self.distance_to_sprite > 30:
            # Вычисление проекции высоты спрайта на экран
            proj_height = min(int(player.PROJ_COEF / self.distance_to_sprite * self.scale), DUBLE_HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            # Выбор текстуры спрайта в зависимости от угла обзора
            if self.viewing_angles:
                if theta < 0:
                    theta += DUBLE_PI
                theta = 360 - int(math.degrees(theta))
                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_positions[angles]
                        break

            # Обработка взаимодействия с ключом
            if self.type == 'key' and self.distance_to_sprite < self.animation_dist:
                if keyboard.is_pressed('e'):
                    self.x += 1000000
                    self.y += 1000000
                    player.number_of_keys += 1
                    self.used = True
                    if not pygame.mixer.Channel(6).get_busy():  # Если звук шагов не проигрывается
                        pygame.mixer.Channel(6).play(player.take_the_key, loops=0)  # Запускаем звук шагов в цикле

            # Анимация спрайта
            sprite_object = self.object
            if self.animation and self.distance_to_sprite < self.animation_dist:
                sprite_object = self.animation[0]
                if self.animation_count < self.animation_speed:
                    self.animation_count += 1
                else:
                    self.animation.rotate()
                    self.animation_count = 0

            # Вычисление позиции спрайта на экране
            sprite_pos = (current_ray * player.SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
            return self.distance_to_sprite, sprite, sprite_pos

        else:
            return (False,)

    def nps(self, player, world_map):
        if not self.is_nps:  # Проверяем, является ли объект NPC
            return player.visible == False

        # Вычисляем направление на игрока
        dx, dy = player.x - self.x, player.y - self.y
        angle = math.atan2(dy, dx)
        distance_to_player = math.sqrt(dx ** 2 + dy ** 2)
        ray_length = distance_to_player

        # Проверяем столкновения с картой
        step = TILE // 16  # Уменьшаем шаг для большей точности
        steps = int(ray_length / step)
        for i in range(1, steps + 1):
            check_x = self.x + i * step * math.cos(angle)
            check_y = self.y + i * step * math.sin(angle)
            cell_x, cell_y = int((check_x // TILE) * TILE), int((check_y // TILE) * TILE)
            if (cell_x, cell_y) in world_map and i * step < distance_to_player:
                player.visible = False
                pygame.mixer.Channel(2).stop()
                self.r_dx, self.r_dy = player.r_x - self.x, player.r_y - self.y
                r_angle = math.atan2(self.r_dy, self.r_dx)
                self.x += self.speed_n * math.cos(r_angle)
                self.y += self.speed_n * math.sin(r_angle)
                if int((self.x // 10) * 10) == int((player.r_x // 10) * 10) and int((self.y // 10) * 10) == int((player.r_y // 10) * 10):
                    if player.from_the_player:
                        player.chens(world_map)
                        player.from_the_player = False
                return

        # Двигаем NPC в сто рону игрока
        if distance_to_player > self.attack_dist:
            self.x += self.speed_n * math.cos(angle)
            self.y += self.speed_n * math.sin(angle)
            self.pos = (self.x - self.side // 2, self.y - self.side // 2)
            player.visible = True
            self.used = True
            if not pygame.mixer.Channel(2).get_busy():  # Если звук шагов не проигрывается
                pygame.mixer.Channel(2).play(player.glich_next_sound, loops=-1)  # Запускаем звук шагов в цикле
            player.r_x, player.r_y = player.x, player.y
            player.from_the_player = True
        else:
            player.loos = True
            pygame.mixer.Channel(2).stop()
            return

    def reset(self, player):
        self.x, self.y = self.initial_x, self.initial_y
        self.pos = self.initial_pos
        self.used = False
        self.animation_count = 0

        # Если это дверь, восстанавливаем коллизии
        if self.type == 'door' and hasattr(self, 'original_collision_rect'):
            player.collision_list.append(self.original_collision_rect)