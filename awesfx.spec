Summary:	Utility programs for the AWE32 sound driver.
Summary(pl):	Programy pomocnicze dla sterownika SoundBlastera AWE32.
Name:		awesfx
Version:	0.4.3c
Release:	1
License:	GPL/distributable
Group:		Applications/Multimedia
Group(pl):	Aplikacje/D¼wiêk
Source:		http://mitglied.tripod.de/iwai/%{name}-%{version}.tgz
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Patch:		awesfx-make.patch
URL:		http://mitglied.tripod.de/iwai/awedrv.html
ExclusiveArch:	%{ix86} alpha
BuildRequires:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The awesfx package contains necessary utilities for the AWE32 sound driver.
This packaing contains the following programs:
 - sfxload      SoundFont file loader
 - setfx        Chorus/reverb effect loader
 - aweset       Change the running mode of AWE driver
 - sf2text      Convert SoundFont to readable text
 - text2sf      Revert from text to SoundFont file
 - gusload      GUS PAT file loader
 - sfxtest      Example program to control AWE driver

%description -l pl
Pakiet awesfx zawieta programy niezbêdne dla wykorzystania mo¿liwo¶ci
sterownika SoundBlastera AWE32. Pakiet zawiera nastêpuj±ce programy:
 - sfxload	Program ³aduj±cy SoundFonty
 - setfx	Program ³aduj±cy efekty chorus/reverb
 - aweset	Zmiana parametrów pracy sterownika AWE
 - sf2text	Konwerter SoundFontów do postaci tekstowej
 - text2sf	Konwerter z postaci tekstowej na SoundFont
 - gusload	Program ³aduj±cy pliki PAT karty Gravis UltraSound
 - sfxtest	Przyk³adowy program wykorzystuj±cy sterownika AWE

%package devel
Summary:	Header files for programs using AWE library.
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
If you want to write programs using Sound Blaster AWE WaveTable, you need
these files.

%description devel -l pl
Je¶li chcesz pisaæ programy wykorzystuj±ce sterownik SoundBlastera AWE
bêdziesz potrzebowa³ tych plików.

%prep
%setup -q
mkdir gu11-rom
cd gu11-rom
unzip $RPM_SOURCE_DIR/gu11-rom.zip
cd ..
%patch -p1

%build
xmkmf
make Makefiles
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/bin} \
	$RPM_BUILD_ROOT%{_datadir}/midi/{soundfont,virtualbank}

make DESTDIR=$RPM_BUILD_ROOT _MANDIR=%{_mandir} install install.man
mv $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin/
mv gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT%{_datadir}/midi/soundfont/gu11-rom.sf2
mv samples/* $RPM_BUILD_ROOT%{_datadir}/midi/virtualbank

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	docs/{ChangeLog.sfx,README,SBKtoSF2.txt} \
	gu11-rom/*

strip --strip-unneeded $RPM_BUILD_ROOT{/bin/*,%{_libdir}/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%doc gu11-rom/*
%{_datadir}/midi/*/*
/usr/lib/*
%attr(755,root,root)/bin/*
%attr(755,root,root)%{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/awe
