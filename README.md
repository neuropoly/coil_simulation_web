# coil_simulation_web
web version of program for simulating RF coil array for MRI

# Getting started

Make sure to have the right Python version (2.7)

Make sure to install Python(x,y) in order to have the right libraries version for Numpy (1.9.2 or later) and MatPlotLib (1.4.3 or later)

# Running the script

In order to run the script in command line, you have to make sure to be in the Scripts directory of the repository and then enter the following command:

" python coil_simulation.py -rada %VALUE% -radb %VALUE% -definition %VALUE% -o %FILENAME.png% -o1 %FILENAME.png% -orientation %1 or 2% -slice %VALUE% -preset %0 or 1% -r %VALUE% -c %VALUE% "

Do not include the percentage symbol when entering the values.

The description of each argument are available by entering the following command:

"python coil_simulation.py -h"

The results will be saved in the project root directory.

# License

The MIT License (MIT)

Copyright (c) 2014 École Polytechnique, Université de Montréal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
