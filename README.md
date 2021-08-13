<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Intruduction_0"></a>Intruduction</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">The goal of this project is to get familiar with animation interpolation in 3D computer graphics. We created an animation system that interpolates between character shapes over time.</p>
<p class="has-line-data" data-line-start="3" data-line-end="4"><img src="https://github.com/gobica/path-tracing/blob/main/picture_103SSP.PNG" alt="alt text"></p>
<h2 class="code-line" data-line-start=5 data-line-end=6 ><a id="Animation_5"></a>Animation</h2>
<p class="has-line-data" data-line-start="6" data-line-end="10">The input is a set of polygonal objects, stored in OBJ files. These objects  have the same<br>
number of vertices and in the same order for the interpolation to work as intended.<br>
Additionally,  an animation description file is given, containing the keyframes as filenametimestamp pairs. The timestamps will be specified in milliseconds from the beginning of the animation.<br>
Note that the keyframes can be non-uniformly spaced, and that negative timestamps are valid.</p>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="CatmullRom_11"></a>Catmull-Rom</h2>
<p class="has-line-data" data-line-start="12" data-line-end="13">To animate the character,  a frame rate is chosen (time between individual frames) and a time range, from which you the timestamps are driven. For each timestamp, you will have to generate new vertex positions by interpolating the vertex positions in the keyframes. To interpolate each individual vertex position, a Catmull-Rom spline is used.</p>

