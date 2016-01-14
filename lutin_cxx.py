#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "clang generic lib c++"

def get_licence():
	return "bsd-like"

def get_compagny_type():
	return "com"

def get_compagny_name():
	return "University of Illinois"

def get_maintainer():
	return ["LLVM Team"]

def get_version():
	return [3,4]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'cxx/src/algorithm.cpp',
		'cxx/src/bind.cpp',
		'cxx/src/chrono.cpp',
		'cxx/src/condition_variable.cpp',
		'cxx/src/debug.cpp',
		'cxx/src/exception.cpp',
		'cxx/src/future.cpp',
		'cxx/src/hash.cpp',
		'cxx/src/ios.cpp',
		'cxx/src/iostream.cpp',
		'cxx/src/locale.cpp',
		'cxx/src/memory.cpp',
		'cxx/src/mutex.cpp',
		'cxx/src/new.cpp',
		'cxx/src/optional.cpp',
		'cxx/src/random.cpp',
		'cxx/src/regex.cpp',
		'cxx/src/shared_mutex.cpp',
		'cxx/src/stdexcept.cpp',
		'cxx/src/string.cpp',
		'cxx/src/strstream.cpp',
		'cxx/src/system_error.cpp',
		'cxx/src/thread.cpp',
		'cxx/src/typeinfo.cpp',
		'cxx/src/utility.cpp',
		'cxx/src/valarray.cpp'
		])
	if target.name=="Windows":
		my_module.add_src_file([
			'src/support/win32/support.cpp',
			'src/support/win32/locale_win32.cpp'
			])
	my_module.compile_version("c++", 2011)
	my_module.compile_flags('c++', [
		"-nostdinc++",
		"-std=c++11",
		"-Wall",
		"-Wextra",
		"-Wshadow",
		"-Wconversion",
		"-Wpadded",
		"-Wstrict-aliasing=2",
		"-Wstrict-overflow=4"
		])
	my_module.add_export_flag('c++', [
	    "-fstrict-aliasing"
	    ])
	# add local include path to build
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "cxx/include"))
	my_module.add_header_file([
		'cxx/include/*'
		],
		destination_path=""
		)
	my_module.add_header_file([
		'cxx/include/experimental/*',
		],
		destination_path="experimental")
	
	if target.name=="Windows":
		my_module.add_header_file([
			'cxx/include/support/win32/*',
			],
			destination_path="include/support/win32")
	# export flag that we use LLVM C++ lib
	my_module.add_export_flag("c++", ["-D__STDCPP_LLVM__", "-nostdinc++"])
	# remove some exception in linux system ...
	my_module.add_export_flag("c++", ["-D__GLIBCXX__"])
	my_module.add_export_flag("c++", ["-D__GLIBC__"])
	my_module.add_export_flag("c++", ["-D_LIBCPP_NO_EXCEPTIONS", "-D__GLIBC__"])
	# dev add basic lib supc used for allocation and basic c++ environement ==> todo: set a basic constructor (-lSystem for MacOS)
	my_module.add_export_flag("link", [target.stdlib_name_libsupc])
	return my_module


