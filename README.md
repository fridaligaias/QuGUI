# QuGUI V2.4 "QuPhiGUI" Abstract
*Modified and extented version of the application. Includes 3D model of qubit orientation probability.*

To introduce this new way of studying the qubit's dynamics, we have to consider what
qualities can be described once the ' phase is known.
Let's consider the following questions:
1. Vertical motion (up/down)
2. Motion along the ![equation](https://latex.codecogs.com/gif.latex?x) axis (if there is, is it negative/positive?)
3. Motion along the ![equation](https://latex.codecogs.com/gif.latex?y) axis (if there is, is it negative/positive?)

Now, let's visualise a group, or better a beam of atoms, that are magnetic (iron, perhaps).
Let's make it go through the gap in between the two ends of a horseshoe magnet. Can you
imagine it?

In a *classical* situation the atoms would spread out and the range of the beam would
'enlarge'- due to their magnetism. However, this is not the case when it's done experimen-
tally. Instead, the beam splits in two: the 'projection' along the ![equation](https://latex.codecogs.com/gif.latex?x) axis is either 'up' or 'down' [50/50].

If a beam is put through a horseshoe magnet with an orientation towards the right [a C
shape], a part of the beam will go "all the way up". If then, the same beam is consequently
put through another horseshoe magnet with this time an upwards orientation [a U shape],
the question changes, yet regardless of any previous results, the beam will go either right or
left.

However, there's always a contact with classical mechanics, even if, in practice, the
questions are always the same three: does the atom have a vertical orientation (up or down),
one along the ![equation](https://latex.codecogs.com/gif.latex?x) axis (positive or negative) or one along the ![equation](https://latex.codecogs.com/gif.latex?y) axis (positive or negative).

The orientation of an object is always 'written' somewhere within it- the question is, how
do we 'read' it? The answer lies within the state of the atom; if the state is completely unde-
ned, it still has a probability of being up/down. The new value of ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta), could perhaps have, ![](https://latex.codecogs.com/gif.latex?%5Cfrac%7B1%7D%7B3%7D) 'up' orientation and ![](https://latex.codecogs.com/gif.latex?%5Cfrac%7B2%7D%7B3%7D) 'down' orientation. This means the state is inclined, depending on how ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) is changed. If ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) needs to be measured, the ratio of intensity between the up/down values must be measured. Talking about orientation, the ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) angle can be compared to 'altitude', whilst the ![phi](https://latex.codecogs.com/gif.latex?%5Cphi) angle with 'longitude'. 
 
 Let's take a case where ![thetais90](https://latex.codecogs.com/gif.latex?%5Ctheta%20%3D%2090%5E%7B%5Ccdot%7D) and ![phiis0](https://latex.codecogs.com/gif.latex?%5Cphi%20%3D%200%5E%7B%5Ccdot%7D). Due to the fact that it is on the horizontal plane, if the magnet splits the beam in two, and if ![phi](https://latex.codecogs.com/gif.latex?%5Cphi) is different from ![0](https://latex.codecogs.com/gif.latex?0), there will always
be a different distribution caused by the magnet on the plane, even if ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) remains the same. This is always the mean value of the orientation.

As it can be seen, orientation may be 'classically' well dened, but it is not the case in
quantum mechanics. As some call it, there is not the same 'sharpness'. However, if there are
many and you take the mean values, then, on average, you get 'an orientation'. This comes
from a certain process, roughly it looks like this:

![](https://latex.codecogs.com/gif.latex?%5Ctext%7BSTATE%7D%20%5Crightarrow%20%5Ctext%7BPROCEDURE%7D%20%5Crightarrow%20%5Ctext%7BMEAN%20VALUE%7D)

But what is the 'procedure'? It is a set of questions. The type of questions depend on
the mathematics of the problem.

Let's take a step back. A vector is determined by its components. In classical mechanics,
the measurements (of the components) are that of the state of the vector - there is no
ambiguity. The difference between the way in which a problem is described in quantum
mechanics, is that the state and the values change when the system is described.

If there is a system, for instance our ![phieq](https://latex.codecogs.com/gif.latex?%7C%5Cpsi%5Crangle%20%3D%20cos%5Ctheta%7C0%5Crangle%20&plus;%20sin%5Ctheta%20e%5E%7Bi%5Cphi%7D0), what is the mean value of the ![](https://latex.codecogs.com/gif.latex?z) component? The 'procedure' is needed to find out. It's based on the state and on a set of observable factors, put on the state. These observable factors are the ![](https://latex.codecogs.com/gif.latex?x), ![](https://latex.codecogs.com/gif.latex?y), and ![](https://latex.codecogs.com/gif.latex?z) components.

The observable factors, given a state, become matrices (that are general operators), more specifically three, one for each direction. After a series of mathematical operations, the mean value of the component along ![](https://latex.codecogs.com/gif.latex?x), ![](https://latex.codecogs.com/gif.latex?y), and ![](https://latex.codecogs.com/gif.latex?z) is obtained. The possible values that can be obtained by measuring may be all 'up', 'down', 'left', 'right', 'forwards', and 'back'.

You might be asking yourself, what's in the system? What can be measured? From the procedure, given the state, ![latlon](https://latex.codecogs.com/gif.latex?cos%5Ctheta%7C0%5Crangle%5B%5Ctext%7Blatitude%7D%5D&plus;sin%5Ctheta%20e%5E%7Bi%5Cphi%7D%7C1%5Crangle%5B%5Ctext%7Blongitude%7D%5D) the two values are 'close relatives' of the angles used to describe the position on an object (take note of the square brackets). Usually, the state is written as a function of similar angles to ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) and ![phi](https://latex.codecogs.com/gif.latex?%5Cphi) , that correspond with angles that would be measured after the procedure.

In order to describe an object's orientation, there are 'standards. The most used conven-
tion for the orientation, is to start from an axis. 2 angles are needed. The first is the angle
the object has in relation to the ![](https://latex.codecogs.com/gif.latex?z) axis, an angle similar (but not the same!) as our angle ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) .

On the horizontal,

![](https://latex.codecogs.com/gif.latex?%5C%5C%20%5Cuparrow%20%5Cimplies%20%5Ctheta%20%3D%200%5E%7B%5Cdegree%7D%20%5C%5C%20%5Crightarrow%20%5Cimplies%20%5Ctheta%20%3D%2090%5E%7B%5Cdegree%7D%20%5C%5C%20%5Cdownarrow%20%5Cimplies%20%5Ctheta%20%3D%20180%5E%7B%5Cdegree%7D)

This corresponds with the 'latitude'. (Note that this new version of QuGUI, V2.4, the ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta) is at ![180deg](https://latex.codecogs.com/gif.latex?180%5E%7B%5Cdegree%7D) at default.) The second angle, which corresponds with the 'longitude', taking
the projection on the horizontal plane, corresponds to how much it 'turns'. If it turns counterclockwise:

![](https://latex.codecogs.com/gif.latex?%5C%5C%20%5Crightarrow%20%5Cimplies%20%5Cphi%3D%200%5E%7B%5Cdegree%7D%20%5C%5C%20%5Cuparrow%20%5Cimplies%20%5Cphi%3D%2090%5E%7B%5Cdegree%7D%20%5C%5C%20%5Cleftarrow%20%5Cimplies%20%5Cphi%3D%20180%5E%7B%5Cdegree%7D)

Now, the equation has changed and become:

![](https://latex.codecogs.com/gif.latex?%7C%5Cpsi%5Crangle%20%3D%20sin%20%5Cleft%28%5Cfrac%7B%5Ctheta%7D%7B2%7D%5Cright%29%7C0%5Crangle%20&plus;%20cos%20%5Cleft%28%5Cfrac%7B%5Ctheta%7D%7B2%7D%20%5Cright%29e%5E%7Bi%5Cphi%7D%7C1%5Crangle)

With the previous ![](https://latex.codecogs.com/gif.latex?%5Ctheta) and ![](https://latex.codecogs.com/gif.latex?%5Cphi), ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta), instead of being at its usual, positive angle, it was oriented 'down', remaining as ![0](https://latex.codecogs.com/gif.latex?0).

If the (overall) mean value of the ![](https://latex.codecogs.com/gif.latex?z) needs to be calculated, and we have a wide range of average values, a magnet can be aligned on the ![](https://latex.codecogs.com/gif.latex?z) axis and, depending on the proportion of
how the beam goes 'up'/'down', the result is given.
They can be 'reconstructed' as an mean value, which are, on average, those given by the ![](https://latex.codecogs.com/gif.latex?%5Ctheta) and ![](https://latex.codecogs.com/gif.latex?%5Cphi) values.

Let's move on to talking in more detail about the 'procedure'. On a side, let's also keep
in mind that vectors are the 'quantic amplitudes', and that the 'operators' are:

![](https://latex.codecogs.com/gif.latex?%5C%5C%20sin%5Cleft%28%5Cfrac%7B%5Ctheta%7D%7B2%7D%20%5Cright%20%29%20%5Cimplies%20%5Ctext%7B%27down%27%7D%20%5C%5C%20cos%20%5Cleft%28%5Cfrac%7B%5Ctheta%7D%7B2%7D%20%5Cright%20%29%20e%5E%7Bi%5Cphi%7D%20%5Cimplies%20%5Ctext%7B%27up%27%7D)

As well as 3, 2x2, matrices:

![](https://latex.codecogs.com/gif.latex?%5Ctext%7B%5Balong%20the%20%7D%20x%20%5Ctext%7B%20axis%5D%20%5Balong%20the%20%7D%20y%20%5Ctext%7B%20axis%5D%20%5Balong%20the%20%7D%20z%20%5Ctext%7B%20axis%5D%7D)

The mean of the state is given by the product of the ![](https://latex.codecogs.com/gif.latex?%5Ctext%7Bmatrix%20%7D%20%5Ccdot%20%5Ctext%7B%20vector%7D).
Let's look at a very simple example: If we get 

![](https://latex.codecogs.com/gif.latex?%5Cfrac%7B2%7D%7B3%7D%20%5Ctext%7B%20%27up%27%20orientation%20and%2C%20%7D%20%5Cfrac%7B1%7D%7B3%7D%20%5Ctext%7B%20%27down%27%20orientation%7D%20%5Cimplies%20%5Ctext%7Bthe%20mean%20value%20is%20%7D%20%5Cfrac%7B1%7D%7B3%7D%20%5Ctext%7B%20%27up%27%7D)
