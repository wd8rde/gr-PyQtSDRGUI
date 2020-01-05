INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_WD8RDE wd8rde)

FIND_PATH(
    WD8RDE_INCLUDE_DIRS
    NAMES wd8rde/api.h
    HINTS $ENV{WD8RDE_DIR}/include
        ${PC_WD8RDE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    WD8RDE_LIBRARIES
    NAMES gnuradio-wd8rde
    HINTS $ENV{WD8RDE_DIR}/lib
        ${PC_WD8RDE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(WD8RDE DEFAULT_MSG WD8RDE_LIBRARIES WD8RDE_INCLUDE_DIRS)
MARK_AS_ADVANCED(WD8RDE_LIBRARIES WD8RDE_INCLUDE_DIRS)

