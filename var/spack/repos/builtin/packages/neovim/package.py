# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Neovim(CMakePackage):
    """NeoVim: the future of vim"""

    homepage = "http://neovim.io"
    url      = "https://github.com/neovim/neovim/archive/v0.4.3.tar.gz"

    version('0.4.3', sha256='2354a60af47a61f54ad1fc115587af8db96dfbe8c8955c516af591d398134a2d')
    version('0.4.2', sha256='bf701dfaa456d0e82f7c3fb885861af1282438cc9622853ca76b22d90d0a2516')
    version('0.4.1', sha256='3148c0909761f36eb9864ddbd228bd2aa0a10016e11034bb764f280c31fa32ab')
    version('0.4.0', sha256='7d2efa5fd85a62170a3184eba5a405970e5b0bb9ed2b1c38409d45cdde4c5160')
    version('0.3.8', sha256='f0b0774e9a4f576058a76412b88405a56f984c4c261ab977e379e23e8f10ae34')
    version('0.3.7', sha256='4ebbcaf2a35af08cf7e04760c69241d233d0b6890344905fa46f053120eae450')
    version('0.3.6', sha256='e01ff99ac4eca427394903956238306eda9f39fbac9f24e70e9f0f2da434e39d')
    version('0.3.4', sha256='a641108bdebfaf319844ed46b1bf35d6f7c30ef5aeadeb29ba06e19c3274bc0e')
    version('0.3.1', sha256='bc5e392d4c076407906ccecbc283e1a44b7832c2f486cad81aa04cc29973ad22')
    version('0.3.0', sha256='f7acb61b16d3f521907d99c486b7a9f1e505e8b2a18c9ef69a6d7f18f29f74b8')
    version('0.2.2', sha256='a838ee07cc9a2ef8ade1b31a2a4f2d5e9339e244ade68e64556c1f4b40ccc5ed')
    version('0.2.1', sha256='9e2c068a8994c9023a5f84cde9eb7188d3c85996a7e42e611e3cd0996e345dd3')
    version('0.2.0', sha256='72e263f9d23fe60403d53a52d4c95026b0be428c1b9c02b80ab55166ea3f62b5')

    depends_on('lua@5.1:5.2')
    depends_on('lua-lpeg')
    depends_on('lua-mpack')
    depends_on('lua-bitlib')
    depends_on('libuv')
    depends_on('jemalloc')
    depends_on('libtermkey')
    depends_on('libvterm')
    depends_on('unibilium')
    depends_on('msgpack-c')
    depends_on('gperf')

    def cmake_args(self):
        args = []
        if self.version >= Version('0.2.1'):
            args = ['-DPREFER_LUA=ON']

        return args
