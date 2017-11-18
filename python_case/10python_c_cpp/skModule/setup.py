
#coding=utf-8

from distutils.core import setup,Extension

MOD="sk"

setup(name=MOD, ext_modules=[Extension(MOD,sources=['sk.c','skWrapper.c'])])


