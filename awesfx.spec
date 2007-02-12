Summary:	Utility programs for the AWE32 sound driver
Summary(pl.UTF-8):	Programy pomocnicze dla sterownika SoundBlastera AWE32
Summary(ru.UTF-8):	Утилиты для звукового драйвера AWE32
Summary(uk.UTF-8):	Утиліти для звукового драйвера AWE32
Name:		awesfx
Version:	0.5.0d
Release:	2
License:	GPL v2
Group:		Applications/Sound
Source0:	http://www.alsa-project.org/~iwai/%{name}-%{version}.tar.gz
# Source0-md5:	c258e52dd67a41fc20a31d25836c7256
# Source1:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source1:	gu11-rom.zip
# Source1-md5:	fe8f019945c0cbfc2d38dc5f0f94eb24
Patch0:		%{name}-etc_dir.patch
URL:		http://www.alsa-project.org/~iwai/awedrv.html#Utils
BuildRequires:	alsa-lib-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	unzip
Obsoletes:	awesfx-devel
ExclusiveArch:	%{ix86} %{x8664} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The awesfx package contains necessary utilities for the AWE32 sound
driver. This package contains the following programs:
 - asfxload - soundFont file loader for ALSA
 - sfxload - soundFont file loader for OSS emulation
 - setfx - chorus/reverb effect loader
 - aweset - change the running mode of AWE driver
 - sf2text - convert SoundFont to readable text
 - text2sf - revert from text to SoundFont file
 - gusload - GUS PAT file loader
 - sfxtest - example program to control AWE driver

%description -l pl.UTF-8
Pakiet awesfx zawiera programy niezbędne dla wykorzystania możliwości
sterownika SoundBlastera AWE32. Pakiet zawiera następujące programy:
 - asfxload - program ładujący SoundFonty dla ALSy
 - sfxload - program ładujący SoundFonty dla emulacji OSS
 - setfx - program ładujący efekty chorus/reverb
 - aweset - zmiana parametrów pracy sterownika AWE
 - sf2text - konwerter SoundFontów do postaci tekstowej
 - text2sf - konwerter z postaci tekstowej na SoundFont
 - gusload - program ładujący pliki PAT karty Gravis UltraSound
 - sfxtest - przykładowy program wykorzystujący sterownika AWE

%description -l ru.UTF-8
Пакет awesfx включает утилиты для звуковой карты AWE32.

%description -l uk.UTF-8
Пакет awesfx містить утиліти для звукової карти AWE32.

%prep
%setup -q
install -d gu11-rom
unzip %{SOURCE1} -d gu11-rom
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/bin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin
mv -f $RPM_BUILD_ROOT%{_bindir}/asfxload $RPM_BUILD_ROOT/bin
cp -f gu11-rom/GU11-ROM.{INS,SF2} $RPM_BUILD_ROOT%{_datadir}/sounds/sf2
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/asfxload.1
echo '.so sfxload.1' > $RPM_BUILD_ROOT%{_mandir}/man1/asfxload.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README SBKtoSF2.txt gu11-rom/*.TXT
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/sounds/sf2
%{_mandir}/man1/*
