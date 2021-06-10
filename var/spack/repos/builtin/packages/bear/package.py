# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Bear(CMakePackage):
    """Bear is a tool that generates a compilation database for clang tooling
    from non-cmake build systems."""
    homepage = "https://github.com/rizsotto/Bear"
    url      = "https://github.com/rizsotto/Bear/archive/2.0.4.tar.gz"

    version('3.0.12', sha256='a057b8b7795ff32d4f68241ad734d4c6e1327b70a105b93a838dd442a1582c1d')
    version('2.2.0',  sha256='6bd61a6d64a24a61eab17e7f2950e688820c72635e1cf7ea8ea7bf9482f3b612')
    version('2.0.4',  sha256='33ea117b09068aa2cd59c0f0f7535ad82c5ee473133779f1cc20f6f99793a63e')

    depends_on('python')
    depends_on('cmake@2.8:', type='build')
    depends_on('cmake@3.12:', type='build', when='@3.0.0:')
    depends_on('pkgconf', type='build', when='@3.0.0:')
    depends_on('grpc', type='build', when='@3.0.0:')
    depends_on('protobuf', type='build', when='@3.0.0:')  
    depends_on('fmt', type='build', when='@3.0.0:')
    depends_on('spdlog', type='build', when='@3.0.0:')
    depends_on('nlohmann-json', type='build', when='@3.0.0:')

    def cmake_args(self):
        args = []

        args = [
                self.define('ENABLE_UNIT_TESTS', False),
                self.define('ENABLE_FUNC_TESTS', False),
                self.define('CMAKE_CXX_COMPILER', self.compiler.cxx),
        ]

        return args
