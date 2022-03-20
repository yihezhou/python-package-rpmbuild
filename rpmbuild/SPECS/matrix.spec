%define _buildnum %(date +%Y%m%d%H%M)
%define __python3 /usr/bin/python3
%define python3_sitelib /usr/lib/python3.6/site-packages

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
%{__python3} setup.py build

# 在buildroot中创建必要的目录，然后在构建的时候运行，将builddir中的文件安装到buildroot中，***不是在安装的时候运行。
%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_bindir}
install -d -m 755 %{buildroot}%{_sysconfdir}/matrix

%{__python3} setup.py install --skip-build --root %{buildroot}

# 安装matrix-service文件，requirements.txt文件, 安装后到目标系统执行pip3 install -r requirements.txt
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/matrix.service
install -p -D -m 644 requirements.txt %{buildroot}/%{_sysconfdir}/requirements.txt

#%check
#%{__python3} setup.py test

#%post
#%systemd_post %{name}.service

#%postun
#%systemd_postun_with_restart %{name}.service

# 将在目标系统中安装的文件列表
%files
%dir %{_sysconfdir}/matrix
%{python3_sitelib}

%{_bindir}/matrix-*
%{_unitdir}/*.service

%doc README.md
%license  LICENSE
