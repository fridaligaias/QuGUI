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

master = Tk()
master.configure(background='LightSkyBlue3')


class Frames(object):
    def newWindow(self):

        win = tk.Toplevel()
        win.iconbitmap(r'C:\Users\hp\Downloads\win_icon-_1_.ico')
        win.title('A Guide to Using QuGUI V2')

        qu1 = tk.PhotoImage(file = "qu1.gif")
        ex1 = tk.PhotoImage(file = "ex1.gif")
        ex2= tk.PhotoImage(file = "ex2.gif")
        ex3 = tk.PhotoImage(file ="ex3.gif")
        ex4 = tk.PhotoImage(file ="ex4.gif")
        ex5 = tk.PhotoImage(file ="ex5.gif")

        frame1 = tk.Frame( master = win, bg = 'thistle')
        frame1.pack(fill='both', expand='yes')


        editArea = tkst.ScrolledText(
            master = frame1,
            wrap   = tk.WORD,
            width  = 80,
            height = 30,
        )

        editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        editArea.insert(tk.INSERT,
        """\
        QuGUI \n An interactive interface for numerical experiments of the dynamics of a qubit.
        \n \n First of all, what are 'dynamics'? Dynamics are all about motion, what causes it, how and to what extent. Therefore, QuGUI is helpful for observing the motion of a qubit, expressed in a mathematical way.
        """)
        editArea.image_create(tk.END, image = qu1)
        editArea.insert(tk.INSERT,
        """\
        \n The diagram above depicts one of many representations of a qubit, this one specifically has taken insipiration from the 'Bloch sphere' but has been, as it could be said, simplified for the purpose of this project.
        In the diagram, only the upper half of the 'sphere' is in fact what we will define as the qubit, the lower half being redundant. The redundancy is due to the fact that any point on the upper half of the sphere has an 'equivalent' point on the lower half and, although negative, is ultimatly the same as its analogous point.
        We can also see the two variables that determine the qubit's initial position: \u03B8 and \u03C6. The position of the qubit is in this case rapresented by \u03C8, the red arrow.
        To understand how the initial position is defined in QuGUI, we can compare the qubit to the more well know bit: it can be said that a qubit is every possible state inbetween |\u03C8\u27E9 = 0 and |\u03C8\u27E9 = 1 (otherwise know as the bit's on/off or True/False states), this other state inbetween is defined as a 'superposition' and it's what makes the qubit different.
        |\u03C8\u27E9 is defined by the equation: \n |\u03C8\u27E9 = cos\u03B8|0\u27E9 + sin\u03B8e\u2071\u1D60|1\u27E9 \n
        To make sense of this equation, it's useful to know the following: \n |\u03B1\u00B2|=cos(\u03B8)\u00B2 \u2192 the probability of finding the qubit in the |0\u27E9 position \n |\u03B2\u00B2|=sin(\u03B8)\u00B2 \u2192 the probability of finding the qubit in the |1\u27E9 position \n keeping in mind that |\u03B1\u00B2| + |\u03B2\u00B2| =1 \u2192 \u03B1=cos(\u03B8), \u03B2=sin(\u03B8)e\u2071\u1D60
        \u2192 |\u03C8\u27E9 = \u03B1|0\u27E9 + \u03B2|1\u27E9
        \n \n To see how a qubit can change it's possition and how, or better yet, to see it's dynamic effect, we can manipulate it using an impulse.
        This impulse is in turn also defined by various parameters: A (AMPLITUDE), \u03C9 (FREQUENCY) and T (PERIOD). \n This QuGUI shows the probability of where the position of a qubit may be, as in, how probable it is for the qubit to be in the |0\u27E9 position or |1\u27E9 position after being affected by an impulse of chosen magnitude.

        \n Hopefully it's now clear what the parameters of QuGUI are for, but if you are looking for specific results, here are some examples:
        To obtain the following, maintain the \u03B8 and \u03C6 angles for the initial position of the qubit at the ground state (as in, the default values).
        """)
        editArea.image_create(tk.END, image= ex1)
        editArea.insert(tk.INSERT,
        """\
        \n \u21B3 A qubit has been influenced by an impulse but with no lasting effect as it can be seen by the return to the initial values of probability for either state.
        """)
        editArea.image_create(tk.END, image = ex2)
        editArea.insert(tk.INSERT,
        """\
        \n \u21B3 Similar to the one above, the impulse doesn't have a substantial effect on the qubit's probability of being either state |0\u27E9 or |1\u27E9. However, due to the higher A value the effect is increased in magnitude and has higher rate of oscillation before settling into a position where the probability if being at either state is decreased and is closer to a superposition.
        """)
        editArea.image_create(tk.END, image = ex3)
        editArea.insert(tk.INSERT,
        """\
        \n \u21B3 Again, another case where the final position is not affected much but the rate of oscillation is clearly inscreased by a notable factor due to the increase of this time not only the A value but of both the \u03C9 and T values. Yet, unlike the previous example, the final position is most definetely similar if not the same as the initial.
        """)
        editArea.image_create(tk.END, image= ex4)
        editArea.insert(tk.INSERT,
        """\
        \n \u21B3 This example portrays the position probabilities of a qubit that has been affected by an impulse with relatively high A and \u03C9 values but a rather low T value. This is one of the more interesting results as it depicts a qubit whose initial position has been completely switched, with very little oscillation. [# NOTE: A similar result can be obtained but with the initial probabilities reversed if the \u03B8 value is changed from 0 to 90 ]
        """)
        editArea.image_create(tk.END, image=ex5)
        editArea.insert(tk.INSERT,
        """\
        \n \u21B3 For this last example, we can see another very interesting result: an example of '50/50' superposition. With a moderatly high A value but low \u03C9 and T values, the impulse oscillates the qubit and leaves it with a 50/50 chance of being in either |0\u27E9 or |1\u27E9 states. [ # NOTE: This idea of having the same probability of being at either state can be likened to Schrödinger's thought experiment, 'Schrödinger's cat' ]
        """)

        editArea.config(state=DISABLED);
        win.mainloop()

        ######



    def mainFrame(self, master):

        master.title('QuGUI V2')
        ##add a text widget that says : Interactive GUI for numerical experiments of the dynamics of an isolated qubit
        master.iconbitmap(r'C:\Users\hp\Downloads\master_icon.ico')
        master.geometry("1200x700")

        ###THE BUTTON FOR THE HELP WINDOW
        button1 =Button(master, text ="HELP!", command =self.newWindow, activebackground = 'yellow')
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

        Label(master,text=u"Insert \u03C9 value:", font='system', background = 'turquoise1').grid(row=0,column=0)
        e1 = Entry(master, textvariable=omega)

        s1 = Scale(master, from_=omega.get(), to=4.0, variable=omega, resolution=0.1,
                   orient=HORIZONTAL, length=360, width=20, background = 'CadetBlue1',
                   activebackground = 'yellow',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        s1.grid(row=0,column=1)

        LL = Label(master,text= u"Insert \u0391 value:", font='system', background = 'SeaGreen3')
        LL.grid(row=1,column=0)
        e2 = Entry(master, textvariable=amp)

        s2 = Scale(master, from_=amp.get(), to=10.0, variable=amp, resolution=0.1,
                   orient=HORIZONTAL, length=360, width=20, background = 'SeaGreen3',
                   activebackground = 'yellow',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        s2.grid(row=1,column=1)

        e3 = Label(master, text= u"Insert \u03A4 value:", font='system', background= 'MediumPurple1')
        e3.grid(row=2, column=0)
        e3= Entry(master, textvariable=period)

        scale3 = Scale(master, from_=period.get(), to=6.0, variable=period, resolution=0.1,
        orient=HORIZONTAL, length=360, width=20, background= 'MediumPurple1',
        activebackground= 'yellow',
                   command=lambda o: plot_waveform(T=period.get(),A=amp.get(),omega=omega.get()))
        scale3.grid(row=2, column=1)

        #THETA
        theta = DoubleVar()
        labelText4 = StringVar()

        e4 = Label(master, text= u"Insert \u03F4 value:", font='system', background= 'SlateBlue1')
        e4.grid(row=3, column=0)
        e4 = Entry(master, textvariable=theta)

        scale4 = Scale(master, from_=0, to=180, variable=theta, resolution=1,
        orient=HORIZONTAL, length=360, width=20, background= 'SlateBlue1',
        activebackground='yellow')
        #make default 180
        scale4.grid(row=3, column =1)

        #PHI
        phi = DoubleVar()
        labelText5 = StringVar()

        e5= Label(master, text= u"Insert \u03A6	value:", font= 'system', background='salmon')
        e5.grid(row=4, column=0)
        e5= Entry(master, textvariable=phi)

        scale5 = Scale(master, from_=0, to=360, variable=phi, resolution=1,
        orient=HORIZONTAL, length= 360, width=20, background='salmon',
        activebackground='yellow')
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
            #y0=[ np.sin(th0) * np.exp(1j*phi0), np.cos(th0) ]
            y0= [np.cos(th0/2) * np.exp(-1j*phi0), np.sin(th0/2) ]
            #sol = solve_ivp(lambda t,y: odefunc(t,y,A,w,T), [-5*T,5*T], y0)
            sol = solve_ivp(odefunc, [-5*T,5*T], y0, t_eval=t, method='BDF')

            #y = sol.sol(t)
            plot_sol(sol.t, sol.y.T)

        b1=Button(master, text='GO',font='system', command=solve_ode,background = 'LightSkyBlue3', activebackground = 'yellow' )
        b1.grid(row=5,column=0)
        b1.bind("<Return>, Button")

        # GRAPH
        ## matplotlib commands
        f = Figure(figsize=(10,4), dpi=100)
        a = f.add_subplot(121)
        b = f.add_subplot(122)
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

            #vector
            v0 = y[:,0]
            v1 = y[:,1]

            phase = np.exp(-1j*np.angle(v1))

            v0 = v0 * phase
            v1 = v1 * phase

            phi = np.angle(v0 * np.sign(np.real(v1)))
            phi = phi + 2.0*np.pi*(phi<0)
            phi = phi / (2.0*np.pi)


            #b.plot(t,P[:,0],label='P(1)')
            b.plot(t,P[:,1],label='P(0)')
            b.plot(t, phi, label='phi')
            #b.plot(t,P[:,1],y, label='P(0)')


            b.legend(loc="center left")
            b.set_title("Probabilities w="+str(omega.get())+" A="+str(amp.get())+" T="+str(period.get()))

            #b.plot(y, label='phi')
            #b.legend(loc="center right")

            canvas.draw()

        # position the canvas
        canvas.get_tk_widget().grid(row=5,column=1)



app = Frames()
app.mainFrame(master)
master.mainloop()
