Summary: Utility programs for the AWE32 sound driver.
Name: awesfx
Version: 0.4.3a
Release: 2
Group: Applications/Multimedia
URL: http//bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/index.html
Source: http://bahamut.mm.t.u-tokyo.ac.jp/~iwai/awedrv/awesfx-%{version}.tgz
Source2: http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source3: awe_voice.h
Patch: awesfx-0.4.3a-make.patch
Copyright: GPL/distributable
Prefix: /usr
ExclusiveArch: i386 alpha
BuildRoot: /var/tmp/awesfx-root
%description
The awesfx package contains necessary utilities for the AWE32
sound driver.

If you must use an AWE32 sound driver, you should install
this package.

%prep
%setup
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
mkdir -p $RPM_BUILD_ROOT/usr/{man/man1,bin}
mkdir -p $RPM_BUILD_ROOT/etc/midi
mkdir -p $RPM_BUILD_ROOT/bin
make install
make install.man
mv $RPM_BUILD_ROOT/usr/bin/sfxload $RPM_BUILD_ROOT/bin/
mv gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT/etc/midi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog.sfx README SBKtoSF2.txt bank-samples
%doc gu11-rom
/etc/midi/GU11-ROM.SF2
/bin/sfxload
/usr/bin/setfx
/usr/bin/sf2text
/usr/bin/text2sf
/usr/bin/gusload
/usr/bin/sfxtest
/usr/man/man1/sfxload.1
