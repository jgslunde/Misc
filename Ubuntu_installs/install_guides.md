## Pip

sudo -H apt install python3-pip
sudo -H pip install --upgrade pip

## Python Packages

sudo -H pip install numpy sympy scipy seaborn matplotlib pandas tensorflow keras sklearn tqdm

sudo apt install jupyter-notebook

sudo -H pip install jupyterlab

## Lapack/Blas/SuperLU/ARPACK

(lapack and blas seem to have the latest version on apt)
sudo apt install libblas-dev liblapack-dev libsuperlu-dev libarpack2-dev

## Armadillo

(armadillo seems to have a newer version on the webpage than on apt. Download from there. Also, it depends on lapack/blas (see above)).
sudo apt install cmake
(cd into downloaded armadillo folder.)
cmake .
make
sudo make install
(This should install Armadillo into the default /usr install location.)

Armadillo must be run with command line arguments -larmadillo, and -llapack -lblas if linalg solvers of armadillo are to be used.

## MPI

Needs MPI implementation from either OpenMPI or MPICH, which can both be installed from terminal. MPICH is faster and more up to date with MPI.
sudo apt install mpich
Compile as
mpic++ -o x.out x.cxx
run as
mpiexec -n 4 ./test.o

## OpenMP

OpenMP seems to work out of the box with a modern compiler, simply adding the -fopenmp flag.

## Matplotlibcpp
https://github.com/lava/matplotlib-cpp
Put the matplotlibcpp.h file in the run directory.
Run with -I/usr/include/python3.7 -lpython3.7m, or -I/usr/include/python2.7 -lpython2.7


## Texlive

sudo apt-get install texlive-full

## Visit websites or Ubuntu Software Center to install

* Visual Studio Code
* GitKraken
* Telegram
* VLC media player
