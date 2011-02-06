#! /bin/sh

# Runs the tn5250j 5250 java emulator

# Sets the tn5250j home directory
TN5250J_HOME='/usr/share/java/tn5250j/'

# Change to the emulator's directory
cd ${TN5250J_HOME}/

# Does the effective launching
java -jar tn5250j.jar
