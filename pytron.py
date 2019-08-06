import sys, pygame

z = 500
x = 300
y = 300
points = [[x,y], [z,z]]
keys_state = {"up":1, "down":0, "left":0, "right":0}
line_player = [(x,y)]
line_pc = [(z,z)]


pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((800,600))

def game_surface():
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (225,225,225), (10, 10, 780, 580), 5)

def keys_last_state():
    act_state = list(keys_state.values())
    if act_state[0] == 1:
        keys_state["up"] = 0
    elif act_state[1] == 1:
        keys_state["down"] = 0
    elif act_state[2] == 1:
        keys_state["left"] = 0
    elif act_state[3] == 1:
        keys_state["right"] = 0

def game_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if keys_state["up"] == 0 and keys_state["down"] != 1:
                    keys_last_state()
                    keys_state["up"] = 1
            elif event.key == pygame.K_s:
                if keys_state["down"] == 0 and keys_state["up"] != 1:
                    keys_last_state()
                    keys_state["down"] = 1
            elif event.key == pygame.K_a:
                if keys_state["left"] == 0 and keys_state["right"] != 1:
                    keys_last_state()
                    keys_state["left"] = 1
            elif event.key == pygame.K_d:
                if keys_state["right"] == 0 and keys_state["left"] != 1:
                    keys_last_state()
                    keys_state["right"] = 1

def move_player():
    if keys_state["up"] == 1:
        points[0][1] -= 1
    elif keys_state["down"] == 1:
        points[0][1] += 1
    elif keys_state["left"] == 1:
        points[0][0] -= 1
    elif keys_state["right"] == 1:
        points[0][0] += 1
    #pygame.draw.circle(surface, (225,225,225), points[0], 1, 0)

def move_pc():
    if keys_state["up"] == 1:
        points[1][1] -= 1
    elif keys_state["down"] == 1:
        points[1][1] += 1
    elif keys_state["left"] == 1:
        points[1][0] -= 1
    elif keys_state["right"] == 1:
        points[1][0] += 1
    pygame.draw.circle(surface, (225,225,225), points[1], 3, 0)

def bike_line():
    for a in range(len(line_player)):
        if points[0][0] == line_player[a][0] and points[0][1] == line_player[a][1]:
            points[0][0] = x
            points[0][1] = y
            line_player.clear()
            line_player.append((x,y))
            break
        elif points[1][0] == line_player[a][0] and points[1][1] == line_player[a][1]:
            points[1][0] = z
            points[1][1] = z
            line_pc.clear()
            line_pc.append((z,z))
            break
    for b in range(len(line_pc)):
        if points[1][0] == line_pc[b][0] and points[1][1] == line_pc[b][1]:
            points[1][0] = z
            points[1][1] = z
            line_pc.clear()
            line_pc.append((z,z))
            break
        elif points[0][0] == line_pc[b][0] and points[0][1] == line_pc[b][1]:
            points[0][0] = x
            points[0][1] = y
            line_player.clear()
            line_player.append((x,y))
            break
    line_player.append((points[0][0], points[0][1]))
    line_pc.append((points[1][0], points[1][1]))
    pygame.draw.lines(surface, (50,200,50), False, line_player, 8)
    pygame.draw.lines(surface, (50,100,200), False, line_pc, 8)

def colision():
    if points[0][0] < 16  or points[0][0] > 780 or points[0][1] < 16 or points[0][1] > 580:
        points[0][0] = x
        points[0][1] = y
        line_player.clear()
        line_player.append((x,y))
    elif points[1][0] < 16  or points[1][0] > 780 or points[1][1] < 16 or points[1][1] > 580:
        points[1][0] = z
        points[1][1] = z
        line_pc.clear()
        line_pc.append((z,z))


while True:
    game_surface()
    colision()
    move_player()
    move_pc()
    bike_line()
    pygame.display.update()
    clock.tick(240)
    colision()
    game_events()
