%define modname	ExtUtils-Depends
%define modver 0.8000

Summary:	Perl module for further extending extensions


Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -qn %{modname}-%{modver}
find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*
