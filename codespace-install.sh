conda config --add channels conda-forge
conda config --set channel_priority strict
conda update conda
conda install -y getfem==5.4.2
