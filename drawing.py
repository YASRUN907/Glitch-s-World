from settings import *  # Импортируем настройки из файла settings.py

class Draw:
    def __init__(self, sc):
        # Инициализация класса Draw, sc - поверхность для рисования
        self.sc = sc  # Сохраняем поверхность для рисования (screen)
        self.font = pygame.font.SysFont('FPS', 25, bold=False)  # Создаем шрифт для отображения FPS (шрифт 'FPS', размер 25, нежирный)
        self.texture = {  # Словарь текстур для разных типов стен
            1: pygame.image.load(stena).convert_alpha(),  # Загружаем изображение стены из переменной stena (из settings.py) и конвертируем его в формат, подходящий для Pygame
            2: pygame.image.load(wall_go).convert(),  # Загружаем изображение стены "go" и конвертируем его
            3: pygame.image.load(wall_run).convert(),  # Загружаем изображение стены "run" и конвертируем его
            4: pygame.image.load(wall_escape).convert(),  # Загружаем изображение стены "escape" и конвертируем его
            5: pygame.image.load(wall_restart).convert(),  # Загружаем изображение стены "restart" и конвертируем его
            6: pygame.image.load(wall_interaction).convert(),  # Загружаем изображение стены "interaction" и конвертируем его
            7: pygame.image.load(freedom).convert(),  # Загружаем изображение "freedom" и конвертируем его
            8: pygame.image.load(wall_tg).convert(),  # Реклама тгк (тгк:ProstoProger)
        }

    def background(self):
        # Рисуем фон (пол и потолок)
        pygame.draw.rect(self.sc, BETON, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))  # Рисуем прямоугольник цвета BETON (из settings.py) в нижней половине экрана (пол)
        pygame.draw.rect(self.sc, BLACK, (0, 0, WIDTH, HALF_HEIGHT))  # Рисуем прямоугольник цвета BLACK (черный) в верхней половине экрана (потолок)

    def world(self, world_objects):
        # Отображаем объекты мира, сортируя их по расстоянию до камеры (для эффекта перспективы)
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):  # Сортируем объекты по расстоянию (первый элемент кортежа) в обратном порядке (дальние объекты рисуются первыми)
            if obj[0]:  # Проверяем, что расстояние не равно нулю (чтобы избежать ошибок)
                _, object, object_pos = obj  # Распаковываем кортеж: _, объект (изображение), позиция объекта (координаты)
                self.sc.blit(object, object_pos)  # Отображаем объект на экране в заданной позиции

    def fps(self, clock, player):
        # Отображаем текущий FPS (кадры в секунду)
        fps = str(int(clock.get_fps()))  # Получаем текущий FPS из объекта clock, преобразуем его в целое число и затем в строку
        render = self.font.render(fps, True, GREEN)  # Рендерим (создаем изображение) текста с FPS зеленым цветом
        self.sc.blit(render, (WIDTH - 38, 10))  # Отображаем текст в верхнем правом углу экрана (с небольшим отступом)
        # Отоброжаем выносливость
        font = pygame.font.SysFont('endurance', 50, bold=False)
        render = font.render(str(player.endurance), True, YELLOW)
        self.sc.blit(render, (60, 10))

        if player.visible:
            self.font_see = pygame.font.SysFont('SEE', 40, bold=False)
            render = self.font_see.render('It sees you', True, RED)
            self.sc.blit(render, (HALF_WIDTH - 70, 10))

        if player.trap1 or player.trap2 or player.trap3 or player.trap4 or player.trap5:
            self.font_trap = pygame.font.SysFont('trap', 36, bold=False)
            render = self.font_trap.render("It knows where you are,", True, ORANGE)
            render2 = self.font_trap.render(f"press the 'i' to get out: {player.in_traping}", True, ORANGE)
            self.sc.blit(render, (10, 50))
            self.sc.blit(render2, (10, 75))