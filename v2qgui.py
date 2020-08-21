import numpy as np
import scipy as scipy
from scipy.integrate import solve_ivp
from tkinter import *
import tkinter as tk
import tkinter.scrolledtext as tkst


import matplotlib
matplotlib.use("tkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

master = Tk()
master.configure(background='azure3')


class Frames(object):
    def newWindow(self):

        win = tk.Toplevel()
        win.iconbitmap(r"C:\Users\hp\Desktop\GRC\win_icon-_1_.ico")
        win.title('A Guide to Using QuGUI V2')
        # IMAGES


        frame1 = tk.Frame( master = win, bg = 'khaki1')
        frame1.pack(fill='both', expand='yes')
        F_font = (15)

        editArea = tkst.ScrolledText(
            master = frame1,
            wrap   = tk.WORD,
            width  = 80,
            height = 30,
            font = F_font
        )
        editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        editArea.insert(tk.INSERT,
        """
        \n
        The \u03C6 phase
        \n To introduce this new way of studying the qubit's dynamics, we have to consider what qualities can be described once the \u03C6 phase is known. \n Let's consider the following questions:
        \n \t 1. Vertical motion (up/down)
        \n \t 2. Motion along the x axis (if there is, is it negative/positive?)
        \n \t 3. Motion along the y axis (if there is, is it negative/positive?)
        \n Now, let's visualise a group, or better, a 'beam' of atoms, that are magnetic (of iron, perhaps). \n Let's make it go through the gap inbetween the two ends of a horseshoe magnet. Can you imagine it? \n In a 'classical' situation, due to their magnetism, the atoms would spread out and the range of the beam would 'enlarge'. \n However, this is not the case when it's done experimentally. \n Instead, the beam splits in two: the 'projection' along the x-axis is either up or down [50/50].
        \n If a beam is put through a horseshoe magnet with an orientation towards the right [a C shape], a part of the beam will go "all the way up". \n If then, the same beam is consequently put through another horseshoe magnet with this time an upwards orientation [a U shape], the question changes, yet regardless of any previous results, the beam will go either right or left.
        \n However, there's always a contact with classical mechanics, even if, in practice, the questions are always the same three: does the atom have a vertical orientation (up or down), one along the x-axis (positive or negative) or one along the y-axis (positive or negative).
        \n The orientation of an object is always 'written' somewhere within it- the question is, how do we 'read' it? \n The answer lies within the state of the atom; if the state is completely undefined, it still has a probability of being up/down. \n The new value of \u03B8, could perhaps have, \u2153 'up' orientation and \u2154 'down' orientation. \n This means the state is inclined, depending on how \u03B8 is changed. \n If \u03B8 needs to be measured, the ratio of intensity between the up\down values ​​must be measured. \n Talking about orientation, the \u03B8 angle can be compared to 'altitude', whilst the \u03C6 angle with 'longitude'.
        \n Let's take a case where \u03B8 = 90\u00B0 and \u03C6 = 0\u00B0. Due to the fact that it is on the horizontal plane, if the magnet splits the beam in two, and if \u03C6 is different from 0, there will always be a different distribution caused by the magnet on the plane, even if \u03B8 remains the same. \n This is always the mean value of the orientation.
        \n As it can be seen, orientation may be 'classically' well defined, but it is not the case in quantum mechanics. As some call it, there is not the same 'sharpness'. \n However, if there are many and you take the mean values, then, on average, you get 'an orientation'. \n This comes from a certain process, roughly it looks like this:
        \n \t STATE \u27f6 PROCEDURE \u27f6 MEAN VALUE
        \n But what is the 'procedure'? It is a set of questions. \n The type of questions depend on the mathematics of the problem.
        \n Let's take a step back. A vector is determined by its components. \n In classical mechanics, the measurements [of the components] are that of the state of the vector - there is no ambiguity. \n The difference between the way in which a problem is described in quantum mechanics, is that the state and the values change when the system is described.
        \n If there is a system, for instanceour |\u03C8\u27E9 = cos\u03B8|0\u27E9 + sin\u03B8e\u2071\u1D60|1\u27E9, what is the mean value of the z component? \n The 'procedure' is needed to find out. \n It's based on the state and on a set of observable factors, put on the state. These observable factors are the x, y, and z components. \n The observable factors, given a state, become matrices (that are general operators), more specifically three, one for each direction. \n After a series of mathematical operations, the mean value of the component along z, y and x is obtained. \n The possible values that can be obtained by measuring may be all 'up', 'down', 'left', 'right', 'forwards', and 'back'.
        \n You might be asking yourself, what's in the system? What can be measured? \n From the procedure, given the state, cos\u03B8|0\u27E9 [latitude] + sin\u03B8e\u2071\u1D60|1\u27E9 [longitude], the two values are 'close relatives' of the angles used to describe the position on an object (take note of the square brackets). \n Usually, the state is written as a function of similar angles to \u03B8 and \u03C6, that correspond with angles that would be measured after the procedure.
        \n In order to describe an object's orientation, there are 'standards'. \n The most used convention for the orientation, is to start from an axis. 2 angles are needed. \n The first is the angle the object has in relation to the z axis, an angle similar (but not the same!) as our angle \u03B8. \n On the horizontal,
        \n \t \t \t \t \u2191 \u21e8 \u03B8 = 0\u00B0
        \n \t \t \t \t \u2192 \u21e8 \u03B8 = 90\u00B0
        \n \t \t \t \t \u2193 \u21e8 \u03B8 = 180\u00B0
        \n This corresponds with the 'latitude'. (Note that this new version of QuGUI, V2.4, the \u03B8 is at 180\u00B0 at default.) \n The second angle, which corresponds with the 'longitude', taking the projection on the horizontal plane, corresponds to how much it 'turns'. If it turns counterclockwise:
        \n \t \t \t \t \u2192 \u21e8 \u03C6 = 0\u00B0
        \n \t \t \t \t \u2191 \u21e8 \u03C6 = 90\u00B0
        \n \t \t \t \t \u2190 \u21e8 \u03C6 = 180\u00B0
        \n Now, the equation has changed and become:
        \n |\u03C8\u27E9 = sin(\u03B8/2)|0\u27E9 + cos(\u03B8/2)e\u2071\u1D60|1\u27E9
        \n With the previous \u03B8 and \u03C6, \u03B8, instead of being at its usual, positive, angle, it was oriented 'down', remaining as 0. \n If the (overall) mean value of the z needs to be calculated, and we have a wide range and many, independent, average values, a magnet can be alligned on the z axis and depending on the proportion of how the beam goes 'up'/'down', the result is given. \n They can be 'recontructed' as an mean value, which are, on average, those given by the \u03C6 and \u03B8 values.
        \n Let's move on to talking in more detail about the 'procedure'. \n On a side, let's also keep in mind that vectors are the 'quantic amplitudes', and that the 'operators' are:
        \n sin(\u03B8/2) \u21e8 'down' \n cos(\u03B8/2)e\u2071\u1D60 \u21e8 'up' \n (3 2x2 matrices) \n [along the z axis] [along the x axis] [along the y axis]
        \n The mean of the state is given by the product of the matrix \u22C5 vector. \n Let's look at a few, very simple examples:
        \n If we get
        \n \t (\u2154) 'up' orientation and, (\u2153) 'down' orientation. \t \t \u21e8 the mean value is (\u2153) 'up'
        \n [A breif side note: \n \u03B8 range = 180, \n \u03C6 range = 360]
        """)

        editArea.config(state=DISABLED);
        win.mainloop()


    def mainFrame(self, master):

        master.title('QuGUI')
        ##add a text widget that says : Interactive GUI for numerical experiments of the dynamics of an isolated qubit
        master.iconbitmap(r"C:\Users\hp\Desktop\GRC\icons\master_icon.ico")
        master.geometry("1200x700")

        ###THE BUTTON FOR THE HELP WINDOW
        button1 =Button(master, text ="HELP!", command =self.newWindow, activebackground = 'azure4')
        button1.grid(row=7, column=0)


        # AMPLITUDE VALUE
        amp = DoubleVar()
        labelText2 = StringVar()
        amp.set(0.1)
        # OMEGA VALUE
        omega = DoubleVar()
        omega.set(0.1)
        labelText = StringVar()
        # PERIOD VALUE
        period = DoubleVar()
        labelText3 = StringVar()
        period.set(0.5)

        Label(master,text=u"Insert \u03C9 value:", font='system', background = 'azure2').grid(row=0,column=0)
        e1 = Entry(master, textvariable=omega)

        s1 = Scale(master, from_=omega.get(), to=4.0, variable=omega, resolution=0.1,
                   orient=HORIZONTAL, length=360, width=20, background = 'azure2',
                   activebackground = 'azure4',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        s1.grid(row=0,column=1)

        LL = Label(master,text= u"Insert \u0391 value:", font='system', background = 'azure2')
        LL.grid(row=1,column=0)
        e2 = Entry(master, textvariable=amp)

        s2 = Scale(master, from_=amp.get(), to=10.0, variable=amp, resolution=0.1,
                   orient=HORIZONTAL, length=360, width=20, background = 'azure2',
                   activebackground = 'azure4',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        s2.grid(row=1,column=1)

        e3 = Label(master, text= u"Insert \u03A4 value:", font='system', background= 'azure2')
        e3.grid(row=2, column=0)
        e3= Entry(master, textvariable=period)

        scale3 = Scale(master, from_=period.get(), to=6.0, variable=period, resolution=0.1,
        orient=HORIZONTAL, length=360, width=20, background= 'azure2',
        activebackground= 'azure4',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        scale3.grid(row=2, column=1)

        #THETA
        theta = DoubleVar()
        labelText4 = StringVar()

        e4 = Label(master, text= u"Insert \u03F4 value:", font='system', background= 'azure2')
        e4.grid(row=3, column=0)
        e4 = Entry(master, textvariable=theta)

        scale4 = Scale(master, from_=0, to=90, variable=theta, resolution=1,
        orient=HORIZONTAL, length=360, width=20, background= 'azure2',
        activebackground='azure4')
        scale4.grid(row=3, column =1)

        #PHI
        phi = DoubleVar()
        labelText5 = StringVar()

        e5= Label(master, text= u"Insert \u03A6	value:", font= 'system', background='azure2')
        e5.grid(row=4, column=0)
        e5= Entry(master, textvariable=phi)

        scale5 = Scale(master, from_=0, to=360, variable=phi, resolution=1,
        orient=HORIZONTAL, length= 360, width=20, background='azure2',
        activebackground='azure4')
        scale5.grid(row=4, column=1)

        ###CALCULATIONS + Button
        def waveform(t, A=1, omega=1, T=1):
            #tau=omega/100;
            #return(A/(1+np.exp((np.abs(t)-T)/tau)))
            return(A*np.cos(omega*t)*np.exp(-t*t/(2*T*T)))

        def odefunc(t,y):
            A=amp.get(); w=omega.get() ; T=period.get()
            sigmax = np.array([ [0, 1], [1,  0] ] )
            sigmaz = np.array([ [1, 0], [0, -1] ]);
            f=waveform(t, A,w,T)
            #ret =np.array([ -1j * f * y[1], -1j * (f * y[0] + y[1]) ])
            ret = (1j * sigmaz @ y + 1j * f * sigmax @ y)/2
            return ret

        def solve_ode():
            # collect the variables for the initial condition
            th0=(np.pi/180.0)*theta.get(); phi0=(np.pi/180.0)*phi.get()
            # collect the variables for the waveform
            A=amp.get(); w=omega.get() ; T=period.get()
            # print("Solving for A=",A,"T=",T,"omega=",w);
            # the time that we use to solve the ode
            t = np.linspace(-5*T, 5*T, num=500)

            # the starting vector
            y0=[ np.sin(th0) * np.exp(1j*phi0), np.cos(th0) ]
            #sol = solve_ivp(lambda t,y: odefunc(t,y,A,w,T), [-5*T,5*T], y0)
            sol = solve_ivp(odefunc, [-5*T,5*T], y0, t_eval=t, method='BDF')

            #y = sol.sol(t)
            plot_sol(sol.t, sol.y.T)

        b1=Button(master, text='GO',font='system', command=solve_ode,background = 'azure2', activebackground = 'azure4' )
        b1.grid(row=5,column=0)
        b1.bind("<Return>, Button")

        # GRAPH
        ## matplotlib commands
        f = Figure(figsize=(10,4), dpi=100)
        a = f.add_subplot(131)
        b = f.add_subplot(132)
        c = f.add_subplot(133, projection='3d')
        ## tkinter-matplotlib connection
        canvas = FigureCanvasTkAgg(f, master=master)
        canvas.draw()

        # create the plot and update the canvas

        def plot_waveform(A=1, omega=1, T=1):
            #print(A,T,omega)
            t = np.linspace(-5*T,5*T,num=500)
            a.clear()
            a.plot(t, waveform(t,A,omega,T) )
            canvas.draw()

        plot_waveform(A=amp.get(), omega=omega.get(), T=period.get() )

        def plot_sol(t,y):
            b.clear()
            #print(y)
            #y = np.linspace(0,np.pi,10)
            #print (y)

            P = np.abs(y)**2

            v0 = y[:,0]
            v1 = y[:,1]
            phase = np.exp(-1j*np.angle(v1))
            v0 = v0 * phase
            v1 = v1 * phase
            phi = np.angle(v0 * np.sign(np.real(v1)))
            phi = phi + 2.0*np.pi*(phi<0)
            b.plot(t,P[:,1],label='P(0)')
            b.plot(t,phi/(2.0*np.pi),label='phi')
            #b.plot(t,P[:,0],label='P(1)')
            #b.plot(t,P[:,1],y, label='P(0)')

            b.legend(loc="center left")
            b.set_title("Probabilities w="+str(omega.get())+" A="+str(amp.get())+" T="+str(period.get()))

            #b.plot(y, label='phi')
            #b.legend(loc="center right")
            c.clear()
            # make a sphere
            foo,bar = np.mgrid[0.0:np.pi:50j,0.0:2.0*np.pi:50j]
            z = np.cos(foo)
            y = np.sin(foo) * np.cos(bar)
            x = np.sin(foo) * np.sin(bar)
            c.plot_surface(x,y,z, rstride=1, cstride=1,
                           color='r', alpha=0.3, linewidth=0)


            # get theta
            theta = np.pi-2*np.arccos(P[:,1])
            z = np.cos(theta)
            y = np.sin(theta) * np.cos(phi)
            x = np.sin(theta) * np.sin(phi)
            c.plot(x,y,z)

            canvas.draw()

        # position the canvas
        canvas.get_tk_widget().grid(row=5,column=1)

app = Frames()
app.mainFrame(master)
master.mainloop()
