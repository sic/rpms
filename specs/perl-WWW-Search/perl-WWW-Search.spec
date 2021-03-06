# $Id$
# Authority: dries
# Upstream: John Heidemann <johnh$isi,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Search

Summary: Virtual base class for WWW searches
Name: perl-WWW-Search
Version: 2.507
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Search/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Search-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::MM_Unix) >= 1.41
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(IO::Capture::Stderr)
BuildRequires: perl(Test::File)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Simple)
Requires: perl >= 0:5.004

%description
Virtual base class for WWW searches.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' lib/WWW/Search/*.pm

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/AutoSearch.1*
%doc %{_mandir}/man1/WebSearch.1*
%doc %{_mandir}/man3/WWW::Search.3pm*
%doc %{_mandir}/man3/WWW::SearchResult.3pm*
%doc %{_mandir}/man3/WWW::Search::*.3pm*
%{_bindir}/AutoSearch
%{_bindir}/WebSearch
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Search/
%{perl_vendorlib}/WWW/Search.pm
%{perl_vendorlib}/WWW/SearchResult.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 2.507-1
- Updated to version 2.507.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.501-1
- Updated to release 2.501.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 2.497-1
- Updated to release 2.497.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.496-1
- Updated to release 2.496.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.494-1
- Updated to release 2.494.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.491-1
- Updated to release 2.491.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.489-1
- Updated to release 2.489.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 2.488-1
- Updated to release 2.488.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.487-1
- Updated to release 2.487.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.484-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.484-1
- Updated to release 2.484.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.479-1
- Updated to release 2.479.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 2.476-1
- Updated to release 2.476.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 2.475
- Initial package.
