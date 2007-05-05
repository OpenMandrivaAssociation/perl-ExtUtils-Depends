%define module ExtUtils-Depends
%define name perl-%module
%define version 0.205
%define release %mkrel 3

Summary: Perl module for further extending extensions
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPL or Artistic
Group:   Development/Perl
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRequires: perl-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -fr
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/*

