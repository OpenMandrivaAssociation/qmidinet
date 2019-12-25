Summary:	A MIDI Network Gateway via UDP/IP Multicast
Name:		qmidinet
Version:	0.6.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound/Utilities
URL:		http://qmidinet.sourceforge.net/
Source0:	http://sourceforge.net/projects/qmidinet/files/qmidinet/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	qttools5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)

%description
QmidiNet is a MIDI network gateway application that sends and receives
MIDI data (ALSA Sequencer and/or JACK MIDI) over the network, using UDP/IP
multicast. Inspired by multimidicast (http://llg.cubic.org/tools) and
designed to be compatible with ipMIDI for Windows (http://nerds.de).

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x --enable-debug
%make_build

%install
%make_install

#menu
desktop-file-install \
  --remove-key="X-SuSE-translate" \
  --remove-key="Version" \
  --add-category="X-Mageia-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
