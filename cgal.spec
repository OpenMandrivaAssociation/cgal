%global debug_package %{nil}

%define uname   CGAL

%define soname  13
%define libname %mklibname %{name} %{soname}
%define devname %mklibname %{name} -d
%define imageio_so 14
%define ImageIO %mklibname %{name}ImageIO %{imageio_so}
%define CGALqt5 %mklibname %{name}qt5 %{imageio_so}

Name:           cgal
Version:        5.0.3
Release:        1
Summary:        Computational Geometry Algorithms Library
Group:          System/Libraries
License:        LGPLv3+ and GPLv3+ and Boost
URL:            http://www.cgal.org/
Source0:	https://github.com/CGAL/cgal/releases/download/releases%2FCGAL-%{version}/%{uname}-%{version}.tar.xz
BuildRequires: cmake
BuildRequires: gmp-devel
BuildRequires: boost-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(glu)
BuildRequires: qt5-qttools
BuildRequires: eigen-devel
BuildRequires: qt5-linguist-tools
BuildRequires: zlib-devel
BuildRequires: mpfr-devel

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
#{_libdir}/lib%{uname}*.so.%{soname}*

#----------------------------------------------------------------------------

%package -n     %{ImageIO}
Group:          System/Libraries
Summary:        Computational Geometry Algorithms Library

%description -n %{ImageIO}
Shared library for %{name}

%files -n       %{ImageIO}
#{_libdir}/lib%{uname}_ImageIO.so.%{imageio_so}*

#----------------------------------------------------------------------------

%package -n     %{CGALqt5}
Group:          System/Libraries
Summary:        Computational Geometry Algorithms Library

%description -n %{CGALqt5}
Shared library for %{name}

%files -n       %{CGALqt5}
#{_libdir}/lib%{uname}_Qt5.so.%{imageio_so}*

#----------------------------------------------------------------------------

%package -n     %{devname}
Group:          Development/C++
Summary:        Development files and tools for CGAL applications
Requires:	%{ImageIO} = %{EVRD}
Requires:	%{CGALqt5} = %{EVRD}
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{uname}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the headers files and tools you may need to
develop applications using CGAL.

%files -n       %{devname}
%doc AUTHORS LICENSE LICENSE.FREE_USE LICENSE.LGPL LICENSE.GPL
%{_includedir}/%{uname}
#{_libdir}/lib%{uname}*.so
%{_libdir}/cmake/%{uname}
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
	-DCGAL_HEADER_ONLY=OFF \
	-DWITH_ZLIB=ON \
	-DWITH_Eigen3=ON \
        -DWITH_CGAL_Qt5=ON \
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
