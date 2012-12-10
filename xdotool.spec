Summary:	Command-line X11 automation tool
Name:		xdotool
Version:	2.20110530.1
Release:	2
License:	BSD-like
Group:		X11/Window Managers/Tools
Source0:	http://semicomplete.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	62d0c2158bbaf882a1cf580421437b2f
URL:		http://www.semicomplete.com/projects/xdotool/
BuildRequires:	perl-tools-pod
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdotool lets you programatically (or manually) simulate keyboard input
and mouse activity, move and resize windows, etc. It does this using
X11's XTEST extension and other Xlib functions.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} static \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}}

%{__make} install-static installman \
	INSTALLBIN=$RPM_BUILD_ROOT%{_bindir}	\
	INSTALLMAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT CHANGELIST README examples
%attr(755,root,root) %{_bindir}/xdotool
%{_mandir}/man1/xdotool.1*

