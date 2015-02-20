Summary:	QLogic PSM libraries
Summary(pl.UTF-8):	Biblioteki QLogic PSM
Name:		infinipath-psm
Version:	1.14
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/infinipath-psm/%{name}-%{version}.tar.gz
# Source0-md5:	76b83f3d1c0ab12d02e9680e514f4b68
Patch0:		%{name}-union.patch
Patch1:		%{name}-format.patch
Patch2:		%{name}-link.patch
URL:		http://www.openfabrics.org/
BuildRequires:	libuuid-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch	%{ix86}
%define psmarch i386
%else
%define psmarch x86_64
%endif

%description
The PSM Messaging API, or PSM API, is QLogic's low-level user-level
communications interface for the Truescale family of products. PSM
users are enabled with mechanisms necessary to implement higher level
communications interfaces in parallel environments.

%description -l pl.UTF-8
PSM Messaging API (lub PSM API) to niskopoziomowy interfejs
komunikacyjny QLogic dla przestrzeni użytkownika dla produktów z
rodziny Truescale. Ten pakiet dostarcza użytkownikom PSM mechanizmy
potrzebne do zaimplementowania interfejsów komunikacyjnych wyższego
poziomu w środowiskach równoległych.

%package devel
Summary:	Header files for PSM API
Summary(pl.UTF-8):	Pliki nagłówkowe PSM API
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for PSM API.

%description devel -l pl.UTF-8
Pliki nagłówkowe PSM API.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	BASECFLAGS="%{rpmcflags} -fPIC -funwind-tables -D_GNU_SOURCE -DPSM_USE_SYS_UUID" \
	arch=%{psmarch}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	arch=%{psmarch}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/libpsm_infinipath.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libpsm_infinipath.so.1
%attr(755,root,root) %{_libdir}/libinfinipath.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libinfinipath.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpsm_infinipath.so
%attr(755,root,root) %{_libdir}/libinfinipath.so
%{_includedir}/psm.h
%{_includedir}/psm_mq.h
