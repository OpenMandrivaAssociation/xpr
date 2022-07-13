Name:		xpr
Version:	1.1.0
Release:	1
Summary:	Dump an X window directly to a printer
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	x11-util-macros

%description
Xpr takes as input a window dump file produced by xwd(1) and formats it for
output on PostScript printers, the Digital LN03 or LA100, the IBM PP3812 page
printer, the HP LaserJet (or other PCL printers), or the HP PaintJet.

%prep
%setup -q

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xpr
%{_bindir}/xdpr
%{_mandir}/man1/xdpr.1*
%{_mandir}/man1/xpr.1*

