# TODO: fix tests
#
# Conditional build:
%bcond_without	python2		# build python 2 module
%bcond_without	python3		# build python 3 module
%bcond_with	tests		# unit/functional tests [one fails on py3 as of 0.12.18, probably network is used]
#
%define 	module	bottle
#
Summary:	Fast and simple WSGI-framework for small web-applications
Summary(pl.UTF-8):	Szybki i prosty szkielet WSGI dla małych aplikacji sieciowych
Name:		python-%{module}
Version:	0.12.18
Release:	5
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/bottle/
Source0:	https://files.pythonhosted.org/packages/source/b/bottle/%{module}-%{version}.tar.gz
# Source0-md5:	a00b7e9a1ab3be7c19c1235fea2ccb40
URL:		http://bottlepy.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bottle is a fast and simple micro-framework for small
web-applications. It offers request dispatching (Routes) with url
parameter support, Templates, a build-in HTTP Server and adapters for
many third party WSGI/HTTP-server and template engines. All in a
single file and with no dependencies other than the Python Standard
Library.

%description -l pl.UTF-8
Bottle jest szybkim i prostym szkieletem dla małych aplikcaji WSGI.
Oferuje mapowanie urli poprzez Routes wspierając urle z parametrami,
wzroce, wbudowany serwer HTTP i wtyczki dla wielu serwerów WSGI/HTTP i
silników wzorców. Wszystko w jednym pliku bez zalezności innych niż
standardowej biblioteki Pythona.

%package -n python3-%{module}
Summary:	Fast and simple WSGI-framework for small web-applications
Summary(pl.UTF-8):	Szybki i prosty szkielet WSGI dla małych aplikacji sieciowych
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
Bottle is a fast and simple micro-framework for small
web-applications. It offers request dispatching (Routes) with url
parameter support, Templates, a build-in HTTP Server and adapters for
many third party WSGI/HTTP-server and template engines. All in a
single file and with no dependencies other than the Python Standard
Library.

%description -n python3-%{module} -l pl.UTF-8
Bottle jest szybkim i prostym szkieletem dla małych aplikcaji WSGI.
Oferuje mapowanie urli poprzez Routes wspierając urle z parametrami,
wzroce, wbudowany serwer HTTP i wtyczki dla wielu serwerów WSGI/HTTP i
silników wzorców. Wszystko w jednym pliku bez zalezności innych niż
standardowej biblioteki Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} test/testall.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test/testall.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{bottle.py,bottle-2}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{bottle.py,bottle-3}
ln -s bootle-3 $RPM_BUILD_ROOT%{_bindir}/bottle
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/bottle-2
%{py_sitescriptdir}/bottle.py[co]
%{py_sitescriptdir}/bottle-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/bottle
%attr(755,root,root) %{_bindir}/bottle-3
%{py3_sitescriptdir}/bottle.py
%{py3_sitescriptdir}/__pycache__/bottle.cpython-*.py[co]
%{py3_sitescriptdir}/bottle-%{version}-py*.egg-info
%endif
