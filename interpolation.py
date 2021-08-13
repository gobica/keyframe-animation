import pywavefront
import numpy as np
import os
import shutil
import fileinput
import helper
# set parameters 
frame_rate = 24
nPoints = []
#read timestamps of keyframe 
files_toberead = []
timestamps = []

filename_timestamps = "input/input_00.txt"
timestamps_file = open(filename_timestamps, "r")

for line in timestamps_file: 
    l = line.split()
    files_toberead.append(l[0])
    timestamps.append(l[1])

nFrames = len(files_toberead)
print(nFrames)

for t in range(len(timestamps)-1): 
    nPoint = (int(timestamps[t+1]) - int(timestamps[t]))*frame_rate//1000
    nPoints.append(nPoint)



print(timestamps)
print(files_toberead)
#number of frames between keyframes
#frames = os.listdir('data')
vertex_positions_all = []
for frame in files_toberead: 
    filename = "data/" + frame
    vertex_positions = []
    with open(filename) as file:
        #ignore first 2 lines
        first_line = file.readline()
        second_line = file.readline()

        for line in file:
            lineArray = []
            l = line.split()
            if l[0] == "v": 
                vp  = (float(l[1]), float(l[2]), float(l[3]))
                vertex_positions.append(vp)
         
    vertex_positions_all.append(vertex_positions)

#ADD FOR REPATED 
#vertex_positions_all.append(vertex_positions_all[0])
#vertex_positions_all.append(vertex_positions_all[1])
#vertex_positions_all.append(vertex_positions_all[2])


filename_input = "data/frame_01.obj"
# The curve C will contain an array of (x, y) points.

for key in range(nFrames-1):
    print("calculating keyframe: ", key)
    file_input = open(filename_input, "rt")
    first_line = file_input.readline()
    second_line = file_input.readline()
    vertex_index = 0

    strings = []
    for i in range(nPoints[key]):
        string = []
        strings.append(string)

    for line in file_input: 
        l = line.split()
        if l[0] == "v": 
            P0 = vertex_positions_all[key -1][vertex_index]
            P1 = vertex_positions_all[key][vertex_index]
            P2 = vertex_positions_all[(key+1) % nFrames][vertex_index]
            P3 = vertex_positions_all[(key+2) % nFrames][vertex_index]
            C = helper.CatmullRomSpline(P0, P1, P2, P3, nPoints[key])

            for i in range(nPoints[key]):
                vox_string = ' '.join(map(str, C[i]))
                string = "v " + vox_string +"\n"
                strings[i].append(string)
            vertex_index+=1
        else: 
            for i in range(nPoints[key]):
                string = line
                strings[i].append(string)

    for i in range(nPoints[key]):
        filename_output = "output/OBJ_file_" + str(key) +"_" + str(i) + ".obj"
        file_output = open(filename_output, "w")
        file_output.writelines(strings[i])
