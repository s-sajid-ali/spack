# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Combblas(CMakePackage):
    """The Combinatorial BLAS (CombBLAS) is an extensible distributed-memory
    parallel graph library offering a small but powerful set of linear algebra
    primitives specifically targeting graph analytics."""

    homepage = "https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/"
    url      = "http://eecs.berkeley.edu/~aydin/CombBLAS_FILES/CombBLAS_beta_16_2.tgz"

    version('16_2', sha256='2a35c725606f18d010c110c66814b6558dae26f6807ac01c843c788fdb5b3ca9')
    version('16_1', sha256='da1e4503d3bf3355187beefa273b4e82a431a7f23781d43681c352125a39ce02')
    version('16_0', sha256='9f8067451545779f96630a1e0fe8b49778163775f062a30d5cb105237608665d')

    depends_on('mpi')
