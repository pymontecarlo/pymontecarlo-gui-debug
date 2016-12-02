"""
Basic GUI using PyQt5, numpy, scipy, h5py and matplotlib
"""

# Standard library modules.
import os
import sys
import logging
import platform

# Third party modules.
from qtpy import QtWidgets

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvas

import numpy as np

import scipy.interpolate

import h5py

# Local modules.
from pymontecarlo_gui_debug._version import get_versions

# Globals and constants variables.

class MainDialog(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('pyMonteCarlo debug')

        # Variables
        self.data = np.transpose(np.array([np.arange(5), np.random.random(5)]))

        fig = Figure((6, 6))

        # Widgets
        self.canvas = FigureCanvas(fig)

        self.btn_save = QtWidgets.QPushButton("Save to HDF5")

        # Layouts
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.btn_save)
        self.setLayout(layout)

        # Signals
        self.btn_save.clicked.connect(self._on_save)

        # Defaults
        self._draw_figure()

    def _draw_figure(self):
        fig = self.canvas.figure
        ax = fig.add_subplot("111")

        xs = self.data[:, 0]
        ys = self.data[:, 1]
        ax.plot(xs, ys, 'o')

        f = scipy.interpolate.interp1d(xs, ys)
        ax.plot(xs, f(xs), '-', lw=3)

        self.canvas.draw()

    def _on_save(self):
        dirpath = os.path.join(os.path.expanduser('~'), '.pymontecarlo')
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        filepath = os.path.join(dirpath, 'debug.h5')
        with h5py.File(filepath, 'w') as f:
            group = f.create_group('debug')
            group.create_dataset('data', data=self.data)

def _setup(argv):
    # Configuration directory
    dirpath = os.path.join(os.path.expanduser('~'), '.pymontecarlo')
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    # Redirect stdout and stderr when frozen
    if getattr(sys, 'frozen', False):
        ## Note: Important since warnings required sys.stderr not be None
        filepath = os.path.join(dirpath, 'pymontecarlo.stdout')
        sys.stdout = open(filepath, 'w')

        filepath = os.path.join(dirpath, 'pymontecarlo.stderr')
        sys.stderr = open(filepath, 'w')

    # Logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if '-d' in argv else logging.INFO)

    fmt = '%(asctime)s - %(levelname)s - %(module)s - %(lineno)d: %(message)s'
    formatter = logging.Formatter(fmt)

    handler = logging.FileHandler(os.path.join(dirpath, 'pymontecarlo.log'), 'w')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if not getattr(sys, 'frozen', False):
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.info('Started pyMonteCarlo')
    logger.info('version = %s', get_versions()['version'])
    logger.info('operating system = %s %s',
                 platform.system(), platform.release())
    logger.info('machine = %s', platform.machine())
    logger.info('processor = %s', platform.processor())

    # Catch all exceptions
#    def _excepthook(exc_type, exc_obj, exc_tb):
#        messagebox.exception(None, exc_obj)
#        sys.__excepthook__(exc_type, exc_obj, exc_tb)
#    sys.excepthook = _excepthook

    # Output sys.path
    logger.info("sys.path = %s", sys.path)

    # Output environment variables
    logger.info('ENVIRON = %s' % os.environ)

def run():
    argv = sys.argv
    _setup(argv)
    app = QtWidgets.QApplication(argv)
    dialog = MainDialog()
    dialog.show()
    app.exec_()

if __name__ == '__main__':
    run()
