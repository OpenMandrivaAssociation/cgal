%global debug_package %{nil}

%global uname   CGAL

%global soname  13
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define devname_qt %mklibname %{name}-qt6 -d
%define oldlibname %mklibname %{name} %{soname}

%global Iimageio_so 14
%define ImageIO %mklibname %{name}ImageIO
%define oldImageIO %mklibname %{name}ImageIO %{imageio_so}

%define CGALqt6 %mklibname %{name}qt6
%define CGALqt5 %mklibname %{name}qt5
%define oldCGALqt5 %mklibname %{name}qt5 %{imageio_so}

%bcond testing	1

Summary:        Computational Geometry Algorithms Library
Name:           cgal
Version:        6.0.1
Release:        1
Group:          System/Libraries
License:        LGPLv3+ and GPLv3+ and Boost
URL:            https://www.cgal.org/
Source0:	https://github.com/CGAL/cgal/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires: cmake ninja
BuildRequires: boost-devel
#BuildRequires: eigen-devel
BuildRequires: gmp-devel
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(mpfr)
BuildRequires: pkgconfig(zlib)
BuildRequires: qt6-qtbase-tools

%description
The goal of the CGAL Open Source Project is to provide easy access
to efficient and reliable geometric algorithms in the form of a C++
library. CGAL is used in various areas needing geometric computation,
such as: computer graphics, scientific visualization, computer aided
design and modeling, geographic information systems, molecular biology,
medical imaging, robotics and motion planning, mesh generation, numerical
methods... More on the projects using CGAL web page.

#----------------------------------------------------------------------------

%package -n     %{devname}
Group:          Development/C++
Summary:        Development files and tools for CGAL applications
#Requires:	%{ImageIO} = %{EVRD}
#Requires:	%{CGALqt5} = %{EVRD}
#Requires:       %{libname} = %{version}-%{release}
Requires:	cmake
Requires:	boost-devel
Requires:	eigen-devel
Requires:	gmp-devel
Requires:	pkgconfig(mpfr)
Requires:	pkgconfig(zlib)
Requires: cmake(Qt6Core)
Requires: cmake(Qt6LinguistTools)
Requires: cmake(Qt6Svg)
Requires: qt6-qtbase-tools

Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{uname}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the headers files and tools you may need to
develop applications using CGAL.

%files -n       %{devname}
%license AUTHORS LICENSE LICENSE.BSL LICENSE.RFL LICENSE.LGPL LICENSE.GPL
%doc CHANGES.md
%{_bindir}/%{name}*
%{_includedir}/%{uname}
#exclude %{_includedir}/CGAL/Qt
%{_libdir}/cmake/%{uname}
#exclude %{libdir}/cmake/%{uname}/demo
#{_libdir}/lib%{uname}*.so
%dir %{_datadir}/%{uname}
%exclude %{_datadir}/%{uname}/demo
%exclude %{_datadir}/%{uname}/examples
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
%exclude %{_datadir}/%{uname}/*/*/skip_vcproj_auto_generation

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%cmake	-Wno-dev \
	-DCGAL_ENABLE_CHECK_HEADERS:BOOL=ON \
	-DCGAL_ENABLE_TESTING:BOOL=%{?with_testing:ON}%{?!without_testing:OFF} \
	-DCGAL_INSTALL_LIB_DIR=%{_lib} \
	-DCGAL_INSTALL_DOC_DIR= \
	-GNinja
%ninja_build

%install
%ninja_install -C build

#rm -f %{buildroot}/%{_bindir}/%{name}_make_macosx_app %{buildroot}/%{_datadir}/%{uname}/*/*/skip_vcproj_auto_generation

# Install demos and examples
mkdir -p %{buildroot}%{_datadir}/%{uname}
cp -a demo %{buildroot}%{_datadir}/%{uname}/demo
cp -a examples %{buildroot}%{_datadir}/%{uname}/examples

