Summary:	Utility programs for the AWE32 sound driver
Summary(pl):	Programy pomocnicze dla sterownika SoundBlastera AWE32
Summary(ru):	õÔÉÌÉÔÙ ÄÌÑ Ú×ÕËÏ×ÏÇÏ ÄÒÁÊ×ÅÒÁ AWE32
Summary(uk):	õÔÉÌ¦ÔÉ ÄÌÑ Ú×ÕËÏ×ÏÇÏ ÄÒÁÊ×ÅÒÁ AWE32
Name:		awesfx
Version:	0.4.4
Release:	3
License:	GPL/distributable
Group:		Applications/Sound
Source0:	http://mitglied.lycos.de/iwai/%{name}-%{version}.tgz
# Source0-md5:	8318bdb22a12b32a16e4d04a68e197d9
# Source1:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source1:	gu11-rom.zip
# Source1-md5:	fe8f019945c0cbfc2d38dc5f0f94eb24
Patch0:		%{name}-make.patch
Patch1:		%{name}-etc_dir.patch
URL:		http://mitglied.tripod.de/iwai/awedrv.html#Utils
BuildRequires:	XFree86-devel
BuildRequires:	unzip
ExclusiveArch:	%{ix86} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The awesfx package contains necessary utilities for the AWE32 sound
driver. This package contains the following programs:
 - sfxload - soundFont file loader
 - setfx - chorus/reverb effect loader
 - aweset - change the running mode of AWE driver
 - sf2text - convert SoundFont to readable text
 - text2sf - revert from text to SoundFont file
 - gusload - GUS PAT file loader
 - sfxtest - example program to control AWE driver

%description -l pl
Pakiet awesfx zawiera programy niezbêdne dla wykorzystania mo¿liwo¶ci
sterownika SoundBlastera AWE32. Pakiet zawiera nastêpuj±ce programy:
 - sfxload - program ³aduj±cy SoundFonty
 - setfx - program ³aduj±cy efekty chorus/reverb
 - aweset - zmiana parametrów pracy sterownika AWE
 - sf2text - konwerter SoundFontów do postaci tekstowej
 - text2sf - konwerter z postaci tekstowej na SoundFont
 - gusload - program ³aduj±cy pliki PAT karty Gravis UltraSound
 - sfxtest - przyk³adowy program wykorzystuj±cy sterownika AWE

%description -l ru
ğÁËÅÔ awesfx ×ËÌÀŞÁÅÔ ÕÔÉÌÉÔÙ ÄÌÑ Ú×ÕËÏ×ÏÊ ËÁÒÔÙ AWE32.

%description -l uk
ğÁËÅÔ awesfx Í¦ÓÔÉÔØ ÕÔÉÌ¦ÔÉ ÄÌÑ Ú×ÕËÏ×Ï§ ËÁÒÔÉ AWE32.

%package devel
Summary:	Header files for programs using AWE library
Summary(pl):	Pliki nag³ówkowe dla programów korzystaj±cych z biblioteki AWE
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
If you want to write programs using Sound Blaster AWE WaveTable, you
need these files.

%description devel -l pl
Je¶li chcesz pisaæ programy wykorzystuj±ce sterownik SoundBlastera AWE
bêdziesz potrzebowa³ tych plików.

%prep
%setup -q
install -d gu11-rom
unzip %{SOURCE1} -d gu11-rom
%patch0 -p1
%patch1 -p1

%build
xmkmf
%{__make} Makefiles
%{__make} \
	OPT_FLAGS="%{rpmcflags}" \
	SOSYMLINK="true"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/bin} \
	$RPM_BUILD_ROOT%{_datadir}/midi/{soundfont,virtualbank}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	_MANDIR=%{_mandir} \
	SOSYMLINK="true"

mv -f $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin
mv -f gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT%{_datadir}/midi/soundfont/gu11-rom.sf2
mv -f samples/* $RPM_BUILD_ROOT%{_datadir}/midi/virtualbank

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc docs/{ChangeLog.sfx,README,SBKtoSF2.txt} gu11-rom
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/midi
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/awe
