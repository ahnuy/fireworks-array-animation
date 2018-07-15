from tkinter import *
from time import *
from math import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=1200, height=900, background= "black")
screen.pack()
##SKY
y = 0
y2 = 36
skyOptions = ["#02013A","#0F0840","#1B1047","#28184D","#351F53","#41265A",\
              "#4E2E60","#5B3566","#673D6C","#744473","#804C79","#8D547F",\
              "#9A5B86","#A6628C","#B36A92","#C07298","#CC799F","#D980A5",\
              "#E688AB","#F290B2","#FF97B8"]
for sky in range (1,21):
    skyColour = (skyOptions[sky%21]) 
    screen.create_rectangle (0,y,1200,y2, fill = skyColour, outline = skyColour)
    y = y + 36
    y2 = y2 + 36
##STARS
for star in range (50):
    x = randint (0,1200)
    y = randint (0,750)
    size = randint (0,2)
    screen.create_oval (x,y,x+size,y+size, fill = "white", outline = "white")
##MOUNTAINS
screen.create_polygon (-5,710,70,690,215,710,545,645,820,690,940,700,1055,675,1205,655,1205,905,-5,905, fill = "#2C0A2F", outline = "#2C0A2F")
screen.create_polygon (-5,760,160,790,410,700,595,740,875,770,1060,760,1105,735,1205,780,1205,905,-5,905, fill = "#481B3A", outline = "#481B3A")
screen.create_polygon (-5,820,230,820,520,780,935,815,1050,795,1110,810,1205,795,1205,905,-5,905, fill = "#7C3F5E", outline = "#7C3F5E")
screen.create_polygon (-5,880,225,855,525,830,930,870,1025,880,1205,865,1205,905,-5,905, fill = "#AF6985", outline = "#AF6985")
##CLOUDS
for cloud in range (1,30):
    x = randint (100,250)
    y = randint (250,300)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#744473", outline = "#744473")
    y2 = randint (300,325)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#5B3566", outline = "#5B3566")
for cloud in range (1,31):
    x = randint (500,650)
    y = randint (75,125)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#744473", outline = "#744473")
    y2 = randint (125,150)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#5B3566", outline = "#5B3566")
for cloud in range (1,36):
    x = randint (850,1000)
    y = randint (350,400)
    s = randint (40,80)
    screen.create_oval (x,y,x+s,y+s,fill = "#744473", outline = "#744473")
    y2 = randint (400,425)
    screen.create_oval (x,y2,x+s,y2+s,fill = "#5B3566", outline = "#5B3566")
##PARTICLE EMPTY ARRAYS
numparticles = 1000
xp = []
yp = []
size = []
particleColours = ["dodgerblue","deep sky blue","light sky blue"]
particles = []
r = []
angle = []
rspeed = []
xrand = randint(100,950)
yrand = randint(150,450)
##FILL PARTICLE ARRAYS
for i in range (numparticles):
    size.append(randint(0,3))
    xp.append(xrand)
    yp.append(yrand)
    particles.append(0)
    r.append(0)
    angle.append(uniform(0,2*pi))
    rspeed.append(uniform(1,15))
for frame in range (150):
    for p in range (numparticles):
        xp[p] = xp[p] + r[p]*cos(angle[p])
        yp[p] = yp[p] - r[p]*sin(angle[p]) + 0.08*frame**2
        r[p] = r[p] + rspeed[p]
        partcolour = particleColours[p%len(particleColours)]
        if i % 2 == 0:
            particles[p] = screen.create_oval (xp[p],yp[p],xp[p]+size[p],yp[p]+size[p], fill=partcolour, outline=partcolour)
        else:
            particles[p] = screen.create_rectangle (xp[p],yp[p],xp[p]+size[p],yp[p]+size[p], fill=partcolour, outline=partcolour)
    ##MICKEY AND MINNIE ON ROCK
    ##rock
    screen.create_polygon (615,900,672,851,715,792,944,759,1108,752,1200,771,1200,900, fill = "#2B2B29")
    ##mickey head
    screen.create_polygon (959,602,961,630,1006,657,1002,585, fill = "#AA7D77", smooth = True)
    screen.create_polygon (990,539,1043,527,1079,535,1096,550,1110,595,1090,640,1052,658,1003,652,989,638,986,620,960,600,975,539, fill = "black", smooth = True)
    ##mickey ears
    screen.create_polygon (1022,550,1059,475,985,455,952,530, fill = "black", smooth = True)
    screen.create_oval (1086,502,1170,605, fill = "black")
    ##minnie bow
    screen.create_polygon (902,523,943,484,969,483,966,522,932,576,906,573, fill = "#A0295F", outline = "#691342", width = 2, smooth = True)
    screen.create_polygon (898,530,943,494,953,494,946,508, fill = "#691342", smooth = True)
    screen.create_polygon (914,547,884,515,890,490,861,470,837,519,881,566, fill = "#A0295F", outline = "#691342", width = 2, smooth = True)
    screen.create_rectangle (892,520,908,545, fill = "#A0295F", outline = "#691342", width = 2)
    screen.create_line (893,528,887,515,872,511, fill = "#691342", width = 3, smooth = True)
    ##minnie ears
    screen.create_polygon (865,505,790,505,800,575,858,575, fill = "black", smooth = True)
    screen.create_oval (920,511,995,606, fill = "black", outline = "#2B2A30", width = 2)
    ##minnie head
    screen.create_polygon (822,605,808,633,851,679,850,630, fill = "#AA7D77", smooth = True)
    screen.create_polygon (894,682,848,660,814,615,812,593,842,555,872,539,909,543,930,563,948,614,945,641,925,667, fill = "black", smooth = True)
    ##minnie bag
    screen.create_polygon (842,728,797,734,770,781,846,775, fill = "#A0295F", outline = "#691342", width = 2, smooth = True)
    ##mickey left leg
    screen.create_polygon (1002,750,939,728,891,781,967,797,1005,771, fill = "black", smooth = True)
    ##minnie dress
    screen.create_polygon (892,670,906,675,918,664,949,677,960,704,939,721,937,746,952,754,956,770,923,801,858,798,826,780,836,697,830,666,866,671, fill = "#056B77", outline = "#056B77", smooth = True)
    ##minnie strap on dress
    screen.create_line (894,727,921,728,940,745, fill = "#A0295F", width = 5, smooth = True)
    ##minnie tail
    screen.create_line (880,792,878,839,915,872,978,905, fill = "black", width = 3, smooth = True)
    ##minnie hand
    screen.create_polygon (804,770,766,773,740,798,733,804,730,811,747,819,760,826,781,817,821,818,841,806,843,787,823,779, fill = "white", outline = "#B5BABE", width = 3, smooth = True)
    screen.create_oval (796,761,840,787, fill = "white", outline = "#B5BABE", width = 3)
    screen.create_line (799,775,785,784, fill = "#B5BABE", width = 3)
    screen.create_line (802,781,791,791, fill = "#B5BABE", width = 3)
    screen.create_line (739,798,760,786, fill = "#B5BABE", width = 3)
    screen.create_line (748,819,749,807,779,795, fill = "#B5BABE", width = 3, smooth = True)
    ##minnie left arm
    screen.create_polygon (826,718,826,749,795,775,822,785,848,758,848,723, fill = "black", smooth = True)
    ##mickey hand
    screen.create_polygon (895,688,867,666,838,643,835,660,842,669,815,683,814,697,810,707,813,717,814,730,824,742,826,731,850,741,883,739,896,726, fill = "white", outline = "#B5BABE", width = 3, smooth = True)
    screen.create_oval (879,683,912,732, fill = "white", outline = "#B5BABE", width = 3)
    screen.create_line (880,695,871,689,858,687, fill = "#B5BABE", width = 3, smooth = True)
    screen.create_line (880,702,864,696,849,702, fill = "#B5BABE", width = 3, smooth = True)
    screen.create_line (879,710,864,710,857,717, fill = "#B5BABE", width = 3, smooth = True)
    screen.create_line (815,698,840,680, fill = "#B5BABE", width = 3)
    screen.create_line (813,712,832,697, fill = "#B5BABE", width = 3)
    screen.create_line (836,670,851,670, fill = "#B5BABE", width = 3)
    ##mickey left arm
    screen.create_polygon (1015,648,977,653,935,678,890,690,897,722,930,715,977,692,995,668, fill = "black", smooth = True)
    ##mickey body
    screen.create_polygon (999,650,975,675,975,724,984,756,1062,740,1041,712,1043,679,1044,650, fill = "black", smooth = True)
    ##mickey right arm
    screen.create_polygon (1038,652,1067,669,1070,725,1052,755,1039,679, fill = "black", smooth = True)
    ##mickey right leg
    screen.create_polygon (1067,771,1108,754,1107,726,1080,723,1048,745, fill = "black", smooth = True)
    ##mickey pants
    screen.create_polygon (978,733,1017,710,1044,715,1063,745,1074,736,1084,761,1083,788,1061,786,1034,802,994,792,965,801,962,753,983,755,976,745, fill = "#930C10", smooth = True)
    ##mickey tail
    screen.create_line (1027,783,1040,822,1026,867,988,900, fill = "black", width = 3, smooth = True)
##    ##GRASS
##    grassOptions = ["#008000","#009900","#00B300","#00CC00","#00E600"]
##    for grass in range (1000):
##        grassColour = choice(grassOptions)
##        xg = randint (605,1210)
##        yg = randint (880,910)
##        yg2 = randint(880,910)
##        sg = randint (-6,6)
##        screen.create_line (xg,yg,xg+sg,yg2+sg, fill = grassColour, width = 3)
    screen.update()
    sleep(0.00)
    for p in range (numparticles):
        screen.delete (particles[p])

##RANDOM TEXT
screen.create_text (600,450, text="END", font="Consolas 32", fill="pink")
