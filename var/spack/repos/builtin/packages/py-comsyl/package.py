# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *

class PyComsyl(PythonPackage):
    """ COherent Modes for SYnchrotron Light makes the coherent mode
    decomposition of synchrotron radiation emitted by electrons passing
    through an undulator placed in a storage ring. COMSYL permits
    naturally the statistical analysis and propagation of the cross
    spectral density along the beamline optics. The coherence properties
    of the X-ray beam at any point of the beamline are completely given in
    terms of the eigenvalues and coherent modes of the cross spectral density."""

    homepage = "https://github.com/s-sajid-ali/comsyl"
    git      = "https://github.com/s-sajid-ali/comsyl.git"

    import_modules = ['autocorrelation',
                      'calculations',
                      'infos',
                      'mathcomsyl',
                      'parallel',
                      'utils',
                      'waveoptics']

    version('develop', branch='master')

    depends_on('petsc+complex')
    depends_on('slepc')
    depends_on('py-petsc4py')
    depends_on('py-slepc4py')
    depends_on('py-numpy')
    depends_on('py-syned')
    depends_on('py-pip', type='build')
    

