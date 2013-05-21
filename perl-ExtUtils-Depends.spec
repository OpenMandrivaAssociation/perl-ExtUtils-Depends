%define upstream_name    ExtUtils-Depends
%define upstream_version 0.304

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Perl module for further extending extensions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	perl-devel

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.304.0-4mdv2012.0
+ Revision: 765231
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.304.0-3
+ Revision: 763726
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.304.0-2
+ Revision: 656908
- rebuild for updated spec-helper

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.304.0-1
+ Revision: 634269
- update to new version 0.304

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.303.0-1mdv2011.0
+ Revision: 604718
- update to new version 0.303

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.302.0-2mdv2010.1
+ Revision: 504816
- rebuild using %%perl_convert_version

* Wed Jul 08 2009 Thierry Vignaud <tv@mandriva.org> 0.302-1mdv2010.0
+ Revision: 393596
- new release

* Sun Sep 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.301-1mdv2009.0
+ Revision: 282401
- update to new version 0.301

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.300-2mdv2009.0
+ Revision: 265361
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 0.300-1mdv2009.0
+ Revision: 192916
- new release
- new release

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.205-6mdv2008.1
+ Revision: 152072
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.205-4mdv2008.0
+ Revision: 64754
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.205-3mdv2008.0
+ Revision: 23412
- enable test


* Tue Feb 21 2006 Stefan van der Eijk <stefan@eijk.nu> 0.205-2mdk
- %%mkrel
- use %%makeinstall_std

* Mon Jan 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.205-1mdk
- new release

* Sat Jan 22 2005 Stefan van der Eijk <stefan@mandrake.org> 0.202-2mdk
- rebuild

* Sun Mar 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.202-1mdk
- new release

* Tue Mar 02 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.104-2mdk
- rebuild
- Own dir

* Fri Nov 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.104-1mdk
- new release

* Mon Aug 18 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.103-1mdk
- new release

* Mon Aug 04 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.102-2mdk
- perl_vendorlib

* Fri Jul 18 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.102-1mdk
- new release

* Thu Jul 10 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.cvs.2003.07.04.1-3mdk
- provides some doc
- generate build system in %%prep

* Fri Jul 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.cvs.2003.07.04.1-2mdk
- fix buildrequires
- fix description
- fix group
- fix summary

* Fri Jul 04 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.0.cvs.2003.07.04.1-1mdk
- initial release

