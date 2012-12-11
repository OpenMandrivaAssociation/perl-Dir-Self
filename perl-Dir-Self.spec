%define upstream_name    Dir-Self
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A __DIR__ constant for the directory your source file is in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dir/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Perl has two pseudo-constants describing the current location in your
source code, '__FILE__' and '__LINE__'. This module adds '__DIR__', which
expands to the directory your source file is in, as an absolute pathname.

This is useful if your code wants to access files in the same directory,
like helper modules or configuration data. This is a bit like the FindBin
manpage except it's not limited to the main program, i.e. you can also use
it in modules. And it actually works.

As of version 0.10 each use of '__DIR__' recomputes the directory name;
this ensures that files in different directories that share the same
package name get correct results. If you don't want this, 'use Dir::Self
qw(:static)' will create a true '__DIR__' constant in your package that
contains the directory name at the point of 'use'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 658747
- rebuild for updated spec-helper

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 554171
- import perl-Dir-Self


* Fri Jul 16 2010 cpan2dist 0.10-1mdv
- initial mdv release, generated with cpan2dist
