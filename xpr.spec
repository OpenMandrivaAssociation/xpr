Name: xpr
Version: 1.0.3
Release: %mkrel 2
Summary: Dump an X window directly to a printer
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xpr takes as input a window dump file produced by xwd(1) and formats it for
output on PostScript printers, the Digital LN03 or LA100, the IBM PP3812 page
printer, the HP LaserJet (or other PCL printers), or the HP PaintJet.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xpr
%{_bindir}/xdpr
%{_mandir}/man1/xdpr.1*
%{_mandir}/man1/xpr.1*
