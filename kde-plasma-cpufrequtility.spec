%define cmake_build_dir build-cmake

Name: kde-plasma-cpufrequtility
Version: 1.5
Release: 1%{?dist}.R
Summary: CPU Frequence Utility plasmoid.
Summary(ru): Плазмоид для управления режимом работы процессора.
Group: Applications/Utility
License: GPL
Source0: http://cloud.github.com/downloads/F1ash/plasmaCpuFreqUtility/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: https://github.com/F1ash/plasmaCpuFreqUtility

Requires: python, PyQt4, PyKDE4, dbus, polkit
BuildRequires: gcc-c++ kdelibs-devel

%description
kde-plasma-cpufrequtility
CPU Frequence Utility plasmoid.

%description -l ru
kde-plasma-cpufrequtility
Плазмоид для управления режимом работы процессора.

%prep
%setup -q
mkdir %{cmake_build_dir}
pushd %{cmake_build_dir}
      %cmake ..
popd

%build
pushd %{cmake_build_dir}
      make %{?_smp_mflags}
popd

%install
pushd %{cmake_build_dir}
      make install DESTDIR=$RPM_BUILD_ROOT
popd

%files
%defattr(-,root,root)
%{_datadir}/kde4/services/%{name}.desktop
%{_datadir}/kde4/apps/plasma/plasmoids/%{name}
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.auth.cpufrequtility.conf
%{_libexecdir}/kde4/cpu_freq_helper
%{_datadir}/dbus-1/system-services/org.freedesktop.auth.cpufrequtility.service
%{_datadir}/polkit-1/actions/org.freedesktop.auth.cpufrequtility.policy

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

* Wed Oct 16 2011 Fl@sh <kaperang07@gmail.com> - 1.5-1
- Initial build

