#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : artikulate
Version  : 18.12.3
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.3/src/artikulate-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/artikulate-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/artikulate-18.12.3.tar.xz.sig
Summary  : Improve your pronunciation by listening to native speakers
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.1 LGPL-3.0
Requires: artikulate-bin = %{version}-%{release}
Requires: artikulate-data = %{version}-%{release}
Requires: artikulate-lib = %{version}-%{release}
Requires: artikulate-license = %{version}-%{release}
Requires: artikulate-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde

%description
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


%package dev
Summary: dev components for the artikulate package.
Group: Development
Requires: artikulate-lib = %{version}-%{release}
Requires: artikulate-bin = %{version}-%{release}
Requires: artikulate-data = %{version}-%{release}
Provides: artikulate-devel = %{version}-%{release}
Requires: artikulate = %{version}-%{release}

%description dev
dev components for the artikulate package.


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
%setup -q -n artikulate-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551981613
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1551981613
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/artikulate
cp COPYING %{buildroot}/usr/share/package-licenses/artikulate/COPYING
cp COPYING-ARTWORK %{buildroot}/usr/share/package-licenses/artikulate/COPYING-ARTWORK
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/artikulate/COPYING-CMAKE-SCRIPTS
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/artikulate/COPYING.DOC
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
/usr/share/artikulate/images/course-gray.png
/usr/share/artikulate/images/course.png
/usr/share/artikulate/images/new-course.png
/usr/share/artikulate/languages/ba.xml
/usr/share/artikulate/languages/ca.xml
/usr/share/artikulate/languages/de.xml
/usr/share/artikulate/languages/du.xml
/usr/share/artikulate/languages/en_BE.xml
/usr/share/artikulate/languages/en_US.xml
/usr/share/artikulate/languages/fr.xml
/usr/share/artikulate/languages/gr.xml
/usr/share/artikulate/languages/hi.xml
/usr/share/artikulate/languages/it.xml
/usr/share/artikulate/languages/mr.xml
/usr/share/artikulate/languages/pl.xml
/usr/share/artikulate/languages/sp.xml
/usr/share/artikulate/schemes/course.xsd
/usr/share/artikulate/schemes/language.xsd
/usr/share/artikulate/schemes/skeleton.xsd
/usr/share/artikulate/sounds/testsound.ogg
/usr/share/config.kcfg/artikulate.kcfg
/usr/share/icons/hicolor/16x16/actions/artikulate-course.png
/usr/share/icons/hicolor/16x16/actions/artikulate-expression.png
/usr/share/icons/hicolor/16x16/actions/artikulate-paragraph.png
/usr/share/icons/hicolor/16x16/actions/artikulate-sentence.png
/usr/share/icons/hicolor/16x16/actions/artikulate-word.png
/usr/share/icons/hicolor/16x16/apps/artikulate.png
/usr/share/icons/hicolor/32x32/actions/artikulate-course-editor.png
/usr/share/icons/hicolor/32x32/actions/artikulate-course.png
/usr/share/icons/hicolor/32x32/actions/artikulate-expression.png
/usr/share/icons/hicolor/32x32/actions/artikulate-paragraph.png
/usr/share/icons/hicolor/32x32/actions/artikulate-sentence.png
/usr/share/icons/hicolor/32x32/actions/artikulate-word.png
/usr/share/icons/hicolor/32x32/apps/artikulate.png
/usr/share/icons/hicolor/48x48/actions/artikulate-course.png
/usr/share/icons/hicolor/48x48/actions/artikulate-expression.png
/usr/share/icons/hicolor/48x48/actions/artikulate-paragraph.png
/usr/share/icons/hicolor/48x48/actions/artikulate-sentence.png
/usr/share/icons/hicolor/48x48/actions/artikulate-word.png
/usr/share/icons/hicolor/48x48/apps/artikulate.png
/usr/share/icons/hicolor/64x64/actions/artikulate-course-editor.png
/usr/share/icons/hicolor/64x64/actions/artikulate-expression.png
/usr/share/icons/hicolor/64x64/actions/artikulate-paragraph.png
/usr/share/icons/hicolor/64x64/actions/artikulate-sentence.png
/usr/share/icons/hicolor/64x64/actions/artikulate-word.png
/usr/share/icons/hicolor/64x64/apps/artikulate.png
/usr/share/icons/hicolor/scalable/actions/artikulate-course-editor.svgz
/usr/share/icons/hicolor/scalable/actions/artikulate-expression.svgz
/usr/share/icons/hicolor/scalable/actions/artikulate-paragraph.svgz
/usr/share/icons/hicolor/scalable/actions/artikulate-sentence.svgz
/usr/share/icons/hicolor/scalable/actions/artikulate-word.svgz
/usr/share/icons/hicolor/scalable/actions/language-artikulate.svg
/usr/share/icons/hicolor/scalable/apps/artikulate.svg
/usr/share/metainfo/org.kde.artikulate.appdata.xml
/usr/share/xdg/artikulate.knsrc

%files dev
%defattr(-,root,root,-)
/usr/lib64/libartikulatecore.so
/usr/lib64/libartikulatelearnerprofile.so
/usr/lib64/libartikulatesound.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/artikulate/editor-apply.png
/usr/share/doc/HTML/ca/artikulate/editor-cancel.png
/usr/share/doc/HTML/ca/artikulate/first-steps-1-create-profile.png
/usr/share/doc/HTML/ca/artikulate/first-steps-3-download-course.png
/usr/share/doc/HTML/ca/artikulate/first-steps-4-start-training.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-expression.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-language.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-media-playback-start.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-media-playback-stop.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-media-record-active.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-media-record.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-paragraph.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-sentence.png
/usr/share/doc/HTML/ca/artikulate/hi32-action-artikulate-word.png
/usr/share/doc/HTML/ca/artikulate/index.cache.bz2
/usr/share/doc/HTML/ca/artikulate/index.docbook
/usr/share/doc/HTML/ca/artikulate/screen-training-progressbar.png
/usr/share/doc/HTML/ca/artikulate/training-finish.png
/usr/share/doc/HTML/ca/artikulate/training-ok.png
/usr/share/doc/HTML/ca/artikulate/training-retry.png
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
/usr/share/package-licenses/artikulate/COPYING
/usr/share/package-licenses/artikulate/COPYING-ARTWORK
/usr/share/package-licenses/artikulate/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/artikulate/COPYING.DOC

%files locales -f artikulate.lang
%defattr(-,root,root,-)

