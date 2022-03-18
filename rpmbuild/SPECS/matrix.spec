%define _buildnum %(date +%Y%m%d%H%M)

Name:       matrix
Version:    0.0.0
Release:    %{_buildnum}
Summary:    matrix api service
License:    matrix
URL:        http://matrix.com
Source0:    %{name}-%{version}.tar.gz
Source1:    matrix-api.service

%description
Matrix api service

%prep
%setup -q -n %{name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
%{__python2} setup.py test

%files
%doc README
