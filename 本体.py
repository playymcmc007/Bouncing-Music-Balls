import math
import pygame
import random
import tkinter
import tkinter.messagebox
def game(): 
    pygame.init()
    pygame.mixer.init()
    files = {
        'star': 'star.png',
        'music': 'music.wav',
        'm1': '1.wav',
        'm2': '2.wav',
        'm3': '3.wav',
        'm4': '4.wav',
        'm5': '5.wav',
        'm6': '6.wav',
        'm7': '7.wav'
    }
    width = 800
    height = 600
    pingmu=pygame.display.set_mode((width, height))
    pygame.display.set_caption("乱弹的音乐小球")
    star_image = pygame.image.load(files['star'])
    star_size = star_image.get_size()
    pygame.mixer.music.load(files['music'])
    icon = pygame.image.load(files['star'])
    pygame.display.set_icon(icon)
    shunxu = [(255, 0, 0),(255, 165, 0),(255, 255, 0), (0, 128, 0), (0, 0, 255),(75, 0, 130),(128, 0, 128)]
    player_shunxu = []
    zhuzi = []
    colors = {
        'red': (255, 0, 0),
        'orange': (255, 165, 0),
        'yellow': (255, 255, 0),
        'green': (0, 128, 0),
        'blue': (0, 0, 255),
        'indigo': (75, 0, 130),
        'purple': (128, 0, 128),
        'cyan': (0, 255, 255),
        'grey': (192, 192, 192)
    }
    color_texts = {
        colors['red']: '红',
        colors['orange']: '橙',
        colors['yellow']: '黄',
        colors['green']: '绿',
        colors['blue']: '蓝',
        colors['indigo']: '靛',
        colors['purple']: '紫'
    }
    sounds = {
        colors['red']: pygame.mixer.Sound(files['m1']),
        colors['orange']: pygame.mixer.Sound(files['m2']),
        colors['yellow']: pygame.mixer.Sound(files['m3']),
        colors['green']: pygame.mixer.Sound(files['m4']),
        colors['blue']: pygame.mixer.Sound(files['m5']),
        colors['indigo']: pygame.mixer.Sound(files['m6']),
        colors['purple']: pygame.mixer.Sound(files['m7']),
    }
    class Pillar:
        def __init__(self, x, y, width, height,color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
        def draw(self, pingmu):
            pygame.draw.rect(pingmu, self.color, (self.x, self.y, self.width, self.height))
    class Particle:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color
            self.daxiao = random.randint(3, 3)
            self.alpha = 114
            self.fade = random.randint(5, 5)
        def update(self):
            self.alpha -= self.fade
            if self.alpha <= 0:
                self.alpha = 0
        def draw(self, pingmu):
            border_color = (self.color[0] + 10 if self.color[0] < 205 else 255,
                            self.color[1] + 20 if self.color[1] < 205 else 255,
                            self.color[2] + 30 if self.color[2] < 205 else 255)
            pygame.draw.circle(pingmu, border_color, (int(self.x), int(self.y)), self.daxiao + 5)
            pygame.draw.circle(pingmu, (self.color[0], self.color[1], self.color[2], self.alpha), (int(self.x), int(self.y)), self.daxiao)
    class Ball:
        def __init__(self, x, y, daxiao, color):
            self.x = x
            self.y = y
            self.daxiao = daxiao
            self.color = color
            self.xspeed = 0
            self.yspeed = 0
            self.gravity = 1
            self.moca = 0.99
            self.particles = []
        def update(self):
            self.yspeed += self.gravity
            self.x += self.xspeed
            self.y += self.yspeed
            if self.x - self.daxiao < 0 or self.x + self.daxiao > width:
                self.xspeed = -self.xspeed
            if self.x - self.daxiao < 0 or self.x + self.daxiao > width:
                if self.x - self.daxiao < 0:
                    self.x = self.daxiao
                else:
                    self.x = width - self.daxiao
                self.xspeed = -self.xspeed
            if self.y + self.daxiao > height:
                self.y = height - self.daxiao
                self.yspeed = -self.yspeed * 0.7
            self.xspeed *= self.moca
            self.yspeed *= self.moca
            if abs(self.xspeed) < 2:
                self.xspeed = 0
            particle = Particle(self.x, self.y, self.color)
            self.particles.append(particle)
            for particle in self.particles:
                particle.update()
                if particle.alpha <= 0:
                    self.particles.remove(particle)
        def draw(self, pingmu):
            pygame.draw.circle(pingmu, self.color, (int(self.x), int(self.y)), self.daxiao)
            for particle in self.particles:
                particle.draw(pingmu)
        def get_rect(self):
            return pygame.Rect(self.x - self.daxiao, self.y - self.daxiao, self.daxiao * 2, self.daxiao * 2)
        def box(self, other):
            xx = self.x - other.x
            yy = self.y - other.y
            jiancexy = (xx**2 + yy**2)**0.5
            if jiancexy < (self.daxiao + other.daxiao):
                self.yspeed, other.yspeed = other.yspeed, self.yspeed
                chongdie = (self.daxiao + other.daxiao) - jiancexy
                if jiancexy != 0:
                    self.x += (xx / jiancexy) * (chongdie / 2)
                    self.y += (yy / jiancexy) * (chongdie / 2)
                    other.x -= (xx / jiancexy) * (chongdie / 2)
                    other.y -= (yy / jiancexy) * (chongdie / 2)
                else:
                    jiaodu = random.uniform(0, 2 * math.pi)
                    self.x += math.cos(jiaodu) * (chongdie / 2)
                    self.y += math.sin(jiaodu) * (chongdie / 2)
                    other.x -= math.cos(jiaodu) * (chongdie / 2)
                    other.y -= math.sin(jiaodu) * (chongdie / 2)
            if self.color == other.color and jiancexy < (self.daxiao + other.daxiao):
                return True
            return False
        def mix(self, other):
            if self.color == other.color and self.daxiao == other.daxiao:
                new_x = (self.x + other.x) / 2
                new_y = (self.y + other.y) / 2
                new_size = self.daxiao * 1.5
                return Ball(new_x, new_y, int(new_size), self.color)
            return None
    balls = [
        Ball(random.randint(0, width), 0, 15, colors['red']),
        Ball(random.randint(0, width), 0, 15, colors['orange']),
        Ball(random.randint(0, width), 0, 15, colors['yellow']),
        Ball(random.randint(0, width), 0, 15, colors['green']),
        Ball(random.randint(0, width), 0, 15, colors['blue']),
        Ball(random.randint(0, width), 0, 15, colors['indigo']),
        Ball(random.randint(0, width), 0, 15, colors['purple'])
    ]
    font = pygame.font.Font("C:\Windows\Fonts\simkai.ttf", 30)
    text_x = 20
    text_y = 20
    text_rect = pygame.Rect(text_x, text_y, 300, 50)
    def dianjishijian(event_pos):
        for ball in balls:
            global new_color
            global new_ball
            if ball.get_rect().collidepoint(event_pos[0], event_pos[1]):
                new_color = ball.color
                new_ball=("生成了新的{}色小球".format(color_texts[new_color]))
                pingmu.fill(colors['grey'], text_rect)
                text = font.render(new_ball, True, new_color)
                print(new_ball)
                pingmu.blit(text, (text_x, text_y))
                pygame.display.flip()
                return True
        return False
    start_ticks = pygame.time.get_ticks()
    display_text = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for ball in balls:
                    point = math.sqrt((mx - ball.x) ** 2 + (my - ball.y) ** 2)
                    if point < ball.daxiao:
                        color_name = ball.color
                        if color_name in sounds:
                            sounds[color_name].play()
                        xxx = random.choice([0, width])
                        yyy = height // 2
                        new = Ball(xxx, yyy, 15, ball.color)
                        new.xspeed = random.uniform(5, 10) if xxx == 0 else random.uniform(-10, -5)
                        new.yspeed = random.uniform(-5, 5)
                        balls.append(new)
                        player_shunxu.append(ball.color)
                        if player_shunxu == shunxu[:len(player_shunxu)]:
                            if len(player_shunxu) == len(shunxu):
                                pygame.mixer.music.play(0)
                                player_shunxu = []
                                zhuzi.append(Pillar(width // 2, height//2+10, 50, 300, colors['cyan']))
                        else:
                            player_shunxu = []
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if dianjishijian(event.pos):
                                display_text = True
                                start_ticks = pygame.time.get_ticks()
        for x in range(0, pingmu.get_width(), star_size[0]):
            for y in range(0, pingmu.get_height(), star_size[1]):
                pingmu.blit(star_image, (x, y))
        pygame.display.flip()
        pingmu.fill(colors['grey'])
        to_remove = set()
        to_add = []
        for i, ball in enumerate(balls):
            ball.update()
            ball.draw(pingmu)
            for ballplus in balls[i+1:]:
                if ball.box(ballplus):
                    mix_ball = ball.mix(ballplus)
                    if mix_ball:
                        to_add.append(mix_ball)
                        to_remove.add(ball)
                        to_remove.add(ballplus)
                    else:
                        ball.yspeed, ballplus.yspeed = ballplus.yspeed, ball.yspeed
                for pillar in zhuzi:
                    if (pillar.x < ball.x + ball.daxiao < pillar.x + pillar.width and
                        pillar.y < ball.y + ball.daxiao < pillar.y + pillar.height):
                        ball.xspeed = -ball.xspeed
                        ball.yspeed = -ball.yspeed
                    pillar.draw(pingmu)
        for ball in to_remove:
            balls.remove(ball)
        balls.extend(to_add)
        if display_text:
                elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
                if elapsed_time > 5:
                    display_text = False
                else:
                    text = font.render(new_ball, True, new_color)
                    pingmu.blit(text, (text_x, text_y))
    pygame.time.Clock().tick(60)  
    pygame.mixer.quit()
    pygame.quit()
    def show_selection():
        selected_option = tkbianliang.get()
        if selected_option:
            tkinter.messagebox.showinfo("谢谢评价", f"您给出了{selected_option}星的评价！")
        else:
            tkinter.messagebox.showinfo("无评价", "你甚至不愿意评一个分！")
    def open_pygame():
        pingjia.destroy()
        game()
    pingjia = tkinter.Tk()
    def close():
        if tkinter.messagebox.askyesno("退出", "要退出吗？"):
            pingjia.destroy()
    star_e = "\U00002B50"#星星符号，电脑里难打出来
    pingjia.title('评价')
    tkbianliang = tkinter.IntVar()
    window_width = 800
    window_height = 200
    screen_width = pingjia.winfo_screenwidth()
    screen_height = pingjia.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    pingjia.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    frame = tkinter.Frame(pingjia)
    pingjia.grid_rowconfigure(0, weight=1)
    pingjia.grid_columnconfigure(0, weight=1)
    frame.grid(row=0, column=0, sticky="nsew")
    label = tkinter.Label(frame, text="请为这个小游戏评价",font="楷体")
    label.grid(row=1, column=0, columnspan=7, sticky='ew')
    tkb1 = tkinter.Radiobutton(frame, text=star_e*1, variable=tkbianliang, value=1)
    tkb1.grid(row=2, column=1)
    tkb2 = tkinter.Radiobutton(frame, text=star_e*2, variable=tkbianliang, value=2)
    tkb2.grid(row=2, column=2)
    tkb3 = tkinter.Radiobutton(frame, text=star_e*3, variable=tkbianliang, value=3)
    tkb3.grid(row=2, column=3)
    tkb4 = tkinter.Radiobutton(frame, text=star_e*4, variable=tkbianliang, value=4)
    tkb4.grid(row=2, column=4)
    tkb5 = tkinter.Radiobutton(frame, text=star_e*5, variable=tkbianliang, value=5)
    tkb5.grid(row=2, column=5)
    confirm_button = tkinter.Button(frame, text="确定", command=show_selection)
    confirm_button.grid(row=3, column=2, sticky='ew')
    pygame_button = tkinter.Button(frame, text="重玩", command=open_pygame)
    pygame_button.grid(row=3, column=4, sticky='ew')
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(6, weight=1)
    pingjia.protocol("WM_DELETE_WINDOW", close)
    pingjia.mainloop()
game()