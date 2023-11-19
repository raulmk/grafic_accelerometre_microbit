#Grafico temperatura

def on_forever():
    led.plot_bar_graph(input.temperature(), 50)
basic.forever(on_forever)


#Mover gota

x = 2
y = 2

def on_forever():
    
    led.plot(x, y)

    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)

    if accX <= 150 and x > 0:
        x -= 1
    if accX > 150 and x < 4:
        x += 1
    if accY <= 150 and y > 0:
        y -= 1
    if accY > 150 and y < 4:
        y += 1
