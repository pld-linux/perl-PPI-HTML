#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PPI
%define		pnam	HTML
Summary:	PPI::HTML - Generate syntax-hightlighted HTML for Perl using PPI
Summary(pl.UTF-8):	PPI::HTML - generowanie HTML-a z podświetlaniem składni dla Perla z PPI
Name:		perl-PPI-HTML
Version:	1.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PPI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7485ae90643992f410fba6ba6573872f
URL:		http://search.cpan.org/dist/PPI-HTML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CSS-Tiny >= 1.10
BuildRequires:	perl-PPI >= 0.990
BuildRequires:	perl-Params-Util >= 0.05
%endif
Requires:	perl-CSS-Tiny >= 1.10
Requires:	perl-PPI >= 0.990
Requires:	perl-Params-Util >= 0.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PPI::HTML converts Perl documents into syntax highlighted HTML pages.

%description -l pl.UTF-8
PPI::HTML konwertuje dokumenty Perla do stron HTML z podświetlaniem
składni.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/ppi2html
%{perl_vendorlib}/PPI/HTML.pm
%{perl_vendorlib}/PPI/HTML
%{_mandir}/man3/PPI::HTML.3pm*
