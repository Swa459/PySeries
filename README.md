# Hello Everyone, This is PySeries.

Well now you might be asking, what the heck is this???

I know I know, let me _Swa459_ clear it.

**Pyseries** a lib which you may trust for:

*- Building a game* like maybe..... A **clicker game**, or maybe a boring **rectangle movement with arrow keys**

*- Build a project which you can build using ***Turtle*** also.*

Now, you might say, **"Bruh, you kidding me? We already have Pygame"**, yeah you are right you have ***Pygame*** the king of game designing.

But this comparision is also not wrong about making a clicker game:

**Py2D an package of PySeries** ***VS*** **The king of game designing Pygame**

**Py2D:**

```
import Py2D

screen = Py2D.Window(title="Clicker", geometry="700x500")

score = Py2D.Score(screen, x=350)
clickMe = Py2D.Label(screen, x=345, y=230)

btn = Py2D.Sprite(screen)
btn.Figure(x=300, y=220, l=9)
clickMe.Above()
clickMe.Text("Click Me")

clicks = {"count": 0}

timer = Py2D.StopWatch(screen, x=350, y=450)
timer.Font(fontsize=24, fontcolor="#000007")

def handle_click(e):
    clicks["count"] += 1

    if clicks["count"] == 1:
        timer.Trigger()

    elif 2 <= clicks["count"] <= 50:
        score.Add(1)

    elif clicks["count"] == 51:
        timer.Stop()

clickMe.IsClicked(handle_click)
btn.IsClicked(handle_click)

screen.run()
```

**Pygame:**

```
import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

font = pygame.font.SysFont(None, 36)
timer_font = pygame.font.SysFont(None, 24)

score = 0
clicks = 0

start_time = None
stop_time = None
running_timer = False

button_rect = pygame.Rect(300, 220, 100, 50)

def draw_text(text, x, y, font, color=BLACK):
    label = font.render(text, True, color)
    rect = label.get_rect(center=(x, y))
    screen.blit(label, rect)

def handle_click():
    global clicks, score, start_time, stop_time, running_timer
    clicks += 1

    if clicks == 1:
        start_time = time.time()
        running_timer = True
    elif 2 <= clicks <= 50:
        score += 1
    elif clicks == 51:
        stop_time = time.time()
        running_timer = False

clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    draw_text(f"Score: {score}", 350, 50, font)

    pygame.draw.rect(screen, RED, button_rect)
    draw_text("Click Me", button_rect.centerx, button_rect.centery, font)

    if running_timer:
        elapsed = time.time() - start_time
    elif stop_time:
        elapsed = stop_time - start_time
    else:
        elapsed = 0
    draw_text(f"Time: {elapsed:.2f}s", 350, 450, timer_font)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                handle_click()

    pygame.display.flip()
    clock.tick(60)
```


**Wait Wait, Abhi bhee picture baaki hai mere dost.**

English Translated **Wait, Wait, Still the picture is pending my friend.**

Ontop of code ease, it also provides faster start-up, what do you say about that? Or totally zipped up, huh??? 😎😎😎

Now let us compete this with ***Turtle***, ok now I got to compromise one thing of course, turtle is way more simplified than Py2D,
but what if we think from the side of Features, Py2D has the most, so I think that Py2D is a better choice.

Also what `Py2D` supports and `Turtle` doesn't?

_- Multiple Screens_

_- More object control_

_- More in-built features such as : Stopwatch & Label_

Now I guess you have seen the `PySound.py` also right? You might have been wondering what is that?

Well as many of you use **Pygame** so of course you should be knowing **Pygame.mixer**, this is also an module of **PySeries**.
