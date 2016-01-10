%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _binary_payload w1.xzdio
%define _source_payload w1.xzdio
%define _disable_lto 1

%bcond_without l10n
%bcond_with icecream
%bcond_with ccache

%define beta %{nil}

%if %{with l10n}
%define langs	en-US af ar as bg bn br bs ca cs cy da de dz el en-GB es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai mk ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-TW zh-CN zu
%define helplangs	bg bn bs ca cs da de dz el en-GB es et eu fi fr gl gu he hi hr hu it ja ko mk nb nl nn pl pt pt-BR ru si sk sl sv tr uk zh-CN zh-TW en-US
%else
%define langs	en-US
%define helplangs	en-US
%endif

%define javaless 0

%define relurl		http://download.documentfoundation.org/libreoffice/src/%{version}
%define devurl		http://dev-www.libreoffice.org/ooo_external
%define srcurl		http://dev-www.libreoffice.org/src/
%define oxyurl		http://ooo.itc.hu/oxygenoffice/download/libreoffice/
%define distroname	OpenMandriva
%define ooname		libreoffice
%define buildver	%{version}.1
%define ooodir		%{_libdir}/libreoffice
%define antpath		%{_builddir}/libreoffice-%{version}/apache-ant-1.8.1
#define unopkg		%{_bindir}/unopkg

%define ccachedir	~/.ccache-OOo

%if %{_use_internal_dependency_generator}
%define __noautoreq 'libjawt.so|libmyspell.so|libstlport_gcc.so|libmono.so|mono|devel\\(libunoidl(.*)'
%define __noautoprov libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1
%else
%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libmono.so\\|mono\\|devel(libunoidl)\\|devel(libunoidl(64bit))
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1
%endif

Summary:	Office suite 
Name:		libreoffice
Epoch:		1
Version:	5.1.0
%if "%beta" != ""
Release:	0.%{beta}.1
%else
Release:	1
%endif
Source0:	%{relurl}/%{ooname}-%{buildver}.tar.xz
Source1:	%{relurl}/%{ooname}-dictionaries-%{buildver}.tar.xz
Source2:	%{relurl}/%{ooname}-help-%{buildver}.tar.xz
Source3:	%{relurl}/%{ooname}-translations-%{buildver}.tar.xz
License:	(MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic
Group:		Office
Url:		http://www.libreoffice.org
Source4:	http://dev-www.libreoffice.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll

Source10:	Mandriva-Rosa_Icons.tar.bz2
#javaless
%if %{javaless}
Source20:	http://archive.apache.org/dist/ant/binaries/apache-ant-1.8.1-bin.tar.bz2
Source30:	%{devurl}/af3c3acf618de6108d65fcdc92b492e1-commons-codec-1.3-src.tar.gz
Source31:	%{devurl}/2c9b0f83ed5890af02c0df1c1776f39b-commons-httpclient-3.1-src.tar.gz 
Source32:	%{devurl}/2ae988b339daec234019a7066f96733e-commons-lang-2.3-src.tar.gz 
%endif
Source33:	%{devurl}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
Source34:	%{devurl}/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source35:	%{devurl}/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source36:	%{devurl}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source37:	%{devurl}/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip

# External Download Sources
Source40:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz

# Extensions
Source50:	%{srcurl}1f467e5bb703f12cbbb09d5cf67ecf4a-converttexttonumber-1-5-0.oxt
Source51:	%{srcurl}b63e6340a02ff1cacfeadb2c42286161-JLanguageTool-1.7.0.tar.bz2
Source52:	%{oxyurl}3ed18025a766f1e955707b969c8113a5-Barcode_1.3.5.0.oxt
Source53:	%{oxyurl}8d74685d41f8bffe8c3e71fe8deac09d-SmART_0.9.5.oxt
Source54:	%{oxyurl}b632bdd25649cc4067bcb410bae23d2b-hunart_0.3.oxt
Source55:	%{srcurl}27211596cf0ad97cab7321239406fde0-gdocs_3.0.1_modified.oxt
Source56:	%{srcurl}b7cae45ad2c23551fd6ccb8ae2c1f59e-numbertext_0.9.5.oxt
Source57:	%{oxyurl}9d60b6cfa3ef1926848710bbcd11115b-typo_0.4.2.oxt
Source58:	%{oxyurl}bbdd5639ada63e3130761daaecae1a10-Validator_1.1.0.0.oxt
Source59:	%{oxyurl}23bd75552206dfcd8fd4e29137dcac84-WatchWindow_1.2.0.0.oxt
Source60:	%{oxyurl}af9314c5972d95a5d6da23ffad818f68-OOOP-gallery-pack-2.8.0.0.zip
Source61:	%{oxyurl}1be202fbbbc13f10592a98f70a4a87fb-OOOP-templates-pack-2.9.0.0.zip
Source62:	%{oxyurl}53ca5e56ccd4cab3693ad32c6bd13343-Sun-ODF-Template-Pack-de_1.0.0.oxt
Source63:	%{oxyurl}472ffb92d82cf502be039203c606643d-Sun-ODF-Template-Pack-en-US_1.0.0.oxt
Source64:	%{oxyurl}4ad003e7bbda5715f5f38fde1f707af2-Sun-ODF-Template-Pack-es_1.0.0.oxt
Source65:	%{oxyurl}a53080dc876edcddb26eb4c3c7537469-Sun-ODF-Template-Pack-fr_1.0.0.oxt
Source66:	%{oxyurl}09ec2dac030e1dcd5ef7fa1692691dc0-Sun-ODF-Template-Pack-hu_1.0.0.oxt
Source67:	%{oxyurl}b33775feda3bcf823cad7ac361fd49a6-Sun-ODF-Template-Pack-it_1.0.0.oxt

Source1000:	libreoffice.rpmlintrc

Patch0:		libreoffice-4.1.0.1-non-fatal-error-during-test.patch
#Patch2:		help-images-mdv64789.patch

# Force Qt4 event loops because with glib event loops libreoffice-kde4 doesn't
# work well
# Requires patched Qt4, see https://bugreports.qt-project.org/browse/QTBUG-16934
# Patch50:	libreoffice-4.1.2.2-kde-qt-event-loop.patch
# From ROSA:
# Hack: Don't display tiny useless scrollbars with libreoffice-kde4
# Impress is known to crash when adding effects (segfault is triggered by 15x18 scrollbar)
Patch51:	libreoffice-4.2.5.2-impress-kde-crash-hack.patch

# OpenMandriva vendor patch
Patch100:	libreoffice-4.3.1.2-vendor.patch
Patch101:	libreoffice-4.2.5.2-desktop-categories.patch

# Other bugfix patches, including upstream
Patch202:	0001-disable-firebird-unit-test.patch

%if %{with icecream}
BuildRequires:	icecream
%endif
%if %{with ccache}
BuildRequires:	ccache
%endif
BuildRequires:	boost-devel
BuildRequires:	bison
BuildRequires:	bsh
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen >= 1.8.4
BuildRequires:	ed
BuildRequires:	firebird-devel
BuildRequires:	flex
BuildRequires:	flute
BuildRequires:	gdb
BuildRequires:	git
BuildRequires:	gperf
BuildRequires:	glm-devel
BuildRequires:	icu
BuildRequires:	imagemagick
BuildRequires:	mysql-connector-c++-devel
BuildRequires:	pentaho-libxml
BuildRequires:	pentaho-reporting-flow-engine
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
#BuildRequires:	python-translate >= 1.9.0
BuildRequires:	servlet3
BuildRequires:	sharutils
BuildRequires:	recode
BuildRequires:	sac
BuildRequires:	tcsh
BuildRequires:	unzip
BuildRequires:	xsltproc >= 1.0.19
BuildRequires:	zip
BuildRequires:	cups-devel
BuildRequires:	hyphen-devel
BuildRequires:	java-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libwpd-0.10)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libwps-0.4)
BuildRequires:	lpsolve-devel
BuildRequires:	nas-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	qt4-devel
BuildRequires:	readline-devel
BuildRequires:	unixODBC-devel
BuildRequires:	vigra-devel
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libetonyek-0.1)
BuildRequires:	pkgconfig(libfreehand-0.1)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glitz)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(graphite2)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(icu-le)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libabw-0.1)
BuildRequires:	pkgconfig(libclucene-core)
BuildRequires:	pkgconfig(libcmis-0.5)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libcdr-0.1)
BuildRequires:	pkgconfig(libe-book-0.1)
BuildRequires:	pkgconfig(libeot)
BuildRequires:	pkgconfig(libexttextcat)
BuildRequires:	pkgconfig(liblangtag) >= 0.5.4
BuildRequires:	pkgconfig(libmspub-0.1)
BuildRequires:	pkgconfig(libmwaw-0.3) >= 0.3.5
BuildRequires:	pkgconfig(libodfgen-0.1)
BuildRequires:	pkgconfig(liborcus-0.10)
BuildRequires:	pkgconfig(libpagemaker-0.0)
BuildRequires:	pkgconfig(librevenge-0.0)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libsvg)
BuildRequires:	pkgconfig(libucpp)
BuildRequires:	pkgconfig(libvisio-0.1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxul)
BuildRequires:	pkgconfig(mdds-1.0) >= 0.12.1
BuildRequires:	pkgconfig(mythes)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(poppler-cpp)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(raptor)
BuildRequires:	pkgconfig(rasqal)
BuildRequires:	pkgconfig(redland)
BuildRequires:	pkgconfig(sane-backends)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmlsec1)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	db-devel
BuildRequires:	locales-en
# required for unit tests
BuildRequires:	fonts-ttf-liberation
BuildRequires:	google-crosextra-carlito-fonts
BuildRequires:	google-crosextra-caladea-fonts
%if !%{javaless}
BuildRequires:	ant
BuildRequires:	ant-apache-regexp
BuildRequires:	apache-commons-codec
BuildRequires:	apache-commons-lang
BuildRequires:	jakarta-commons-httpclient
BuildRequires:	junit
BuildRequires:	java-1.8.0-openjdk-devel
Suggests:	%{name}-java = %{EVRD}
%endif 
# STLport-devel 4.5 + private patches are needed
BuildConflicts:	STLport-devel
# Requres to all our packages
Requires:	%{name}-base = %{EVRD}
Requires:	%{name}-calc = %{EVRD}
Requires:	%{name}-draw = %{EVRD}
Requires:	%{name}-impress = %{EVRD}
Requires:	%{name}-math = %{EVRD}
Requires:	%{name}-writer = %{EVRD}
Provides:	LibreOffice = %{EVRD}
Provides:	LibreOffice-libs = %{EVRD}

%description
LibreOffice is an Open Source, community-developed, multi-platform
office productivity suite. It includes the key desktop applications,
such as a word processor, spreadsheet, presentation manager, formula
editing and drawing program, with a user interface and feature set
similar to other office suites. Sophisticated and flexible,
LibreOffice also works transparently with a variety of file
formats, including Microsoft Office.

%files

#----------------------------------------------------------------------------

%package base
Summary:	LibreOffice office suite - database
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description base
This package contains the database component for LibreOffice.

You can extend the functionality of LibreOffice Base by installing these
packages:

 * unixodbc: ODBC database support
 * libmyodbc | odbc-postgresql | libsqliteodbc | tdsodbc | mdbtools: ODBC
   drivers for:
   - MySQL
   - PostgreSQL
   - SQLite
   - MS SQL / Sybase SQL
   - *.mdb (JET / MS Access)
 * libmysql-java | libpg-java | libsapdbc-java: JDBC Drivers
   for:
   - MySQL
   - PostgreSQL
   - MaxDB

%files base -f file-lists/base_list.txt
%{_mandir}/man1/lobase*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-base_72.svg

#----------------------------------------------------------------------------

%package calc
Summary:	LibreOffice office suite - spreadsheet
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description calc
This package contains the spreadsheet component for LibreOffice.

%files calc -f file-lists/calc_list.txt
%{_mandir}/man1/localc*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-calc_72.svg

#----------------------------------------------------------------------------

%package common
Summary:	LibreOffice office suite common files
Group:		Office
# Require at least one style to be installed
Requires:	%{name}-style = %{EVRD}
Suggests:	%{name}-help-en_US = %{EVRD}
# And then general requires for OOo follows
Requires:	ghostscript
Requires:	fonts-ttf-liberation
Requires:	google-crosextra-carlito-fonts
Requires:	google-crosextra-caladea-fonts
Requires:	desktop-common-data >= 2008
# rpm will automatically grab the require for libsane1, but there are some
# configs needed at this package, so we must require it too.
Requires:	sane-backends
# Due to %{_bindir}/paperconf
# Requires:	paper-utils
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	update-alternatives
# Upstream merged
Conflicts:	%{name}-core < %{EVRD}
Obsoletes:	%{name}-core < %{EVRD}
Conflicts:	%{name}-java-common < %{EVRD}
Obsoletes:	%{name}-java-common < %{EVRD}
Conflicts:	%{name}-dtd-officedocument1.0 < %{EVRD}
Obsoletes:	%{name}-dtd-officedocument1.0 < %{EVRD}
Conflicts:	%{name}-extension-xsltfilter < %{EVRD}
Obsoletes:	%{name}-extension-xsltfilter < %{EVRD}

%description common
This package contains the application-independent files of LibreOffice.

%files common -f file-lists/core_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo_72.svg
%{_mandir}/man1/loffice*
%{_mandir}/man1/lofromtemplate*
%{_mandir}/man1/libreoffice*
%{_mandir}/man1/unopkg.1*
%{_libdir}/libreoffice/program/classes/ScriptProviderForBeanShell.jar
%{_libdir}/libreoffice/program/services/scriptproviderforbeanshell.rdb

#----------------------------------------------------------------------------

%package java
Summary:	Java dependent parts of LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=1056
Requires:	pentaho-reporting-flow-engine

%description java
Java dependent parts of LibreOffice.

This package contains templates and other optional parts of LibreOffice
that require a Java stack (such as OpenJDK) to be installed.

%files java -f file-lists/java_common_list.txt

#----------------------------------------------------------------------------

%package devel
Summary:	LibreOffice SDK - development files
Group:		Office
Requires:	%{name}-common = %{EVRD}
%if "%{_lib}" == "lib64"
Provides:	devel(libxmlreader(64bit)) = %{EVRD}
Provides:	devel(libxmlreaderlo(64bit)) = %{EVRD}
Provides:	devel(libreg(64bit)) = %{EVRD}
Provides:	devel(libreglo(64bit)) = %{EVRD}
%else
Provides:	devel(libxmlreader) = %{EVRD}
Provides:	devel(libxmlreaderlo) = %{EVRD}
Provides:	devel(libreg) = %{EVRD}
Provides:	devel(libreglo) = %{EVRD}
%endif

%description devel
This package contains the files needed to build plugins/add-ons for
LibreOffice (includes, IDL files, build tools, ...). It also contains the
zipped source of the UNO Java libraries for use in IDEs like eclipse.

%files devel -f file-lists/sdk_list.uniq.sorted.txt

#----------------------------------------------------------------------------

%package devel-doc
Summary:	LibreOffice SDK - documentation
Group:		Office

%description devel-doc
This package contains the documentation of the LibreOffice SDK:

 * C++/Java API reference
 * IDL reference
 * C++/Java/Basic examples

It also contains the gsicheck utility.

%files devel-doc -f file-lists/sdk_doc_list.txt

#----------------------------------------------------------------------------

%package draw
Summary:	LibreOffice office suite - drawing
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description draw
This package contains the drawing component for LibreOffice.

%files draw -f file-lists/draw_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-draw_72.svg
%{_mandir}/man1/lodraw*

#----------------------------------------------------------------------------

%package gnome
Summary:	GNOME Integration for LibreOffice (VFS, GConf)
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description gnome
This package contains the GNOME VFS support and a GConf backend.

%files gnome -f file-lists/gnome_list.uniq.sorted.txt

#----------------------------------------------------------------------------

%package impress
Summary:	LibreOffice office suite - presentation
Group:		Office
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-draw = %{EVRD}
Obsoletes:	%{name}-presentation-minimizer < %{EVRD}

%description impress
This package contains the presentation component for LibreOffice.

%files impress -f file-lists/impress_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-impress_72.svg
%{_mandir}/man1/loimpress*

#----------------------------------------------------------------------------

%package kde4
Summary:	KDE4 Integration for LibreOffice (Widgets, Dialogs, Addressbook)
Group:		Office
Requires:	%{name}-common = %{EVRD}
Suggests:	%{name}-style-oxygen = %{EVRD}

%description kde4
This package contains the KDE4 plugin for drawing LibreOffice widgets with
KDE4/Qt4.x and a KDEish File Picker when running under KDE4.

%files kde4 -f file-lists/kde4_list.txt
%{_libdir}/libreoffice/program/libkde4be1lo.so
%{_libdir}/libreoffice/program/libvclplug_kde4lo.so

#----------------------------------------------------------------------------

%package math
Summary:	LibreOffice office suite - equation editor
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description math
This package contains the equation editor component for LibreOffice.

%files math -f file-lists/math_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-math_72.svg
%{_mandir}/man1/lomath*

#----------------------------------------------------------------------------

%package openclipart
Summary:	LibreOffice Open Clipart data
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description openclipart
This package contains the LibreOffice Open Clipart data, including images
and sounds.

%files openclipart
%{ooodir}/share/gallery/Draws
%{ooodir}/share/gallery/Elements
%{ooodir}/share/gallery/Photos
%{ooodir}/share/gallery/apples*
%{ooodir}/share/gallery/arrows*
%{ooodir}/share/gallery/bigapple*
%{ooodir}/share/gallery/bullets*
%{ooodir}/share/gallery/computers*
%{ooodir}/share/gallery/diagrams*
%{ooodir}/share/gallery/education*
%{ooodir}/share/gallery/environment*
%{ooodir}/share/gallery/finance*
%{ooodir}/share/gallery/flower*
%{ooodir}/share/gallery/htmlexpo*
%{ooodir}/share/gallery/people*
%{ooodir}/share/gallery/sg[0-9]*.*
%{ooodir}/share/gallery/sky.*
%{ooodir}/share/gallery/sounds*
%{ooodir}/share/gallery/symbols*
%{ooodir}/share/gallery/transportation*
%{ooodir}/share/gallery/txtshapes*
%{ooodir}/share/gallery/www-back*
%{ooodir}/share/gallery/www-graf*

#----------------------------------------------------------------------------

%package pyuno
Summary:	Python bindings for UNO library
Group:		Office
Requires:	%{name}-common = %{EVRD}
Conflicts:	%{name}-mailmerge < %{EVRD}
Obsoletes:	%{name}-mailmerge < %{EVRD}

%description pyuno
This package contains the Python bindings for the UNO library.

%files pyuno -f file-lists/pyuno_list.txt

#----------------------------------------------------------------------------

%package style-galaxy
Summary:	Default symbol style for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}

%description style-galaxy
This package contains the "Galaxy" symbol style from Sun, normally used on
MS Windows (tm) and when not using GNOME or KDE. Needs to be manually enabled
in the LibreOffice option menu.

%files style-galaxy
%{ooodir}/share/config/images_galaxy.zip

#----------------------------------------------------------------------------

%package style-hicontrast
Summary:	Hicontrast symbol style for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}

%description style-hicontrast
This package contains the "hicontrast" symbol style, needs to be manually
enabled in the LibreOffice option menu.

%files style-hicontrast
%{ooodir}/share/config/images_hicontrast.zip

#----------------------------------------------------------------------------

%package style-oxygen
Summary:	Oxygen symbol style for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}

%description style-oxygen
This package contains the "oxygen" symbol style, default style for KDE4.

%files style-oxygen
%{ooodir}/share/config/images_oxygen.zip

#----------------------------------------------------------------------------

%package style-tango
Summary:	Tango symbol style for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}

%description style-tango
This package contains the "tango" symbol style, default style for GTK/Gnome.

%files style-tango
%{ooodir}/share/config/images_tango.zip

#----------------------------------------------------------------------------

%package writer
Summary:	LibreOffice office suite - word processor
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description writer
This package contains the word processor component for LibreOffice.

%files writer -f file-lists/writer_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-writer_72.svg
%{_mandir}/man1/loweb*
%{_mandir}/man1/lowriter*

#----------------------------------------------------------------------------

%package wiki-publisher
Summary:	LibreOffice office suite - Wiki Publisher extension
Group:		Office
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-writer = %{EVRD}
%if !%{javaless}
Requires:	apache-commons-codec
Requires:	apache-commons-lang
Requires:	jakarta-commons-httpclient
Requires:	apache-commons-logging
%endif

%description wiki-publisher
With Wiki Publisher extesion is possible by using %{name}-writer to create 
wiki page articles on MediaWiki servers without having to know the syntax of 
MediaWiki markup language. This extension also enables publishing of the
wiki pages.

%files wiki-publisher
%{ooodir}/share/extensions/wiki-publisher

#----------------------------------------------------------------------------

%package extension-barcode
Summary:	LibreOffice extension for generating barcodes
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-barcode
LibreOffice extension for generating barcodes.

%files extension-barcode
%{ooodir}/share/extensions/Barcode

#----------------------------------------------------------------------------

%package extension-converttexttonumber
Summary:	Text to number converter for LibreOffice
Group:		Office
Requires:	%{name}-calc = %{EVRD}

%description extension-converttexttonumber
ConvertTextToNumber replaces numbers and dates, formatted as text, with
real numbers.

Choices can be made about marking of cells, including cells with
non-default decimal separators, conversion of dates, and more.

As a result of the conversion, the text cells will become real numbers,
and then will be counted as expected in formulas Calc.

%files extension-converttexttonumber
%{ooodir}/share/extensions/ConvertTextToNumber

#----------------------------------------------------------------------------

%package extension-gdocs
Summary:	LibreOffice Import/Export filter for Google Docs
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-gdocs
LibreOffice Import/Export filter for Google Docs.

%files extension-gdocs
%{ooodir}/share/extensions/gdocs

#----------------------------------------------------------------------------

%package extension-hunart
Summary:	Hungarian cross-reference toolbar extension for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-hunart
Hungarian cross-reference toolbar extension for LibreOffice.

%files extension-hunart
%{ooodir}/share/extensions/hunart

#----------------------------------------------------------------------------

%package extension-languagetool
Summary:	A LibreOffice extension for style and grammar proofreading
Group:		Office
Requires:	%{name}-writer = %{EVRD}

%description extension-languagetool
A LibreOffice extension for style and grammar proofreading.

%files extension-languagetool
%{ooodir}/share/extensions/LanguageTool

#----------------------------------------------------------------------------

%package extension-mysql
Summary:	MySQL/MariaDB connector for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-mysql
MySQL/MariaDB connector for LibreOffice.

%files extension-mysql
%{ooodir}/share/extensions/mysql-connector-ooo

#----------------------------------------------------------------------------

%package extension-nlpsolver
Summary:	Solver extension for LibreOffice Calc
Group:		Office
Requires:	%{name}-calc = %{EVRD}

%description extension-nlpsolver
Extension integrating a solver engine for optimizing nonlinear programming
models into Calc.

%files extension-nlpsolver
%{ooodir}/share/extensions/nlpsolver

#----------------------------------------------------------------------------

%package extension-numbertext
Summary:	Number-to-Text conversion function for LibreOffice Calc
Group:		Office
Requires:	%{name}-calc = %{EVRD}

%description extension-numbertext
Number-to-Text conversion function for LibreOffice Calc.

%files extension-numbertext
%{ooodir}/share/extensions/numbertext

#----------------------------------------------------------------------------

%package extension-SmART
Summary:	Diagram generator for LibreOffice Draw and Impress
Group:		Office
Url:		http://extensions.libreoffice.org/extension-center/smart
Requires:	%{name}-common = %{EVRD}
Obsoletes:	%{name}-extension-diagram < %{EVRD}

%description extension-SmART
SmART Gallery extension is the advanced version of Diagram (aka. Diagram 2)
for LibreOffice and OpenOffice.org office suites. This Extension is designed
to create your favorite diagrams with few clicks in Draw and Impress
applications.

%files extension-SmART
%{ooodir}/share/extensions/SmART

#----------------------------------------------------------------------------

%package extension-typo
Summary:	Typographic toolbar for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-typo
Typographic toolbar for LibreOffice.

%files extension-typo
%{ooodir}/share/extensions/typo

#----------------------------------------------------------------------------

%package extension-validator
Summary:	A LibreOffice Calc extension that validates cells based on selected rules
Group:		Office
Requires:	%{name}-calc = %{EVRD}

%description extension-validator
A LibreOffice Calc extension that validates cells based on selected rules.

%files extension-validator
%{ooodir}/share/extensions/Validator

#----------------------------------------------------------------------------

%package extension-watchwindow
Summary:	Macro debugging tool for LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description extension-watchwindow
The Watch window allows you to observe the value of variables during the
execution of a program. Define the variable in the Watch text box.
Click on Enable Watch to add the variable to the list box and to display
its values.

%files extension-watchwindow
%{ooodir}/share/extensions/WatchWindow

#----------------------------------------------------------------------------

%package postgresql
Summary:	PostgreSQL connector for LibreOffice
Group:		Office
Requires:	%{name}-base = %{EVRD}

%description postgresql
A PostgreSQl connector for the database front-end for LibreOffice. Allows
creation and management of PostgreSQL databases through a GUI.

%files postgresql
%{ooodir}/program/libpostgresql-sdbclo.so
%{ooodir}/program/libpostgresql-sdbc-impllo.so
%{ooodir}/program/postgresql-sdbc.ini
%{ooodir}/program/services/postgresql-sdbc.rdb
%{ooodir}/share/registry/postgresql.xcd

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-af
Summary:	Afrikaans language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-af
Requires:	urw-fonts
Requires:	myspell-af
Provides:	LibreOffice-l10n-af = %{EVRD}

%description l10n-af
This package contains the localization of LibreOffice in Afrikaans.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ar
Summary:	Arabic language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ar
Requires:	fonts-ttf-arabic
Provides:	LibreOffice-l10n-ar = %{EVRD}

%description l10n-ar
This package contains the localization of LibreOffice in Arabic.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-as
Summary:	Assamese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-as
Provides:	LibreOffice-l10n-as = %{EVRD}

%description l10n-as
This package contains the localization of LibreOffice in Assamese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-bg
Summary:	Bulgarian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bg
Provides:	LibreOffice-l10n-bg = %{EVRD}
Suggests:	%{ooname}-help-bg = %{EVRD}

%description l10n-bg
This package contains the localization of LibreOffice in Bulgarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-bn
Summary:	Bengali language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bn
Provides:	LibreOffice-l10n-bn = %{EVRD}
Suggests:	%{ooname}-help-bn = %{EVRD}

%description l10n-bn
This package contains the localization of LibreOffice in Bengali.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-br
Summary:	Breton language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-br
Provides:	LibreOffice-l10n-br = %{EVRD}

%description l10n-br
This package contains the localization of LibreOffice in Breton.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-bs
Summary:	Bosnian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bs
Provides:	LibreOffice-l10n-bs = %{EVRD}
Suggests:	%{ooname}-help-bs = %{EVRD}

%description l10n-bs
This package contains the localization of LibreOffice in Bosnian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ca
Summary:	Catalan language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ca
Requires:	urw-fonts
Requires:	myspell-ca
Provides:	LibreOffice-l10n-ca = %{EVRD}
Suggests:	%{ooname}-help-ca = %{EVRD}

%description l10n-ca
This package contains the localization of LibreOffice in Catalan.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-cs
Summary:	Czech language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-cs
Requires:	urw-fonts
Requires:	myspell-cs
Requires:	myspell-hyph-cs
Provides:	LibreOffice-l10n-cs = %{EVRD}
Suggests:	%{ooname}-help-cs = %{EVRD}

%description l10n-cs
This package contains the localization of LibreOffice in Czech.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-cy
Summary:	Welsh language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-cy
Requires:	urw-fonts
Requires:	myspell-cy
Provides:	LibreOffice-l10n-cy = %{EVRD}

%description l10n-cy
This package contains the localization of LibreOffice in Welsh.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-da
Summary:	Danish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-da
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-da, myspell-hyph-da
Provides:	LibreOffice-l10n-da = %{EVRD}
Suggests:	%{ooname}-help-da = %{EVRD}

%description l10n-da
This package contains the localization of LibreOffice in Danish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-de
Summary:	German language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-de
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-de
Requires:	myspell-hyph-de
Provides:	LibreOffice-l10n-de = %{EVRD}
Suggests:	%{ooname}-help-de = %{EVRD}

%description l10n-de
This package contains the localization of LibreOffice in German.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-dz
Summary:	Dzongkha language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-dz
Provides:	LibreOffice-l10n-dz = %{EVRD}
Suggests:	%{ooname}-help-dz = %{EVRD}

%description l10n-dz
This package contains the localization of LibreOffice in Dzongkha.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-el
Summary:	Greek language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-el
Requires:	fonts-type1-greek
Requires:	myspell-el
Requires:	myspell-hyph-el
Provides:	LibreOffice-l10n-el = %{EVRD}
Suggests:	%{ooname}-help-el = %{EVRD}

%description l10n-el
This package contains the localization of LibreOffice in Greek.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-en_GB
Summary:	British language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-en
Requires:	urw-fonts
Requires:	myspell-en_GB
Requires:	myspell-hyph-en
Provides:	LibreOffice-l10n-en_GB = %{EVRD}
Suggests:	%{ooname}-help-en_GB = %{EVRD}

%description l10n-en_GB
This package contains the localization of LibreOffice in British.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-es
Summary:	Spanish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-es
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-es
Requires:	myspell-hyph-es
Provides:	LibreOffice-l10n-es = %{EVRD}
Suggests:	%{ooname}-help-es = %{EVRD}

%description l10n-es
This package contains the localization of LibreOffice in Spanish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-et
Summary:	Estonian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-et
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-et
Requires:	myspell-hyph-et
Provides:	LibreOffice-l10n-et = %{EVRD}
Suggests:	%{ooname}-help-et = %{EVRD}

%description l10n-et
This package contains the localization of LibreOffice in Estonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-eu
Summary:	Basque language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-eu
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Provides:	LibreOffice-l10n-eu = %{EVRD}
Suggests:	%{ooname}-help-eu = %{EVRD}

%description l10n-eu
This package contains the localization of LibreOffice in Basque.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-fa
Summary:	Farsi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-fa
Provides:	LibreOffice-l10n-fa = %{EVRD}

%description l10n-fa
This package contains the localization of LibreOffice in Farsi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-fi
Summary:	Finnish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-fi
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Provides:	LibreOffice-l10n-fi = %{EVRD}
Suggests:	%{ooname}-help-fi = %{EVRD}

%description l10n-fi
This package contains the localization of LibreOffice in Finnish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-fr
Summary:	French language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-fr
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-fr
Requires:	myspell-hyph-fr
Provides:	LibreOffice-l10n-fr = %{EVRD}
Suggests:	%{ooname}-help-fr = %{EVRD}

%description l10n-fr
This package contains the localization of LibreOffice in French.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ga
Summary:	Irish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ga
Provides:	LibreOffice-l10n-ga = %{EVRD}

%description l10n-ga
This package contains the localization of LibreOffice in Irish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-gl
Summary:	Galician language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-gl
Provides:	LibreOffice-l10n-gl = %{EVRD}
Suggests:	%{ooname}-help-gl = %{EVRD}

%description l10n-gl
This package contains the localization of LibreOffice in Galician.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-gu
Summary:	Gujarati language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-gu
Provides:	LibreOffice-l10n-gu = %{EVRD}
Suggests:	%{ooname}-help-gu = %{EVRD}

%description l10n-gu
This package contains the localization of LibreOffice in Gujarati.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-he
Summary:	Hebrew language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-he
Requires:	urw-fonts
Provides:	LibreOffice-l10n-he = %{EVRD}
Suggests:	%{ooname}-help-he = %{EVRD}

%description l10n-he
This package contains the localization of LibreOffice in Hebrew.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-hi
Summary:	Hindi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-hi
Requires:	urw-fonts
Provides:	LibreOffice-l10n-hi = %{EVRD}
Suggests:	%{ooname}-help-hi = %{EVRD}

%description l10n-hi
This package contains the localization of LibreOffice in Hindi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-hr
Summary:	Croatian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-hr
Provides:	LibreOffice-l10n-hr = %{EVRD}
Suggests:	%{ooname}-help-hr = %{EVRD}

%description l10n-hr
This package contains the localization of LibreOffice in Croatian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-hu
Summary:	Hungarian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-hu
Requires:	urw-fonts
Requires:	myspell-hu
Requires:	myspell-hyph-hu
Provides:	LibreOffice-l10n-hu = %{EVRD}
Suggests:	%{ooname}-help-hu = %{EVRD}

%description l10n-hu
This package contains the localization of LibreOffice in Hungarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-it
Summary:	Italian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-it
Requires:	myspell-hyph-it
Provides:	LibreOffice-l10n-it = %{EVRD}
Suggests:	%{ooname}-help-it = %{EVRD}

%description l10n-it
This package contains the localization of LibreOffice in Italian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ja
Summary:	Japanese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ja
Requires:	fonts-ttf-japanese
Provides:	LibreOffice-l10n-ja = %{EVRD}
Suggests:	%{ooname}-help-ja = %{EVRD}

%description l10n-ja
This package contains the localization of LibreOffice in Japanese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-kn
Summary:	Kannada language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-kn
Provides:	LibreOffice-l10n-kn = %{EVRD}

%description l10n-kn
This package contains the localization of LibreOffice in Kannada.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ko
Summary:	Korean language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ko
Requires:	fonts-ttf-korean >= 1.0.2
Provides:	LibreOffice-l10n-ko = %{EVRD}
Suggests:	%{ooname}-help-ko = %{EVRD}

%description l10n-ko
This package contains the localization of LibreOffice in Korean.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-lt
Summary:	Lithuanian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-lt
Provides:	LibreOffice-l10n-lt = %{EVRD}

%description l10n-lt
This package contains the localization of LibreOffice in Lithuanian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-lv
Summary:	Latvian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-lv
Provides:	LibreOffice-l10n-lv = %{EVRD}

%description l10n-lv
This package contains the localization of LibreOffice in Latvian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-mai
Summary:	Maithili language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-mai
Provides:	LibreOffice-l10n-mai = %{EVRD}

%description l10n-mai
This package contains the localization of LibreOffice in Maithili.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ml
Summary:	Malayalam language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ml
Provides:	LibreOffice-l10n-ml = %{EVRD}

%description l10n-ml
This package contains the localization of LibreOffice in Malayalam.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-mk
Summary:	Macedonian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-mk
Provides:	LibreOffice-l10n-mk = %{EVRD}
Suggests:	%{ooname}-help-mk = %{EVRD}

%description l10n-mk
This package contains the localization of LibreOffice in Macedonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-mr
Summary:	Marathi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-mr
Provides:	LibreOffice-l10n-mr = %{EVRD}

%description l10n-mr
This package contains the localization of LibreOffice in Marathi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-nb
Summary:	Norwegian Bokmal language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-no
Requires:	urw-fonts
Provides:	LibreOffice-l10n-nb = %{EVRD}
Suggests:	%{ooname}-help-nb = %{EVRD}

%description l10n-nb
This package contains the localization of LibreOffice in Norwegian Bokmal.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-nl
Summary:	Dutch language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-nl
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-nl
Requires:	myspell-hyph-nl
Provides:	LibreOffice-l10n-nl = %{EVRD}
Suggests:	%{ooname}-help-nl = %{EVRD}

%description l10n-nl
This package contains the localization of LibreOffice in Dutch.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-nn
Summary:	Norwegian Nynorsk language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-no
Requires:	urw-fonts
Provides:	LibreOffice-l10n-nn = %{EVRD}
Suggests:	%{ooname}-help-nn = %{EVRD}

%description l10n-nn
This package contains the localization of LibreOffice in Norwegian Nynorsk.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-nr
Summary:	Ndebele language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-nr
Provides:	LibreOffice-l10n-nr = %{EVRD}

%description l10n-nr
This package contains the localization of LibreOffice in Ndebele.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-nso
Summary:	Northern Shoto language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-nso
Provides:	LibreOffice-l10n-nso = %{EVRD}

%description l10n-nso
This package contains the localization of LibreOffice in Northern Shoto.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-or
Summary:	Oriya language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-or
Provides:	LibreOffice-l10n-or = %{EVRD}

%description l10n-or
This package contains the localization of LibreOffice in Oriya.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-pa_IN
Summary:	Punjabi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-pa
Provides:	LibreOffice-l10n-pa_IN = %{EVRD}
Provides:	LibreOffice-l10n-pa = %{EVRD}

%description l10n-pa_IN
This package contains the localization of LibreOffice in Punjabi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-pl
Summary:	Polish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-pl
Requires:	urw-fonts
Requires:	myspell-pl
Requires:	myspell-hyph-pl
Provides:	LibreOffice-l10n-pl = %{EVRD}
Suggests:	%{ooname}-help-pl = %{EVRD}

%description l10n-pl
This package contains the localization of LibreOffice in Polish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-pt
Summary:	Portuguese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-pt
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-pt
Requires:	myspell-hyph-pt
Provides:	LibreOffice-l10n-pt = %{EVRD}
Suggests:	%{ooname}-help-pt = %{EVRD}

%description l10n-pt
This package contains the localization of LibreOffice in Portuguese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-pt_BR
Summary:	Portuguese Brazilian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	locales-pt
Requires:	urw-fonts
Requires:	myspell-pt_BR
Provides:	LibreOffice-l10n_pt_BR = %{EVRD}
Suggests:	%{ooname}-help-pt_BR = %{EVRD}

%description l10n-pt_BR
This package contains the localization of LibreOffice in Portuguese
Brazilian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ro
Summary:	Romanian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ro
Provides:	LibreOffice-l10n-ro = %{EVRD}

%description l10n-ro
This package contains the localization of LibreOffice in Romanian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ru
Summary:	Russian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ru
Requires:	urw-fonts
Requires:	myspell-ru
Requires:	myspell-hyph-ru
Provides:	LibreOffice-l10n-ru = %{EVRD}
Suggests:	%{ooname}-help-ru = %{EVRD}

%description l10n-ru
This package contains the localization of LibreOffice in Russian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-shs
Summary:	Secwepemctsin language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-shs
Provides:	LibreOffice-l10n-shs = %{EVRD}

%description l10n-shs
This package contains the localization of LibreOffice in Secwepemctsin.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-si
Summary:	Sinhalese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-si
Provides:	LibreOffice-l10n-si = %{EVRD}
Suggests:	%{ooname}-help-si = %{EVRD}

%description l10n-si
This package contains the localization of LibreOffice in Sinhalese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-sk
Summary:	Slovak language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sk
Requires:	urw-fonts
Requires:	myspell-sk
Requires:	myspell-hyph-sk
Provides:	LibreOffice-l10n-sk = %{EVRD}
Suggests:	%{ooname}-help-sk = %{EVRD}

%description l10n-sk
This package contains the localization of LibreOffice in Slovak.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-sl
Summary:	Slovenian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sl
Requires:	urw-fonts
Requires:	myspell-sl, myspell-hyph-sl
Provides:	LibreOffice-l10n-sl = %{EVRD}
Suggests:	%{ooname}-help-sl = %{EVRD}

%description l10n-sl
This package contains the localization of LibreOffice in Slovenian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-sr
Summary:	Serbian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sr
Provides:	LibreOffice-l10n-sr = %{EVRD}

%description l10n-sr
This package contains the localization of LibreOffice in Serbian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-st
Summary:	Sotho language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-st
Provides:	LibreOffice-l10n-st = %{EVRD}

%description l10n-st
This package contains the localization of LibreOffice in Sotho.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ss
Summary:	Swati language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ss
Provides:	LibreOffice-l10n-ss = %{EVRD}

%description l10n-ss
This package contains the localization of LibreOffice in Swati.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-sv
Summary:	Swedish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sv
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-sv
Requires:	myspell-hyph-sv
Provides:	LibreOffice-l10n-sv = %{EVRD}
Suggests:	%{ooname}-help-sv = %{EVRD}

%description l10n-sv
This package contains the localization of LibreOffice in Swedish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ta
Summary:	Tamil language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ta
Requires:	urw-fonts
Provides:	LibreOffice-l10n-ta = %{EVRD}

%description l10n-ta
This package contains the localization of LibreOffice in Tamil.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-te
Summary:	Telugu language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-te
Provides:	LibreOffice-l10n-te = %{EVRD}

%description l10n-te
This package contains the localization of LibreOffice in Telugu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-th
Summary:	Thai language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-th
Provides:	LibreOffice-l10n-th = %{EVRD}

%description l10n-th
This package contains the localization of LibreOffice in Thai.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-tn
Summary:	Tswana language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-tn
Provides:	LibreOffice-l10n-tn = %{EVRD}

%description l10n-tn
This package contains the localization of LibreOffice in Tswana.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-tr
Summary:	Turkish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-tr
Requires:	urw-fonts
Provides:	LibreOffice-l10n-tr = %{EVRD}
Suggests:	%{ooname}-help-tr = %{EVRD}

%description l10n-tr
This package contains the localization of LibreOffice in Turkish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ts
Summary:	Tsonga language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ts
Provides:	LibreOffice-l10n-ts = %{EVRD}

%description l10n-ts
This package contains the localization of LibreOffice in Tsonga.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-uk
Summary:	Ukrainian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-uk
Provides:	LibreOffice-l10n-uk = %{EVRD}
Suggests:	%{ooname}-help-uk = %{EVRD}

%description l10n-uk
This package contains the localization of LibreOffice in Ukrainian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-ve
Summary:	Venda language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ve
Provides:	LibreOffice-l10n-ve = %{EVRD}

%description l10n-ve
This package contains the localization of LibreOffice in Venda.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-xh
Summary:	Xhosa language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-xh
Provides:	LibreOffice-l10n-xh = %{EVRD}

%description l10n-xh
This package contains the localization of LibreOffice in Xhosa.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-zh_CN
Summary:	Chinese Simplified language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Provides:	LibreOffice-l10n-zh_CN = %{EVRD}
Suggests:	%{ooname}-help-zh_CN = %{EVRD}

%description l10n-zh_CN
This package contains the localization of LibreOffice in Chinese Simplified.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-zh_TW
Summary:	Chinese Traditional language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Provides:	LibreOffice-l10n-zh_TW = %{EVRD}
Suggests:	%{ooname}-help-zh_TW = %{EVRD}

%description l10n-zh_TW
This package contains the localization of LibreOffice in Chinese
Traditional.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package l10n-zu
Summary:	Zulu language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zu
Requires:	urw-fonts
Requires:	myspell-zu
Provides:	LibreOffice-l10n-zu = %{EVRD}

%description l10n-zu
This package contains the localization of LibreOffice in Zulu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-bg
Summary:	Bulgarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bg = %{EVRD}
Provides:	LibreOffice-help-bg = %{EVRD}

%description help-bg
This package contains the localized help files of LibreOffice in Bulgarian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-bn
Summary:	Bengali help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bn = %{EVRD}
Provides:	LibreOffice-help-bn = %{EVRD}

%description help-bn
This package contains the localized help files of LibreOffice in Bengali.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-bs
Summary:	Bosnian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bs = %{EVRD}
Provides:	LibreOffice-help-bs = %{EVRD}

%description help-bs
This package contains the localized help files of LibreOffice in Bosnian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-ca
Summary:	Catalan help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ca = %{EVRD}
Provides:	LibreOffice-help-ca = %{EVRD}

%description help-ca
This package contains the localized help files of LibreOffice in Catalan.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-cs
Summary:	Czech help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-cs = %{EVRD}
Provides:	LibreOffice-help-cs = %{EVRD}

%description help-cs
This package contains the localized help files of LibreOffice in Czech.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-da
Summary:	Danish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-da = %{EVRD}
Provides:	LibreOffice-help-da = %{EVRD}

%description help-da
This package contains the localized help files of LibreOffice in Danish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-de
Summary:	German help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-de = %{EVRD}
Provides:	LibreOffice-help-de = %{EVRD}

%description help-de
This package contains the localized help files of LibreOffice in German.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-dz
Summary:	Dzongkha help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-dz = %{EVRD}
Provides:	LibreOffice-help-dz = %{EVRD}

%description help-dz
This package contains the localized help files of LibreOffice in Dzongkha.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-el
Summary:	Greek help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-el = %{EVRD}
Provides:	LibreOffice-help-el = %{EVRD}

%description help-el
This package contains the localized help files of LibreOffice in Greek.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-en_GB
Summary:	British help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-en_GB = %{EVRD}
Provides:	LibreOffice-help-en_GB = %{EVRD}

%description help-en_GB
This package contains the localized help files of LibreOffice in British.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-en_US
Summary:	American English help for LibreOffice 
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Provides:	LibreOffice-help-en_US = %{EVRD}

%description help-en_US
This package contains the localized help files of LibreOffice
in American English.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-es
Summary:	Spanish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-es = %{EVRD}
Provides:	LibreOffice-help-es = %{EVRD}

%description help-es
This package contains the localized help files of LibreOffice in Spanish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-et
Summary:	Estonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-et = %{EVRD}
Provides:	LibreOffice-help-et = %{EVRD}

%description help-et
This package contains the localized help files of LibreOffice in Estonian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-eu
Summary:	Basque help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-eu = %{EVRD}
Provides:	LibreOffice-help-eu = %{EVRD}

%description help-eu
This package contains the localized help files of LibreOffice in Basque.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-fi
Summary:	Finnish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fi = %{EVRD}
Provides:	LibreOffice-help-fi = %{EVRD}

%description help-fi
This package contains the localized help files of LibreOffice in Finnish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-fr
Summary:	French help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fr = %{EVRD}
Provides:	LibreOffice-help-fr = %{EVRD}

%description help-fr
This package contains the localized help files of LibreOffice in French.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-gu
Summary:	Gujarati help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gu = %{EVRD}
Provides:	LibreOffice-help-gu = %{EVRD}

%description help-gu
This package contains the localized help files of LibreOffice in Gujarati.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-gl
Summary:	Galician help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gl = %{EVRD}
Provides:	LibreOffice-help-gl = %{EVRD}

%description help-gl
This package contains the localized help files of LibreOffice in Galician.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-he
Summary:	Hebrew help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-he = %{EVRD}
Provides:	LibreOffice-help-he = %{EVRD}

%description help-he
This package contains the localized help files of LibreOffice in Hebrew.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-hi
Summary:	Hindi help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hi = %{EVRD}
Provides:	LibreOffice-help-hi = %{EVRD}

%description help-hi
This package contains the localized help files of LibreOffice in Hindi.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-hr
Summary:	Croatian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hr = %{EVRD}
Provides:	LibreOffice-help-hr = %{EVRD}

%description help-hr
This package contains the localized help files of LibreOffice in Croatian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-hu
Summary:	Hungarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hu = %{EVRD}
Provides:	LibreOffice-help-hu = %{EVRD}

%description help-hu
This package contains the localized help files of LibreOffice in Hungarian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-it
Summary:	Italian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-it = %{EVRD}
Provides:	LibreOffice-help-it = %{EVRD}

%description help-it
This package contains the localized help files of LibreOffice in Italian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-ja
Summary:	Japanese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ja = %{EVRD}
Provides:	LibreOffice-help-ja = %{EVRD}

%description help-ja
This package contains the localized help files of LibreOffice in Japanese.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-ko
Summary:	Korean help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ko = %{EVRD}
Provides:	LibreOffice-help-ko = %{EVRD}

%description help-ko
This package contains the localized help files of LibreOffice in Korean.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-mk
Summary:	Macedonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-mk = %{EVRD}
Provides:	LibreOffice-help-mk = %{EVRD}

%description help-mk
This package contains the localized help files of LibreOffice in Macedonian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-nb
Summary:	Norwegian Bokmal help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nb = %{EVRD}
Provides:	LibreOffice-help-nb = %{EVRD}

%description help-nb
This package contains the localized help files of LibreOffice in Norwegian
Bokmal.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-nl
Summary:	Dutch help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nl = %{EVRD}
Provides:	LibreOffice-help-nl = %{EVRD}

%description help-nl
This package contains the localized help files of LibreOffice in Dutch.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-nn
Summary:	Norwegian Nynorsk help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nn = %{EVRD}
Provides:	LibreOffice-help-nn = %{EVRD}

%description help-nn
This package contains the localized help files of LibreOffice in Norwegian
Nynorsk.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-pl
Summary:	Polish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pl = %{EVRD}
Provides:	LibreOffice-help-pl = %{EVRD}

%description help-pl
This package contains the localized help files of LibreOffice in Polish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-pt
Summary:	Portuguese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt = %{EVRD}
Provides:	LibreOffice-help-pt = %{EVRD}

%description help-pt
This package contains the localized help files of LibreOffice in Portuguese.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-pt_BR
Summary:	Portuguese Brazilian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt_BR = %{EVRD}
Provides:	LibreOffice-help-pt_BR = %{EVRD}

%description help-pt_BR
This package contains the localized help files of LibreOffice in Portuguese
Brazilian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-ru
Summary:	Russian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ru = %{EVRD}
Provides:	LibreOffice-help-ru = %{EVRD}

%description help-ru
This package contains the localized help files of LibreOffice in Russian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-si
Summary:	Sinhalese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-si = %{EVRD}
Provides:	LibreOffice-help-si = %{EVRD}

%description help-si
This package contains the localized help files of LibreOffice in Sinhalese.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-sk
Summary:	Slovak help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sk = %{EVRD}
Provides:	LibreOffice-help-sk = %{EVRD}

%description help-sk
This package contains the localized help files of LibreOffice in Slovak.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-sl
Summary:	Slovenian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sl = %{EVRD}
Provides:	LibreOffice-help-sl = %{EVRD}

%description help-sl
This package contains the localized help files of LibreOffice in Slovenian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-sv
Summary:	Swedish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sv = %{EVRD}
Provides:	LibreOffice-help-sv = %{EVRD}

%description help-sv
This package contains the localized help files of LibreOffice in Swedish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-tr
Summary:	Turkish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-tr = %{EVRD}
Provides:	LibreOffice-help-tr = %{EVRD}

%description help-tr
This package contains the localized help files of LibreOffice in Turkish.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-uk
Summary:	Ukrainian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-uk = %{EVRD}
Provides:	LibreOffice-help-uk = %{EVRD}

%description help-uk
This package contains the localized help files of LibreOffice in Ukrainian.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-zh_CN
Summary:	Chinese Simplified help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_CN = %{EVRD}
Provides:	LibreOffice-help-zn_CN = %{EVRD}

%description help-zh_CN
This package contains the localized help files of LibreOffice in Chinese
Simplified.
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package help-zh_TW
Summary:	Chinese Traditional help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_TW = %{EVRD}
Provides:	LibreOffice-help-zn_CT = %{EVRD}

%description help-zh_TW
This package contains the localized help files of LibreOffice in Chinese
Traditional.
%endif

#----------------------------------------------------------------------------

%package templates-common
Summary:	Files used by LibreOffice templates
Group:		Office

%description templates-common
Files used by LibreOffice templates.

%files templates-common
%{ooodir}/share/template/common/dummy_common_templates.txt
%{ooodir}/share/template/common/educate
%{ooodir}/share/template/common/finance
%{ooodir}/share/template/common/forms
%{ooodir}/share/template/common/labels
%{ooodir}/share/template/common/layout/31407-squares.otp
%{ooodir}/share/template/common/layout/Blue*.otp
%{ooodir}/share/template/common/layout/Cool_Space.otp
%{ooodir}/share/template/common/layout/Cubes.otp
%{ooodir}/share/template/common/layout/Doppellinie-blau.otp
%{ooodir}/share/template/common/layout/EarthLight.otp
%{ooodir}/share/template/common/layout/Girasoles.otp
%{ooodir}/share/template/common/layout/Glossy.otp
%{ooodir}/share/template/common/layout/Green.otp
%{ooodir}/share/template/common/layout/Grey.otp
%{ooodir}/share/template/common/layout/Hatch.otp
%{ooodir}/share/template/common/layout/Human.otp
%{ooodir}/share/template/common/layout/Infantil.otp
%{ooodir}/share/template/common/layout/Lamp.otp
%{ooodir}/share/template/common/layout/Lay_grafity.otp
%{ooodir}/share/template/common/layout/Lay_wood.otp
%{ooodir}/share/template/common/layout/Marble.otp
%{ooodir}/share/template/common/layout/MediaStyle.otp
%{ooodir}/share/template/common/layout/Mondo*.otp
%{ooodir}/share/template/common/layout/Movie.otp
%{ooodir}/share/template/common/layout/NavyBlue.otp
%{ooodir}/share/template/common/layout/Notepad.otp
%{ooodir}/share/template/common/layout/Openblue.otp
%{ooodir}/share/template/common/layout/Orange.otp
%{ooodir}/share/template/common/layout/PhotoFrame.otp
%{ooodir}/share/template/common/layout/Plantillafiesta.otp
%{ooodir}/share/template/common/layout/Praesentation_Radial_*.otp
%{ooodir}/share/template/common/layout/Quadratisch*.otp
%{ooodir}/share/template/common/layout/RedStar.otp
%{ooodir}/share/template/common/layout/Sidepanel_*.otp
%{ooodir}/share/template/common/layout/Solar.otp
%{ooodir}/share/template/common/layout/Soleil.otp
%{ooodir}/share/template/common/layout/Sunburst.otp
%{ooodir}/share/template/common/layout/Worldwide*.otp
%{ooodir}/share/template/common/layout/abstract*.otp
%{ooodir}/share/template/common/layout/aquarius.otp
%{ooodir}/share/template/common/layout/blau.otp
%{ooodir}/share/template/common/layout/blue-elegance.otp
%{ooodir}/share/template/common/layout/blue.otp
%{ooodir}/share/template/common/layout/carton.otp
%{ooodir}/share/template/common/layout/chalkboard*.otp
%{ooodir}/share/template/common/layout/circulos_*.otp
%{ooodir}/share/template/common/layout/citrus-e.otp
%{ooodir}/share/template/common/layout/compladients.otp
%{ooodir}/share/template/common/layout/cross_*.otp
%{ooodir}/share/template/common/layout/edge-*.otp
%{ooodir}/share/template/common/layout/education-*.otp
%{ooodir}/share/template/common/layout/emotion.otp
%{ooodir}/share/template/common/layout/emotion2.otp
%{ooodir}/share/template/common/layout/eos.otp
%{ooodir}/share/template/common/layout/exec-??.otp
%{ooodir}/share/template/common/layout/fields-of-peace.otp
%{ooodir}/share/template/common/layout/fresh-morning.otp
%{ooodir}/share/template/common/layout/glowing-rectangles.otp
%{ooodir}/share/template/common/layout/golthia.otp
%{ooodir}/share/template/common/layout/green-concentration.otp
%{ooodir}/share/template/common/layout/greenish-wallpaper.otp
%{ooodir}/share/template/common/layout/holiday-*.otp
%{ooodir}/share/template/common/layout/humanist_presentation.otp
%{ooodir}/share/template/common/layout/inspire-*.otp
%{ooodir}/share/template/common/layout/kde.otp
%{ooodir}/share/template/common/layout/keynote.otp
%{ooodir}/share/template/common/layout/letterpress.otp
%{ooodir}/share/template/common/layout/line_*.otp
%{ooodir}/share/template/common/layout/list.txt
%{ooodir}/share/template/common/layout/macos103.otp
%{ooodir}/share/template/common/layout/moebius-strip.otp
%{ooodir}/share/template/common/layout/more-green.otp
%{ooodir}/share/template/common/layout/ooo2.otp
%{ooodir}/share/template/common/layout/ooo2_spot.otp
%{ooodir}/share/template/common/layout/openoffice.org_gulls.otp
%{ooodir}/share/template/common/layout/perspective-*.otp
%{ooodir}/share/template/common/layout/reo-veo*.otp
%{ooodir}/share/template/common/layout/schatten_*.otp
%{ooodir}/share/template/common/layout/science-*.otp
%{ooodir}/share/template/common/layout/sedi.otp
%{ooodir}/share/template/common/layout/standard-*.otp
%{ooodir}/share/template/common/layout/sun.otp
%{ooodir}/share/template/common/layout/texture-*.jpg.otp
%{ooodir}/share/template/common/layout/vortrag_*.otp
%{ooodir}/share/template/common/misc
%{ooodir}/share/template/common/officorr/dummy_common_templates.txt
%{ooodir}/share/template/common/offimisc/dummy_common_templates.txt
%{ooodir}/share/template/common/personal/szivesoldal.otg
%{ooodir}/share/template/common/presnt/dummy_common_templates.txt

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-cs
Summary:	Czech templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-cs
Czech templates for LibreOffice.

%files templates-cs
%{ooodir}/share/template/cs
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-de
Summary:	German templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-de
German templates for LibreOffice.

%files templates-de
%{ooodir}/share/template/de
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_de
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-en_US
Summary:	US English templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-en_US
US English templates for LibreOffice.

%files templates-en_US
%{ooodir}/share/template/en-US
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_en-US
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-es
Summary:	Spanish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-es
Spanish templates for LibreOffice.

%files templates-es
%{ooodir}/share/template/es
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_es
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-fi
Summary:	Finnish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-fi
Finnish templates for LibreOffice.

%files templates-fi
%{ooodir}/share/template/fi
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-fr
Summary:	French templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-fr
French templates for LibreOffice.

%files templates-fr
%{ooodir}/share/template/fr
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_fr
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-hu
Summary:	Hungarian templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-hu
Hungarian templates for LibreOffice.

%files templates-hu
%{ooodir}/share/template/hu
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_hu
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-it
Summary:	Italian templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-it
Italian templates for LibreOffice.

%files templates-it
%{ooodir}/share/template/it
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_it
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-ja
Summary:	Japanese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-ja
Japanese templates for LibreOffice.

%files templates-ja
%{ooodir}/share/template/ja
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-nl
Summary:	Dutch templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-nl
Dutch templates for LibreOffice.

%files templates-nl
%{ooodir}/share/template/nl
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-pl
Summary:	Polish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-pl
Polish templates for LibreOffice.

%files templates-pl
%{ooodir}/share/template/pl
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-pt_BR
Summary:	Brazilian Portuguese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-pt_BR
Brazilian Portuguese templates for LibreOffice.

%files templates-pt_BR
%{ooodir}/share/template/pt-BR
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-sv
Summary:	Swedish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-sv
Swedish templates for LibreOffice.

%files templates-sv
%{ooodir}/share/template/sv
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-tr
Summary:	Turkish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-tr
Turkish templates for LibreOffice.

%files templates-tr
%{ooodir}/share/template/tr
%endif

#----------------------------------------------------------------------------

%if %{with l10n}
%package templates-zh_CN
Summary:	Simplified Chinese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-zh_CN
Simplified Chinese templates for LibreOffice.

%files templates-zh_CN
%{ooodir}/share/template/zh-CN
%endif

#----------------------------------------------------------------------------

%prep
%setup -q -c -a 1 -a 2 -a 3
rm -rf git-hooks */git-hooks
for a in */*; do mv `pwd`/$a .; done

#ant
%if %{javaless}
tar -xjvf %{SOURCE20}
%endif
%apply_patches

# to make the friggin cppunit tests work
mkdir -p ~/tmp
chmod 777 ~/tmp

%build
# Use linker flags to reduce memory consumption (bfd only)
#global ldflags %{ldflags} -Wl,--no-keep-memory -Wl,--reduce-memory-overheads

export CC=gcc
export CXX=g++

# path to external tarballs
EXTSRCDIR=`dirname %{SOURCE0}`

# Workaround for bug http://qa.mandriva.com/show_bug.cgi?id=27771
# if [ -z $QTDIR ]; then
# . /etc/profile.d/60qt4.sh
# fi
export QT4DIR=%{_libdir}/qt4
%ifarch X86_64 
	export QT4INC=/usr/lib/qt4/include
%else
	export QT4INC=%{_libdir}/qt4/include
%endif 
export QT4LIB=%{_libdir}/qt4/lib

export KDE4DIR=%{_libdir}/kde4
%ifarch X86_64 
	export KDE4INC=/usr/lib/kde4/include
%else
	export KDE4INC=%{_libdir}/kde4/include
%endif 
export KDE4LIB=%{_libdir}/kde4/lib

export LC_ALL=en_US.UTF-8
export LANG=en_US

%if !%{with icecream}
# sbin due to icu stuff there
#PATH=/bin:/usr/bin:/usr/X11R6/bin:$QTPATH:/usr/sbin:$PATH
PATH=$PATH:/usr/sbin
export PATH
%endif

%if %{with ccache}
export CCACHE_DIR=%{ccachedir}
%endif

export ARCH_FLAGS="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CC="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="%{optflags} -O2"
# Workaround for abf builds running out of memory
export ARCH_FLAGS_CC="$ARCH_FLAGS_CC -g0"
export ARCH_FLAGS_CXX="$ARCH_FLAGS_CXX -g0"
export CFLAGS=$ARCH_FLAGS_CC
export CXXFLAGS=$ARCH_FLAGS_CXX

echo "Configure start at: "`date` >> ooobuildtime.log 

touch autogen.lastrun
%configure2_5x \
	%{?_smp_mflags:--with-parallelism="`getconf _NPROCESSORS_ONLN`"} \
	--with-vendor=OpenMandriva \
	--with-build-version="OpenMandriva %{version}-%{release}" \
	--disable-gltf \
	--disable-coinmp \
	--disable-fetch-external \
	--with-external-tar="$EXTSRCDIR" \
	--enable-gstreamer \
	--disable-gstreamer-0.10 \
	--enable-release-build \
	--disable-kde \
	--enable-kde4 \
	--enable-lockdown \
	--disable-gconf \
	--enable-opengl \
	--enable-eot \
	--enable-odk \
	--enable-split-app-modules \
	--enable-split-opt-features \
	--enable-extra-gallery \
	--enable-extra-template \
	--with-sun-templates \
	--without-fonts \
	--without-junit \
	--enable-silent-rules \
%if %{javaless}
	--with-ant-home="%{antpath}" \
%else
	--with-jdk-home="%{java_home}" \
%endif
	--without-system-hsqldb \
	--with-lang="%{langs}" \
	--without-myspell-dicts \
	--with-system-dicts \
	--with-help \
	--with-external-dict-dir=%{_datadir}/dict/ooo \
	--with-external-hyph-dir=%{_datadir}/dict/ooo \
	--with-external-thes-dir=%{_datadir}/dict/ooo \
	--with-system-libs \
	--with-system-ucpp \
	--without-system-npapi-headers \
	--enable-ext-watch-window \
	--enable-ext-diagram \
	--enable-ext-validator \
	--enable-ext-barcode \
	--enable-ext-ct2n \
	--enable-ext-numbertext \
	--enable-ext-hunart \
	--enable-ext-typo \
	--enable-ext-google-docs \
	--enable-ext-nlpsolver \
	--enable-ext-languagetool \
	--enable-ext-wiki-publisher \
	--enable-verbose \
	--enable-hardlink-deliver \
	--enable-ext-mariadb-connector \
	--with-servlet-api-jar=/usr/share/java/tomcat-servlet-3.0-api.jar \
%if %{with ccache} && !%{with icecream}
	--with-gcc-speedup=ccache \
%else
 %if !%{with ccache} && %{with icecream}
	--with-gcc-speedup=icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
 %else
  %if %{with ccache} && %{with icecream}
	--with-gcc-speedup=ccache,icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
  %endif
 %endif
%endif

sed -i -e "s,\$ENV{'MD5SUM'},md5sum,g" solenv/bin/modules/installer/systemactions.pm solenv/bin/modules/installer.pm

echo "Configure end at: "`date` >> ooobuildtime.log 
echo "Make start at: "`date` >> ooobuildtime.log 

# some configs  to improve build process 
# http://wiki.services.openoffice.org/wiki/Building_OpenOffice.org
# needs to check if it does any effect 
export nodep=TRUE
export NO_HIDS=TRUE 
export MAXPROCESS=4 

# (tpg) silent output to reduce memory and free space 
# We use make build here because the default target is "allandcheck".
# Checking should go to %check
ulimit -c unlimited

%ifarch %{ix86}
# seems to fail on this file test
rm -f writerperfect/qa/unit/data/draw/libvisio/pass/EDB-22679-1.vsd
rm -f writerperfect/qa/unit/data/writer/libwpd/pass/EDB-14344-1.wpd
%endif

make -r -s V=0 \
	ARCH_FLAGS="$ARCH_FLAGS" \
	ARCH_FLAGS_CC="$ARCH_FLAGS_CC" \
	ARCH_FLAGS_CXX="$ARCH_FLAGS_CXX" \
	ARCH_FLAGS_OPT="$ARCH_FLAGS_OPT" \
	build

echo "Make end at: "`date` >> ooobuildtime.log 
echo "Install start at: "`date` >> ooobuildtime.log 

%check
# FIXME enable once the connection failures in firebird and hsqldb are fixed
# make check

%install
# sbin due to icu stuff there
PATH=$PATH:/usr/sbin

make DESTDIR=%{buildroot} distro-pack-install
rm -rf %{buildroot}/opt

# use the dicts from myspell-<lang>
# rm -rf %{buildroot}%{ooodir}/share/dict/ooo
# ln -s %{_datadir}/dict/ooo %{buildroot}%{ooodir}/share/dict

# Mandriva Rosa icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/scalable/apps/
tar -xjvf %{SOURCE10} --exclude Libre_Office* -C %{buildroot}%{_iconsdir}/hicolor/scalable/apps/

sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-calc_72/'    %{buildroot}%{ooodir}/share/xdg/calc.desktop
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-writer_72/'  %{buildroot}%{ooodir}/share/xdg/writer.desktop 
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-impress_72/' %{buildroot}%{ooodir}/share/xdg/impress.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-draw_72/'    %{buildroot}%{ooodir}/share/xdg/draw.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-base_72/'    %{buildroot}%{ooodir}/share/xdg/base.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-math_72/'    %{buildroot}%{ooodir}/share/xdg/math.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo_72/'         %{buildroot}%{ooodir}/share/xdg/startcenter.desktop

# ensure links are converted to files
for app in base calc draw impress math startcenter writer xsltfilter; do
    cp --remove-destination %{buildroot}%{ooodir}/share/xdg/$app.desktop %{buildroot}%{_datadir}/applications/libreoffice-$app.desktop
done

# some genius committed commit log files...
rm %{buildroot}%{ooodir}/share/template/common/svn-commit*.tmp

# fix permissions for stripping
find %{buildroot} -type f -exec chmod u+rw '{}' \;

# fix permission of .so libraries
find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod a+x '{}' \;

# Anssi patch
# remove /usr/bin/soffice (made with update-alternatives)
# rm -f %{buildroot}%{_bindir}/soffice

# Anssi 
# Install a random UNO extension into BUILDROOT and remove it, so that unopkg
# creates the cache directories and files that can then be ghostified.
# Simple "list" would create everything but files inside
# "com.sun.star.comp.deployment.component.PackageRegistryBackend".
# Note that this has to be run before below bro calls below that rename needed
# files and thus disable unopkg for the rest of install stage.
# First make sure there is no actual data pre-existing in this directory,
# as that will be lost due to the ghostification:
# [ $(find %{buildroot}%{ooodir}/share/uno_packages/cache -type f | wc -l) -eq 0 ]
# %{buildroot}%{ooodir}/program/unopkg add --shared %{_builddir}/libreoffice-%{version}/solver/340/unxlng*/bin/pdfimport/pdfimport.oxt
# %{buildroot}%{ooodir}/program/unopkg remove --shared pdfimport.oxt
# # clean cache
# %{buildroot}%{ooodir}/program/unopkg list --shared
# # there should be more files now:
# [ $(find %{buildroot}%{ooodir}/share/uno_packages/cache | wc -l) -ge 5 ]
# for path in $(find %{buildroot}%{ooodir}/share/uno_packages/cache/); do
#       if [ -d $path ]; then
#               echo "%%dir ${path#%{buildroot}}" >> build/common_list.txt
#       else
#               echo "%%ghost ${path#%{buildroot}}" >> build/common_list.txt
#       fi
# done

# Change progress bar colors
sed -i '/^ProgressBarColor/d;/^ProgressFrameColor/d' \
	%{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressBarColor=68,135,223' >> %{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressFrameColor=112,171,229' >> %{buildroot}%{ooodir}/program/sofficerc

#dev300 fix position and size
sed -i '/^ProgressPosition/d;/^ProgressSize/d' \
	%{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressPosition=10,307' >> %{buildroot}%{ooodir}/program/sofficerc
echo 'ProgressSize=377,9' >> %{buildroot}%{ooodir}/program/sofficerc

# common shouldn't depend on writer...
# but common does depend on libswdlo.so
grep libswdlo.so file-lists/writer_list.txt >>file-lists/common_list.txt
sed -i -e '/libswdlo.so/d' file-lists/writer_list.txt

## Installation fixes
## remove fix wrong manpages files, extension gz->xz
for p in common base calc writer impress draw math; do
	sed -i '/^.*man.*\.gz$/d' file-lists/${p}_list.txt 
done;

## drop GTK dependency from -common
sed -i -e '/^.*pluginapp.bin$/d' file-lists/core_list.txt
echo '%{ooodir}/program/pluginapp.bin' >>file-lists/gnome_list.txt

## sort removing duplicates
sort -u file-lists/gnome_list.txt > file-lists/gnome_list.uniq.sorted.txt 
sort -u file-lists/sdk_list.txt   > file-lists/sdk_list.uniq.sorted.txt 

# Fix weirdo filenames wreaking havoc because they're regular expressions
sed -i -e 's/\[/?/g;s/\]/?/g' file-lists/sdk*.txt

## styles have their own packages
for i in oxygen galaxy hicontrast tango; do
	sed -i "/^.*images_$i\.zip$/d" file-lists/common_list.txt 
done
# galaxy style too
sed -i "/^.*images\.zip$/d" file-lists/common_list.txt 

## Split help
cd file-lists
for i in lang_*.txt; do
	grep /help/ $i >${i/lang/help} || touch ${i/lang/help}
	sed -i -e '/\/help\//d' $i
done
cd ..

# Split gallery
grep /share/gallery/ file-lists/common_list.txt >file-lists/gallery_list.txt
sed -i -e '/\/share\/gallery\//d' file-lists/common_list.txt
# We catch those in a regex to catch Sun Template extras
sed -i -e '/gallery\/sg[0-9]*\..*/d' file-lists/gallery_list.txt

## merge en-US with common
cat file-lists/lang_en_US_list.txt >> file-lists/common_list.txt
## merge dtd with common
cat file-lists/dtd_list.txt >> file-lists/common_list.txt
sort -u file-lists/common_list.txt >  file-lists/common_list.uniq.sorted.txt
cat file-lists/common_list.uniq.sorted.txt >>file-lists/core_list.txt

## make sure we don't have duplicate files in core
sort -u file-lists/core_list.txt > file-lists/core_list.uniq.sorted.txt
cat file-lists/core_list.uniq.sorted.txt > file-lists/core_list.txt

# %%files for help-* and l10n-* packages
%if %{with l10n}
%{expand:%(for i in %{langs}; do
	[ "$i" = "en-US" ] && continue;
	i=`echo $i |sed -e 's,-,_,g'`;
	[ "$i" = "sh" ] && echo "%%files l10n-shs -f file-lists/lang_${i}_list.txt" || echo "%%files l10n-$i -f file-lists/lang_${i}_list.txt";
done)}

%{expand:%(for i in %{helplangs}; do
	l=`echo $i |sed -e 's,-,_,g'`;
	echo "%%files help-$l -f file-lists/help_${l}_list.txt";
	echo "%%_libdir/libreoffice/help/$i";
done)}
%endif
