%define url_ver %(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	Build infrastructure and utilities for GNOME C++ bindings
Name:		mm-common
Version:	1.0.5
Release:	1
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		http://www.gtkmm.org/
Source0:	http://ftp.acc.umu.se/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
BuildArch:	noarch
BuildRequires:	curl
BuildRequires:  doxygen
BuildRequires:  meson
BuildRequires:	wget
BuildRequires:  pkgconfig(python)

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is only a required
dependency for building the C++ bindings from the gnome.org version
control repository.  An installation of mm-common is not required for
building tarball releases, unless configured to use maintainer-mode.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* NEWS ChangeLog AUTHORS
%doc %{_datadir}/doc/mm-common/skeletonmm.tar.xz
%{_bindir}/mm-common-prepare
%{_bindir}/mm-common-get
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}
%{_datadir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*
