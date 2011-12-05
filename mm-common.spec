
Name:		mm-common
Summary:	Build infrastructure and utilities for GNOME C++ bindings
Version:	0.9.5
Release:	2
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Development/GNOME and GTK+
Url: http://www.gtkmm.org/
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

%files
%doc README NEWS ChangeLog AUTHORS
%{_bindir}/mm-common-prepare
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}/
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*
