#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	FillInForm
Summary:	Populates HTML Forms with CGI data
Summary(pl):	Wype³nia formê HTML z danymi CGI
Name:		perl-HTML-FillInForm
Version:	1.04
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fcb04346abbf5082f541973314254ea8
URL:		http://search.cpan.org/dist/HTML-FillInForm/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module automatically inserts data from a previous HTML form into
the HTML input and select tags. It is a subclass of HTML::Parser and
uses it to parse the HTML and insert the values into the form tags.

%description -l pl
Modu³ automatycznie wstawia dane z poprzedniego formularza HTML w
wej¶cie i tagi select HTML-a. Jest to podklasa HTML::Parser i korzysta
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
%dir %{perl_vendorlib}/HTML
%{perl_vendorlib}/HTML/FillInForm.pm
%{_mandir}/man3/*
