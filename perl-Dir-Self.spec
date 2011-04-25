%define upstream_name    Dir-Self
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A __DIR__ constant for the directory your source file is in
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dir/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


