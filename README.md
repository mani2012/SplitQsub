SplitQsub
==============

Splits a commands file into multiple qsub files.  

Python program that given a set of commands in one file, will split it in to multiple qsub files, which can then be submitted to run all parallel at once

#### 1. Running

1.1 Prerequisite: Need to have python 2.7.3 or later version installed and add python to your PATH variable (Usually already done as part of python installation)
    
1.2 Change directory to where you downloaded the code 

1.3 Simply run `python setup.py install` if you want to install globally or
simply run `python setup.py install --user` if you want to install for the local user.

1.4 For usage information, simply run `splitqsub -h` after installation as above or 
simply run `python splitqsub/split_qsub.py -h` if you want to try without installing.

```{r}
usage: split_qsub.py [-h] [--version] -commandsFile CMD_FILE -headerFile HEADER_FILE 
                     [-footerFile FOOTER_FILE]
                     [-numlines NUM_LINES] 
                     [-qsubFilePrefix QSUB_PREFIX]
                     [-outDir OUTDIR]

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -commandsFile CMD_FILE
                        Commands File that has to be split into multiple qsub
                        files
  -headerFile HEADER_FILE
                        Header file that contains the header with replaceable
                        fields to be included in all qsub files
  -footerFile FOOTER_FILE
                        Footer file that contains the footer to be included in
                        all qsub files
  -numlines NUM_LINES   Splits every given number of lines default (1) into a
                        separate qsub file
  -qsubFilePrefix QSUB_PREFIX
                        Specify Commands File that has to be split into
                        multiple qsub files
  -outDir OUTDIR        Output Directory (Default=. (current directory))

```
1.5 Script to submit all the generated qsub files. You can simply run `submit_qsub.sh` or `splitqsub/submit_qsub.sh`.

```{r}
#!/bin/bash
for filename in ./*.qsub; do
    qsub "$filename"
done
```

####  2. Support and Contact

SplitQsub is developed by Solaiappan Manimaran.

Department of Biostatistics  
School of Public Health  
Boston University  
801 Massachusetts Avenue 3rd Floor  
Boston, MA 02118  

