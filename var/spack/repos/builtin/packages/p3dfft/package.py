# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class P3dfft(AutotoolsPackage):
    """P3DFFT stands for Parallel Three-Dimensional Fast Fourier Transforms.
    It is a library for large-scale computer simulations on parallel platforms.
    It implements 3D FFT and related algorithms such as Chebyshev transform
    (an important class of algorithm for simulations in a wide range of fields)."""

    homepage = "https://www.p3dfft.net"
    url      = "https://github.com/sdsc/p3dfft/archive/2.7.9.tar.gz"
    git      = "https://github.com/sdsc/p3dfft.git"

    version('develop', branch='master')
    version('2.7.9', sha256='c61b4705be59f20f06ef2fa11971f3648f82560c1078311c464c12f581b36ed1')

    variant('fftw', default=True,
            description='Builds with FFTW library')
    variant('essl', default=False,
            description='Builds with ESSL library')
    variant('mpi', default=True,
            description="Enable MPI support.")
    variant('measure', default=False,
            description="Define if you want to use"
                        "the measure fftw planner flag")
    variant('estimate', default=False,
            description="Define if you want to"
                        "use the estimate fftw planner flag")
    variant('patient', default=False,
            description="Define if you want to"
                        "use the patient fftw planner flag")

    # TODO: Add more configure options!

    depends_on('libtool', type=('build'))
    depends_on('autoconf', type=('build'))
    depends_on('automake', type=('build'))
    depends_on('mpi', when='+mpi')
    depends_on('fftw', when='+fftw')
    depends_on('essl', when='+essl')

    def configure_args(self):
        args = []

        if '%gcc' in self.spec:
            args.append('--enable-gnu')

        if '%intel' in self.spec:
            args.append('--enable-intel')

        if '%xl' in self.spec:
            args.append('--enable-ibm')

        if '%cce' in self.spec:
            args.append('--enable-cray')

        if '%pgi' in self.spec:
            args.append('--enable-pgi')

        if '+mpi' in self.spec:
            args.append('CC=%s' % self.spec['mpi'].mpicc)
            args.append('CXX=%s' % self.spec['mpi'].mpicxx)
            args.append('FC=%s' % self.spec['mpi'].mpifc)

        if '+openmpi' in self.spec:
            args.append('--enable-openmpi')

        if '+fftw' in self.spec:
            args.append('--enable-fftw')
            args.append('--with-fftw=%s' % self.spec['fftw'].prefix)

            if 'fftw+measure' in self.spec:
                args.append('--enable-fftwmeasure')
            if 'fftw+estimate' in self.spec:
                args.append('--enable-fftwestimate')
            if 'fftw+patient' in self.spec:
                args.append('--enable-fftwpatient')

        if '+essl' in self.spec:
            args.append('--enable-essl')
            args.append('--with-essl-lib=%s' %
                        self.spec['essl'].prefix.lib)
            args.append('--with-essl-inc=%s' %
                        self.spec['essl'].prefix.include)

        if '+mkl' in self.spec:
            args.append('--enable-mkl')
            args.append('--with-mkl-lib=%s' %
                        self.spec['mkl'].prefix.lib)
            args.append('--with-mkl-inc=%s' %
                        self.spec['mkl'].prefix.include)

        return args
