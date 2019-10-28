from __future__ import division, print_function

import vpython as vp
from vpython import *

# rod = cylinder(pos=vector(0,2,1),
#         axis=vector(5,5,5), radius=1)
#
# rod.color = vector(0,0,1)
#
#
# rod.rotate(angle=60,
#            axis=vec(0,0,0),
#            origin=vector(1,5,4))
# rate( 100 )

# f1 = gcurve(color=color.cyan)	# a graphics curve
# for x in arange(0, 8.05, 0.1):	# x goes from 0 to 8
#     f1.plot(pos=(x,5*cos(2*x)*exp(-0.2*x)))	# plot
#
# f1 = gcurve(data=[ [1,2],[5,-2],[8,4] ],
#             color=color.green)
# f1.plot(data=[100,-30]) # add a single point
# f1.plot(data=[[100,-30], [20,50], [0,-10]]) # add a list
# f1.plot(1,2)
# f1.plot([1,2])
# f1.plot([1,2], [3,4], [5,6])
# f1.plot([ [1,2], [3,4], [5,6] ])
# f1 = gcurve(color=color.cyan)
# f2 = gvbars(delta=0.05, color=color.blue)
# for x in arange(0., 8.05, 0.1):
#     f1.plot(x,5*cos(2*x)*exp(-0.2*x))	 # gcurve
#     f2.plot(x,4*cos(0.5*x)*exp(-0.1*x)) #vbars
# f1.data = [ [10,20], [30,40], [50,60] ]

# box()
# def B(b):
#     print("The button said this: ", b.text)
# button( bind=B, text='Click me!' )
# scene.append_to_caption('\n\n')
#
# def R(r):
#     print(r.checked) # alternates
# radio(bind=R, text='Run') # text to right of button
# scene.append_to_caption('\n\n')
#
# def C(r):
#     print(r.checked) # alternates
# checkbox(bind=C, text='Run') # text to right of checkbox
# scene.append_to_caption('\n\n')
#
# def S(s):
#     print(s.value)
# slider( bind=S )
# scene.append_to_caption('\n\n')
#
# def M(m):
#     print(m.selected, m.index)
# menu( choices=['cat', 'dog', 'horse'], bind=M )
# scene.append_to_caption('\n\n')
#
# def T(s):
#     print(s.text, s.number)
# winput( bind=T )


handle = cylinder( size=vector(1,.2,.2),                   color=vector(0.72,0.42,0) )

head = box( size=vector(.2,.6,.2), pos=vector(1.1,0,0),              color=color.gray(.6) )

hammer = compound([handle, head])
hammer.axis = vector(1,1,0)
