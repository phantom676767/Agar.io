from pygame import *
from math import hypot
from random import randint 
from socket import *
from threading import Thread
from menu import Launcher

window = Launcher()
window.mainloop()

name = window.name
# name = "Phantom"


sock = socket(AF_INET, SOCK_STREAM)
HOST = window.ip
PORT = window.port
# HOST = "localhost"
# PORT = 8080
sock.connect((HOST, PORT))
my_data = list(map(int, sock.recv(64).decode().strip().split(',')))
my_id = my_data[0]
my_player = my_data[1:]
sock.setblocking(False)

init()
window = display.set_mode((1000, 700))
clock = time.Clock()
running = True
lose = False
player = [my_player[0], my_player[1], my_player[2]]
foods = []
all_players = []
f = font.Font(None, 50)
name_font = font.Font(None, 20)

def receive_data():
   global all_players, running, lose
   while running:
       try:
           data = sock.recv(4096).decode().strip()
           if data == "LOSE":
               lose = True
           elif data:
               parts = data.strip('|').split('|')
               all_players = [list(map(int, p.split(',')[0:4])) + [p.split(',')[-1]] for p in parts if len(p.split(',')) == 5]
               print("Всі гравці:", all_players)
       except:
           pass
       
Thread(target=receive_data, daemon=True).start()

class Food:
    def __init__(self, x, y, r = 5, c = (255, 0, 0)):
        self.x = x
        self.y = y
        self.radius = r
        self.color = c

    def check_collision(self, player_x, player_y, player_r):
       dx = self.x - player_x
       dy = self.y - player_y
       return hypot(dx, dy) <= self.radius + player_r
    
for i in range(500):
    food = Food(x = randint(-2000, 2000), y = randint(-2000, 2000), r = 5, c = (randint(0, 255), randint(0,255), randint(0,255)))
    foods.append(food)

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
   
    window.fill((255, 255, 255))
    scale = max(0.3, min(50 / player[2], 1.5))
    # поле
    # sx = int((0 - player[0]))
    # sy = int((0 - player[1]))
    # draw.circle(window, (0, 0, 0), (sx, sy), 2000)
    for p in all_players:
       if p[0] == my_id: continue
       sx = int((p[1] - my_player[0]) * scale + 500)
       sy = int((p[2] - my_player[1]) * scale + 500)
       player_name = name_font.render(p[4], 1, (0, 0, 0))
       window.blit(player_name, (sx - 25, sy - 50))
       draw.circle(window, (255, 0, 0), (sx, sy), int(p[3] * scale))

    my_player_name = name_font.render(name, 1, (0, 0, 0))
    window.blit(my_player_name, (475, 300))
    draw.circle(window, (0, 255, 0), (500, 350), int(my_player[2] * scale))



    to_remove = []
    for food in foods:
        if food.check_collision(player[0], player[1], player[2]):
            to_remove.append(food)
            player[2] += int(food.radius * 0.2)
        else:
            sx = int((food.x - player[0]) * scale + 500)
            sy = int((food.y - player[1]) * scale + 500)
            draw.circle(window, food.color, (sx, sy), int(food.radius * scale))

    for food in to_remove:
        foods.remove(food)

    if lose:
        t = f.render('U lose!', 1, (244, 0, 0))
        window.blit(t, (400, 500))

    if not lose:
        keys = key.get_pressed()
        if keys[K_w]:
            player[1] -=15
        if keys[K_a]:
            player[0] -=15
        if keys[K_s]:
            player[1] +=15
        if keys[K_d]:
            player[0] +=15

        try:
           msg = f"{my_id},{my_player[0]},{my_player[1]},{my_player[2]},{name}"
           sock.send(msg.encode())
        except:
           pass
        







    display.update()
    clock.tick(60)

quit()

