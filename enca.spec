Name: enca
Summary: Character set analyzer and detector
Version: 1.16
Release: 1%{?dist}
License: GPLv2
Group: Applications/Text
Source: http://dl.cihar.com/enca/enca-%{version}.tar.xz
URL: http://cihar.com/software/enca


%description
Enca is an Extremely Naive Charset Analyser. It detects character set and
encoding of text files and can also convert them to other encodings using
either a built-in converter or external libraries and tools like libiconv,
librecode, or cstocs.

Currently, it has support for Belarussian, Bulgarian, Croatian, Czech,
Estonian, Latvian, Lithuanian, Polish, Russian, Slovak, Slovene, Ukrainian,
Chinese and some multibyte encodings (mostly variants of Unicode)
independent on the language.

This package also contains shared Enca library other programs can make use of.

Install %{name} if you need to cope with text files of dubious origin
and unknown encoding and convert them to some reasonable encoding.


%package devel
Summary: Header files and libraries for %{name} charset analyzer
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains the static libraries and header files
for writing programs using the Extremely Naive Charset Analyser library,
and its API documentation.

Install %{name}-devel if you are going to create applications using the Enca
library.


%prep
%setup -q


%build

%configure \
	--disable-dependency-tracking \
	--disable-rpath \
	--without-librecode \
	--disable-external \
	--disable-static \
	--disable-gtk-doc
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT HTML_DIR=/tmp/html

rm -rf $RPM_BUILD_ROOT/tmp/html
rm -rf $RPM_BUILD_ROOT/%{_libexecdir}
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%{_bindir}/*
%{_libdir}/libenca.so.*
%{_mandir}/*/*
%doc AUTHORS COPYING FAQ README THANKS TODO

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%doc README.devel


%changelog
* Thu Sep 10 2015 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.16-1
- update to 1.16

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.15-1
- update to 1.15

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar  5 2013 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.14-1
- update to 1.14

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 29 2010 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.13-1
- update to 1.13

* Tue Aug 25 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.10-1
- Update to 1.10
- Change urls for new upstream

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-4
- Autorebuild for GCC 4.3

* Thu Aug 16 2007 Dmitry Butskoy <Dmitry@Butskoy.name>
- Change License tag to GPLv2

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.9-3
- rebuild for FC6

* Tue Feb 14 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.9-2
- rebuild for FC5

* Mon Dec 19 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.9-1
- upgrade to 1.9

* Mon Nov 28 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 1.8-1
- upgrade to 1.8
- update description
