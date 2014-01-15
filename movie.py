# This file is part of Architype.
# Architype is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Architype is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License 
# along with Architype.  If not, see <http://www.gnu.org/licenses/>.
# Author Jonathan Byrne 2014

import sys,os,re, subprocess, time

popFolder=os.getcwd()+"/population/"
os.chdir(popFolder)
meshList=[]
ppmList=[]
commandList=[]
commandList.append("ls | grep .jpg > frames.txt")
commandList.append("mencoder mf://@frames.txt -mf w=800:h=600:fps=10:type=jpg -ovc xvid -ovc x264 -x264encopts bitrate=3000:pass=1:nr=2000 -o a.avi")
commandList.append("rm -f *.ppm")
commandList.append("rm -f *.jpg")


def createPPM(fileName):
    print "creating ppms"
    if sys.platform == 'linux2':
        cmd = './linuxMedit '+popFolder+fileName
    else:
        cmd = 'ffmedit -xv 600 600 '+popFolder+fileName
    print cmd
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    process.communicate()

for fileName in os.listdir(popFolder):    
    if fileName.endswith('.mesh'):
        meshList.append(fileName)

for mesh in meshList:
    createPPM(mesh)

for fileName in os.listdir(popFolder):
    if fileName.endswith('.ppm'):
        print "found ppm"
        ppmList.append(fileName)

for ppmFile in ppmList:
    jpgFile=ppmFile.replace('ppm','jpg')
    cmd = "convert "+popFolder+ppmFile+" "+popFolder+jpgFile
    print cmd
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    process.communicate()

for cmd in commandList:
    print cmd
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    process.communicate()
