from end import *  # Импортируем все из файла end.py, отвечающего за концовки игры
from player import Player  # Импортируем класс Player из файла player.py, отвечающий за игрока.
from ray_cast import ray_casting_walls  # Импортируем функцию ray_casting_walls из файла ray_cast.py, отвечающую за рейкастинг стен.
from drawing import Draw  # Импортируем класс Draw из файла drawing.py, отвечающий за отрисовку объектов.
from sprite_object import Sprite  # Импортируем класс Sprite из файла sprite_object.py, отвечающий за спрайты.
from map import world_map  # Импортируем карту мира из файла map.py.

pygame.init()  # Инициализируем Pygame, необходимо для работы библиотеки.

sc = pygame.display.set_mode((WIDTH, HEIGHT))  # Создаем игровое окно с заданными шириной и высотой.
clock = pygame.time.Clock()  # Создаем объект Clock для управления временем в игре (FPS).
pygame.display.set_caption("Glitch's World")  # Устанавливаем заголовок окна игры.
icon_image = pygame.image.load(icon)  # Загружаем изображение иконки игры.
pygame.display.set_icon(icon_image)  # Устанавливаем иконку для окна игры.
pygame.mixer.set_num_channels(16)  # Устанавливаем 16 каналов (индексы 0-15)
sprites = Sprite()  # Создаем экземпляр класса Sprite для управления спрайтами.
drawing = Draw(sc)  # Создаем экземпляр класса Draw для отрисовки объектов на экране.
player = Player(sprites)  # Создаем экземпляр класса Player для управления игроком.
home_screen(sc, player)

while player.RunGame:  # Основной игровой цикл, работает пока игрок не захочет выйти.
    for event in pygame.event.get():  # Обрабатываем события, такие как нажатия клавиш, закрытие окна и т.д.
        if event.type == pygame.QUIT:  # Если игрок нажал на кнопку закрытия окна.
            player.RunGame = False  # Завершаем игровой цикл.

    if player.home:
        player.is_playing = False
        start(sc, player)
    else:
        pygame.mouse.set_visible(False)
        player.is_playing = True
    if player.in_settings:
        settings(sc, player)
    else:
        pygame.mouse.set_visible(False)
    if player.game:  # Если игра запущена.
        sc.fill(BLACK)  # Закрашиваем экран черным цветом.
        fps = clock.get_fps()  # Получаем текущий FPS.
        player.speed = 60 / (0.5 * (int(fps) + 0.0000001))  # Рассчитываем скорость игрока в зависимости от FPS.
        player.speed_angle = 60 / (60 * (int(fps) + 0.0000001))  # Рассчитываем скорость поворота игрока в зависимости от FPS.
        player.speed_run = 60 / (0.5 * (int(fps) + 0.0000001))  # Рассчитываем скорость бега игрока в зависимости от FPS.

        speed_nps = (player.speed / 100) *  player.speed_multiplier  # Вычисляем скорость NPC
        if speed_nps > 30:
            speed_nps = 0

        if player.speed > 30:  # Если скорость игрока больше 30
            muve = False  # Отключаем движение
        else:
            muve = True  # Включаем движение
        if player.Mouving and muve and not (player.trap1 or player.trap2 or player.trap3 or player.trap4 or player.trap5):  # Если игрок двигается и движение включено
            player.mouvement()  # Включаем управление

        drawing.background()  # Рисуем фон.
        walls = ray_casting_walls(player, drawing.texture)  # Получаем стены, видимые игроку с помощью рейкастинга.
        drawing.world(walls + [obj.object_locate(player, world_map) for obj in sprites.list_of_object])  # Рисуем мир, включая стены и спрайты.

        # Обновляем поведение NPC
        for sprite in sprites.list_of_object:  # Для каждого спрайта в списке
            if hasattr(sprite, 'nps'):  # Проверяем, есть ли у спрайта метод nps
                sprite.nps(player, world_map)  # Вызываем метод nps, если он есть
                sprite.speed_n = speed_nps  # Устанавливаем скорость NPC
        drawing.fps(clock, player)  # Отображаем FPS на экране.
    elif player.restarting:  # Если идет перезапуск
        player.load = True # Запускаем анимацию загрузки
        player.restart_game()  # Вызываем метод перезапуска
    player.exit()  # Вызов функции выхода из игры
    if player.win:  # Если игрок выиграл.
        win(player, sc)  # Вызываем функцию отображения экрана победы.
    if player.loos:  # Если игрок проиграл.
        loos(player, sc)  # Вызываем функцию отображения экрана поражения.
    if player.load:
        loading(sc,player)

    pygame.display.flip()  # Обновляем содержимое экрана.
    clock.tick(FPS)  # Ограничиваем частоту кадров в секунду (FPS).