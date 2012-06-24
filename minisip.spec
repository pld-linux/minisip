Summary:	minisip - SIP user agent with security enhancements
Summary(pl):	minisip - agent u�ytkownika SIP z rozszerzeniami bezpiecze�stwa
Name:		minisip
Version:	0.7.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://www.minisip.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	1c1bca512414430feced8d0011b8439c
URL:		http://www.minisip.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libmikey-devel >= 0.4.0
BuildRequires:	libmsip-devel >= 0.3.0
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
minisip is a soft telephone which uses the SIP protocol. It provides
additional security, such as encryption and authentication, by using
the SRTP (RFC 3711) and MIKEY (RFC 3830) protocols. It uses GTK+ for
the graphical interface.

%description -l pl
minisip to telefon programowy u�ywaj�cy protoko�u SIP. Udost�pnia
dodatkowe bezpiecze�stwo, takie jak szyfrowanie i uwierzytelnianie
poprzez u�ywanie protoko��w SRTP (RFC 3711) i MIKEY (RFC 3830). U�ywa
interfejsu graficznego GTK+.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	 --enable-alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/minisip
