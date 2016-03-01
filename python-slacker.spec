#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	slacker
Summary:	Slack API client
Name:		python-%{module}
Version:	0.9.2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/slacker/%{module}-%{version}.tar.gz
# Source0-md5:	55d089c4350b3a74d0f1a007b0a93fee
URL:		https://github.com/os/slacker/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slacker is a full-featured Python interface for the Slack API.

%package -n python3-%{module}
Summary:	Slack API client
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Slacker is a full-featured Python interface for the Slack API.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
