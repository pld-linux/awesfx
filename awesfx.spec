Summary:	Utility programs for the AWE32 sound driver
Summary(pl):	Programy pomocnicze dla sterownika SoundBlastera AWE32
Name:		awesfx
Version:	0.4.3c
Release:	2
License:	GPL/distributable
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/DºwiÍk
Group(pt_BR):	AplicaÁıes/Som
Source0:	http://mitglied.tripod.de/iwai/%{name}-%{version}.tgz
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Patch0:		%{name}-make.patch
URL:		http://mitglied.tripod.de/iwai/awedrv.html#Utils
ExclusiveArch:	%{ix86} alpha
BuildRequires:	unzip
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The awesfx package contains necessary utilities for the AWE32 sound
driver. This packaing contains the following programs:
 - sfxload - soundFont file loader
 - setfx - chorus/reverb effect loader
 - aweset - change the running mode of AWE driver
 - sf2text - convert SoundFont to readable text
 - text2sf - revert from text to SoundFont file
 - gusload - GUS PAT file loader
 - sfxtest - example program to control AWE driver

%description -l pl
Pakiet awesfx zawieta programy niezbÍdne dla wykorzystania moøliwo∂ci
sterownika SoundBlastera AWE32. Pakiet zawiera nastÍpuj±ce programy:
 - sfxload - program ≥aduj±cy SoundFonty
 - setfx - program ≥aduj±cy efekty chorus/reverb
 - aweset - zmiana parametrÛw pracy sterownika AWE
 - sf2text - konwerter SoundFontÛw do postaci tekstowej
 - text2sf - konwerter z postaci tekstowej na SoundFont
 - gusload - program ≥aduj±cy pliki PAT karty Gravis UltraSound
 - sfxtest - przyk≥adowy program wykorzystuj±cy sterownika AWE

%package devel
Summary:	Header files for programs using AWE library
Summary(pl):	Pliki nag≥Ûwkowe dla programÛw korzystaj±cych z biblioteki AWE
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
If you want to write programs using Sound Blaster AWE WaveTable, you
need these files.

%description devel -l pl
Je∂li chcesz pisaÊ programy wykorzystuj±ce sterownik SoundBlastera AWE
bÍdziesz potrzebowa≥ tych plikÛw.

%prep
%setup -q
mkdir gu11-rom
(cd gu11-rom
unzip %{SOURCE2}
)
%patch -p1

%build
xmkmf
%{__make} Makefiles
%{__make} OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/bin} \
	$RPM_BUILD_ROOT%{_datadir}/midi/{soundfont,virtualbank}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	_MANDIR=%{_mandir}

mv -f $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin/
mv -f gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT%{_datadir}/midi/soundfont/gu11-rom.sf2
mv -f samples/* $RPM_BUILD_ROOT%{_datadir}/midi/virtualbank

gzip -9nf docs/{ChangeLog.sfx,README,SBKtoSF2.txt} \
	gu11-rom/*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/*.gz gu11-rom/*
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/midi
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/awe
%attr(755,root,root) %{_libdir}/lib*.so
