%define debug_package %{nil}

%define mybuildnumber %{?build_number}%{?!build_number:1}

Name:           better-symlinks
Version:        0.0.2
Release:        %{mybuildnumber}%{?dist}
Summary:        A very simple tool to manage your symlinks
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Rudd-O/%{name}
Source0:        https://github.com/Rudd-O/%{name}/archive/{%version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  make
Requires:       python3

%description
This program is a more comprehensive version of the `symlinks`
program commonly used on UNIX systems.

%prep
%setup -q

%build
# variables must be kept in sync with install
make DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}

%install
rm -rf $RPM_BUILD_ROOT
# variables must be kept in sync with build
for target in install ; do
    make $target DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir}
done

%files
%attr(0755, root, root) %{_bindir}/%{name}
%doc README.md

%changelog
* Tue Feb 01 2022 Manuel Amador (Rudd-O) <rudd-o@rudd-o.com>
- First release.
