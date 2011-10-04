#specfile originally created for Fedora, modified for Moblin Linux
Summary: X.Org X11 xkb utilities
Name: xorg-x11-xkb-utils
Version: 7.2
Release: 4
License: MIT/X11
Group: User Interface/X
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# use the macro so the doc dir is changed automagically
%define xkbutils_version 1.0.1
Source0: ftp://ftp.x.org/pub/individual/app/xkbutils-%{xkbutils_version}.tar.bz2
Source1: ftp://ftp.x.org/pub/individual/app/xkbcomp-1.0.5.tar.bz2
Source2: ftp://ftp.x.org/pub/individual/app/xkbevd-1.0.2.tar.bz2
Source3: ftp://ftp.x.org/pub/individual/app/xkbprint-1.0.1.tar.bz2
Source4: ftp://ftp.x.org/pub/individual/app/setxkbmap-1.0.4.tar.bz2

BuildRequires: pkgconfig
BuildRequires: libxkbfile-devel
BuildRequires: libX11-devel
BuildRequires: libXaw-devel
BuildRequires: libXt-devel
BuildRequires: pkgconfig(inputproto)
# FIXME: xkbvleds requires libXext, but autotools doesn't check/require it:
# gcc  -O2 -g -march=i386 -mcpu=i686   -o xkbvleds  xkbvleds-xkbvleds.o
# xkbvleds-LED.o xkbvleds-utils.o -lXaw7 -lXmu -lXt -lSM -lICE -lXext -lXpm -lX11 -ldl
# /usr/bin/ld: cannot find -lXext
# libXext-devel needed for xkbutils (from above error)
BuildRequires: libXext-devel
# FIXME: xkbvleds requires libXext, but autotools doesn't check/require it:
# gcc  -O2 -g -march=i386 -mcpu=i686   -o xkbvleds  xkbvleds-xkbvleds.o
# xkbvleds-LED.o xkbvleds-utils.o -lXaw7 -lXmu -lXt -lSM -lICE -lXext -lXpm -lX11 -ldl
# /usr/bin/ld: cannot find -lXpm
# libXpm-devel needed for xkbutils (from above error)
BuildRequires: libXpm-devel

Provides: setxkbmap, xkbcomp, xkbevd, xkbprint, xkbutils
Obsoletes: XFree86, xorg-x11

%description
X.Org X11 xkb utilities

%prep
%setup -q -c %{name}-%{version} -a1 -a2 -a3 -a4

%build
export CFLAGS="$RPM_OPT_FLAGS -DHAVE_STRCASECMP"
for pkg in xkbutils setxkbmap xkbcomp xkbevd xkbprint ; do
    pushd $pkg-*
    %configure
    make
    popd
done

%install
rm -rf $RPM_BUILD_ROOT
for pkg in xkbutils setxkbmap xkbcomp xkbevd xkbprint ; do
    pushd $pkg-*
    make install DESTDIR=$RPM_BUILD_ROOT
    popd
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc xkbutils-%{xkbutils_version}/AUTHORS xkbutils-%{xkbutils_version}/COPYING xkbutils-%{xkbutils_version}/INSTALL
%doc xkbutils-%{xkbutils_version}/NEWS xkbutils-%{xkbutils_version}/README xkbutils-%{xkbutils_version}/ChangeLog
%{_bindir}/setxkbmap
%{_bindir}/xkbbell
%{_bindir}/xkbcomp
%{_bindir}/xkbevd
%{_bindir}/xkbprint
%{_bindir}/xkbvleds
%{_bindir}/xkbwatch
%doc %{_mandir}/man1/setxkbmap.1*
%doc %{_mandir}/man1/xkbcomp.1*
%doc %{_mandir}/man1/xkbevd.1*
%doc %{_mandir}/man1/xkbprint.1*

