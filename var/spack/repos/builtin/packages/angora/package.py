# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Angora(AutotoolsPackage):
    """ Angora is a free, open-source software package that computes
    numerical solutions to electromagnetic radiation and scattering problems """

    homepage = "http://www.angorafdtd.org/"
    url      = "https://bitbucket.org/backmanlab/angora/get/0.22.5.tar.gz"
    git      = "https://bitbucket.org/backmanlab/angora.git"

    version('master', branch='master')
    version('0.22.5', sha256='f95e4a8a7a570f5c4e093ec04fdf89ee352a4cbd4f3f4d36a288f3950d2af602')

    depends_on('libconfig')
    depends_on('blitz')
    depends_on('boost+mpi')
    depends_on('hdf5+cxx')
    depends_on('mpi')

    depends_on("automake@1.14.1", when="@master")
    depends_on("autoconf", when="@master")

    def autoreconf(self, spec, prefix):
        automake_args = ['--add-missing']
        automake = which('automake')
        automake(*automake_args)

    def configure_args(self):
        args = []
        
        args.append('--with-mpi=%s' %
                    self.spec['mpi'].prefix)

        args.append('--with-hdf5=%s' %
                    self.spec['hdf5'].prefix)

        args.append('--with-blitz=%s' %
                    self.spec['blitz'].prefix)

        args.append('--with-boost=%s' %
                    self.spec['boost'].prefix)

        args.append('--with-config=%s' %
                    self.spec['libconfig'].prefix)

        return args

    def flag_handler(self, name, flags):
        flags.append(self.compiler.cxx98_flag)
        return (None, None, flags)
    
