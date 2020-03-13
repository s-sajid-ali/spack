# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Angora(AutotoolsPackage):
    """ Angora is a free, open-source software package that computes
    numerical solutions to electromagnetic radiation and scattering problems """

    homepage = "http://www.angorafdtd.org/"
    url      = "http://www.angorafdtd.org/angora/angora-0.22.5.tar.gz"

    version('0.22.5', sha256='f95e4a8a7a570f5c4e093ec04fdf89ee352a4cbd4f3f4d36a288f3950d2af602')

    variant('mpi', default=True,
            description="Enable MPI support.")

    depends_on('libconfig')
    depends_on('blitz')
    depends_on('boost')
    depends_on('hdf5')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
