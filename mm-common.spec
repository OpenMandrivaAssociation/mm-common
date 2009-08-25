%define name mm-common
%define version 0.6.1
%define release %mkrel 1

Summary: Build infrastructure and utilities for GNOME C++ bindings
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Development/GNOME and GTK+
Url: http://www.gtkmm.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: curl
BuildRequires: wget

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is only a required
dependency for building the C++ bindings from the gnome.org version
control repository.  An installation of mm-common is not required for
building tarball releases, unless configured to use maintainer-mode.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS ChangeLog AUTHORS
%_bindir/mm-common-prepare
%_datadir/aclocal/*.m4
%_datadir/%name
%_datadir/pkgconfig/mm-common-libstdc++.pc

