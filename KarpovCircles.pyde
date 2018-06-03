'''From a Tweet from Peter Karpov
June 1, 2018
with Curtis'''

def setup():
    global new_r,n_sides
    new_r = 300.0
    n_sides = 600
    size(600,600)
    colorMode(HSB)
    noStroke()
    
def draw():
    background(100)
    global new_r,n_sides
    translate(width/2,height/2)
    rotate(-PI/2)
    while n_sides > 2:
        fill(255)
        #fill(255-(40*n_sides-20),255,255) #rainbow polygons
        beginShape()
        for n in range(n_sides):
            angle = 2*n*PI/n_sides
            vertex(new_r*cos(angle),
                   new_r*sin(angle))
            #rotate()
        endShape(CLOSE)
        #println(new_r)
        new_r = new_r * cos(PI/n_sides)
        n_sides -= 1
        fill(0) #black circle
        ellipse(0,0,2*new_r,2*new_r)
    noLoop()
    
    