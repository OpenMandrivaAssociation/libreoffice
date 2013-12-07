%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _binary_payload w1.xzdio
%define _source_payload w1.xzdio

%bcond_without l10n
%bcond_with icecream
%bcond_with ccache

%if %{with l10n}
%define langs	en-US af ar as bg bn br bs ca cs cy da de dz el en-GB es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai mk ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-TW zh-CN zu
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
%define	ooname		libreoffice
%define buildver	%{version}.2
%define ooodir		%{_libdir}/libreoffice
%define firefox_plugin	libnpsoplugin.so
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
Version:	4.1.3
Release:	6
License:	(MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic
Group:		Office
Url:		http://www.libreoffice.org
Source0:	%{relurl}/%{ooname}-%{buildver}.tar.xz
Source1:	%{relurl}/%{ooname}-dictionaries-%{buildver}.tar.xz
Source2:	%{relurl}/%{ooname}-help-%{buildver}.tar.xz
Source3:	%{relurl}/%{ooname}-translations-%{buildver}.tar.xz
Source4:	http://dev-www.libreoffice.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll

Source10:	Mandriva-Rosa_Icons.tar.bz2
#javaless
%if %{javaless}
Source20:	http://archive.apache.org/dist/ant/binaries/apache-ant-1.8.1-bin.tar.bz2
Source30:	%{devurl}/af3c3acf618de6108d65fcdc92b492e1-commons-codec-1.3-src.tar.gz
Source31:	%{devurl}/2c9b0f83ed5890af02c0df1c1776f39b-commons-httpclient-3.1-src.tar.gz 
Source32:	%{devurl}/2ae988b339daec234019a7066f96733e-commons-lang-2.3-src.tar.gz 
Source33:	%{devurl}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
%endif
Source34:	%{devurl}/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz
Source35:	%{devurl}/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source36:	%{devurl}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source37:	%{devurl}/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip

# External Download Sources
Source40:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz

# Extensions
Source50:	%{srcurl}451ccf439a36a568653b024534669971-ConvertTextToNumber-1.3.2.oxt
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
Patch1:		libreoffice-3.5.2.2-icu-49.patch
Patch2:		help-images-mdv64789.patch
Patch3:		libreoffice-4.1-libcmis-0.4.patch

# Force Qt4 event loops because with glib event loops libreoffice-kde4 doesn't
# work well
# Requires patched Qt4, see https://bugreports.qt-project.org/browse/QTBUG-16934
Patch50:	libreoffice-4.1.2.2-kde-qt-event-loop.patch
# From ROSA:
# Hack: Don't display tiny useless scrollbars with libreoffice-kde4
# Impress is known to crash when adding effects (segfault is triggered by 15x18 scrollbar)
Patch51:        libreoffice-4.1.2.2-impress-kde-crash-hack.patch

# ROSA vendor patch
Patch100:       libreoffice-4.1-vendor.patch

# Other bugfix patches, including upstream
Patch202:       0001-Resolves-rhbz-968892-force-render-full-grapheme-with.patch

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
BuildRequires:	doxygen
BuildRequires:	ed
BuildRequires:	flex
BuildRequires:	flute
BuildRequires:	git
BuildRequires:	gperf
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
BuildRequires:	python-translate >= 1.9.0
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
BuildRequires:	libwpd-devel >= 0.9.0
BuildRequires:	libwpg-devel
BuildRequires:	libwps-devel
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
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glitz)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(graphite2)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(icu-le)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libclucene-core)
BuildRequires:	pkgconfig(libcmis-0.4)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libcdr-0.0)
BuildRequires:	pkgconfig(libexttextcat)
BuildRequires:	pkgconfig(libixion-0.6)
BuildRequires:	pkgconfig(liblangtag)
BuildRequires:	pkgconfig(libmspub-0.0)
BuildRequires:	pkgconfig(libmwaw-0.1)
BuildRequires:	pkgconfig(libodfgen-0.0)
BuildRequires:	pkgconfig(liborcus-0.6)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libsvg)
BuildRequires:	pkgconfig(libucpp)
BuildRequires:	pkgconfig(libvisio-0.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libxul)
BuildRequires:	pkgconfig(mdds)
BuildRequires:	pkgconfig(mythes)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(nspr)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(ORBit-2.0)
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
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmlsec1)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	db-devel
%if !%{javaless}
BuildRequires:	ant
BuildRequires:	hsqldb1.8.0
BuildRequires:	jakarta-commons-codec
BuildRequires:	jakarta-commons-lang
BuildRequires:	jakarta-commons-httpclient
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
Obsoletes:	openoffice.org < 1:3.3-1:2011.0 

%description
LibreOffice is an Open Source, community-developed, multi-platform
office productivity suite. It includes the key desktop applications,
such as a word processor, spreadsheet, presentation manager, formula
editing and drawing program, with a user interface and feature set
similar to other office suites. Sophisticated and flexible,
LibreOffice also works transparently with a variety of file
formats, including Microsoft Office.

%package base
Summary:	LibreOffice office suite - database
Group:		Office
Requires:	%{name}-common = %{EVRD}
# Heavy java deps
%if !%{javaless}
Requires:	hsqldb1.8.0
%endif
Obsoletes:	openoffice.org-base < 1:3.3-1:2011.0 

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

%package calc
Summary:	LibreOffice office suite - spreadsheet
Group:		Office
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-calc < 1:3.3-1:2011.0 

%description calc
This package contains the spreadsheet component for LibreOffice.

%package common
Summary:	LibreOffice office suite common files
Group:		Office
# Require at least one style to be installed
Requires:	%{name}-style = %{EVRD}
Suggests:	%{name}-help-en_US = %{EVRD}
# And then general requires for OOo follows
Requires:	ghostscript
Requires:	fonts-ttf-liberation
Requires:	desktop-common-data >= 2008
# rpm will automatically grab the require for libsane1, but there are some
# configs needed at this package, so we must require it too.
Requires:	sane-backends
# Due to %{_bindir}/paperconf
# Requires:	paper-utils
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	update-alternatives

Obsoletes:	openoffice.org-common < 1:3.3-1:2011.0 
Conflicts:	%{name}-common = 1:3.2-rc4.0

# Upstream merged in 4.1.1
Obsoletes:	%{name}-core < %{EVRD}
Obsoletes:	%{name}-java-common < %{EVRD}
Obsoletes:	%{name}-dtd-officedocument1.0 < %{EVRD}

# Upstream dropped this packages in 3.4
Obsoletes:	%{name}-l10n-pt_AO = 1:3.3.2-1
Obsoletes:	%{name}-help-pt_AO = 1:3.3.2-1
Obsoletes:	%{name}-help-ta    = 1:3.3.2-1
Obsoletes:	%{name}-help-zu    = 1:3.3.2-1
Obsoletes:	%{name}-help-cy    = 1:3.3.2-1
Obsoletes:	%{name}-help-ar    = 1:3.3.2-1
Obsoletes:	%{name}-help-af    = 1:3.3.2-1
Obsoletes:	%{name}-help-br    = 1:3.3.2-1
# This is a test locale -- shouldn't ever have shipped
Obsoletes:	%{name}-l10n-qtz < %{EVRD}
Obsoletes:	%{name}-help-qtz < %{EVRD}

%description common
This package contains the application-independent files of LibreOffice.

%package java
Summary:	Java dependent parts of LibreOffice
Group:		Office
Requires:	%{name}-common = %{EVRD}

%description java
Java dependent parts of LibreOffice.

This package contains templates and other optional parts of LibreOffice
that require a Java stack (such as OpenJDK) to be installed.

%package devel
Summary:	LibreOffice SDK - development files
Group:		Office
Requires:	%{name}-common = %{EVRD}
%if "%{_lib}" == "lib64"
Provides:	devel(libxmlreader(64bit)) = %{EVRD}
Provides:	devel(libxmlreaderlo(64bit)) = %{EVRD}
Provides:	devel(libreg(64bit)) = %{EVRD}
%else
Provides:	devel(libxmlreader) = %{EVRD}
Provides:	devel(libxmlreaderlo) = %{EVRD}
Provides:	devel(libreg) = %{EVRD}
%endif
Obsoletes:	openoffice.org-devel < 1:3.3-1:2011.0 

%description devel
This package contains the files needed to build plugins/add-ons for
LibreOffice (includes, IDL files, build tools, ...). It also contains the
zipped source of the UNO Java libraries for use in IDEs like eclipse.

%package devel-doc
Summary:	LibreOffice SDK - documentation
Group:		Office
Obsoletes:	openoffice.org-devel-doc < 1:3.3-1:2011.0 

%description devel-doc
This package contains the documentation of the LibreOffice SDK:

 * C++/Java API reference
 * IDL reference
 * C++/Java/Basic examples

It also contains the gsicheck utility.

%package draw
Group:		Office
Summary:	LibreOffice office suite - drawing
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-draw < 1:3.3-1:2011.0 

%description draw
This package contains the drawing component for LibreOffice.

%package gnome
Group:		Office
Summary:	GNOME Integration for LibreOffice (VFS, GConf)
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-gnome < 1:3.3-1:2011.0 

%description gnome
This package contains the GNOME VFS support and a GConf backend.

%package impress
Group:		Office
Summary:	LibreOffice office suite - presentation
Requires:	%{name}-common = %{EVRD} 
Requires:	%{name}-draw = %{EVRD}
Obsoletes:	openoffice.org-impress < 1:3.3-1:2011.0 

%description impress
This package contains the presentation component for LibreOffice.

%package kde4
Group:		Office
Summary:	KDE4 Integration for LibreOffice (Widgets, Dialogs, Addressbook)
Requires:	%{name}-common = %{EVRD}
Suggests:	%{name}-style-oxygen = %{EVRD} 
Obsoletes:	openoffice.org-kde4 < 1:3.3-1:2011.0 

%description kde4
This package contains the KDE4 plugin for drawing LibreOffice widgets with
KDE4/Qt4.x and a KDEish File Picker when running under KDE4.
 
%package math
Group:		Office
Summary:	LibreOffice office suite - equation editor
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-math < 1:3.3-1:2011.0 

%description math
This package contains the equation editor component for LibreOffice.

%package openclipart
Group:		Office
Summary:	LibreOffice Open Clipart data
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-openclipart < 1:3.3-1:2011.0 

%description openclipart
This package contains the LibreOffice Open Clipart data, including images
and sounds.

%package pyuno
Group:		Office
Summary:	Python bindings for UNO library
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-pyuno < 1:3.3-1:2011.0 

%description pyuno
This package contains the Python bindings for the UNO library.

%package style-galaxy
Group:		Office
Summary:	Default symbol style for LibreOffice
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-galaxy < 1:3.3-1:2011.0 

%description style-galaxy
This package contains the "Galaxy" symbol style from Sun, normally used on
MS Windows (tm) and when not using GNOME or KDE. Needs to be manually enabled
in the LibreOffice option menu.

%package style-crystal
Group:		Office
Summary:	Crystal symbol style for LibreOffice
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-crystal < 1:3.3-1:2011.0 

%description style-crystal
This package contains the "crystal" symbol style, default style for KDE.

%package style-hicontrast
Group:		Office
Summary:	Hicontrast symbol style for LibreOffice
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-hicontrast < 1:3.3-1:2011.0 

%description style-hicontrast
This package contains the "hicontrast" symbol style, needs to be manually
enabled in the LibreOffice option menu.

%package style-tango
Group:		Office
Summary:	Tango symbol style for LibreOffice
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-tango < 1:3.3-1:2011.0 

%description style-tango
This package contains the "tango" symbol style, default style for GTK/Gnome.

%package style-oxygen
Group:		Office
Summary:	Oxygen symbol style for LibreOffice
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-oxygen < 1:3.3-1:2011.0 

%description style-oxygen
This package contains the "oxygen" symbol style, default style for KDE4.

%package writer
Group:		Office
Summary:	LibreOffice office suite - word processor
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-writer < 1:3.3-1:2011.0 

%description writer
This package contains the wordprocessor component for LibreOffice.

%package wiki-publisher
Group:		Office
Summary:	LibreOffice office suite - Wiki Publisher extension
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-writer = %{EVRD}
%if !%{javaless}
Requires:	jakarta-commons-codec
Requires:	jakarta-commons-httpclient
Requires:	jakarta-commons-lang
Requires:	jakarta-commons-logging
%endif
Obsoletes:	openoffice.org-wiki-publisher < 1:3.3-1:2011.0 

%description wiki-publisher
With Wiki Publisher extesion is possible by using %{name}-writer to create 
wiki page articles on MediaWiki servers without having to know the syntax of 
MediaWiki markup language. This extension also enables publishing of the
wiki pages.


%package extension-xsltfilter
Summary: XSLT based export filters for XHTML and Docbook formats
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-xsltfilter
XSLT based export filters for XHTML and Docbook formats


%package extension-typo
Summary: Typographic toolbar for Libreoffice
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-typo
Typographic toolbar for Libreoffice


%package extension-numbertext
Summary: Number-to-Text conversion function for Libreoffice calc
Group: Office
Requires: %{name}-common = %{EVRD}
Requires: %{name}-calc = %{EVRD}

%description extension-numbertext
Number-to-Text conversion function for Libreoffice calc


%package extension-nlpsolver
Summary: Solver extension for Libreoffice Calc
Group: Office
Requires: %{name}-common = %{EVRD}
Requires: %{name}-calc = %{EVRD}

%description extension-nlpsolver
Extension integrating a solver engine for optimizing
nonlinear programming models into Calc


%package extension-hunart
Summary: Hungarian cross-reference toolbar extension
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-hunart
Hungarian cross-reference toolbar extension


%package extension-gdocs
Summary: Libreoffice Import/Export filter for Google Docs
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-gdocs
Libreoffice Import/Export filter for Google Docs


%package extension-watchwindow
Summary: Macro debugging tool for Libreoffice
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-watchwindow
The Watch window allows you to observe the value of variables during the
execution of a program. Define the variable in the Watch text box.
Click on Enable Watch to add the variable to the list box and to display
its values.


%package extension-validator
Summary: A LibreOffice Calc extension that validates cells based on selected rules
Group: Office
Requires: %{name}-calc = %{EVRD}

%description extension-validator
A LibreOffice Calc extension that validates cells based on selected rules


%package extension-languagetool
Summary: A LibreOffice extension for style and grammar proofreading
Group: Office
Requires: %{name}-writer = %{EVRD}

%description extension-languagetool
A LibreOffice extension for style and grammar proofreading


%package extension-diagram
Summary: Diagram extension for LibreOffice Impress and Draw
Group: Office
Requires: %{name}-common = %{EVRD}

%description extension-diagram
SmART Gallery extension is the advanced version of Diagram
(aka. Diagram 2) for LibreOffice and OpenOffice.org office suites.

This Extension is designed to create your favorite diagrams
with few clicks in Draw and Impress applications.

%package extension-converttexttonumber
Summary: Text to number converter for LibreOffice
Group: Office
Requires: %{name}-calc = %{EVRD}

%description extension-converttexttonumber
ConvertTextToNumber replaces numbers and dates, formatted as text, with
real numbers.

Choices can be made about marking of cells, including cells with
non-default decimal separators, conversion of dates, and more.

As a result of the conversion, the text cells will become real numbers,
and then will be counted as expected in formulas Calc.

%package extension-barcode
Summary: LibreOffice extension for generating barcodes
Group: Office

%description extension-barcode
LibreOffice extension for generating barcodes


%package extension-mysql
Summary: MySQL/MariaDB connector for LibreOffice
Group: Office

%description extension-mysql
MySQL/MariaDB connector for LibreOffice


%package mailmerge
Summary:	Tool for mailing a LO document to a database of addresses
Group:		Office
Requires:	%{name}-writer = %{EVRD}
Requires:	%{name}-calc = %{EVRD}
Requires:	%{name}-base = %{EVRD}

%description mailmerge
Tool for mailing a LO document to a database of addresses


%package presentation-minimizer
Group:		Office
Summary:	LibreOffice office suite - Presentation Minimizer extension
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-impress = %{EVRD}
Obsoletes:	openoffice.org-presentation-minimizer < 1:3.3-1:2011.0 

%description presentation-minimizer
With Presentation Minimizer extesion is possible to reduce the file size 
of the presentation by compressing images and removing data not needed in 
a automatizated way.

Note: The Presentation Minimizer also works on 
Microsoft PowerPoint presentations. 

%package postgresql
Summary:	PostgreSQL connector for LibreOffice
Group:		Office
Requires:	%{name}-base = %{EVRD}

%description postgresql
A PostgreSQl connector for the database front-end for LibreOffice. Allows
creation and management of PostgreSQL databases through a GUI.

%package templates-common
Summary:	Files used by LibreOffice templates
Group:		Office

%description templates-common
Files used by LibreOffice templates

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
Obsoletes:	openoffice.org-l10n-af < 1:3.3-1:2011.0 

%description l10n-af
This package contains the localization of LibreOffice in Afrikaans.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-ar
Summary:	Arabic language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ar
Requires:	fonts-ttf-arabic
Provides:	LibreOffice-l10n-ar = %{EVRD}
Obsoletes:	openoffice.org-l10n-ar < 1:3.3-1:2011.0 

%description l10n-ar
This package contains the localization of LibreOffice in Arabic.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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

%package l10n-bg
Summary:	Bulgarian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bg
Provides:	LibreOffice-l10n-bg = %{EVRD}
Suggests:	%{ooname}-help-bg = %{EVRD}
Obsoletes:	openoffice.org-l10n-bg < 1:3.3-1:2011.0 

%description l10n-bg
This package contains the localization of LibreOffice in Bulgarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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

%package l10n-br
Summary:	Breton language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-br
Provides:	LibreOffice-l10n-br = %{EVRD}
Obsoletes:	openoffice.org-l10n-br < 1:3.3-1:2011.0 

%description l10n-br
This package contains the localization of LibreOffice in Breton.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-bs
Summary:	Bosnian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bs
Provides:	LibreOffice-l10n-bs = %{EVRD}
Suggests:	%{ooname}-help-bs = %{EVRD}
Obsoletes:	openoffice.org-l10n-bs < 1:3.3-1:2011.0 

%description l10n-bs
This package contains the localization of LibreOffice in Bosnian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-ca < 1:3.3-1:2011.0 

%description l10n-ca
This package contains the localization of LibreOffice in Catalan.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-cs < 1:3.3-1:2011.0 

%description l10n-cs
This package contains the localization of LibreOffice in Czech.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-cs
Summary:	Czech templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-cs
Czech templates for LibreOffice

%package l10n-cy
Summary:	Welsh language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-cy
Requires:	urw-fonts
Requires:	myspell-cy
Provides:	LibreOffice-l10n-cy = %{EVRD}
Obsoletes:	openoffice.org-l10n-cy < 1:3.3-1:2011.0 

%description l10n-cy
This package contains the localization of LibreOffice in Welsh.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-da < 1:3.3-1:2011.0 

%description l10n-da
This package contains the localization of LibreOffice in Danish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-de < 1:3.3-1:2011.0 

%description l10n-de
This package contains the localization of LibreOffice in German.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-de
Summary:	German templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-de
German templates for LibreOffice

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
Obsoletes:	openoffice.org-l10n-el < 1:3.3-1:2011.0 

%description l10n-el
This package contains the localization of LibreOffice in Greek.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-en_GB < 1:3.3-1:2011.0 

%description l10n-en_GB
 package contains the localization of LibreOffice in British.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-en_US
Summary:	US English templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-en_US
US English templates for LibreOffice

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
Obsoletes:	openoffice.org-l10n-es < 1:3.3-1:2011.0 

%description l10n-es
This package contains the localization of LibreOffice in Spanish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-es
Summary:	Spanish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-es
Spanish templates for LibreOffice


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
Obsoletes:	openoffice.org-l10n-et < 1:3.3-1:2011.0 

%description l10n-et
This package contains the localization of LibreOffice in Estonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-eu < 1:3.3-1:2011.0 

%description l10n-eu
This package contains the localization of LibreOffice in Basque.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-fi < 1:3.3-1:2011.0 

%description l10n-fi
This package contains the localization of LibreOffice in Finnish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-fi
Summary:	Finnish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-fi
Finnish templates for LibreOffice

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
Obsoletes:	openoffice.org-l10n-fr < 1:3.3-1:2011.0 

%description l10n-fr
This package contains the localization of LibreOffice in French.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-fr
Summary:	French templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-fr
French templates for LibreOffice


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

%package l10n-he
Summary:	Hebrew language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-he
Requires:	urw-fonts
Provides:	LibreOffice-l10n-he = %{EVRD}
Suggests:	%{ooname}-help-he = %{EVRD} 
Obsoletes:	openoffice.org-l10n-he < 1:3.3-1:2011.0 

%description l10n-he
This package contains the localization of LibreOffice in Hebrew.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-hi
Summary:	Hindi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-hi
Requires:	urw-fonts
Provides:	LibreOffice-l10n-hi = %{EVRD}
Suggests:	%{ooname}-help-hi = %{EVRD} 
Obsoletes:	openoffice.org-l10n-hi < 1:3.3-1:2011.0 

%description l10n-hi
This package contains the localization of LibreOffice in Hindi.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-hu < 1:3.3-1:2011.0 

%description l10n-hu
This package contains the localization of LibreOffice in Hungarian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-hu
Summary:	Hungarian templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-hu
Hungarian templates for LibreOffice


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
Obsoletes:	openoffice.org-l10n-it < 1:3.3-1:2011.0 

%description l10n-it
This package contains the localization of LibreOffice in Italian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-it
Summary:	Italian templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-it
Italian templates for LibreOffice

%package l10n-ja
Summary:	Japanese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ja
Requires:	fonts-ttf-japanese
Provides:	LibreOffice-l10n-ja = %{EVRD}
Suggests:	%{ooname}-help-ja = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ja < 1:3.3-1:2011.0 

%description l10n-ja
This package contains the localization of LibreOffice in Japanese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-ja
Summary:	Japanese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-ja
Japanese templates for LibreOffice

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

%package l10n-ko
Summary:	Korean language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ko
Requires:	fonts-ttf-korean >= 1.0.2
Provides:	LibreOffice-l10n-ko = %{EVRD}
Suggests:	%{ooname}-help-ko = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ko < 1:3.3-1:2011.0 

%description l10n-ko
This package contains the localization of LibreOffice in Korean.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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

%package l10n-mk
Summary:	Macedonian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-mk
Provides:	LibreOffice-l10n-mk = %{EVRD}
Suggests:	%{ooname}-help-mk = %{EVRD} 
Obsoletes:	openoffice.org-l10n-mk < 1:3.3-1:2011.0 

%description l10n-mk
This package contains the localization of LibreOffice in Macedonian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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

%package l10n-nb
Summary:	Norwegian Bokmal language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-no
Requires:	urw-fonts
Provides:	LibreOffice-l10n-nb = %{EVRD}
Suggests:	%{ooname}-help-nb = %{EVRD} 
Obsoletes:	openoffice.org-l10n-nb < 1:3.3-1:2011.0 

%description l10n-nb
This package contains the localization of LibreOffice in Norwegian Bokmal.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-nl < 1:3.3-1:2011.0 

%description l10n-nl
This package contains the localization of LibreOffice in Dutch.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-nl
Summary:	Dutch templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-nl
Dutch templates for LibreOffice

%package l10n-nn
Summary:	Norwegian Nynorsk language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-no
Requires:	urw-fonts
Provides:	LibreOffice-l10n-nn = %{EVRD}
Suggests:	%{ooname}-help-nn = %{EVRD} 
Obsoletes:	openoffice.org-l10n-nn < 1:3.3-1:2011.0 

%description l10n-nn
This package contains the localization of LibreOffice in Norwegian Nynorsk.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-pl < 1:3.3-1:2011.0 

%description l10n-pl
This package contains the localization of LibreOffice in Polish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-pl
Summary:	Polish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-pl
Polish templates for LibreOffice

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
Obsoletes:	openoffice.org-l10n-pt < 1:3.3-1:2011.0 

%description l10n-pt
This package contains the localization of LibreOffice in Portuguese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-pt_BR
Summary:	Portuguese Brazilian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	locales-pt
Requires:	urw-fonts
Requires:	myspell-pt_BR
Provides:	LibreOffice-l10n_pt_BR = %{EVRD}
Suggests:	%{ooname}-help-pt_BR = %{EVRD} 
Obsoletes:	openoffice.org-l10n-pt_BR < 1:3.3-1:2011.0 

%description l10n-pt_BR
This package contains the localization of LibreOffice in Portuguese
Brazilian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-pt_BR
Summary:	Brazilian Portuguese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-pt_BR
Brazilian Portuguese templates for LibreOffice


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

%package l10n-ru
Summary:	Russian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ru
Requires:	urw-fonts >= 2.0-6mdk
Requires:	myspell-ru
Requires:	myspell-hyph-ru
Provides:	LibreOffice-l10n-ru = %{EVRD}
Suggests:	%{ooname}-help-ru = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ru < 1:3.3-1:2011.0 

%description l10n-ru
This package contains the localization of LibreOffice in Russian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-sk < 1:3.3-1:2011.0 

%description l10n-sk
This package contains the localization of LibreOffice in Slovak.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-sl < 1:3.3-1:2011.0 

%description l10n-sl
This package contains the localization of LibreOffice in Slovenian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Obsoletes:	openoffice.org-l10n-sv < 1:3.3-1:2011.0 

%description l10n-sv
This package contains the localization of LibreOffice in Swedish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-sv
Summary:	Swedish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-sv
Swedish templates for LibreOffice

%package l10n-ta
Summary:	Tamil language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ta
Requires:	urw-fonts
Provides:	LibreOffice-l10n-ta = %{EVRD}
Obsoletes:	openoffice.org-l10n-ta < 1:3.3-1:2011.0 

%description l10n-ta
This package contains the localization of LibreOffice in Tamil.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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

%package l10n-tr
Summary:	Turkish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-tr
Requires:	urw-fonts
Provides:	LibreOffice-l10n-tr = %{EVRD}
Suggests:	%{ooname}-help-tr = %{EVRD} 
Obsoletes:	openoffice.org-l10n-tr < 1:3.3-1:2011.0 

%description l10n-tr
This package contains the localization of LibreOffice in Turkish.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-tr
Summary:	Turkish templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-tr
Turkish templates for LibreOffice

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

%package l10n-zh_CN
Summary:	Chinese Simplified language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Provides:	LibreOffice-l10n-zh_CN = %{EVRD}
Suggests:	%{ooname}-help-zh_CN = %{EVRD} 
Obsoletes:	openoffice.org-l10n-zh_CN < 1:3.3-1:2011.0 

%description l10n-zh_CN
This package contains the localization of LibreOffice in Chinese Simplified.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package templates-zh_CN
Summary:	Simplified Chinese templates for LibreOffice
Group:		Office
Requires:	%{name}-templates-common = %{EVRD}

%description templates-zh_CN
Simplified Chinese templates for LibreOffice

%package l10n-zh_TW
Summary:	Chinese Traditional language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zh
Requires:	fonts-ttf-chinese
Provides:	LibreOffice-l10n-zh_TW = %{EVRD}
Suggests:	%{ooname}-help-zh_TW = %{EVRD}
Obsoletes:	openoffice.org-l10n-zh_TW < 1:3.3-1:2011.0 

%description l10n-zh_TW
This package contains the localization of LibreOffice in Chinese
Traditional.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-zu
Summary:	Zulu language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-zu
Requires:	urw-fonts
Requires:	myspell-zu
Provides:	LibreOffice-l10n-zu = %{EVRD}
Obsoletes:	openoffice.org-l10n-zu < 1:3.3-1:2011.0 

%description l10n-zu
This package contains the localization of LibreOffice in Zulu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package help-bg
Summary:	Bulgarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bg = %{EVRD}
Provides:	LibreOffice-help-bg = %{EVRD}
Obsoletes:	openoffice.org-help-bg < 1:3.3-1:2011.0 

%description help-bg
This package contains the localized help files of LibreOffice in Bulgarian.

%package help-bn
Summary:	Bengali help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bn = %{EVRD}
Provides:	LibreOffice-help-bn = %{EVRD}

%description help-bn
This package contains the localized help files of LibreOffice in Bengali.

%package help-bs
Summary:	Bosnian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bs = %{EVRD}
Provides:	LibreOffice-help-bs = %{EVRD}
Obsoletes:	openoffice.org-help-bs < 1:3.3-1:2011.0 

%description help-bs
This package contains the localized help files of LibreOffice in Bosnian.

%package help-ca
Summary:	Catalan help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ca = %{EVRD}
Provides:	LibreOffice-help-ca = %{EVRD}
Obsoletes:	openoffice.org-help-ca < 1:3.3-1:2011.0 

%description help-ca
This package contains the localized help files of LibreOffice in Catalan.

%package help-cs
Summary:	Czech help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-cs = %{EVRD}
Provides:	LibreOffice-help-cs = %{EVRD}
Obsoletes:	openoffice.org-help-cs < 1:3.3-1:2011.0 

%description help-cs
This package contains the localized help files of LibreOffice in Czech.

%package help-da
Summary:	Danish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-da = %{EVRD}
Provides:	LibreOffice-help-da = %{EVRD}
Obsoletes:	openoffice.org-help-da < 1:3.3-1:2011.0 

%description help-da
This package contains the localized help files of LibreOffice in Danish.

%package help-de
Summary:	German help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-de = %{EVRD}
Provides:	LibreOffice-help-de = %{EVRD}
Obsoletes:	openoffice.org-help-de < 1:3.3-1:2011.0 

%description help-de
This package contains the localized help files of LibreOffice in German.

%package help-dz
Summary:	Dzongkha help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-dz = %{EVRD}
Provides:	LibreOffice-help-dz = %{EVRD}

%description help-dz
This package contains the localized help files of LibreOffice in Dzongkha.

%package help-el
Summary:	Greek help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-el = %{EVRD}
Provides:	LibreOffice-help-el = %{EVRD}
Obsoletes:	openoffice.org-help-el < 1:3.3-1:2011.0 

%description help-el
This package contains the localized help files of LibreOffice in Greek.

%package help-en_GB
Summary:	British help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-en_GB = %{EVRD}
Provides:	LibreOffice-help-en_GB = %{EVRD}
Obsoletes:	openoffice.org-help-en_GB < 1:3.3-1:2011.0 

%description help-en_GB
This package contains the localized help files of LibreOffice in British.

%package help-en_US 
Summary:	American English help for LibreOffice 
Group:		Office 
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Provides:	LibreOffice-help-en_US = %{EVRD}
Obsoletes:	openoffice.org-help-en_US < 1:3.3-1:2011.0 

%description help-en_US
This package contains the localized help files of LibreOffice
in American English.

%package help-es
Summary:	Spanish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-es = %{EVRD}
Provides:	LibreOffice-help-es = %{EVRD}
Obsoletes:	openoffice.org-help-es < 1:3.3-1:2011.0 

%description help-es
This package contains the localized help files of LibreOffice in Spanish.

%package help-et
Summary:	Estonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-et = %{EVRD}
Provides:	LibreOffice-help-et = %{EVRD}
Obsoletes:	openoffice.org-help-et < 1:3.3-1:2011.0 

%description help-et
This package contains the localized help files of LibreOffice in Estonian.

%package help-eu
Summary:	Basque help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-eu = %{EVRD}
Provides:	LibreOffice-help-eu = %{EVRD}
Obsoletes:	openoffice.org-help-eu < 1:3.3-1:2011.0 

%description help-eu
This package contains the localized help files of LibreOffice in Basque.

%package help-fi
Summary:	Finnish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fi = %{EVRD}
Provides:	LibreOffice-help-fi = %{EVRD}
Obsoletes:	openoffice.org-help-fi < 1:3.3-1:2011.0 

%description help-fi
This package contains the localized help files of LibreOffice in Finnish.

%package help-fr
Summary:	French help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fr = %{EVRD}
Provides:	LibreOffice-help-fr = %{EVRD}
Obsoletes:	openoffice.org-help-fr < 1:3.3-1:2011.0 

%description help-fr
This package contains the localized help files of LibreOffice in French.

%package help-gu
Summary:	Gujarati help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gu = %{EVRD}
Provides:	LibreOffice-help-gu = %{EVRD}

%description help-gu
This package contains the localized help files of LibreOffice in Gujarati.

%package help-gl
Summary:	Galician help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gl = %{EVRD}
Provides:	LibreOffice-help-gl = %{EVRD}

%description help-gl
This package contains the localized help files of LibreOffice in Galician.

%package help-he
Summary:	Hebrew help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-he = %{EVRD}
Provides:	LibreOffice-help-he = %{EVRD}
Obsoletes:	openoffice.org-help-he < 1:3.3-1:2011.0 

%description help-he
This package contains the localized help files of LibreOffice in Hebrew.

%package help-hi
Summary:	Hindi help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hi = %{EVRD}
Provides:	LibreOffice-help-hi = %{EVRD}
Obsoletes:	openoffice.org-help-hi < 1:3.3-1:2011.0 

%description help-hi
This package contains the localized help files of LibreOffice in Hindi.

%package help-hr
Summary:	Croatian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hr = %{EVRD}
Provides:	LibreOffice-help-hr = %{EVRD}

%description help-hr
This package contains the localized help files of LibreOffice in Croatian.

%package help-hu
Summary:	Hungarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hu = %{EVRD}
Provides:	LibreOffice-help-hu = %{EVRD}
Obsoletes:	openoffice.org-help-hu < 1:3.3-1:2011.0 

%description help-hu
This package contains the localized help files of LibreOffice in Hungarian.

%package help-it
Summary:	Italian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-it = %{EVRD}
Provides:	LibreOffice-help-it = %{EVRD}
Obsoletes:	openoffice.org-help-it < 1:3.3-1:2011.0 

%description help-it
This package contains the localized help files of LibreOffice in Italian.

%package help-ja
Summary:	Japanese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ja = %{EVRD}
Provides:	LibreOffice-help-ja = %{EVRD}
Obsoletes:	openoffice.org-help-ja < 1:3.3-1:2011.0 

%description help-ja
This package contains the localized help files of LibreOffice in Japanese. 

%package help-ko
Summary:	Korean help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ko = %{EVRD}
Provides:	LibreOffice-help-ko = %{EVRD}
Obsoletes:	openoffice.org-help-ko < 1:3.3-1:2011.0 

%description help-ko
This package contains the localized help files of LibreOffice in Korean.

%package help-mk
Summary:	Macedonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-mk = %{EVRD}
Provides:	LibreOffice-help-mk = %{EVRD}
Obsoletes:	openoffice.org-help-mk < 1:3.3-1:2011.0 

%description help-mk
This package contains the localized help files of LibreOffice in Macedonian.

%package help-nb
Summary:	Norwegian Bokmal help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nb = %{EVRD}
Provides:	LibreOffice-help-nb = %{EVRD}
Obsoletes:	openoffice.org-help-nb < 1:3.3-1:2011.0 

%description help-nb
This package contains the localized help files of LibreOffice in Norwegian
Bokmal.

%package help-nl
Summary:	Dutch help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nl = %{EVRD}
Provides:	LibreOffice-help-nl = %{EVRD}
Obsoletes:	openoffice.org-help-nl < 1:3.3-1:2011.0 

%description help-nl
This package contains the localized help files of LibreOffice in Dutch.

%package help-nn
Summary:	Norwegian Nynorsk help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nn = %{EVRD}
Provides:	LibreOffice-help-nn = %{EVRD}
Obsoletes:	openoffice.org-help-nn < 1:3.3-1:2011.0 

%description help-nn
This package contains the localized help files of LibreOffice in Norwegian
Nynorsk.

%package help-pl
Summary:	Polish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pl = %{EVRD}
Provides:	LibreOffice-help-pl = %{EVRD}
Obsoletes:	openoffice.org-help-pl < 1:3.3-1:2011.0 

%description help-pl
This package contains the localized help files of LibreOffice in Polish.

%package help-pt
Summary:	Portuguese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt = %{EVRD}
Provides:	LibreOffice-help-pt = %{EVRD}
Obsoletes:	openoffice.org-help-pt < 1:3.3-1:2011.0 

%description help-pt
This package contains the localized help files of LibreOffice in Portuguese.

%package help-pt_BR
Summary:	Portuguese Brazilian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt_BR = %{EVRD}
Provides:	LibreOffice-help-pt_BR = %{EVRD}
Obsoletes:	openoffice.org-help-pt_BR < 1:3.3-1:2011.0 

%description help-pt_BR
This package contains the localized help files of LibreOffice in Portuguese
Brazilian.

%package help-ru
Summary:	Russian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ru = %{EVRD}
Provides:	LibreOffice-help-ru = %{EVRD}
Obsoletes:	openoffice.org-help-ru < 1:3.3-1:2011.0 

%description help-ru
This package contains the localized help files of LibreOffice in Russian.

%package help-si
Summary:	Sinhalese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-si = %{EVRD}
Provides:	LibreOffice-help-si = %{EVRD}

%description help-si
This package contains the localized help files of LibreOffice in Sinhalese.

%package help-sk
Summary:	Slovak help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sk = %{EVRD}
Provides:	LibreOffice-help-sk = %{EVRD}
Obsoletes:	openoffice.org-help-sk < 1:3.3-1:2011.0 

%description help-sk
This package contains the localized help files of LibreOffice in Slovak.

%package help-sl
Summary:	Slovenian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sl = %{EVRD}
Provides:	LibreOffice-help-sl = %{EVRD}
Obsoletes:	openoffice.org-help-sl < 1:3.3-1:2011.0 

%description help-sl
This package contains the localized help files of LibreOffice in Slovenian.

%package help-sv
Summary:	Swedish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sv = %{EVRD}
Provides:	LibreOffice-help-sv = %{EVRD}
Obsoletes:	openoffice.org-help-sv < 1:3.3-1:2011.0 

%description help-sv
This package contains the localized help files of LibreOffice in Swedish.

%package help-tr
Summary:	Turkish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-tr = %{EVRD}
Provides:	LibreOffice-help-tr = %{EVRD}
Obsoletes:	openoffice.org-help-tr < 1:3.3-1:2011.0 

%description help-tr
This package contains the localized help files of LibreOffice in Turkish.

%package help-uk
Summary:	Ukrainian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-uk = %{EVRD}
Provides:	LibreOffice-help-uk = %{EVRD}

%description help-uk
This package contains the localized help files of LibreOffice in Ukrainian.

%package help-zh_CN
Summary:	Chinese Simplified help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_CN = %{EVRD}
Provides:	LibreOffice-help-zn_CN = %{EVRD}
Obsoletes:	openoffice.org-help-zn_CN < 1:3.3-1:2011.0 

%description help-zh_CN
This package contains the localized help files of LibreOffice in Chinese
Simplified.

%package help-zh_TW
Summary:	Chinese Traditional help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_TW = %{EVRD}
Provides:	LibreOffice-help-zn_CT = %{EVRD}
Obsoletes:	openoffice.org-help-zn_CT < 1:3.3-1:2011.0 

%description help-zh_TW
This package contains the localized help files of LibreOffice in Chinese
Traditional.

%endif

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
export ARCH_FLAGS_CXX="$ARCH_FLAGS_CC -g0"

echo "Configure start at: "`date` >> ooobuildtime.log 

touch autogen.lastrun
%configure2_5x \
	%{?_smp_mflags:--with-parallelism="`getconf _NPROCESSORS_ONLN`"} \
	--with-vendor=OpenMandriva \
	--with-build-version="OpenMandriva %{version}-%{release}" \
	--disable-fetch-external \
	--disable-gstreamer-0.10 \
	--enable-gstreamer \
	--enable-release-build \
	--disable-kde \
	--enable-kde4 \
	--enable-lockdown \
	--enable-opengl \
	--enable-odk \
	--enable-split-app-modules \
  	--enable-split-opt-features \
	--enable-telepathy \
	--enable-extra-gallery \
	--enable-extra-template \
	--with-sun-templates \
	--without-fonts \
	--without-junit \
	--enable-silent-rules \
%if %{javaless}
	--with-ant-home="%{antpath}" \
%else
	--with-system-hsqldb \
%endif
	--with-lang="%{langs}" \
	--without-myspell-dicts \
	--with-system-dicts \
	--with-help \
	--with-external-dict-dir=%{_datadir}/dict/ooo \
	--with-external-hyph-dir=%{_datadir}/dict/ooo \
	--with-external-thes-dir=%{_datadir}/dict/ooo \
	--with-system-libs \
	--with-system-ucpp \
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
	--disable-verbose \
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

mkdir -p src
ln -sf %{SOURCE2} src/
ln -sf %{SOURCE3} src/
ln -sf %{SOURCE4} src/
%if %{javaless}
ln -sf %{SOURCE30} src/
ln -sf %{SOURCE31} src/
ln -sf %{SOURCE32} src/
ln -sf %{SOURCE33} src/
%endif
ln -sf %{SOURCE34} src/
ln -sf %{SOURCE35} src/
ln -sf %{SOURCE36} src/
ln -sf %{SOURCE37} src/

ln -sf %{SOURCE40} src/

ln -sf %{SOURCE50} src/
ln -sf %{SOURCE51} src/
ln -sf %{SOURCE52} src/
ln -sf %{SOURCE53} src/
ln -sf %{SOURCE54} src/
ln -sf %{SOURCE55} src/
ln -sf %{SOURCE56} src/
ln -sf %{SOURCE57} src/
ln -sf %{SOURCE58} src/
ln -sf %{SOURCE59} src/
ln -sf %{SOURCE60} src/
ln -sf %{SOURCE61} src/
ln -sf %{SOURCE62} src/
ln -sf %{SOURCE63} src/
ln -sf %{SOURCE64} src/
ln -sf %{SOURCE65} src/
ln -sf %{SOURCE66} src/
ln -sf %{SOURCE67} src/

touch src.downloaded

# (tpg) silent output to reduce memory and free space 
make -r -s V=0 \
	ARCH_FLAGS="$ARCH_FLAGS" \
	ARCH_FLAGS_CC="$ARCH_FLAGS_CC" \
	ARCH_FLAGS_CXX="$ARCH_FLAGS_CXX" \
	ARCH_FLAGS_OPT="$ARCH_FLAGS_OPT"

echo "Make end at: "`date` >> ooobuildtime.log 
echo "Install start at: "`date` >> ooobuildtime.log 

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
for i in oxygen galaxy crystal hicontrast tango; do
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
sort -u file-lists/common_list.txt >  file-lists/common_list.uniq.sorted.txt 
cat file-lists/common_list.uniq.sorted.txt >>file-lists/core_list.txt

%post common
%update_icon_cache gnome
%update_icon_cache hicolor

# Firefox plugin
if [ $1 -gt 1 ]
then
  update-alternatives --remove %{firefox_plugin} \
  %{ooodir}/program/libnpsoplugin.so
fi
update-alternatives \
  --install %{_libdir}/mozilla/plugins/libnpsoplugin.so %{firefox_plugin} \
  %{ooodir}/program/libnpsoplugin.so 1

%postun common
%clean_icon_cache gnome
%clean_icon_cache hicolor

# Firefox plugin
if [ $1 -eq 0 ]
then
  update-alternatives --remove %{firefox_plugin} \
  %{ooodir}/program/libnpsoplugin.so
fi

%files

%files base -f file-lists/base_list.txt
%{_mandir}/man1/lobase*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-base_72.svg

%files calc -f file-lists/calc_list.txt
%{_mandir}/man1/localc*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-calc_72.svg

%files common -f file-lists/core_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo_72.svg
%{_mandir}/man1/loffice*
%{_mandir}/man1/lofromtemplate*
%{_mandir}/man1/libreoffice*
%{_mandir}/man1/unopkg.1*
%{_libdir}/libreoffice/program/classes/ScriptProviderForBeanShell.jar
%{_libdir}/libreoffice/program/services/scriptproviderforbeanshell.rdb

%files devel -f file-lists/sdk_list.uniq.sorted.txt

%files devel-doc -f file-lists/sdk_doc_list.txt

%files java -f file-lists/java_common_list.txt

%files draw -f file-lists/draw_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-draw_72.svg
%{_mandir}/man1/lodraw*

%files gnome -f file-lists/gnome_list.uniq.sorted.txt

%files impress -f file-lists/impress_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-impress_72.svg
%{_mandir}/man1/loimpress*

%files kde4 -f file-lists/kde4_list.txt
%{_libdir}/libreoffice/program/libkde4be1lo.so

%files math -f file-lists/math_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-math_72.svg
%{_mandir}/man1/lomath*

%files openclipart -f file-lists/gallery_list.txt
%{ooodir}/share/gallery/Draws
%{ooodir}/share/gallery/Elements
%{ooodir}/share/gallery/Photos
%{ooodir}/share/gallery/apples*
%{ooodir}/share/gallery/bigapple*
%{ooodir}/share/gallery/flower*
%{ooodir}/share/gallery/sg[0-9]*.*
%{ooodir}/share/gallery/sky.*
%{ooodir}/share/gallery/arrows.sdg
%{ooodir}/share/gallery/arrows.sdv
%{ooodir}/share/gallery/arrows.str
%{ooodir}/share/gallery/arrows.thm
%{ooodir}/share/gallery/arrows/A01-Arrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A02-Arrow-DarkBlue-Right.png
%{ooodir}/share/gallery/arrows/A03-Arrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A04-Arrow-DarkRed-Right.png
%{ooodir}/share/gallery/arrows/A05-Arrow-Blue-Left.png
%{ooodir}/share/gallery/arrows/A06-Arrow-Red-Right.png
%{ooodir}/share/gallery/arrows/A07-Arrow-LightBlue-Left.png
%{ooodir}/share/gallery/arrows/A08-Arrow-DarkRed-Right.png
%{ooodir}/share/gallery/arrows/A09-Arrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A10-Arrow-Purple-Right.png
%{ooodir}/share/gallery/arrows/A11-Arrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A12-Arrow-LightBlue-Right.png
%{ooodir}/share/gallery/arrows/A13-Arrow-Gray-Right.png
%{ooodir}/share/gallery/arrows/A14-CircleArrow-Green.png
%{ooodir}/share/gallery/arrows/A15-CircleArrow.png
%{ooodir}/share/gallery/arrows/A16-CircleArrow.png
%{ooodir}/share/gallery/arrows/A17-CircleArrow.png
%{ooodir}/share/gallery/arrows/A18-CircleArrow.png
%{ooodir}/share/gallery/arrows/A19-CircleArrow.png
%{ooodir}/share/gallery/arrows/A20-CircleArrow-LightBlue.png
%{ooodir}/share/gallery/arrows/A21-CircleArrow-Green.png
%{ooodir}/share/gallery/arrows/A22-CircleArrow.png
%{ooodir}/share/gallery/arrows/A23-CurvedArrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A24-CurvedArrow-LightBlue-Right.png
%{ooodir}/share/gallery/arrows/A25-CurvedArrow-DarkBlue.png
%{ooodir}/share/gallery/arrows/A26-CurvedArrow-Orange.png
%{ooodir}/share/gallery/arrows/A27-CurvedArrow-DarkRed.png
%{ooodir}/share/gallery/arrows/A28-CurvedArrow-DarkBlue.png
%{ooodir}/share/gallery/arrows/A29-CurvedArrow-Green.png
%{ooodir}/share/gallery/arrows/A30-CurvedArrow-Gray.png
%{ooodir}/share/gallery/arrows/A31-CurvedArrow-LightBlue.png
%{ooodir}/share/gallery/arrows/A32-CurvedArrow-Orange.png
%{ooodir}/share/gallery/arrows/A33-CurvedArrow-LightBlue-TwoDirections.png
%{ooodir}/share/gallery/arrows/A34-CurvedArrow-Green-TwoDirections.png
%{ooodir}/share/gallery/arrows/A35-CurvedArrow-Brown-Left.png
%{ooodir}/share/gallery/arrows/A36-CurvedArrow-LightBlue-Up.png
%{ooodir}/share/gallery/arrows/A37-CurvedArrow-Gray-TwoDirections.png
%{ooodir}/share/gallery/arrows/A38-CurvedArrow-Gray-TwoDirections.png
%{ooodir}/share/gallery/arrows/A39-CurvedArrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A40-CurvedArrow-Gray-Up.png
%{ooodir}/share/gallery/arrows/A41-CurvedArrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A42-TrendArrow-Red-GoUp.png
%{ooodir}/share/gallery/arrows/A43-TrendArrow-Green-GoDown.png
%{ooodir}/share/gallery/arrows/A44-TrendArrow-Orange-GoUp.png
%{ooodir}/share/gallery/arrows/A45-TrendArrow-Red-GoUp.png
%{ooodir}/share/gallery/arrows/A46-TrendArrow-Orange-GoUp.png
%{ooodir}/share/gallery/arrows/A47-TrendArrow-LightBlue.png
%{ooodir}/share/gallery/arrows/A48-TrendArrow-Orange-TwoDirections.png
%{ooodir}/share/gallery/arrows/A49-TrendArrow-Yellow-ThreeDirections.png
%{ooodir}/share/gallery/arrows/A50-TrendArrow-LightBlue-FourDirections.png
%{ooodir}/share/gallery/arrows/A51-TrendArrow-Blue-FourDirections.png
%{ooodir}/share/gallery/arrows/A52-TrendArrow-Blue-FourDirections.png
%{ooodir}/share/gallery/arrows/A53-TrendArrow-LightBlue-TwoDirections.png
%{ooodir}/share/gallery/arrows/A54-TrendArrow-Red-TwoDirections.png
%{ooodir}/share/gallery/arrows/A55-TrendArrow-TwoDirections.png
%{ooodir}/share/gallery/arrows/A56-TrendArrow-Blue-TwoDirections.png
%{ooodir}/share/gallery/arrows/A57-Arrow-Yellow-Left.png
%{ooodir}/share/gallery/arrows/A58-Arrow-Red-Right.png
%{ooodir}/share/gallery/arrows/A59-CurvedArrow-Gray-Left.png
%{ooodir}/share/gallery/arrows/A60-CurvedArrow-Purple-Right.png
%{ooodir}/share/gallery/arrows/A61-Arrow-StripedOrange-Left.png
%{ooodir}/share/gallery/arrows/A62-Arrow-StripedBlue-Right.png
%{ooodir}/share/gallery/arrows/A63-Arrow-LightBlue-Left.png
%{ooodir}/share/gallery/arrows/A64-Arrow-Green-Right.png
%{ooodir}/share/gallery/arrows/A65-Arrow-DarkBlue-Up.png
%{ooodir}/share/gallery/arrows/A66-Arrow-Green-Down.png
%{ooodir}/share/gallery/arrows/A67-Arrow-Yellow-Left.png
%{ooodir}/share/gallery/arrows/A68-Arrow-Gray-Right.png
%{ooodir}/share/gallery/bullets/blkpearl.gif
%{ooodir}/share/gallery/bullets/bluarrow.gif
%{ooodir}/share/gallery/bullets/bluball.gif
%{ooodir}/share/gallery/bullets/bludiamd.gif
%{ooodir}/share/gallery/bullets/bluered.gif
%{ooodir}/share/gallery/bullets/blusqare.gif
%{ooodir}/share/gallery/bullets/blustar.gif
%{ooodir}/share/gallery/bullets/coffee_1.gif
%{ooodir}/share/gallery/bullets/coffee_2.gif
%{ooodir}/share/gallery/bullets/coffee_3.gif
%{ooodir}/share/gallery/bullets/coffee_4.gif
%{ooodir}/share/gallery/bullets/coffee_5.gif
%{ooodir}/share/gallery/bullets/con-blue.gif
%{ooodir}/share/gallery/bullets/con-cyan.gif
%{ooodir}/share/gallery/bullets/con-green.gif
%{ooodir}/share/gallery/bullets/con-lilac.gif
%{ooodir}/share/gallery/bullets/con-oran.gif
%{ooodir}/share/gallery/bullets/con-pink.gif
%{ooodir}/share/gallery/bullets/con-red.gif
%{ooodir}/share/gallery/bullets/con-yellow.gif
%{ooodir}/share/gallery/bullets/corner_1.gif
%{ooodir}/share/gallery/bullets/corner_2.gif
%{ooodir}/share/gallery/bullets/corner_3.gif
%{ooodir}/share/gallery/bullets/corner_4.gif
%{ooodir}/share/gallery/bullets/darkball.gif
%{ooodir}/share/gallery/bullets/darkblue.gif
%{ooodir}/share/gallery/bullets/gldpearl.gif
%{ooodir}/share/gallery/bullets/golfball.gif
%{ooodir}/share/gallery/bullets/grnarrow.gif
%{ooodir}/share/gallery/bullets/grnball.gif
%{ooodir}/share/gallery/bullets/grndiamd.gif
%{ooodir}/share/gallery/bullets/grnpearl.gif
%{ooodir}/share/gallery/bullets/grnsqare.gif
%{ooodir}/share/gallery/bullets/grnstar.gif
%{ooodir}/share/gallery/bullets/gryarrow.gif
%{ooodir}/share/gallery/bullets/gryball.gif
%{ooodir}/share/gallery/bullets/grydiamd.gif
%{ooodir}/share/gallery/bullets/grysqare.gif
%{ooodir}/share/gallery/bullets/grystar.gif
%{ooodir}/share/gallery/bullets/orgarrow.gif
%{ooodir}/share/gallery/bullets/orgball.gif
%{ooodir}/share/gallery/bullets/orgdiamd.gif
%{ooodir}/share/gallery/bullets/orgsqare.gif
%{ooodir}/share/gallery/bullets/orgstar.gif
%{ooodir}/share/gallery/bullets/pebble_1.gif
%{ooodir}/share/gallery/bullets/pebble_2.gif
%{ooodir}/share/gallery/bullets/pebble_3.gif
%{ooodir}/share/gallery/bullets/poliball.gif
%{ooodir}/share/gallery/bullets/popcorn_1.gif
%{ooodir}/share/gallery/bullets/popcorn_2.gif
%{ooodir}/share/gallery/bullets/rainbow.gif
%{ooodir}/share/gallery/bullets/redarrow.gif
%{ooodir}/share/gallery/bullets/redball.gif
%{ooodir}/share/gallery/bullets/reddiamd.gif
%{ooodir}/share/gallery/bullets/redsqare.gif
%{ooodir}/share/gallery/bullets/redstar.gif
%{ooodir}/share/gallery/bullets/whtpearl.gif
%{ooodir}/share/gallery/bullets/ylwarrow.gif
%{ooodir}/share/gallery/bullets/ylwball.gif
%{ooodir}/share/gallery/bullets/ylwdiamd.gif
%{ooodir}/share/gallery/bullets/ylwsqare.gif
%{ooodir}/share/gallery/bullets/ylwstar.gif
%{ooodir}/share/gallery/computers.sdg
%{ooodir}/share/gallery/computers.sdv
%{ooodir}/share/gallery/computers.str
%{ooodir}/share/gallery/computers.thm
%{ooodir}/share/gallery/computers/Computer-Cloud.png
%{ooodir}/share/gallery/computers/Computer-Desktop.png
%{ooodir}/share/gallery/computers/Computer-Laptop-Black.png
%{ooodir}/share/gallery/computers/Computer-Laptop-Silver.png
%{ooodir}/share/gallery/computers/Database-Add.png
%{ooodir}/share/gallery/computers/Database-Delete.png
%{ooodir}/share/gallery/computers/Database-Download.png
%{ooodir}/share/gallery/computers/Database.png
%{ooodir}/share/gallery/computers/Folder01-Blue.png
%{ooodir}/share/gallery/computers/Folder02-Green.png
%{ooodir}/share/gallery/computers/Folder03-Manilla.png
%{ooodir}/share/gallery/computers/Folder04-Yellow.png
%{ooodir}/share/gallery/computers/Folder05-OpenBlue.png
%{ooodir}/share/gallery/computers/Folder06-OpenGreen.png
%{ooodir}/share/gallery/computers/Folder07-OpenManilla.png
%{ooodir}/share/gallery/computers/Folder08-OpenYellow.png
%{ooodir}/share/gallery/computers/Server.png
%{ooodir}/share/gallery/computers/WirelessAccessPoint.png
%{ooodir}/share/gallery/diagrams.sdg
%{ooodir}/share/gallery/diagrams.sdv
%{ooodir}/share/gallery/diagrams.str
%{ooodir}/share/gallery/diagrams.thm
%{ooodir}/share/gallery/diagrams/Component-Circle01-Transparent-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Circle02-Transparent-Bule.png
%{ooodir}/share/gallery/diagrams/Component-Circle03-Transparent-Green.png
%{ooodir}/share/gallery/diagrams/Component-Circle04-Transparent-Orange.png
%{ooodir}/share/gallery/diagrams/Component-Circle05-Transparent-Red.png
%{ooodir}/share/gallery/diagrams/Component-Cube01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Cube02-LightBlue.png
%{ooodir}/share/gallery/diagrams/Component-Cube03-Green.png
%{ooodir}/share/gallery/diagrams/Component-Cube04-Orange.png
%{ooodir}/share/gallery/diagrams/Component-Cube05-DarkRed.png
%{ooodir}/share/gallery/diagrams/Component-Cuboid01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Cuboid02-Blue.png
%{ooodir}/share/gallery/diagrams/Component-Cuboid03-Green.png
%{ooodir}/share/gallery/diagrams/Component-Cuboid04-Orange.png
%{ooodir}/share/gallery/diagrams/Component-Cuboid05-Red.png
%{ooodir}/share/gallery/diagrams/Component-Gear01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Gear02-LightBlue.png
%{ooodir}/share/gallery/diagrams/Component-Gear03-Green.png
%{ooodir}/share/gallery/diagrams/Component-Gear04-DarkRed.png
%{ooodir}/share/gallery/diagrams/Component-Gear05-Orange.png
%{ooodir}/share/gallery/diagrams/Component-Person01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Person02-Blue.png
%{ooodir}/share/gallery/diagrams/Component-Person03-Green.png
%{ooodir}/share/gallery/diagrams/Component-Person04-DarkRed.png
%{ooodir}/share/gallery/diagrams/Component-Person05-Orange.png
%{ooodir}/share/gallery/diagrams/Component-PuzzlePiece01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-PuzzlePiece02-Blue.png
%{ooodir}/share/gallery/diagrams/Component-PuzzlePiece03-Green.png
%{ooodir}/share/gallery/diagrams/Component-PuzzlePiece04-Red.png
%{ooodir}/share/gallery/diagrams/Component-PuzzlePiece05-Orange.png
%{ooodir}/share/gallery/diagrams/Component-Sphere01-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Component-Sphere02-LightBlue.png
%{ooodir}/share/gallery/diagrams/Component-Sphere03-Green.png
%{ooodir}/share/gallery/diagrams/Component-Sphere04-DarkRed.png
%{ooodir}/share/gallery/diagrams/Component-Sphere05-Orange.png
%{ooodir}/share/gallery/diagrams/Cycle01-Transparent.png
%{ooodir}/share/gallery/diagrams/Cycle02-Transparent-Blue.png
%{ooodir}/share/gallery/diagrams/Cycle03-Blue.png
%{ooodir}/share/gallery/diagrams/Cycle04-Blue.png
%{ooodir}/share/gallery/diagrams/Cycle05.png
%{ooodir}/share/gallery/diagrams/Cycle06.png
%{ooodir}/share/gallery/diagrams/Cycle07.png
%{ooodir}/share/gallery/diagrams/Cycle08-Blue.png
%{ooodir}/share/gallery/diagrams/Cycle09-Orange.png
%{ooodir}/share/gallery/diagrams/Donut01-LightBlue.png
%{ooodir}/share/gallery/diagrams/Donut02-Blue.png
%{ooodir}/share/gallery/diagrams/Donut03-Blue.png
%{ooodir}/share/gallery/diagrams/Donut04-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Donut05-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Donut06-Blue.png
%{ooodir}/share/gallery/diagrams/Donut07-Blue.png
%{ooodir}/share/gallery/diagrams/Graph.png
%{ooodir}/share/gallery/diagrams/People01-Blue.png
%{ooodir}/share/gallery/diagrams/People02.png
%{ooodir}/share/gallery/diagrams/Pillars01-Orange.png
%{ooodir}/share/gallery/diagrams/Pillars02-LightBlue.png
%{ooodir}/share/gallery/diagrams/Process01-Blue.png
%{ooodir}/share/gallery/diagrams/Process02-Blue.png
%{ooodir}/share/gallery/diagrams/Process03-Blue.emf
%{ooodir}/share/gallery/diagrams/Process04-GoUp-Blue.png
%{ooodir}/share/gallery/diagrams/Process05-GoUp-Red.png
%{ooodir}/share/gallery/diagrams/Process06-GoUp-Yellow.png
%{ooodir}/share/gallery/diagrams/Process07-Blue.png
%{ooodir}/share/gallery/diagrams/Pyramid01.png
%{ooodir}/share/gallery/diagrams/Pyramid02-Blue.png
%{ooodir}/share/gallery/diagrams/Pyramid03.emf
%{ooodir}/share/gallery/diagrams/Radial01-Green.emf
%{ooodir}/share/gallery/diagrams/Radial02-Green.emf
%{ooodir}/share/gallery/diagrams/Radial03-Sphere.png
%{ooodir}/share/gallery/diagrams/Radial04-Sphere-Red.png
%{ooodir}/share/gallery/diagrams/Radial05-Sphere-Blue.png
%{ooodir}/share/gallery/diagrams/Radial06-Arrows-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Radial07-Arrows-DarkBlue.png
%{ooodir}/share/gallery/diagrams/Section-Circle.emf
%{ooodir}/share/gallery/diagrams/Section-Cubes01.png
%{ooodir}/share/gallery/diagrams/Section-Cubes02-Blue.png
%{ooodir}/share/gallery/diagrams/Section-Cubes03-Orange.png
%{ooodir}/share/gallery/diagrams/Section-Cubes04.png
%{ooodir}/share/gallery/diagrams/Section-Cubes05.png
%{ooodir}/share/gallery/diagrams/Section-Cuboids01-Blue.png
%{ooodir}/share/gallery/diagrams/Section-Cuboids02-Blue.png
%{ooodir}/share/gallery/diagrams/Section-Cuboids03.png
%{ooodir}/share/gallery/diagrams/Section-Gears01.png
%{ooodir}/share/gallery/diagrams/Section-Gears02-Blue.emf
%{ooodir}/share/gallery/diagrams/Section-Gears03.png
%{ooodir}/share/gallery/diagrams/Section-Hexagons01.png
%{ooodir}/share/gallery/diagrams/Section-Hexagons02-Blue.png
%{ooodir}/share/gallery/diagrams/Section-Hexagons03-Blue.png
%{ooodir}/share/gallery/diagrams/Section-Hexagons04-Orange.emf
%{ooodir}/share/gallery/diagrams/Section-Leaves01-LightBlue.png
%{ooodir}/share/gallery/diagrams/Section-Leaves02-Green.png
%{ooodir}/share/gallery/diagrams/Section-Pasters01.png
%{ooodir}/share/gallery/diagrams/Section-Pasters02-Blue.emf
%{ooodir}/share/gallery/diagrams/Section-Puzzle01.emf
%{ooodir}/share/gallery/diagrams/Section-Puzzle02.png
%{ooodir}/share/gallery/diagrams/Section-Puzzle03.png
%{ooodir}/share/gallery/diagrams/Section-Rectangles.png
%{ooodir}/share/gallery/diagrams/Section-Squares.png
%{ooodir}/share/gallery/diagrams/Section-Triangle.emf
%{ooodir}/share/gallery/diagrams/Target.png
%{ooodir}/share/gallery/diagrams/Venn01.png
%{ooodir}/share/gallery/diagrams/Venn02.png
%{ooodir}/share/gallery/diagrams/Venn03.png
%{ooodir}/share/gallery/diagrams/Venn04.png
%{ooodir}/share/gallery/diagrams/Venn05.png
%{ooodir}/share/gallery/diagrams/Venn06-Blue.png
%{ooodir}/share/gallery/diagrams/Venn07-Blue.emf
%{ooodir}/share/gallery/diagrams/Venn08.png
%{ooodir}/share/gallery/education.sdg
%{ooodir}/share/gallery/education.sdv
%{ooodir}/share/gallery/education.str
%{ooodir}/share/gallery/education.thm
%{ooodir}/share/gallery/education/Blackboard.png
%{ooodir}/share/gallery/education/Books.png
%{ooodir}/share/gallery/education/Chalk.png
%{ooodir}/share/gallery/education/Globe.png
%{ooodir}/share/gallery/education/Glue.png
%{ooodir}/share/gallery/education/GraduationCap.png
%{ooodir}/share/gallery/education/Microscope.png
%{ooodir}/share/gallery/education/Notebook.png
%{ooodir}/share/gallery/education/PaperClip-Blue.png
%{ooodir}/share/gallery/education/PaperClip-Red.png
%{ooodir}/share/gallery/education/Pencil.png
%{ooodir}/share/gallery/education/Ruler.png
%{ooodir}/share/gallery/education/TestTubes.png
%{ooodir}/share/gallery/environment.sdg
%{ooodir}/share/gallery/environment.sdv
%{ooodir}/share/gallery/environment.str
%{ooodir}/share/gallery/environment.thm
%{ooodir}/share/gallery/environment/DrippingFaucet.png
%{ooodir}/share/gallery/environment/Earth.png
%{ooodir}/share/gallery/environment/EndangeredAnimals1.png
%{ooodir}/share/gallery/environment/EndangeredAnimals2.png
%{ooodir}/share/gallery/environment/GreenCar.png
%{ooodir}/share/gallery/environment/GreenFactory.png
%{ooodir}/share/gallery/environment/GreenHouse.png
%{ooodir}/share/gallery/environment/Leaf1.png
%{ooodir}/share/gallery/environment/Leaf2.png
%{ooodir}/share/gallery/environment/LightBulb-Flourescent-Off.png
%{ooodir}/share/gallery/environment/LightBulb-Flourescent-On.png
%{ooodir}/share/gallery/environment/LightBulb-Standard-Off1.png
%{ooodir}/share/gallery/environment/LightBulb-Standard-Off2.png
%{ooodir}/share/gallery/environment/LightBulb-Standard-On.png
%{ooodir}/share/gallery/environment/Pollution-Car.png
%{ooodir}/share/gallery/environment/Pollution-Factory.png
%{ooodir}/share/gallery/environment/Raindrop.png
%{ooodir}/share/gallery/environment/RecycleBin.png
%{ooodir}/share/gallery/environment/RecycleSymbol.png
%{ooodir}/share/gallery/environment/RenewableEnergy-Solar.png
%{ooodir}/share/gallery/environment/RenewableEnergy-Water.png
%{ooodir}/share/gallery/environment/RenewableEnergy-Wind.png
%{ooodir}/share/gallery/environment/RenewableEnergySymbol.png
%{ooodir}/share/gallery/environment/Sun1.png
%{ooodir}/share/gallery/environment/Sun2.png
%{ooodir}/share/gallery/finance.sdg
%{ooodir}/share/gallery/finance.sdv
%{ooodir}/share/gallery/finance.str
%{ooodir}/share/gallery/finance.thm
%{ooodir}/share/gallery/finance/ATM01.png
%{ooodir}/share/gallery/finance/ATM02.png
%{ooodir}/share/gallery/finance/Agreement.png
%{ooodir}/share/gallery/finance/Balance-Balanced1.png
%{ooodir}/share/gallery/finance/Balance-Balanced2.png
%{ooodir}/share/gallery/finance/Balance-Unbalanced1.png
%{ooodir}/share/gallery/finance/Balance-Unbalanced2.png
%{ooodir}/share/gallery/finance/Calculator.png
%{ooodir}/share/gallery/finance/Chart-Decrease1.png
%{ooodir}/share/gallery/finance/Chart-Decrease2.png
%{ooodir}/share/gallery/finance/Chart-Increase1.png
%{ooodir}/share/gallery/finance/Chart-Increase2.png
%{ooodir}/share/gallery/finance/Chart-Plateau.png
%{ooodir}/share/gallery/finance/Check.png
%{ooodir}/share/gallery/finance/Contract.png
%{ooodir}/share/gallery/finance/CreditCard-Black.png
%{ooodir}/share/gallery/finance/CreditCard-Cut.png
%{ooodir}/share/gallery/finance/CreditCard-Gold.png
%{ooodir}/share/gallery/finance/Currency-Dollar.png
%{ooodir}/share/gallery/finance/Currency-Dollars.png
%{ooodir}/share/gallery/finance/Currency-Stack.png
%{ooodir}/share/gallery/finance/Currency-StackCoins.png
%{ooodir}/share/gallery/finance/GoldBar-Stack.png
%{ooodir}/share/gallery/finance/GoldBar.png
%{ooodir}/share/gallery/finance/MoneyBag01.png
%{ooodir}/share/gallery/finance/MoneyBag02.png
%{ooodir}/share/gallery/finance/PercentSign.png
%{ooodir}/share/gallery/finance/PiggyBank-Coins.png
%{ooodir}/share/gallery/finance/PiggyBank-Currency.png
%{ooodir}/share/gallery/finance/PiggyBank01-Broken.png
%{ooodir}/share/gallery/finance/PiggyBank02-Broken.png
%{ooodir}/share/gallery/finance/Portfolio.png
%{ooodir}/share/gallery/finance/PriceTag.png
%{ooodir}/share/gallery/finance/Safe-Closed.png
%{ooodir}/share/gallery/finance/Safe-Empty.png
%{ooodir}/share/gallery/finance/Safe-Full.png
%{ooodir}/share/gallery/finance/Seal-Gold.png
%{ooodir}/share/gallery/finance/Seal-Red.png
%{ooodir}/share/gallery/finance/Seal-Silver.png
%{ooodir}/share/gallery/finance/Wallet-Empty.png
%{ooodir}/share/gallery/finance/Wallet-Full1.png
%{ooodir}/share/gallery/finance/Wallet-Full2.png
%{ooodir}/share/gallery/htmlexpo/bludown.gif
%{ooodir}/share/gallery/htmlexpo/blufirs.gif
%{ooodir}/share/gallery/htmlexpo/blufirs_.gif
%{ooodir}/share/gallery/htmlexpo/blulast.gif
%{ooodir}/share/gallery/htmlexpo/blulast_.gif
%{ooodir}/share/gallery/htmlexpo/blunav.gif
%{ooodir}/share/gallery/htmlexpo/blunext.gif
%{ooodir}/share/gallery/htmlexpo/blunext_.gif
%{ooodir}/share/gallery/htmlexpo/bluprev.gif
%{ooodir}/share/gallery/htmlexpo/bluprev_.gif
%{ooodir}/share/gallery/htmlexpo/blutext.gif
%{ooodir}/share/gallery/htmlexpo/bluup.gif
%{ooodir}/share/gallery/htmlexpo/cubdown.gif
%{ooodir}/share/gallery/htmlexpo/cubfirs.gif
%{ooodir}/share/gallery/htmlexpo/cubfirs_.gif
%{ooodir}/share/gallery/htmlexpo/cublast.gif
%{ooodir}/share/gallery/htmlexpo/cublast_.gif
%{ooodir}/share/gallery/htmlexpo/cubnav.gif
%{ooodir}/share/gallery/htmlexpo/cubnext.gif
%{ooodir}/share/gallery/htmlexpo/cubnext_.gif
%{ooodir}/share/gallery/htmlexpo/cubprev.gif
%{ooodir}/share/gallery/htmlexpo/cubprev_.gif
%{ooodir}/share/gallery/htmlexpo/cubtext.gif
%{ooodir}/share/gallery/htmlexpo/cubup.gif
%{ooodir}/share/gallery/htmlexpo/gredown.gif
%{ooodir}/share/gallery/htmlexpo/grefirs.gif
%{ooodir}/share/gallery/htmlexpo/grefirs_.gif
%{ooodir}/share/gallery/htmlexpo/grelast.gif
%{ooodir}/share/gallery/htmlexpo/grelast_.gif
%{ooodir}/share/gallery/htmlexpo/grenav.gif
%{ooodir}/share/gallery/htmlexpo/grenext.gif
%{ooodir}/share/gallery/htmlexpo/grenext_.gif
%{ooodir}/share/gallery/htmlexpo/greprev.gif
%{ooodir}/share/gallery/htmlexpo/greprev_.gif
%{ooodir}/share/gallery/htmlexpo/gretext.gif
%{ooodir}/share/gallery/htmlexpo/greup.gif
%{ooodir}/share/gallery/htmlexpo/simdown.gif
%{ooodir}/share/gallery/htmlexpo/simfirs.gif
%{ooodir}/share/gallery/htmlexpo/simfirs_.gif
%{ooodir}/share/gallery/htmlexpo/simlast.gif
%{ooodir}/share/gallery/htmlexpo/simlast_.gif
%{ooodir}/share/gallery/htmlexpo/simnav.gif
%{ooodir}/share/gallery/htmlexpo/simnext.gif
%{ooodir}/share/gallery/htmlexpo/simnext_.gif
%{ooodir}/share/gallery/htmlexpo/simprev.gif
%{ooodir}/share/gallery/htmlexpo/simprev_.gif
%{ooodir}/share/gallery/htmlexpo/simtext.gif
%{ooodir}/share/gallery/htmlexpo/simup.gif
%{ooodir}/share/gallery/people.sdg
%{ooodir}/share/gallery/people.sdv
%{ooodir}/share/gallery/people.str
%{ooodir}/share/gallery/people.thm
%{ooodir}/share/gallery/people/Artist-Female1.png
%{ooodir}/share/gallery/people/Artist-Female2.png
%{ooodir}/share/gallery/people/Artist-Male1.png
%{ooodir}/share/gallery/people/Artist-Male2.png
%{ooodir}/share/gallery/people/BusinessPerson-Female1.png
%{ooodir}/share/gallery/people/BusinessPerson-Female2.png
%{ooodir}/share/gallery/people/BusinessPerson-Female3.png
%{ooodir}/share/gallery/people/BusinessPerson-Female4.png
%{ooodir}/share/gallery/people/BusinessPerson-Female5.png
%{ooodir}/share/gallery/people/BusinessPerson-Female6.png
%{ooodir}/share/gallery/people/BusinessPerson-HeadSet1.png
%{ooodir}/share/gallery/people/BusinessPerson-HeadSet2.png
%{ooodir}/share/gallery/people/BusinessPerson-Male1.png
%{ooodir}/share/gallery/people/BusinessPerson-Male2.png
%{ooodir}/share/gallery/people/BusinessPerson-Male3.png
%{ooodir}/share/gallery/people/BusinessPerson-Male4.png
%{ooodir}/share/gallery/people/BusinessPerson-Male5.png
%{ooodir}/share/gallery/people/BusinessPerson-Male6.png
%{ooodir}/share/gallery/people/Chef1.png
%{ooodir}/share/gallery/people/Chef2.png
%{ooodir}/share/gallery/people/Computer-User-Female1.png
%{ooodir}/share/gallery/people/Computer-User-Female2.png
%{ooodir}/share/gallery/people/Computer-User-Male1.png
%{ooodir}/share/gallery/people/Computer-User-Male2.png
%{ooodir}/share/gallery/people/ConstructionWorker.png
%{ooodir}/share/gallery/people/ConstructionWorker2.png
%{ooodir}/share/gallery/people/Detective1.png
%{ooodir}/share/gallery/people/Detective2.png
%{ooodir}/share/gallery/people/Doctor-Female1.png
%{ooodir}/share/gallery/people/Doctor-Female2.png
%{ooodir}/share/gallery/people/Doctor-Male1.png
%{ooodir}/share/gallery/people/Doctor-Male2.png
%{ooodir}/share/gallery/people/Nurse1.png
%{ooodir}/share/gallery/people/Nurse2.png
%{ooodir}/share/gallery/people/PoliceOfficer1.png
%{ooodir}/share/gallery/people/PoliceOfficer2.png
%{ooodir}/share/gallery/people/Presenter-Female1.png
%{ooodir}/share/gallery/people/Presenter-Female2.png
%{ooodir}/share/gallery/people/Presenter-Male1.png
%{ooodir}/share/gallery/people/Presenter-Male2.png
%{ooodir}/share/gallery/people/Student-Female.png
%{ooodir}/share/gallery/people/Student-Male.png
%{ooodir}/share/gallery/people/Surgeon-Female1.png
%{ooodir}/share/gallery/people/Surgeon-Female2.png
%{ooodir}/share/gallery/people/Surgeon1.png
%{ooodir}/share/gallery/people/Surgeon2.png
%{ooodir}/share/gallery/people/Teacher1.png
%{ooodir}/share/gallery/people/Teacher2.png
%{ooodir}/share/gallery/people/Tourist-Female1.png
%{ooodir}/share/gallery/people/Tourist-Female2.png
%{ooodir}/share/gallery/people/Tourist-Male1.png
%{ooodir}/share/gallery/people/Tourist-Male2.png
%{ooodir}/share/gallery/sounds.sdg
%{ooodir}/share/gallery/sounds.sdv
%{ooodir}/share/gallery/sounds.str
%{ooodir}/share/gallery/sounds.thm
%{ooodir}/share/gallery/sounds/apert.wav
%{ooodir}/share/gallery/sounds/apert2.wav
%{ooodir}/share/gallery/sounds/applause.wav
%{ooodir}/share/gallery/sounds/beam.wav
%{ooodir}/share/gallery/sounds/beam2.wav
%{ooodir}/share/gallery/sounds/cow.wav
%{ooodir}/share/gallery/sounds/curve.wav
%{ooodir}/share/gallery/sounds/drama.wav
%{ooodir}/share/gallery/sounds/explos.wav
%{ooodir}/share/gallery/sounds/falling.wav
%{ooodir}/share/gallery/sounds/glasses.wav
%{ooodir}/share/gallery/sounds/gong.wav
%{ooodir}/share/gallery/sounds/horse.wav
%{ooodir}/share/gallery/sounds/kling.wav
%{ooodir}/share/gallery/sounds/kongas.wav
%{ooodir}/share/gallery/sounds/laser.wav
%{ooodir}/share/gallery/sounds/left.wav
%{ooodir}/share/gallery/sounds/nature1.wav
%{ooodir}/share/gallery/sounds/nature2.wav
%{ooodir}/share/gallery/sounds/ok.wav
%{ooodir}/share/gallery/sounds/pluck.wav
%{ooodir}/share/gallery/sounds/roll.wav
%{ooodir}/share/gallery/sounds/romans.wav
%{ooodir}/share/gallery/sounds/soft.wav
%{ooodir}/share/gallery/sounds/space.wav
%{ooodir}/share/gallery/sounds/space2.wav
%{ooodir}/share/gallery/sounds/space3.wav
%{ooodir}/share/gallery/sounds/sparcle.wav
%{ooodir}/share/gallery/sounds/strom.wav
%{ooodir}/share/gallery/sounds/theetone.wav
%{ooodir}/share/gallery/sounds/top.wav
%{ooodir}/share/gallery/sounds/train.wav
%{ooodir}/share/gallery/sounds/untie.wav
%{ooodir}/share/gallery/sounds/ups.wav
%{ooodir}/share/gallery/sounds/wallewal.wav
%{ooodir}/share/gallery/symbols.sdg
%{ooodir}/share/gallery/symbols.sdv
%{ooodir}/share/gallery/symbols.str
%{ooodir}/share/gallery/symbols.thm
%{ooodir}/share/gallery/symbols/Book.png
%{ooodir}/share/gallery/symbols/Box01.png
%{ooodir}/share/gallery/symbols/Box02.png
%{ooodir}/share/gallery/symbols/Bulb01-Yellow.png
%{ooodir}/share/gallery/symbols/Bulb02-Yellow.png
%{ooodir}/share/gallery/symbols/Calendar.png
%{ooodir}/share/gallery/symbols/Chart.png
%{ooodir}/share/gallery/symbols/Clipboard.png
%{ooodir}/share/gallery/symbols/Clock.png
%{ooodir}/share/gallery/symbols/Compass.png
%{ooodir}/share/gallery/symbols/Emotion01-Laughing.png
%{ooodir}/share/gallery/symbols/Emotion02-Smiling.png
%{ooodir}/share/gallery/symbols/Emotion03-Calm.png
%{ooodir}/share/gallery/symbols/Emotion04-Frowning.png
%{ooodir}/share/gallery/symbols/Emotion05-Angry.png
%{ooodir}/share/gallery/symbols/Emotion06-Crying.png
%{ooodir}/share/gallery/symbols/Flag01-Red.png
%{ooodir}/share/gallery/symbols/Flag02-Green.png
%{ooodir}/share/gallery/symbols/Flag03-Blue.png
%{ooodir}/share/gallery/symbols/Gift.png
%{ooodir}/share/gallery/symbols/House.png
%{ooodir}/share/gallery/symbols/Icon-Computer01-White.png
%{ooodir}/share/gallery/symbols/Icon-Computer02-Black.png
%{ooodir}/share/gallery/symbols/Icon-Disk01-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Disk02-Green.png
%{ooodir}/share/gallery/symbols/Icon-Document01-Grey.png
%{ooodir}/share/gallery/symbols/Icon-Document02-Grey.png
%{ooodir}/share/gallery/symbols/Icon-Document03-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Document04-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Envelope01-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Envelope02-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Envelope03-Open-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Envelope04-Open-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Folder01-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Folder02-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Folder03-Open-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Folder04-Open-Yellow.png
%{ooodir}/share/gallery/symbols/Icon-Gear01-Grey.png
%{ooodir}/share/gallery/symbols/Icon-Gear02-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Network01-Blue.png
%{ooodir}/share/gallery/symbols/Icon-Network02.png
%{ooodir}/share/gallery/symbols/Icon-Pencil01.png
%{ooodir}/share/gallery/symbols/Icon-Pencil02.png
%{ooodir}/share/gallery/symbols/Icon-Printer01-White.png
%{ooodir}/share/gallery/symbols/Icon-Printer02-Black.png
%{ooodir}/share/gallery/symbols/Key01.png
%{ooodir}/share/gallery/symbols/Key02.png
%{ooodir}/share/gallery/symbols/Lock01-Yellow.png
%{ooodir}/share/gallery/symbols/Lock02-Yellow.png
%{ooodir}/share/gallery/symbols/Lock03-Blue.png
%{ooodir}/share/gallery/symbols/Lock04-Blue.png
%{ooodir}/share/gallery/symbols/Magnet.png
%{ooodir}/share/gallery/symbols/MagnifyingGlass.png
%{ooodir}/share/gallery/symbols/Medal.png
%{ooodir}/share/gallery/symbols/Notebook.png
%{ooodir}/share/gallery/symbols/Phone.png
%{ooodir}/share/gallery/symbols/PieChart.png
%{ooodir}/share/gallery/symbols/Pin.png
%{ooodir}/share/gallery/symbols/PuzzlePiece.png
%{ooodir}/share/gallery/symbols/PuzzlePieces.png
%{ooodir}/share/gallery/symbols/Roadblock.png
%{ooodir}/share/gallery/symbols/Scissors.png
%{ooodir}/share/gallery/symbols/Shield01.png
%{ooodir}/share/gallery/symbols/Shield02-Orange.png
%{ooodir}/share/gallery/symbols/Shield03-Blue.png
%{ooodir}/share/gallery/symbols/Sign-Ban01.png
%{ooodir}/share/gallery/symbols/Sign-Ban02.png
%{ooodir}/share/gallery/symbols/Sign-CheckBox01.png
%{ooodir}/share/gallery/symbols/Sign-CheckBox02-Unchecked.png
%{ooodir}/share/gallery/symbols/Sign-Checkmark01-Green.png
%{ooodir}/share/gallery/symbols/Sign-Checkmark02-Green.png
%{ooodir}/share/gallery/symbols/Sign-DoNotEnter.png
%{ooodir}/share/gallery/symbols/Sign-Error01.png
%{ooodir}/share/gallery/symbols/Sign-Error02.png
%{ooodir}/share/gallery/symbols/Sign-ExclamationPoint01-Red.png
%{ooodir}/share/gallery/symbols/Sign-ExclamationPoint02-Orange.png
%{ooodir}/share/gallery/symbols/Sign-Help01-Green.png
%{ooodir}/share/gallery/symbols/Sign-Help02-Blue.png
%{ooodir}/share/gallery/symbols/Sign-Information.png
%{ooodir}/share/gallery/symbols/Sign-Null.png
%{ooodir}/share/gallery/symbols/Sign-QuestionMark01-Blue.png
%{ooodir}/share/gallery/symbols/Sign-QuestionMark02-Red.png
%{ooodir}/share/gallery/symbols/Sign-RadioButton01.png
%{ooodir}/share/gallery/symbols/Sign-RadioButton02-Unchecked.png
%{ooodir}/share/gallery/symbols/Sign-Warning01-Red.png
%{ooodir}/share/gallery/symbols/Sign-Warning02-Orange.png
%{ooodir}/share/gallery/symbols/Sign-X01-Red.png
%{ooodir}/share/gallery/symbols/Sign-X02-Red.png
%{ooodir}/share/gallery/symbols/Star-Yellow.png
%{ooodir}/share/gallery/symbols/Wrench.png
%{ooodir}/share/gallery/transportation.sdg
%{ooodir}/share/gallery/transportation.sdv
%{ooodir}/share/gallery/transportation.str
%{ooodir}/share/gallery/transportation.thm
%{ooodir}/share/gallery/transportation/Airplane-Blue.png
%{ooodir}/share/gallery/transportation/Bicycle-Blue.png
%{ooodir}/share/gallery/transportation/Boat.png
%{ooodir}/share/gallery/transportation/Bus.png
%{ooodir}/share/gallery/transportation/Canoe-Blue.png
%{ooodir}/share/gallery/transportation/Car-Red.png
%{ooodir}/share/gallery/transportation/Helicopter-Blue.png
%{ooodir}/share/gallery/transportation/Motorcycle-Red.png
%{ooodir}/share/gallery/transportation/Pedestrian-Blue.png
%{ooodir}/share/gallery/transportation/PersonalTransporter-Green.png
%{ooodir}/share/gallery/transportation/Sailboat-Red.png
%{ooodir}/share/gallery/transportation/Scooter-Orange.png
%{ooodir}/share/gallery/transportation/Train-Red.png
%{ooodir}/share/gallery/transportation/Truck-Blue.png
%{ooodir}/share/gallery/txtshapes.sdg
%{ooodir}/share/gallery/txtshapes.sdv
%{ooodir}/share/gallery/txtshapes.str
%{ooodir}/share/gallery/txtshapes.thm
%{ooodir}/share/gallery/txtshapes/Circle01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Circle02-LightBlue.png
%{ooodir}/share/gallery/txtshapes/Circle03-Green.png
%{ooodir}/share/gallery/txtshapes/Circle04-DarkRed.png
%{ooodir}/share/gallery/txtshapes/Circle05-Orange.png
%{ooodir}/share/gallery/txtshapes/Hexagon01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Hexagon02-Blue.png
%{ooodir}/share/gallery/txtshapes/Hexagon03-Green.png
%{ooodir}/share/gallery/txtshapes/Hexagon04-DarkRed.png
%{ooodir}/share/gallery/txtshapes/Hexagon05-Orange.png
%{ooodir}/share/gallery/txtshapes/Leaf01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Leaf02-LightBlue.png
%{ooodir}/share/gallery/txtshapes/Leaf03-Green.png
%{ooodir}/share/gallery/txtshapes/Leaf04-DarkRed.png
%{ooodir}/share/gallery/txtshapes/Leaf05-Orange.png
%{ooodir}/share/gallery/txtshapes/Paster01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Paster02-LightBlue.png
%{ooodir}/share/gallery/txtshapes/Paster03-Green.png
%{ooodir}/share/gallery/txtshapes/Paster04-Red.png
%{ooodir}/share/gallery/txtshapes/Paster05-Orange.png
%{ooodir}/share/gallery/txtshapes/Rectangle01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Rectangle02-LightBlue.png
%{ooodir}/share/gallery/txtshapes/Rectangle03-Green.png
%{ooodir}/share/gallery/txtshapes/Rectangle04-DarkRed.png
%{ooodir}/share/gallery/txtshapes/Rectangle05-Orange.png
%{ooodir}/share/gallery/txtshapes/Rectangle06-Striped-Blue.png
%{ooodir}/share/gallery/txtshapes/Rectangle07-Striped-Green.png
%{ooodir}/share/gallery/txtshapes/Rectangle08-Striped-Red.png
%{ooodir}/share/gallery/txtshapes/Rectangle09-Striped-Orange.png
%{ooodir}/share/gallery/txtshapes/Square01-DarkBlue.png
%{ooodir}/share/gallery/txtshapes/Square02-LightBlue.png
%{ooodir}/share/gallery/txtshapes/Square03-Green.png
%{ooodir}/share/gallery/txtshapes/Square04-DarkRed.png
%{ooodir}/share/gallery/txtshapes/Square05-Orange.png
%{ooodir}/share/gallery/txtshapes/Square06-Striped-Blue.png
%{ooodir}/share/gallery/txtshapes/Square07-Striped-Green.png
%{ooodir}/share/gallery/txtshapes/Square08-Striped-Red.png
%{ooodir}/share/gallery/txtshapes/Square09-Striped-Orange.png
%{ooodir}/share/gallery/www-back/aqua.jpg
%{ooodir}/share/gallery/www-back/bathroom.jpg
%{ooodir}/share/gallery/www-back/blocks.jpg
%{ooodir}/share/gallery/www-back/blow_green.jpg
%{ooodir}/share/gallery/www-back/blueblop.jpg
%{ooodir}/share/gallery/www-back/bulging.jpg
%{ooodir}/share/gallery/www-back/canvas_blue.jpg
%{ooodir}/share/gallery/www-back/cheese.jpg
%{ooodir}/share/gallery/www-back/chocolate.jpg
%{ooodir}/share/gallery/www-back/citrus.jpg
%{ooodir}/share/gallery/www-back/confetti.jpg
%{ooodir}/share/gallery/www-back/daisy.jpg
%{ooodir}/share/gallery/www-back/fluffy-grey.jpg
%{ooodir}/share/gallery/www-back/fluffy.jpg
%{ooodir}/share/gallery/www-back/fuzzy-blue.jpg
%{ooodir}/share/gallery/www-back/fuzzy-darkgrey.jpg
%{ooodir}/share/gallery/www-back/fuzzy-grey.jpg
%{ooodir}/share/gallery/www-back/fuzzy-lightgrey.jpg
%{ooodir}/share/gallery/www-back/fuzzy_light.jpg
%{ooodir}/share/gallery/www-back/gregre.gif
%{ooodir}/share/gallery/www-back/grey.gif
%{ooodir}/share/gallery/www-back/grypaws.gif
%{ooodir}/share/gallery/www-back/ice-blue.jpg
%{ooodir}/share/gallery/www-back/ice-light.jpg
%{ooodir}/share/gallery/www-back/imitation_leather.jpg
%{ooodir}/share/gallery/www-back/interstices.jpg
%{ooodir}/share/gallery/www-back/jeans.jpg
%{ooodir}/share/gallery/www-back/jeansblk.jpg
%{ooodir}/share/gallery/www-back/lawn-artificial.jpg
%{ooodir}/share/gallery/www-back/lawn.jpg
%{ooodir}/share/gallery/www-back/lightblue-wet.jpg
%{ooodir}/share/gallery/www-back/linen-fine.jpg
%{ooodir}/share/gallery/www-back/lino-green.jpg
%{ooodir}/share/gallery/www-back/liquid-blue.jpg
%{ooodir}/share/gallery/www-back/marble.jpg
%{ooodir}/share/gallery/www-back/marble_dark.jpg
%{ooodir}/share/gallery/www-back/mazes.jpg
%{ooodir}/share/gallery/www-back/mint.gif
%{ooodir}/share/gallery/www-back/notes.gif
%{ooodir}/share/gallery/www-back/pattern.jpg
%{ooodir}/share/gallery/www-back/pebble-light.jpg
%{ooodir}/share/gallery/www-back/pink.gif
%{ooodir}/share/gallery/www-back/pool.jpg
%{ooodir}/share/gallery/www-back/popcorn.jpg
%{ooodir}/share/gallery/www-back/purple.jpg
%{ooodir}/share/gallery/www-back/reddark.jpg
%{ooodir}/share/gallery/www-back/rings-green.jpg
%{ooodir}/share/gallery/www-back/rings-orange.jpg
%{ooodir}/share/gallery/www-back/roses.jpg
%{ooodir}/share/gallery/www-back/sand-light.jpg
%{ooodir}/share/gallery/www-back/sand.jpg
%{ooodir}/share/gallery/www-back/sky.jpg
%{ooodir}/share/gallery/www-back/soft-structure_grey.jpg
%{ooodir}/share/gallery/www-back/space.jpg
%{ooodir}/share/gallery/www-back/stone-dark.jpg
%{ooodir}/share/gallery/www-back/stone.jpg
%{ooodir}/share/gallery/www-back/structure.jpg
%{ooodir}/share/gallery/www-back/structure_darkgreen.gif
%{ooodir}/share/gallery/www-back/structure_green.jpg
%{ooodir}/share/gallery/www-back/wall-grey.jpg
%{ooodir}/share/gallery/www-back/wet-turquoise.jpg
%{ooodir}/share/gallery/www-back/wood.jpg
%{ooodir}/share/gallery/www-graf/bluat.gif
%{ooodir}/share/gallery/www-graf/bluback.gif
%{ooodir}/share/gallery/www-graf/bludisk.gif
%{ooodir}/share/gallery/www-graf/bludown.gif
%{ooodir}/share/gallery/www-graf/bluhome.gif
%{ooodir}/share/gallery/www-graf/bluinfo.gif
%{ooodir}/share/gallery/www-graf/bluleft.gif
%{ooodir}/share/gallery/www-graf/blumail.gif
%{ooodir}/share/gallery/www-graf/bluminus.gif
%{ooodir}/share/gallery/www-graf/bluplus.gif
%{ooodir}/share/gallery/www-graf/bluquest.gif
%{ooodir}/share/gallery/www-graf/bluright.gif
%{ooodir}/share/gallery/www-graf/bluup.gif
%{ooodir}/share/gallery/www-graf/gredisk.gif
%{ooodir}/share/gallery/www-graf/gredown.gif
%{ooodir}/share/gallery/www-graf/grehome.gif
%{ooodir}/share/gallery/www-graf/greinfo.gif
%{ooodir}/share/gallery/www-graf/greleft.gif
%{ooodir}/share/gallery/www-graf/gremail.gif
%{ooodir}/share/gallery/www-graf/greminus.gif
%{ooodir}/share/gallery/www-graf/greplus.gif
%{ooodir}/share/gallery/www-graf/grequest.gif
%{ooodir}/share/gallery/www-graf/greright.gif
%{ooodir}/share/gallery/www-graf/greup.gif
%{ooodir}/share/gallery/www-graf/grnat.gif
%{ooodir}/share/gallery/www-graf/grnback.gif
%{ooodir}/share/gallery/www-graf/grndisk.gif
%{ooodir}/share/gallery/www-graf/grndown.gif
%{ooodir}/share/gallery/www-graf/grnexcla.gif
%{ooodir}/share/gallery/www-graf/grnhome.gif
%{ooodir}/share/gallery/www-graf/grninfo.gif
%{ooodir}/share/gallery/www-graf/grnleft.gif
%{ooodir}/share/gallery/www-graf/grnmail.gif
%{ooodir}/share/gallery/www-graf/grnminus.gif
%{ooodir}/share/gallery/www-graf/grnplus.gif
%{ooodir}/share/gallery/www-graf/grnquest.gif
%{ooodir}/share/gallery/www-graf/grnright.gif
%{ooodir}/share/gallery/www-graf/grnup.gif
%{ooodir}/share/gallery/www-graf/gryat.gif
%{ooodir}/share/gallery/www-graf/gryback.gif
%{ooodir}/share/gallery/www-graf/grydisk.gif
%{ooodir}/share/gallery/www-graf/grydown.gif
%{ooodir}/share/gallery/www-graf/gryhome.gif
%{ooodir}/share/gallery/www-graf/gryinfo.gif
%{ooodir}/share/gallery/www-graf/gryleft.gif
%{ooodir}/share/gallery/www-graf/grymail.gif
%{ooodir}/share/gallery/www-graf/gryminus.gif
%{ooodir}/share/gallery/www-graf/gryplus.gif
%{ooodir}/share/gallery/www-graf/gryquest.gif
%{ooodir}/share/gallery/www-graf/gryright.gif
%{ooodir}/share/gallery/www-graf/gryup.gif
%{ooodir}/share/gallery/www-graf/men@work.gif
%{ooodir}/share/gallery/www-graf/orgat.gif
%{ooodir}/share/gallery/www-graf/orgback.gif
%{ooodir}/share/gallery/www-graf/orgdisk.gif
%{ooodir}/share/gallery/www-graf/orgdown.gif
%{ooodir}/share/gallery/www-graf/orghome.gif
%{ooodir}/share/gallery/www-graf/orginfo.gif
%{ooodir}/share/gallery/www-graf/orgleft.gif
%{ooodir}/share/gallery/www-graf/orgmail.gif
%{ooodir}/share/gallery/www-graf/orgminus.gif
%{ooodir}/share/gallery/www-graf/orgplus.gif
%{ooodir}/share/gallery/www-graf/orgquest.gif
%{ooodir}/share/gallery/www-graf/orgright.gif
%{ooodir}/share/gallery/www-graf/orgup.gif
%{ooodir}/share/gallery/www-graf/redat.gif
%{ooodir}/share/gallery/www-graf/redback.gif
%{ooodir}/share/gallery/www-graf/reddisk.gif
%{ooodir}/share/gallery/www-graf/reddown.gif
%{ooodir}/share/gallery/www-graf/redhome.gif
%{ooodir}/share/gallery/www-graf/redinfo.gif
%{ooodir}/share/gallery/www-graf/redleft.gif
%{ooodir}/share/gallery/www-graf/redmail.gif
%{ooodir}/share/gallery/www-graf/redminus.gif
%{ooodir}/share/gallery/www-graf/redplus.gif
%{ooodir}/share/gallery/www-graf/redquest.gif
%{ooodir}/share/gallery/www-graf/redright.gif
%{ooodir}/share/gallery/www-graf/redup.gif
%{ooodir}/share/gallery/www-graf/turdown.gif
%{ooodir}/share/gallery/www-graf/turhome.gif
%{ooodir}/share/gallery/www-graf/turleft.gif
%{ooodir}/share/gallery/www-graf/turright.gif
%{ooodir}/share/gallery/www-graf/turup.gif
%{ooodir}/share/gallery/www-graf/viohome.gif
%{ooodir}/share/gallery/www-graf/violeft.gif
%{ooodir}/share/gallery/www-graf/vioright.gif
%{ooodir}/share/gallery/www-graf/vioup.gif
%{ooodir}/share/gallery/www-graf/ylwdown.gif
%{ooodir}/share/gallery/www-graf/ylwhome.gif
%{ooodir}/share/gallery/www-graf/ylwleft.gif
%{ooodir}/share/gallery/www-graf/ylwmail.gif
%{ooodir}/share/gallery/www-graf/ylwright.gif
%{ooodir}/share/gallery/www-graf/ylwup.gif

%files pyuno -f file-lists/pyuno_list.txt

%files extension-diagram
%{ooodir}/share/extensions/Diagram

%files extension-converttexttonumber
%{ooodir}/share/extensions/ConvertTextToNumber

%files extension-barcode
%{ooodir}/share/extensions/Barcode

%files extension-languagetool
%{ooodir}/share/extensions/LanguageTool

%files extension-validator
%{ooodir}/share/extensions/Validator

%files extension-xsltfilter -f file-lists/dtd_list.txt
%{ooodir}/share/registry/xsltfilter.xcd
%{ooodir}/share/xslt/docbook
%{ooodir}/share/xslt/export/xhtml
%{_datadir}/applications/libreoffice-xsltfilter.desktop

%files extension-typo
%{ooodir}/share/extensions/typo

%files extension-numbertext
%{ooodir}/share/extensions/numbertext

%files extension-nlpsolver
%{ooodir}/share/extensions/nlpsolver

%files extension-hunart
%{ooodir}/share/extensions/hunart

%files extension-gdocs
%{ooodir}/share/extensions/gdocs

%files extension-watchwindow
%{ooodir}/share/extensions/WatchWindow

%files extension-mysql
%{ooodir}/share/extensions/mysql-connector-ooo

%files mailmerge -f file-lists/mailmerge_list.txt

%files style-galaxy
%{ooodir}/share/config/images.zip

%files style-crystal
%{ooodir}/share/config/images_crystal.zip

%files style-hicontrast
%{ooodir}/share/config/images_hicontrast.zip

%files style-tango
%{ooodir}/share/config/images_tango.zip

%files style-oxygen
%{ooodir}/share/config/images_oxygen.zip

%files writer -f file-lists/writer_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-writer_72.svg
%{_mandir}/man1/loweb*
%{_mandir}/man1/lowriter*

%files wiki-publisher
%{ooodir}/share/extensions/wiki-publisher

%files presentation-minimizer
%{ooodir}/share/extensions/presentation-minimizer

%files postgresql
%{ooodir}/program/libpostgresql-sdbclo.so
%{ooodir}/program/libpostgresql-sdbc-impllo.so
%{ooodir}/program/postgresql-sdbc.ini
%{ooodir}/program/services/postgresql-sdbc.rdb
%{ooodir}/share/registry/postgresqlsdbc.xcd

%if %{with l10n}
%{expand:%(for i in %{langs}; do
	[ "$i" = "en-US" ] && continue;
	i=`echo $i |sed -e 's,-,_,g'`;
	[ "$i" = "sh" ] && echo "%%files l10n-shs -f file-lists/lang_${i}_list.txt" || echo "%%files l10n-$i -f file-lists/lang_${i}_list.txt";
done)}
%endif

%{expand:%(for i in %{helplangs}; do
	l=`echo $i |sed -e 's,-,_,g'`;
	echo "%%files help-$l -f file-lists/help_${l}_list.txt";
	echo "%%_libdir/libreoffice/help/$i";
done)}

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
%{ooodir}/share/template/common/officorr
%{ooodir}/share/template/common/offimisc
%{ooodir}/share/template/common/personal
%{ooodir}/share/template/common/presnt

%files templates-cs
%{ooodir}/share/template/cs

%files templates-de
%{ooodir}/share/template/de
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_de

%files templates-en_US
%{ooodir}/share/template/en-US
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_en-US

%files templates-es
%{ooodir}/share/template/es
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_es

%files templates-fi
%{ooodir}/share/template/fi

%files templates-fr
%{ooodir}/share/template/fr
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_fr

%files templates-hu
%{ooodir}/share/template/hu
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_hu

%files templates-it
%{ooodir}/share/template/it
%{ooodir}/share/extensions/Sun_ODF_Template_Pack_it

%files templates-ja
%{ooodir}/share/template/ja

%files templates-nl
%{ooodir}/share/template/nl

%files templates-pl
%{ooodir}/share/template/pl

%files templates-pt_BR
%{ooodir}/share/template/pt-BR

%files templates-sv
%{ooodir}/share/template/sv

%files templates-tr
%{ooodir}/share/template/tr

%files templates-zh_CN
%{ooodir}/share/template/zh-CN
