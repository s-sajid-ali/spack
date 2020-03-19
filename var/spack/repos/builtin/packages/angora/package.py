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

    version('0.22.5', sha256='f95e4a8a7a570f5c4e093ec04fdf89ee352a4cbd4f3f4d36a288f3950d2af602')

    depends_on('libconfig')
    depends_on('blitz')
    depends_on('boost')
    depends_on('hdf5')
    depends_on('mpi')

    def configure_args(self):
        args = []
        
        args.append('--with-mpi=%s' %
                    self.spec['mpi'].prefix.lib)

        args.append('--with-hdf5=%s' %
                    self.spec['hdf5'].prefix.lib)

        args.append('--with-blitz=%s' %
                    self.spec['blitz'].prefix.lib)

        args.append('--with-boost=%s' %
                    self.spec['boost'].prefix.lib)

        args.append('--with-config=%s' %
                    self.spec['libconfig'].prefix.lib)

        return args
