#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools, CMake
import os


class LibOggConan(ConanFile):
    name = "libogg"
    version = "1.3.3"
    url = "https://github.com/bincrafters/conan-libogg"
    description = "Ogg is a free, open container format maintained by the Xiph.Org Foundation."
    license = "https://www.xiph.org/licenses/bsd/"
    exports_sources = ["CMakeLists.txt", "LICENSE"]
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"

    def source(self):
        source_url = "https://github.com/xiph/ogg/archive"
        tools.get("{}/v{}.tar.gz".format(source_url, self.version))
        extracted_dir = "ogg-" + self.version
        os.rename(extracted_dir, "sources")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="sources")
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include", src="sources/include")
        self.copy(pattern="*.h", dst="include", src="include")
        with tools.chdir("sources"):
            self.copy(pattern="LICENSE")
            self.copy(pattern="*.dll", dst="bin", src="bin", keep_path=False)
            self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
            self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
            self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
            self.copy(pattern="*.dylib", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
