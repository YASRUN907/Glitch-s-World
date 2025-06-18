from settings import *  # Импорт настроек игры из файла settings.py.
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT, matrix_map  # Импорт данных карты и размеров мира.
import math  # Импорт математической библиотеки.
from numba import njit  # Импорт декоратора njit из библиотеки Numba для ускорения кода.

@njit(fastmath=True)  # Декоратор для JIT-компиляции функции с оптимизацией математических операций.
def mapping(a, b):  # Функция для определения координат тайла, в котором находится точка (a, b).
    return (a // TILE) * TILE, (b // TILE) * TILE  # Возвращает координаты левого верхнего угла тайла.

@njit(fastmath=True)  # Декоратор для JIT-компиляции функции с оптимизацией математических операций.
def ray_cast(player_pos, player_angle, world_map, NUM_RAYS, PROJ_COEF, DELTA_ANGLE):  # Функция для трассировки лучей.
    casted_walls = []  # Список для хранения данных о пересечениях лучей со стенами.
    ox, oy = player_pos  # Координаты игрока.
    x_pos, y_pos = mapping(ox, oy)  # Координаты тайла, в котором находится игрок.
    cur_angle = player_angle - HALF_FOV  # Угол первого луча.

    for ray in range(NUM_RAYS):  # Цикл по количеству лучей.
        sin_cur = math.sin(cur_angle)  # Синус текущего угла.
        cos_cur = math.cos(cur_angle)  # Косинус текущего угла.

        # Проверка вертикалей
        x, dx = (x_pos + TILE, 1) if cos_cur >= 0 else (x_pos, -1)  # Начальная координата x и приращение для вертикалей.
        for _ in range(0, WORLD_WIDTH, TILE):  # Цикл по вертикальным линиям сетки.
            depth_v = (x - ox) / cos_cur  # Расстояние до вертикальной линии.
            y = oy + depth_v * sin_cur  # Координата y точки пересечения.
            tile_v = mapping(x + dx, y)  # Координаты тайла, в котором находится точка пересечения.
            if tile_v in world_map:  # Если тайл является стеной.
                tevture_v = world_map[tile_v]  # Получение текстуры стены.
                break
            x += dx * TILE  # Переход к следующей вертикальной линии.

        # Проверка горизонталей
        y, dy = (y_pos + TILE, 1) if sin_cur >= 0 else (y_pos, -1)  # Начальная координата y и приращение для горизонталей.
        for _ in range(0, WORLD_HEIGHT, TILE):  # Цикл по горизонтальным линиям сетки.
            depth_h = (y - oy) / sin_cur  # Расстояние до горизонтальной линии.
            x = ox + depth_h * cos_cur  # Координата x точки пересечения.
            tile_h = mapping(x, y + dy)  # Координаты тайла, в котором находится точка пересечения.
            if tile_h in world_map:  # Если тайл является стеной.
                tevture_h = world_map[tile_h]  # Получение текстуры стены.
                break
            y += dy * TILE  # Переход к следующей горизонтальной линии.

        # Определение, какая глубина меньше
        depth, offset, texture = (depth_v, y, tevture_v) if depth_v < depth_h else (depth_h, x, tevture_h)  # Выбор ближайшей точки пересечения.
        offset = int(offset) % TILE  # Вычисление смещения текстуры.
        depth *= math.cos(cur_angle - player_angle)  # Коррекция глубины с учетом угла.
        prog_helight = int(PROJ_COEF / depth)  # Вычисление высоты проекции стены.
        depth = max(depth, 0.00001)  # Предотвращение деления на ноль.

        casted_walls.append((depth, offset, prog_helight, texture))  # Добавление данных о стене в список.
        # Перейти к следующему лучу
        cur_angle += DELTA_ANGLE  # Увеличение угла для следующего луча.
    return casted_walls  # Возвращает список данных о стенах.


def ray_casting_walls(player, textures):  # Функция для отрисовки стен на основе трассировки лучей.
    casted_walls = ray_cast(player.pos, player.angle, world_map, player.NUM_RAYS, player.PROJ_COEF, player.DELTA_ANGLE)  # Получение данных о стенах.
    walls = []  # Список для хранения данных для отрисовки стен.
    for ray, casted_values in enumerate(casted_walls):  # Цикл по данным о стенах.
        depth, offset, prog_helight, texture = casted_values  # Извлечение данных о стене.
        if prog_helight > HEIGHT:  # Если высота проекции стены больше высоты экрана.
            coeff = prog_helight / HEIGHT  # Вычисление коэффициента масштабирования.
            texture_height = TEXTURE_HEIGHT / coeff  # Вычисление высоты текстуры.
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE,
                                                       HALF_TEXTURE_HEIGHT - texture_height // 2,
                                                       TEXTURE_SCALE, texture_height)  # Вырезание части текстуры.
            wall_column = pygame.transform.scale(wall_column, (player.SCALE, HEIGHT))  # Масштабирование текстуры до высоты экрана.
            wall_pos = (ray * player.SCALE, 0)  # Вычисление позиции стены на экране.
        else:  # Если высота проекции стены меньше высоты экрана.
            wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)  # Вырезание части текстуры.
            wall_column = pygame.transform.scale(wall_column, (player.SCALE, prog_helight))  # Масштабирование текстуры до высоты проекции.
            wall_pos = (ray * player.SCALE, HALF_HEIGHT - prog_helight // 2)  # Вычисление позиции стены на экране.
        walls.append((depth, wall_column, wall_pos))  # Добавление данных для отрисовки стены в список.
    return walls  # Возвращает список данных для отрисовки стен.