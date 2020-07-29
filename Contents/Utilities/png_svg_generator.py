import os
import subprocess


def run_generator():

    java_program = os.path.join("/Applications", 'plantuml.jar')

    in_file = os.path.join("/Users/gradyke/Documents/CodingCaselawProject"
                           "/TPRESManual/DitaTopics/Ditamap_VolI/Topics/images",
                           'QuoteDia.txt')

    subprocess.call(['java', '-jar', java_program, in_file])


if __name__ == "__main__":
    run_generator()

# PROBLEM: WHEN -tsvg IS ADDED AFTER java_program (...java_program, '-tsvg', ...
# THIS RESULTS IN AN SVG FILE THAT OXYGENXML CAN'T TRANSFORM. SEE
# https://bugs.openjdk.java.net/browse/JDK-4723021 which explains the bug in
# Java.

# BUT SEE https://issues.apache.org/jira/browse/BATIK-1106
# Which describes a Java patch that fixes the problem.