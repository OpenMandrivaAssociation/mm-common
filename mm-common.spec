%define name mm-common
%define version 0.9.5
%define release %mkrel 2

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
%_datadir/pkgconfig/*.pc
%_mandir/man1/*.1*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-2mdv2011.0
+ Revision: 666471
- mass rebuild

* Wed Mar 30 2011 Götz Waschk <waschk@mandriva.org> 0.9.5-1
+ Revision: 649050
- update to new version 0.9.5

* Wed Mar 23 2011 Funda Wang <fwang@mandriva.org> 0.9.4-1
+ Revision: 647767
- new version 0.9.4

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2mdv2011.0
+ Revision: 606653
- rebuild

* Fri Feb 05 2010 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 501241
- update to new version 0.9.2

* Thu Dec 31 2009 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2010.1
+ Revision: 484421
- update to new version 0.9.1

* Sun Dec 27 2009 Götz Waschk <waschk@mandriva.org> 0.9-1mdv2010.1
+ Revision: 482778
- update to new version 0.9

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2010.0
+ Revision: 446546
- update to new version 0.8

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2010.0
+ Revision: 437210
- new version
- update file list

* Wed Sep 02 2009 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 425497
- update to new version 0.7.2

* Fri Aug 28 2009 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 421999
- update to new version 0.7.1

* Fri Aug 28 2009 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2010.0
+ Revision: 421931
- update to new version 0.7

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 421110
- update to new version 0.6.1

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2010.0
+ Revision: 421021
- import mm-common


* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2010.0
- initial package
