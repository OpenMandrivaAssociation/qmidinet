Summary:	A MIDI Network Gateway via UDP/IP Multicast
Name:		qmidinet
Version:	0.9.11
Release:	1
License:	GPLv2+
Group:		Sound/Utilities
URL:		https://qmidinet.sourceforge.net/
Source0:	https://sourceforge.net/projects/qmidinet/files/qmidinet/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)

%description
QmidiNet is a MIDI network gateway application that sends and receives
MIDI data (ALSA Sequencer and/or JACK MIDI) over the network, using UDP/IP
multicast. Inspired by multimidicast (http://llg.cubic.org/tools) and
designed to be compatible with ipMIDI for Windows (http://nerds.de).

%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes
%make_build

%install
%make_install -C build

#menu
desktop-file-install \
  --remove-key="X-SuSE-translate" \
  --remove-key="Version" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/org.rncbc.qmidinet.desktop

%files
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/applications/org.rncbc.qmidinet.desktop
#{_datadir}/metainfo/%{name}.appdata.xml
#{_iconsdir}/hicolor/*x*/apps/%{name}.png
#{_iconsdir}/hicolor/scalable/apps/qmidinet.svg
%{_mandir}/man1/qmidinet.1.*
%{_mandir}/fr/man1/qmidinet.1.*
