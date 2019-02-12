GlowScript 2.7 VPython
'''
Earthorbit.py
Simulate the orbit of earth or a planet aound a star 
'''
def keyInput(evt):
    s = evt.key
    if s == "b":
        earth.vel = earth.vel *1.5 
        print(earth.vel) 
    if s == "r":
        earth.vel = earth.vel /2.0
        print(earth.vel) 
scene.bind ('keydown', keyInput)
def keyIRel(evt):
    s = evt.key
    if s = 'keyup':
        earth.vel = earth.vel
scene.bind('keyup', keyIRel)
#define constants 
G = 6.67E-11
AU = 1.5E11 #this is one astronomical unit the Earth-sun distance
YEAR = 365.25 * 24 * 60 * 60
#create objects for sun and earth 
starA= sphere(pos=vec(-AU,0,0), mass = 2E30, radius = 1E10, color = color.yellow)
starB = sphere(pos=vec(AU,0,0), mass = 2E30, radius = 1E10, color = color.red)
planet = sphere(pos=vec(0,AU,0), mass = 2E26, radius = 1E9, color = color.cyan)
planet2=sphere(pos=vec(0,AU,0), mass = 2E26, radius = 1E9, color = color.green)
#initial conditions 
starA.vel = vec(0, 1.1E4,0)
starB.vel = vec(0,-1.1E4,0)
planet.vel = vec(1.1E3,2.2E3,1.1E4)# edited planet's z component
planet2.vel=vec(1.15E3,2.2E3,1.1E4)

starA.trail = curve(pos=starA.pos, color = starA.color)
starB.trail = curve(pos=starB.pos, color = starB.color)
planet.trail = curve(pos=planet.pos, color = planet.color)
planet2.trail=curve(pos=planet2.pos,color=planet2.color)
counter = 0 #for printing values 
L = vector(0,0,0) #angular momentum 
rmin = AU
rmax = 0 
t = 0

#time step 
h = 1E5
scene.autoscale = 1 

while True: #loop through calculations to animate
    #determine rmin and rmax to figure out a semimajor axis
    r = mag(starA.pos - starB.pos)
    F = -G*starA.mass*starB.mass*(starA.pos-starB.pos)/r**3 #this is the force on star A 
    #the force on star B will be the negative of star A 
    starA.vel = starA.vel + F/starA.mass*h
    starB.vel = starB.vel - F/starB.mass*h
    starA.pos = starA.pos + starA.vel*h 
    starB.pos = starB.pos + starB.vel*h 
    starA.trail.append(pos=starA.pos, color = starA.color)
    starB.trail.append(pos=starB.pos, color = starB.color)
    
    
    accP = -G*starA.mass*(planet.pos - starA.pos)/(mag(planet.pos - starA.pos))**3-G*starB.mass*(planet.pos - starB.pos)/(mag(planet.pos - starB.pos))**3
    
    planet.vel = planet.vel + accP*h
    planet.pos = planet.pos + planet.vel*h
    planet.trail.append(pos=planet.pos)
    
    planet2.vel = planet2.vel + accP*h
    planet2.pos = planet2.pos + planet2.vel*h
    planet2.trail.append(pos=planet2.pos)
    
    
    
    t = t + h
    rate(100)
