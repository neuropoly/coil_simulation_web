# coil_simulation_web

Program for simulating RF coil array for MRI.

# Dependencies
- Python (2.7)
- Numpy (1.9.2 or later)
- MatPlotLib (1.4.3 or later)

# Getting started

In order to run the script in command line, you have to make sure to be in the ``Scripts/`` folder of the repository. Example command below:
~~~
python coil_simulation.py -rada 5 -radb 4 -definition 20 -o b1.png -o1 coil.png -orientation 1 -slice 0 -preset 1 -r 3 -c 5
~~~

The description of each argument are available by entering the following command:

~~~
python coil_simulation.py -h
~~~

The results will be saved in the project root directory.

# License

The MIT License (MIT)

Copyright (c) 2015 École Polytechnique, Université de Montréal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
