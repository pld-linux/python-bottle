#
# Conditional build:
%bcond_without	python2		# build python 2 module
%bcond_without	python3		# build python 3 module
#
%define 	module	bottle
#
Summary:	Fast and simple WSGI-framework for small web-applications
Summary(pl.UTF-8):	Szybki i prosty szkielet WSGI dla małych aplikacji sieciowych
Name:		python-%{module}
Version:	0.12.9
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/b/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	f5850258a86224a791171e8ecbb66d99
URL:		http://bottlepy.org
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
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
%{__python} setup.py build -b build-2
%endif

%if %{with python3}
%{__python3} setup.py build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build -b build-2 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build -b build-3 \
	install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{module}-*.egg-info
%endif
