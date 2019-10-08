%define major 5
%define libname %mklibname KF5GrantleeTheme %{major}
%define devname %mklibname KF5GrantleeTheme -d

Name: grantleetheme
# This used to live in kdepim
Epoch:		3
Version:	19.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for PIM handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KF5AkonadiSearch)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(Grantlee5)

%description
KDE library for PIM handling

%package -n %{libname}
Summary: KDE library for PIM handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for PIM handling

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
cd ../
%ninja -C build

%install
%ninja_install -C build
%find_lang libgrantleetheme

%files -f libgrantleetheme.lang
%{_datadir}/qlogging-categories5/grantleetheme.categories
%{_datadir}/qlogging-categories5/grantleetheme.renamecategories

%files -n %{libname}
%{_libdir}/libKF5GrantleeTheme.so.%{major}*
%{_libdir}/grantlee/*/kde_grantlee_plugin.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
