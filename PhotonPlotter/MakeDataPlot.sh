#!/bin/bash
#Chad Brisbois
#
#The goal of this script is to automatically download fermi data
#    export it to an ASCII file, and plot it in reference to a 
#    trigger time that will also be automatically obtained. 
#
#Presently, it will just export existing data, and plot the energy of photons vs time
#
#
#Usage: MakeDataPlot.sh <GRB-Name>
#
#<GRB-Name> -- this is the GRB designation such as 090510A, or 130427A
#
#



#100 MeV
LOWE=100000000 


#Name of GRB
GRB=$1

DIR="./$GRB"

if [ ! -d "$DIR" ]
then
    echo "Data for this GRB does not exist on this system"
    echo "Downloading Data and creating folders"
    echo "I made the folder:"
    mkdir "$DIR"
    ls
fi



