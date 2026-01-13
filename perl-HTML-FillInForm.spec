#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	FillInForm
Summary:	Populates HTML Forms with CGI data
Summary(pl.UTF-8):	Wypełnia formę HTML z danymi CGI
Name:		perl-HTML-FillInForm
Version:	2.00
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f2ab6814077e3a2d41a456f34ecb028f
URL:		http://search.cpan.org/dist/HTML-FillInForm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.26
%endif
Requires:	perl-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module automatically inserts data from a previous HTML form into
the HTML input and select tags. It is a subclass of HTML::Parser and
uses it to parse the HTML and insert the values into the form tags.

%description -l pl.UTF-8
Moduł automatycznie wstawia dane z poprzedniego formularza HTML w
wejście i tagi select HTML-a. Jest to podklasa HTML::Parser i korzysta
z niego do parsowania HTML i wstawiania danych w tagi formularza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/FillInForm.pm
%{_mandir}/man3/*
