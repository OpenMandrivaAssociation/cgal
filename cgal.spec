%define uname   CGAL

%define soname  11
%define libname %mklibname %{name} %{soname}
%define devname %mklibname %{name} -d

Name:           cgal
Version:        4.7
Release:        1
Summary:        Computational Geometry Algorithms Library
Group:          System/Libraries
License:        LGPLv3+ and GPLv3+ and Boost
URL:            http://www.cgal.org/
Source0:	https://github.com/CGAL/cgal/releases/download/releases%2FCGAL-4.7/%{uname}-%{version}.tar.xz	

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  qt5-devel
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(zlib)

%description
The goal of the CGAL Open Source Project is to provide easy access
to efficient and reliable geometric algorithms in the form of a C++
library. CGAL is used in various areas needing geometric computation,
such as: computer graphics, scientific visualization, computer aided
design and modeling, geographic information systems, molecular biology,
medical imaging, robotics and motion planning, mesh generation, numerical
methods... More on the projects using CGAL web page.

#----------------------------------------------------------------------------

%package -n     %{libname}
Group:          System/Libraries
Summary:        Computational Geometry Algorithms Library

%description -n %{libname}
Shared library for %{name}

%files -n       %{libname}
%{_libdir}/lib%{uname}*.so.%{soname}*

#----------------------------------------------------------------------------

%package -n     %{devname}
Group:          Development/C++
Summary:        Development files and tools for CGAL applications
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{uname}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the headers files and tools you may need to
develop applications using CGAL.

%files -n       %{devname}
%doc AUTHORS LICENSE LICENSE.FREE_USE LICENSE.LGPL LICENSE.GPL CHANGES
%{_includedir}/%{uname}
%{_libdir}/lib%{uname}*.so
%{_libdir}/%{uname}
%dir %{_datadir}/%{uname}
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}_create_cmake_script.1*

#----------------------------------------------------------------------------

%package        demos-source
Group:          Documentation
Summary:        Examples and demos of CGAL algorithms
Requires:       %{devname} = %{version}-%{release}

%description    demos-source
This package provides the sources of examples and demos of CGAL algorithms.

%files          demos-source
%{_datadir}/%{uname}/demo
%{_datadir}/%{uname}/examples

#----------------------------------------------------------------------------

%prep
%setup -q -n %{uname}-%{version}

%build
%cmake	-DCMAKE_BUILD_TYPE=Release \
	-DWITH_ZLIB=ON \
	-DWITH_CGAL_Qt3=OFF \
	-DCGAL_INSTALL_LIB_DIR=%{_lib} \
	-DCGAL_INSTALL_DOC_DIR=
%make

%install
%makeinstall_std -C build
rm -f %{buildroot}/%{_bindir}/%{name}_make_macosx_app %{buildroot}/%{_datadir}/%{uname}/*/*/skip_vcproj_auto_generation

# Install demos and examples
mkdir -p %{buildroot}%{_datadir}/%{uname}
cp -a demo %{buildroot}%{_datadir}/%{uname}/demo
cp -a examples %{buildroot}%{_datadir}/%{uname}/examples
