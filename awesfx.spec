Summary:	Utility programs for the AWE32 sound driver.
Name:		awesfx
Version:	0.4.3b
Release:	2
License:	GPL/distributable
Group:		Applications/Multimedia
Source:		http://bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/%{name}-%{version}.tgz
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source3:	awe_voice.h
Patch:		awesfx-0.4.3a-make.patch
URL:		http://bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/
ExclusiveArch:	%{ix86} alpha
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

%prep
%setup -q
mkdir gu11-rom
cd gu11-rom
unzip $RPM_SOURCE_DIR/gu11-rom.zip
cd ..
%patch -p1
mkdir include/linux
cp $RPM_SOURCE_DIR/awe_voice.h include/linux

%build
xmkmf
make Makefiles
make 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},/etc/midi,/bin}

make install install.man
mv $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin/
mv gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT/etc/midi

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	ChangeLog.sfx README SBKtoSF2.txt bank-samples
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc gu11-rom
/etc/midi/GU11-ROM.SF2
/bin/sfxload
%{_bindir}/setfx
%{_bindir}/sf2text
%{_bindir}/text2sf
%{_bindir}/gusload
%{_bindir}/sfxtest
%{_mandir}/man1/*
