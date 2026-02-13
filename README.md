# 🎮 PySeries

> A lightweight Python library for building games and interactive applications with simplicity in mind.

## 🤔 What is PySeries?

PySeries is a collection of Python packages designed to make game development and interactive graphics more accessible. Whether you're building your first clicker game or experimenting with graphical applications, PySeries offers a gentle learning curve without sacrificing functionality.

### 📦 Core Packages

- **Py2D** - The main graphics and game development package
- **PySound** - Audio rendering and sound management (similar to `pygame.mixer`)

---

## 🎯 Who Should Use PySeries?

PySeries is **perfect** for:
- 🎓 Beginners learning game development
- 🚀 Rapid prototyping of simple games
- 🎨 Building clicker games, basic platformers, and GUI applications
- 📚 Educational projects and coding workshops

PySeries might **not** be ideal for:
- 🎮 Complex, production-ready games
- ⚡ Performance-critical applications
- 🌐 Cross-platform game deployment
- 🎬 Advanced graphics and animation systems

---

## ⚖️ Framework Comparison

Let's see how **Py2D**, **Pygame**, and **Turtle** stack up against each other:

### 🏆 Py2D

#### ✅ Pros
- Extremely concise syntax - less boilerplate code
- Faster startup time for small projects
- Built-in high-level features (Stopwatch, Score, TextBox)
- Multi-window support out of the box
- Rich color palette (300+ named colors)
- Great for beginners and quick prototypes

#### ❌ Cons
- Smaller community and ecosystem
- Limited documentation and tutorials
- Less suitable for complex game mechanics
- Fewer third-party extensions
- Not widely adopted in production

---

### 🎨 Pygame

#### ✅ Pros
- Industry-standard library with huge community
- Extensive documentation, tutorials, and resources
- High performance and optimization
- Cross-platform compatibility
- Rich ecosystem of plugins and extensions
- Suitable for production-level games
- Active development and long-term support

#### ❌ Cons
- More verbose code for simple projects
- Steeper learning curve for beginners
- Requires more boilerplate for basic functionality
- Manual implementation of common UI elements
- Longer initial setup time

---

### 🐢 Turtle

#### ✅ Pros
- Simplest syntax - perfect for absolute beginners
- Built into Python standard library (no installation)
- Excellent for teaching programming concepts
- Immediate visual feedback
- Great documentation for learners
- Zero configuration required

#### ❌ Cons
- Very limited game development features
- Poor performance for complex graphics
- Single window limitation
- No built-in audio support
- Not suitable for real game projects
- Limited control over graphics rendering

---

## 💻 Code Comparison: Building a Clicker Game

Let's build the same clicker game in all three frameworks:

### 🎯 Py2D Implementation

```python
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

**Lines of code: ~20** | **Complexity: Low** ⭐⭐

---

### 🎮 Pygame Implementation

```python
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

**Lines of code: ~65** | **Complexity: Medium** ⭐⭐⭐

---

### 🐢 Turtle Implementation

```python
import turtle
import time

# Setup
screen = turtle.Screen()
screen.setup(700, 500)
screen.title("Clicker")
screen.tracer(0)

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 200)

# Timer display
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.goto(0, -200)

# Click button
button = turtle.Turtle()
button.shape("square")
button.color("red")
button.shapesize(stretch_wid=2.5, stretch_len=5)
button.penup()
button.goto(0, 0)

# Label
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.goto(0, 0)

# State
score = 0
clicks = 0
start_time = None
stop_time = None
running_timer = False

def update_display():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))
    
    if running_timer:
        elapsed = time.time() - start_time
    elif stop_time:
        elapsed = stop_time - start_time
    else:
        elapsed = 0
    
    timer_display.clear()
    timer_display.write(f"Time: {elapsed:.2f}s", align="center", font=("Arial", 18, "normal"))
    
    label.clear()
    label.write("Click Me", align="center", font=("Arial", 16, "normal"))

def handle_click(x, y):
    global clicks, score, start_time, stop_time, running_timer
    
    # Check if click is on button (approximate)
    if -50 < x < 50 and -25 < y < 25:
        clicks += 1
        if clicks == 1:
            start_time = time.time()
            running_timer = True
        elif 2 <= clicks <= 50:
            score += 1
        elif clicks == 51:
            stop_time = time.time()
            running_timer = False

screen.onclick(handle_click)

# Game loop
while True:
    update_display()
    screen.update()
    time.sleep(0.016)  # ~60 FPS
```

**Lines of code: ~75** | **Complexity: Medium-High** ⭐⭐⭐⭐

*Note: Turtle struggles with precise click detection and lacks built-in UI components*

---

## 📊 Quick Comparison Table

| Feature | Py2D | Pygame | Turtle |
|---------|------|--------|--------|
| **Learning Curve** | ⭐⭐ Easy | ⭐⭐⭐ Moderate | ⭐ Very Easy |
| **Code Verbosity** | ⭐⭐⭐⭐⭐ Minimal | ⭐⭐⭐ Moderate | ⭐⭐⭐⭐ Low |
| **Performance** | ⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐ Limited |
| **Community Support** | ⭐⭐ Growing | ⭐⭐⭐⭐⭐ Massive | ⭐⭐⭐⭐ Strong |
| **Built-in Features** | ⭐⭐⭐⭐ Rich | ⭐⭐⭐ Standard | ⭐⭐ Basic |
| **Production Ready** | ⭐⭐ Prototyping | ⭐⭐⭐⭐⭐ Yes | ⭐ Education Only |
| **Installation** | `pip install` | `pip install` | Built-in |
| **Best For** | Quick Projects | Serious Games | Learning |

---

## 🎵 PySound - Audio Made Simple

Just like **Pygame** has `pygame.mixer`, **PySeries** includes **PySound** for managing game audio and sound effects.

```python
import PySound

# Load and play background music
PySound.load_music("background.mp3")
PySound.play_music(loops=-1)  # Loop forever

# Play sound effects
click_sound = PySound.Sound("click.wav")
click_sound.play()
```

---

## 🌈 Rich Color Palette

Py2D comes with **300+ named colors** built-in, making it easy to design visually appealing games:

```python
# Use descriptive color names
sprite.color("crimson")
background.fill("midnightblue")
text.color("goldenrod")
```

No more memorizing RGB values or hex codes!

---

## 🚀 Getting Started

### Installation

```bash
pip install PySeries
```

### Quick Example

```python
import Py2D

# Create a window
screen = Py2D.Window(title="My First Game", geometry="800x600")

# Add a sprite
player = Py2D.Sprite(screen)
player.Figure(x=400, y=300, shape="circle", radius=25)
player.color("crimson")

# Run the game
screen.run()
```

---

## 🎓 When to Use What?

### Choose **Py2D** if you want:
- To build something quickly with minimal code
- A gentler introduction than Pygame
- Built-in UI components (buttons, scores, timers)
- To prototype game ideas fast

### Choose **Pygame** if you want:
- To build a serious, distributable game
- Maximum control and performance
- Access to a large community and resources
- Industry-standard game development experience

### Choose **Turtle** if you want:
- The absolute simplest way to learn programming
- No installation requirements
- To teach basic coding concepts visually
- Simple drawing and animation projects

---

## 📚 Documentation & Resources

- 📖 [Full Documentation](#) *(coming soon)*
- 💬 [Community Discord](#) *(coming soon)*
- 🎥 [Video Tutorials](#) *(coming soon)*
- 🐛 [Report Issues](#)

---

## 🤝 Contributing

PySeries is open source and welcomes contributions! Whether it's bug fixes, new features, or documentation improvements, we'd love your help.

---

## 💭 Final Thoughts

Each framework has its place:
- **Turtle** is perfect for absolute beginners
- **Py2D** bridges the gap between learning and real development
- **Pygame** is the professional choice for serious projects

Choose the tool that matches your goals and skill level. Happy coding! 🎮✨

---

*Made with ❤️ by Swa459*
