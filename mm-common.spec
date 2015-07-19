%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Build infrastructure and utilities for GNOME C++ bindings
Name:		mm-common
Version:	0.9.7
Release:	3
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		http://www.gtkmm.org/
Source0:	http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	curl
BuildRequires:	wget

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
%makeinstall_std

%files
%doc README NEWS ChangeLog AUTHORS
%{_bindir}/mm-common-prepare
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*
