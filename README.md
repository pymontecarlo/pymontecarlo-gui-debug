#pymontecarlo GUI debug

This is a project to test and debug different options to build the 
pymontecarlo distribution on the different operating systems.

##Installation

###Windows

1. Clone git repository

```
git clone https://github.com/pymontecarlo/pymontecarlo-gui-debug.git
```

2. Manually download and install wheels from 
   [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
  
  * numpy
  * scipy
  * h5py
  
3. Use pip to install 

  ```
  pip install nose setuptools matplotlib qtpy PyQt5 py2exe cx_Freeze
  ```
  
 
