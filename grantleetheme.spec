#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define libname %mklibname KPim6GrantleeTheme
%define devname %mklibname KPim6GrantleeTheme -d

Name:		grantleetheme
Version:	25.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/grantleetheme/-/archive/%{gitbranch}/grantleetheme-%{gitbranchd}.tar.bz2#/grantleetheme-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/grantleetheme-%{version}.tar.xz
%endif
Summary: KDE library for PIM handling
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Qml)
BuildRequires: sasl-devel
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant
# Renamed after 6.0 2025-05-25
%rename plasma6-grantleetheme
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KDE library for PIM handling

%package -n %{libname}
Summary: KDE library for PIM handling
Group: System/Libraries
Requires: %{name} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft...
Obsoletes: %{mklibname KF5GrantleeTheme 5}
Obsoletes: %{mklibname KPim5GrantleeTheme}

%description -n %{libname}
KDE library for PIM handling

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# Not a 1:1 replacement, but we need to get rid of old cruft...
Obsoletes: %{mklibname -d KF5GrantleeTheme}
Obsoletes: %{mklibname -d KPim5GrantleeTheme}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/grantleetheme.categories
%{_datadir}/qlogging-categories6/grantleetheme.renamecategories

%files -n %{libname}
%{_libdir}/libKPim6GrantleeTheme.so*
%{_qtdir}/plugins/kf6/ktexttemplate/kde_grantlee_plugin.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
