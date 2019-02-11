GlowScript 2.7 VPython
'''
monteCarloElectronScattering in 3D
'''

# initial conditons for gold
mass = 9.11e-31 # in kg
massG = 196 # gram/mole
#massG = 3.2e-22
density = 19.3 #in g/cm3
D = 0.5 # slab thickness in micrometers
Z = 79
eradius = 1e-9 # in micro meter
Vx = 40000000
Vy = 40000000
Vz = 40000000
num_electrons = 1000
V= sqrt(Vx**2 + Vy**2 + Vz**2)
T = 0.5 * mass * V**2 * 6.42e18 * 0.001# initial energy in Kilo electron volts
B = V/2.8e8

electron_list = []
bScattered = 0
absorbed = 0
transmitted = 0

slab = cylinder(pos = vector(-0.5,0, 0), axis = vec(2,0,0), radius = 0.01, color = color.red)
slab2 = cylinder(pos = vector(-0.5,-D, 0), axis = vec(2,0,0), radius = 0.01, color = color.red)

for i in arange(num_electrons):
    part = sphere(color=color.yellow, radius=0.01)
    part.pos=vector(0,0,0)
    part.trail= curve(pos=part.pos, color=color.yellow, radius=0.001)
    electron_list.append(part)
    
 
def move(thetaN, phiN, T):
    global bScattered
    global absorbed
    global transmitted
    for i in arange (num_electrons):
        rand1 = random() 
        rand2 = random()
        rand3 = random()
    
        theta = acos(1- 2*B*rand1/(1 + B-rand1))
        phi = 2*pi*rand2
    
        thetaN1 = acos(cos(thetaN) * cos(theta) + sin(thetaN) * sin(theta) * cos(phi))
        phiN1 = atan(sin(thetaN*sin(theta)*sin(phi))/(cos(theta)-cos(thetaN1)*cos(thetaN))) + phiN
    
        Sn = -1.02 * B * (B+1) * massG * T**2 * log(rand3) / ( Z * (Z+1) * density)
      

        Rx = Sn * (sin(thetaN1) * cos(phiN1))
        Ry = Sn * (sin(thetaN1) * sin(phiN1))
        Rz = Sn * (cos(thetaN1))
   
        dTds = -7.83 * (density * Z/(massG * T)) * log(174*T/Z)

        T = T - abs(dTds) * Sn
   
        thetaN = thetaN1
        phiN = phiN1
    
        electron_list[i].pos.x = electron_list[i].pos.x + Rx
        electron_list[i].pos.y = electron_list[i].pos.y - Ry
        electron_list[i].pos.z = electron_list[i].pos.z - Rz
        electron_list[i].trail.append(pos = electron_list[i].pos)
        
       
scene = display(title='Random Walk 2D', x=300, y=0, width = 800, height = 800)

thetaN = acos(Vz/V) # initial theta
phiN = acos(Vx/sqrt(Vx**2 + Vy**2))   # initial pheta

while True:
    move(thetaN, phiN, T)
    rate(10)
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
