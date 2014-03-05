%define debug_package %{nil}

Name:		netio
Version: 	1.31
Release:	2
License: 	GPL
Group: 		Monitoring
Url:		http://www.ars.de/ars/ars.nsf/docs/netio
Source:		http://www.ars.de/ars/ars.nsf/netio-131.tar.bz2
Summary: 	Network benchmarking tool
BuildRequires:  glibc-devel libgcc gcc gcc-c++
BuildRequires:  dos2unix

%description
This is a network benchmark for, OS/2 2.x, Windows NT/2000 and Unix.
It measures the net throughput of a network via NetBIOS, TCP and UDP
protocols (Unix only supports TCP and UDP) using various different
packet sizes.

%prep
%setup -q -n %{name}-131

%build

dos2unix *.c *.h
%make linux

%install
mkdir -p %{buildroot}/%{_sbindir}
cp -pr netio %{buildroot}/%{_sbindir}

%files 
%doc bin/win32-i386.exe
%doc bin/os2-i386.exe
%doc netio.doc
/usr/sbin/netio
