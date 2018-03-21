##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *
import os
import json


class Nekcem(Package):
    """Spectral-element solver for Maxwell's equations, drift-diffusion
       equations, and more."""

    # Links to homepage and git
    homepage = "https://nekcem.mcs.anl.gov"
    url      = "https://github.com/NekCEM/NekCEM/archive/development.zip"

    # Variants
    variant('mpi', default=True, description='Build with MPI')

    # We only have a development version
    version('develop', git='https://github.com/NekCEM/NekCEM.git')
    version('0b8bedd', git='https://github.com/NekCEM/NekCEM.git',
            commit='0b8beddfdcca646bfcc866dfda1c5f893338399b')

    # dependencies
    depends_on('mpi', when='+mpi')
    depends_on('blas')
    depends_on('lapack')

    @run_before('install')
    def fortran_check(self):
        if not self.compiler.fc:
            msg = 'NekCEM can not be built without a Fortran compiler.'
            raise RuntimeError(msg)

    @run_after('install')
    def test_install(self):
        NekCEM_test = join_path(self.prefix.bin, 'NekCEM', 'tests', '2dboxpec')
        with working_dir(NekCEM_test):
            makenek = Executable(join_path(self.prefix.bin, 'makenek'))
            makenek(os.path.basename(NekCEM_test))
            if not os.path.isfile('nekcem'):
                msg = 'Cannot build example: %s' % NekCEM_test
                raise RuntimeError(msg)

    def install(self, spec, prefix):
        binDir = 'bin'
        nek = 'nek'
        cNek = 'configurenek'
        mNek = 'makenek'

        FC = self.compiler.f77
        CC = self.compiler.cc

        fflags = spec.compiler_flags['fflags']
        cflags = spec.compiler_flags['cflags']
        ldflags = spec.compiler_flags['ldflags']

        if '+mpi' in spec:
            FC = spec['mpi'].mpif77
            CC = spec['mpi'].mpicc

        with working_dir(binDir):
            fflags = ['-O3'] + fflags
            cflags = ['-O3'] + cflags
            fflags += ['-I.']
            cflags += ['-I.', '-DGLOBAL_LONG_LONG']

            if self.compiler.name == 'gcc' or self.compiler.name == 'clang':
                # assuming 'clang' uses 'gfortran'
                fflags += ['-fdefault-real-8', '-fdefault-double-8']
                cflags += ['-DUNDERSCORE']
            elif self.compiler.name == 'intel':
                fflags += ['-r8']
                cflags += ['-DUNDERSCORE']
            elif self.compiler.name == 'xl' or self.compiler.name == 'xl_r':
                fflags += ['-qrealsize=8']
                cflags += ['-DPREFIX=jl_', '-DIBM']
            elif self.compiler.name == 'pgi':
                fflags += ['-r8']
                cflags += ['-DUNDERSCORE']

            if '+mpi' in spec:
                fflags += ['-DMPI', '-DMPIIO']
                cflags += ['-DMPI', '-DMPIIO']
            blasLapack = spec['lapack'].libs + spec['blas'].libs
            ldflags += blasLapack.ld_flags.split()
            all_arch = {
                'spack-arch': {
                    'FC': FC, 'FFLAGS': fflags,
                    'CC': CC, 'CFLAGS': cflags,
                    'LD': FC, 'LDFLAGS': ldflags
                }
            }
            os.rename('arch.json', 'arch.json.orig')
            with open('arch.json', 'w') as file:
                file.write(json.dumps(all_arch))
            filter_file(r'^ARCH=.*$', 'ARCH=spack-arch', 'makenek')
            filter_file(r'^NEK=.*', 'NEK="%s"' % prefix.bin.NekCEM,
                        'makenek')

        # Install NekCEM in prefix/bin
        install_tree('../NekCEM', prefix.bin.NekCEM)
        # Create symlinks to makenek, nek and configurenek scripts
        with working_dir(prefix.bin):
            os.symlink(os.path.join('NekCEM', binDir, mNek), mNek)
            os.symlink(os.path.join('NekCEM', binDir, cNek), cNek)
            os.symlink(os.path.join('NekCEM', binDir, nek), nek)
