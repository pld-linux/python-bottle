%define 	module	bottle
Summary:	Fast and simple WSGI-framework for small web-applications
Summary(pl.UTF-8):	Szybki i prosty szkielet WSGI dla małych aplikacji sieciowych
Name:		python-%{module}
Version:	0.8.3
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	8d0c8282d8311dc63099f98d362f2e63
URL:		http://bottle.paws.de/docs/dev/index.html
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
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

%prep
%setup -q -n %{module}-%{version}

%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
