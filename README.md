# Intruduction
The goal of this project is to get familiar with animation interpolation in 3D computer graphics. We created an animation system that interpolates between character shapes over time. 

## Animation 
The input is a set of polygonal objects, stored in OBJ files. These objects  have the same
number of vertices and in the same order for the interpolation to work as intended.
Additionally,  an animation description file is given, containing the keyframes as filenametimestamp pairs. The timestamps will be specified in milliseconds from the beginning of the animation.
Note that the keyframes can be non-uniformly spaced, and that negative timestamps are valid.

To animate the character,  a frame rate is chosen (time between individual frames) and a time range, from which you the timestamps are driven. For each timestamp, you will have to generate new vertex positions by interpolating the vertex positions in the keyframes. To interpolate each individual vertex position, a Catmull-Rom spline is used.
