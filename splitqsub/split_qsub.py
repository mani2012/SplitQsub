#!/usr/bin/env python
# Author: Solaiappan Manimaran
# Splits a commands file into multiple qsub files

#usage information: split_qsub.py -h

#       SplitQsub 1.0 - Python program that given a set of commands in one file, 
#       will split it in to multiple qsub files, 
#       which can then be submitted to run all parallel at once
#       Copyright (C) 2015  Johnson Lab - Boston University
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, argparse

def splitQsub(inputArgs):
    with open(inputArgs.cmd_file,'r') as in1:
        count = 0
        qcount = 1
        outlines = []
        qname = inputArgs.qsub_prefix+str(qcount)
        for ln in in1:
            outlines.append(ln)
            count += 1
            if (count == inputArgs.num_lines):
                writeQsub(outlines, qname, inputArgs.outdir, inputArgs.header_file, inputArgs.footer_file)
                outlines = []
                count = 0
                qcount += 1
                qname = inputArgs.qsub_prefix+str(qcount)

def writeQsub(outlines, qname, outdir, headerfile, footerfile):
    outfile = qname+'.qsub'
    of = outdir + os.path.sep + outfile
    with open(of,'w') as out1:
        with open(headerfile,'r') as in1:
            for ln in in1:
                if "@@QNAME@@" in ln:
                    ln = ln.replace("@@QNAME@@", qname)
                out1.write(ln)
        for oln in outlines:
            out1.write(oln)
        if footerfile != "":
            with open(footerfile,'r') as in2:
                for ln in in2:
                    out1.write(ln)
            


parser = argparse.ArgumentParser(description="SplitQsub")

# create the top-level parser
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-commandsFile', action='store', dest='cmd_file', required=True, 
    help='Commands File that has to be split into multiple qsub files')
parser.add_argument('-headerFile', action='store', dest='header_file', required=True, 
    help='Header file that contains the header with replaceable fields to be included in all qsub files')
parser.add_argument('-footerFile', action='store', dest='footer_file', required=False, 
    default="", help='Footer file that contains the footer to be included in all qsub files')
parser.add_argument('-numlines', action='store', dest='num_lines', required=False, 
    default=1, type=int, help='Splits every given number of lines default (1) into a separate qsub file')
parser.add_argument('-qsubFilePrefix', action='store', dest='qsub_prefix', required=False, 
    default="p", help='Specify Commands File that has to be split into multiple qsub files')
parser.add_argument('-outDir', action='store', default='.', dest='outdir',
    help='Output Directory (Default=. (current directory))')

def main():
    inputArgs = parser.parse_args()
    splitQsub(inputArgs)

if __name__ == "__main__":
    main()
