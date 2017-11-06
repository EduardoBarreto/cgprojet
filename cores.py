from vpython import *

# This version uses VPython slider
# See ButtonsSlidersMenus1 for a version that uses Jupyter slider

cancopy = 'You can Ctrl-C or Command-C copy these RGB and HSV values:\n'
scene.title = cancopy
scene.append_to_title("RGB = <1.000, 0.000, 0.000>, HSV = <0.000, 0.000, 0.000>")

coisa = extrusion(path=paths.arc(radius=2, angle1=-pi / 3, angle2=pi + pi / 3),
                  shape=[[shapes.triangle(length=2), shapes.circle(pos=[0, .5], radius=0.2),
                          shapes.trapezoid(pos=[0, -0.2], width=0.6, height=0.4)],
                         [shapes.rectangle(pos=[0, 1.8], width=1, height=0.3)]],
                  )

C = ['Red', 'Green', 'Blue', 'Hue', 'Saturation', 'Value']
sliders = []


def set_coisa(sl):
    if sl.id < 3:
        rgb = vector(sliders[0].value, sliders[1].value, sliders[2].value)
        hsv = color.rgb_to_hsv(rgb)
        sliders[3].value = int(1000 * hsv.x) / 1000  # reset HSV slider positions; display 3 figures
        sliders[4].value = int(1000 * hsv.y) / 1000
        sliders[5].value = int(1000 * hsv.z) / 1000
    else:
        hsv = vector(sliders[3].value, sliders[4].value, sliders[5].value)
        rgb = color.hsv_to_rgb(hsv)
        sliders[0].value = int(1000 * rgb.x) / 1000  # reset RGB slider positions; display 3 figures
        sliders[1].value = int(1000 * rgb.y) / 1000
        sliders[2].value = int(1000 * rgb.z) / 1000
    coisa.color= rgb
    # For readability, limit precision of display of quantities to 3 figures
    f = "RGB = <{:1.3f}, {:1.3f}, {:1.3f}>, HSV = <{:1.3f}, {:1.3f}, {:1.3f}>"
    scene.title = cancopy + f.format(rgb.x, rgb.y, rgb.z, hsv.x, hsv.y, hsv.z)
 pi=3,14
    ang=0
    while true:
        rate(100)        
    ang=ang + (pi/180)
    if(ang<=(pi/2)):
        coisa.rotate(angle=(pi/180),axis=(0,1,0),origin=(0,0,0)
                     
   if((pi/2) < ang <= pi):
        coisa.rotate(angle=(-pi/180),axis=(1,0,0),origin=(0,0,0))

scene.caption = '\n'
for i in range(6):  # Create the 3 RGB and 3 HSV sliders
    sliders.append(slider(length=300, left=10, min=0, max=1, bind=set_coisa, id=i))
    scene.append_to_caption('    ' + C[i] + '\n\n')  # Display slider name
    if i == 2: scene.append_to_caption("\n\n")  # Separate the RGB and HSV sliders
sliders[0].value = 1
sliders[4].value = sliders[5].value = 1
set_coisa(sliders[0])
