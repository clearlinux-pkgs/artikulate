#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : artikulate
Version  : 21.12.1
Release  : 36
URL      : https://download.kde.org/stable/release-service/21.12.1/src/artikulate-21.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.1/src/artikulate-21.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.1/src/artikulate-21.12.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: artikulate-bin = %{version}-%{release}
Requires: artikulate-data = %{version}-%{release}
Requires: artikulate-lib = %{version}-%{release}
Requires: artikulate-license = %{version}-%{release}
Requires: artikulate-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : kirigami2-dev
BuildRequires : qtmultimedia-dev

%description
<!--
SPDX-License-Identifier: CC-BY-SA-4.0
-->
Artikulate
==========
Artikulate is a language learning application that helps improving pronunciation skills for
various languages. This repository maintains the application and language specifications. All course
files are maintained in a separate repository named "artikulate-data" and hosted on the KDE
infrastructure.

%package bin
Summary: bin components for the artikulate package.
Group: Binaries
Requires: artikulate-data = %{version}-%{release}
Requires: artikulate-license = %{version}-%{release}

%description bin
bin components for the artikulate package.


%package data
Summary: data components for the artikulate package.
Group: Data

%description data
data components for the artikulate package.


%package doc
Summary: doc components for the artikulate package.
Group: Documentation

%description doc
doc components for the artikulate package.


%package lib
Summary: lib components for the artikulate package.
Group: Libraries
Requires: artikulate-data = %{version}-%{release}
Requires: artikulate-license = %{version}-%{release}

%description lib
lib components for the artikulate package.


%package license
Summary: license components for the artikulate package.
Group: Default

%description license
license components for the artikulate package.


%package locales
Summary: locales components for the artikulate package.
Group: Default

%description locales
locales components for the artikulate package.


%prep
%setup -q -n artikulate-21.12.1
cd %{_builddir}/artikulate-21.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641936406
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1641936406
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/artikulate
cp %{_builddir}/artikulate-21.12.1/COPYING %{buildroot}/usr/share/package-licenses/artikulate/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/artikulate-21.12.1/COPYING.DOC %{buildroot}/usr/share/package-licenses/artikulate/7b3e5f0e946c0b599b04a45deebb1aaed782070d
cp %{_builddir}/artikulate-21.12.1/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/artikulate/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
cp %{_builddir}/artikulate-21.12.1/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/artikulate/7b3e5f0e946c0b599b04a45deebb1aaed782070d
cp %{_builddir}/artikulate-21.12.1/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/artikulate/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/artikulate-21.12.1/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/artikulate/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/artikulate-21.12.1/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/artikulate/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/artikulate-21.12.1/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/artikulate/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/artikulate-21.12.1/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/artikulate/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/artikulate-21.12.1/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/artikulate/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/artikulate-21.12.1/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/artikulate/6f1f675aa5f6a2bbaa573b8343044b166be28399
cp %{_builddir}/artikulate-21.12.1/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/artikulate/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/artikulate-21.12.1/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/artikulate/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/artikulate-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/artikulate/cc250ebd38b8d0ac13fc06208c14452ec41f40f1
cp %{_builddir}/artikulate-21.12.1/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/artikulate/cc250ebd38b8d0ac13fc06208c14452ec41f40f1
cp %{_builddir}/artikulate-21.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/artikulate/cbca59e0e62dd8bfc0468847678552cadebea0a9
cp %{_builddir}/artikulate-21.12.1/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/artikulate/cbca59e0e62dd8bfc0468847678552cadebea0a9
cp %{_builddir}/artikulate-21.12.1/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/artikulate/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
cp %{_builddir}/artikulate-21.12.1/libsound/src/qtgstreamerbackend/qtgstreamerbackend.json.license %{buildroot}/usr/share/package-licenses/artikulate/cb036b5481429dea37c9c20c313d7aa1d911b181
cp %{_builddir}/artikulate-21.12.1/libsound/src/qtmultimediabackend/qtmultimediabackend.json.license %{buildroot}/usr/share/package-licenses/artikulate/cb036b5481429dea37c9c20c313d7aa1d911b181
cp %{_builddir}/artikulate-21.12.1/logo.png.license %{buildroot}/usr/share/package-licenses/artikulate/528d7843c59ad6acea9d2211aa8c2101de4bafc8
pushd clr-build
%make_install
popd
%find_lang artikulate

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/artikulate
/usr/bin/artikulate_editor

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.artikulate.desktop
/usr/share/config.kcfg/artikulate.kcfg
/usr/share/icons/hicolor/16x16/apps/artikulate.png
/usr/share/icons/hicolor/32x32/apps/artikulate.png
/usr/share/icons/hicolor/48x48/apps/artikulate.png
/usr/share/icons/hicolor/64x64/apps/artikulate.png
/usr/share/icons/hicolor/scalable/apps/artikulate.svg
/usr/share/knsrcfiles/artikulate.knsrc
/usr/share/metainfo/org.kde.artikulate.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/artikulate/first-steps-1-create-profile.png
/usr/share/doc/HTML/ca/artikulate/first-steps-3-download-course.png
/usr/share/doc/HTML/ca/artikulate/first-steps-4-start-training.png
/usr/share/doc/HTML/ca/artikulate/index.cache.bz2
/usr/share/doc/HTML/ca/artikulate/index.docbook
/usr/share/doc/HTML/de/artikulate/index.cache.bz2
/usr/share/doc/HTML/de/artikulate/index.docbook
/usr/share/doc/HTML/en/artikulate/editor-apply.png
/usr/share/doc/HTML/en/artikulate/editor-cancel.png
/usr/share/doc/HTML/en/artikulate/editor-screenshot-editing-phrase.png
/usr/share/doc/HTML/en/artikulate/editor-screenshot-unit.png
/usr/share/doc/HTML/en/artikulate/editor-set-repository.png
/usr/share/doc/HTML/en/artikulate/first-steps-1-create-profile.png
/usr/share/doc/HTML/en/artikulate/first-steps-2-set-language.png
/usr/share/doc/HTML/en/artikulate/first-steps-3-download-course.png
/usr/share/doc/HTML/en/artikulate/first-steps-4-start-training.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-expression.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-language.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-media-playback-start.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-media-playback-stop.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-media-record-active.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-media-record.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-paragraph.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-sentence.png
/usr/share/doc/HTML/en/artikulate/hi32-action-artikulate-word.png
/usr/share/doc/HTML/en/artikulate/index.cache.bz2
/usr/share/doc/HTML/en/artikulate/index.docbook
/usr/share/doc/HTML/en/artikulate/screen-training-icon-finish.png
/usr/share/doc/HTML/en/artikulate/screen-training-overview.png
/usr/share/doc/HTML/en/artikulate/screen-training-progressbar.png
/usr/share/doc/HTML/en/artikulate/training-finish.png
/usr/share/doc/HTML/en/artikulate/training-ok.png
/usr/share/doc/HTML/en/artikulate/training-retry.png
/usr/share/doc/HTML/es/artikulate/index.cache.bz2
/usr/share/doc/HTML/es/artikulate/index.docbook
/usr/share/doc/HTML/et/artikulate/index.cache.bz2
/usr/share/doc/HTML/et/artikulate/index.docbook
/usr/share/doc/HTML/id/artikulate/index.cache.bz2
/usr/share/doc/HTML/id/artikulate/index.docbook
/usr/share/doc/HTML/nl/artikulate/index.cache.bz2
/usr/share/doc/HTML/nl/artikulate/index.docbook
/usr/share/doc/HTML/pt/artikulate/index.cache.bz2
/usr/share/doc/HTML/pt/artikulate/index.docbook
/usr/share/doc/HTML/pt_BR/artikulate/index.cache.bz2
/usr/share/doc/HTML/pt_BR/artikulate/index.docbook
/usr/share/doc/HTML/sv/artikulate/index.cache.bz2
/usr/share/doc/HTML/sv/artikulate/index.docbook
/usr/share/doc/HTML/uk/artikulate/index.cache.bz2
/usr/share/doc/HTML/uk/artikulate/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libartikulatecore.so.0
/usr/lib64/libartikulatelearnerprofile.so.0
/usr/lib64/libartikulatesound.so.0
/usr/lib64/qt5/plugins/artikulate/libsound/qtmultimediabackend.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/artikulate/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/artikulate/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/artikulate/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/artikulate/528d7843c59ad6acea9d2211aa8c2101de4bafc8
/usr/share/package-licenses/artikulate/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/artikulate/680ed9349d3d12bd39ddd36e8c4bc6b1b0cb1c0e
/usr/share/package-licenses/artikulate/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/artikulate/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/artikulate/7b3e5f0e946c0b599b04a45deebb1aaed782070d
/usr/share/package-licenses/artikulate/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/artikulate/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/artikulate/cb036b5481429dea37c9c20c313d7aa1d911b181
/usr/share/package-licenses/artikulate/cbca59e0e62dd8bfc0468847678552cadebea0a9
/usr/share/package-licenses/artikulate/cc250ebd38b8d0ac13fc06208c14452ec41f40f1
/usr/share/package-licenses/artikulate/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f artikulate.lang
%defattr(-,root,root,-)

