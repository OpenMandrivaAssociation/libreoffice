%define _enable_debug_packages %{nil}
%define debug_package %{nil}
%define _binary_payload w1.xzdio
%define _source_payload w1.xzdio

%define l10n	1
%{?_with_l10n: %global l10n 1}
%{?_without_l10n: %global l10n 0}
%if %l10n
%define langs	"en-US af ar as bg bn br bs ca cs cy da de dz el en-GB es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai mk ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-TW zh-CN zu"
%else
%define langs	"en-US"
%endif

%define javaless 0
# As of 4.0, doesn't work -- probably the extensions need porting
%define extensionenabled 1

%define relurl		http://download.documentfoundation.org/libreoffice/src/%{version}
%define devurl		http://dev-www.libreoffice.org/ooo_external
%define distroname	Mandriva
%define	ooname		libreoffice
%define buildver	%{version}.1
%define ooodir		%{_libdir}/libreoffice
%define firefox_plugin	libnpsoplugin.so
%define antpath		%{_builddir}/libreoffice-%{version}/apache-ant-1.8.1
#define unopkg		%{_bindir}/unopkg

%define use_icecream    0	
%{?_with_icecream: %global use_icecream 1}
%{?_without_icecream: %global use_icecream 0}

%define use_ccache	0
%define ccachedir	~/.ccache-OOo
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}

%if %{_use_internal_dependency_generator}
%define __noautoreq libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libmono.so\\|mono
%define __noautoprov libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1
%else
%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libmono.so\\|mono
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1
%endif

Summary:	Office suite 
Name:		libreoffice
Epoch:		1
Version:	4.1.0
Release:	1
License:	(MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic
Group:		Office
Url:		http://www.libreoffice.org
Source0:	%{relurl}/%{ooname}-%{buildver}.tar.xz
Source1:	%{relurl}/%{ooname}-dictionaries-%{buildver}.tar.xz
Source2:	%{relurl}/%{ooname}-help-%{buildver}.tar.xz
Source3:	%{relurl}/%{ooname}-translations-%{buildver}.tar.xz
Source10:	Mandriva-Rosa_Icons.tar.bz2
#javaless
%if %{javaless}
Source20:	http://archive.apache.org/dist/ant/binaries/apache-ant-1.8.1-bin.tar.bz2
Source30:	%{devurl}/af3c3acf618de6108d65fcdc92b492e1-commons-codec-1.3-src.tar.gz
Source31:	%{devurl}/2c9b0f83ed5890af02c0df1c1776f39b-commons-httpclient-3.1-src.tar.gz 
Source32:	%{devurl}/2ae988b339daec234019a7066f96733e-commons-lang-2.3-src.tar.gz 
Source33:	%{devurl}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
%endif
# External Download Sources
Source40:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz
Source100:	libreoffice.rpmlintrc

Patch0:		libreoffice-4.1.0.1-non-fatal-error-during-test.patch
Patch1:		libreoffice-3.5.2.2-icu-49.patch
Patch2:		help-images-mdv64789.patch

%if %{use_icecream}
BuildRequires:	icecream
%endif
%if %{use_ccache}
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
BuildRequires:	pentaho-libxml
BuildRequires:	pentaho-reporting-flow-engine
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	python-translate >= 1.9.0
BuildRequires:	servlet
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
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(icu-le)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libclucene-core)
BuildRequires:	pkgconfig(libcmis-0.3)
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
BuildRequires:	hsqldb
BuildRequires:	jakarta-commons-codec
BuildRequires:	jakarta-commons-lang
BuildRequires:	jakarta-commons-httpclient
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
Suggests:	%{name}-dtd-officedocument1.0 = %{EVRD}
%if %extensionenabled
Suggests:	%{name}-pdfimport = %{EVRD}
%endif
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
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
# Heavy java deps
%if !%{javaless}
Requires:	hsqldb
%endif
Suggests:	%{name}-java-common = %{EVRD}
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
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-calc < 1:3.3-1:2011.0 

%description calc
This package contains the spreadsheet component for LibreOffice.

%package common
Summary:	LibreOffice office suite architecture independent files
Group:		Office
# Require the architecture dependant stuff
Requires:	%{name}-core = %{EVRD}
# Require at least one style to be installed
Requires:	%{name}-style = %{EVRD}
# Also suggest java-common, as it may be used by some macros
Suggests:	%{name}-java-common = %{EVRD}
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

# Upstream dropped this packages in 3.4
Obsoletes:	%{name}-l10n-pt_AO = 1:3.3.2-1
Obsoletes:	%{name}-help-pt_AO = 1:3.3.2-1
Obsoletes:	%{name}-help-ta    = 1:3.3.2-1
Obsoletes:	%{name}-help-zu    = 1:3.3.2-1
Obsoletes:	%{name}-help-cy    = 1:3.3.2-1
Obsoletes:	%{name}-help-ar    = 1:3.3.2-1
Obsoletes:	%{name}-help-af    = 1:3.3.2-1
Obsoletes:	%{name}-help-br    = 1:3.3.2-1

%description common
This package contains the architecture-independent files of LibreOffice.

%package core
Summary:	LibreOffice office suite architecture dependent files
Group:		Office
# binfilter has been removed in 4.0
Obsoletes:	%{name}-filter-binfilter < %{EVRD}
Obsoletes:	openoffice.org-core < 1:3.3-1:2011.0 

%description core
This package contains the architecture-dependent core files of LibreOffice.
See the libreoffice package for more information.

%package devel
Summary:	LibreOffice SDK - development files
Group:		Office
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
%if "%{_lib}" == "lib64"
Provides:	devel(libxmlreader(64bit)) = %{EVRD}
Provides:	devel(libreg(64bit)) = %{EVRD}
%else
Provides:	devel(libxmlreader) = %{EVRD}
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
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-draw < 1:3.3-1:2011.0 

%description draw
This package contains the drawing component for LibreOffice.

%package dtd-officedocument1.0
Group:		Office
Summary:	OfficeDocument 1.0 DTD

%description dtd-officedocument1.0
This package contains the Document Type Definition (DTD) of the LibreOffice
1.x(!) XML file format.

%package gnome
Group:		Office
Summary:	GNOME Integration for LibreOffice (VFS, GConf)
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-core = %{EVRD}
Obsoletes:	openoffice.org-gnome < 1:3.3-1:2011.0 

%description gnome
This package contains the GNOME VFS support and a GConf backend.

%package impress
Group:		Office
Summary:	LibreOffice office suite - presentation
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD} 
Requires:	%{name}-draw = %{EVRD}
Obsoletes:	openoffice.org-impress < 1:3.3-1:2011.0 

%description impress
This package contains the presentation component for LibreOffice.

%package kde4
Group:		Office
Summary:	KDE4 Integration for LibreOffice (Widgets, Dialogs, Addressbook)
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-core = %{EVRD}
Suggests:	%{name}-style-oxygen = %{EVRD} 
Obsoletes:	openoffice.org-kde4 < 1:3.3-1:2011.0 

%description kde4
This package contains the KDE4 plugin for drawing LibreOffice widgets with
KDE4/Qt4.x and a KDEish File Picker when running under KDE4.
 
%package java-common
Group:		Office
Summary:	LibreOffice office suite Java support arch. independent files
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	java
Requires:	bsh
Obsoletes:	openoffice.org-java-common < 1:3.3-1:2011.0 

%description java-common
This package contains the architecture-independent files of the Java support
for LibreOffice (Java classes, scripts, config snippets).

Also contains the LibreOffice Office Bean for embedding LibreOffice in
custom Java applications.

%package math
Group:		Office
Summary:	LibreOffice office suite - equation editor
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-math < 1:3.3-1:2011.0 

%description math
This package contains the equation editor component for LibreOffice.

%package openclipart
Group:		Office
Summary:	LibreOffice Open Clipart data
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-openclipart < 1:3.3-1:2011.0 

%description openclipart
This package contains the LibreOffice Open Clipart data, including images
and sounds.

%package pyuno
Group:		Office
Summary:	Python bindings for UNO library
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-pyuno < 1:3.3-1:2011.0 

%description pyuno
This package contains the Python bindings for the UNO library.

%package style-galaxy
Group:		Office
Summary:	Default symbol style for LibreOffice
Requires:	%{name}-core = %{EVRD}
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
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-crystal < 1:3.3-1:2011.0 

%description style-crystal
This package contains the "crystal" symbol style, default style for KDE.

%package style-hicontrast
Group:		Office
Summary:	Hicontrast symbol style for LibreOffice
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-hicontrast < 1:3.3-1:2011.0 

%description style-hicontrast
This package contains the "hicontrast" symbol style, needs to be manually
enabled in the LibreOffice option menu.

%package style-tango
Group:		Office
Summary:	Tango symbol style for LibreOffice
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-tango < 1:3.3-1:2011.0 

%description style-tango
This package contains the "tango" symbol style, default style for GTK/Gnome.

%package style-oxygen
Group:		Office
Summary:	Oxygen symbol style for LibreOffice
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Provides:	%{name}-style = %{EVRD}
Obsoletes:	openoffice.org-style-oxygen < 1:3.3-1:2011.0 

%description style-oxygen
This package contains the "oxygen" symbol style, default style for KDE4.

%package writer
Group:		Office
Summary:	LibreOffice office suite - word processor
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Obsoletes:	openoffice.org-writer < 1:3.3-1:2011.0 

%description writer
This package contains the wordprocessor component for LibreOffice.

%if %extensionenabled
%package pdfimport
Group:		Office
Summary:	LibreOffice office suite - PDF Import extension
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-draw = %{EVRD}
Obsoletes:	openoffice.org-pdfimport < 1:3.3-1:2011.0 

%description pdfimport
PDF import extension enables PDF documments importing and basic editing of PDF
documments by using LibreOffice-draw application.

%package presenter-screen
Group:		Office
Summary:	LibreOffice office suite - Presenter Screen extension
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-impress = %{EVRD}
Obsoletes:	openoffice.org-presenter-screen < 1:3.3-1:2011.0 
Conflicts:	%{name}-presenter-screen <= 1:3.2-rc4.0

%description presenter-screen
Presenter Screen extension helps users to see upcoming slides and slide notes
of presentations inside a second view not visible for the spectators.

%package report-builder
Group:		Office
Summary:	LibreOffice office suite - Report Builder extension
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-base = %{EVRD}

%description report-builder
By using %{name}-base the Report Builder extesion enables creating of smart and 
professional looking reports. Further the reports can be exported to PDF or 
OpenDocuments formats.

%package wiki-publisher
Group:		Office
Summary:	LibreOffice office suite - Wiki Publisher extension
Requires:	%{name}-core = %{EVRD}
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

%package presentation-minimizer
Group:		Office
Summary:	LibreOffice office suite - Presentation Minimizer extension
Requires:	%{name}-core = %{EVRD}
Requires:	%{name}-common = %{EVRD}
Requires:	%{name}-impress = %{EVRD}
Obsoletes:	openoffice.org-presentation-minimizer < 1:3.3-1:2011.0 

%description presentation-minimizer
With Presentation Minimizer extesion is possible to reduce the file size 
of the presentation by compressing images and removing data not needed in 
a automatizated way.

Note: The Presentation Minimizer also works on 
Microsoft PowerPoint presentations. 
%endif

%package postgresql
Summary:	PostgreSQL connector for LibreOffice
Group:		Office
Requires:	%{name}-base = %{EVRD}

%description postgresql
A PostgreSQl connector for the database front-end for LibreOffice. Allows
creation and management of PostgreSQL databases through a GUI.

%if %l10n
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
Requires:	fonts-ttf-korean >= 2.1
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

%package l10n-qtz
Summary:	QTZ language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	urw-fonts
Provides:	LibreOffice-l10n_qtz = %{EVRD}
Suggests:	%{ooname}-help-qtz = %{EVRD} 

%description l10n-qtz
This package contains the localization of LibreOffice in QTZ.

It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

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
Suggests:	%{ooname}-help-shs = %{EVRD} 

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

%package help-qtz
Summary:	QTZ help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-qtz = %{EVRD}
Provides:	LibreOffice-help-qtz = %{EVRD}

%description help-qtz
This package contains the localized help files of LibreOffice in QTZ

%package help-ro
Summary:	Romanian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ro = %{EVRD}
Provides:	LibreOffice-help-ro = %{EVRD}

%description help-ro
This package contains the localized help files of LibreOffice in Romanian.

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

%if !%{use_icecream}
# sbin due to icu stuff there
#PATH=/bin:/usr/bin:/usr/X11R6/bin:$QTPATH:/usr/sbin:$PATH
PATH=$PATH:/usr/sbin
export PATH
%endif

%if %{use_ccache}
export CCACHE_DIR=%{ccachedir}
%endif

export ARCH_FLAGS="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CC="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="%{optflags} -O2"

echo "Configure start at: "`date` >> ooobuildtime.log 

ENVCFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing" \
ENVCXXFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden " \
#./autogen.sh \
# 	--prefix=%{_prefix} \
#	--exec-prefix=%{_prefix} \
#	--bindir=%{_bindir} \
#	--sbindir=%{_sbindir} \
#	--sysconfdir=%{_sysconfdir} \
#	--datadir=%{_datadir} \
#	--includedir=%{_includedir} \
#	--libdir=%{_libdir} \
#	--libexecdir=%{_libdir} \
#	--localstatedir=/var \
#	--mandir=%{_mandir} \
#	--infodir=%{_infodir} \
touch autogen.lastrun
%configure2_5x \
	--with-distro=%{distroname} \
	--with-vendor=Mandriva \
	%{?_smp_mflags:--with-parallelism="`getconf _NPROCESSORS_ONLN`"} \
	--with-build-version="%{buildver}" \
	--disable-fetch-external \
	--disable-gstreamer-0.10 \
	--enable-gstreamer \
	--disable-kde \
	--enable-kde4 \
	--enable-lockdown \
	--enable-opengl \
	--enable-odk \
	--enable-split-app-modules \
  	--enable-split-opt-features \
	--enable-telepathy \
	--without-fonts \
	--without-junit \
%if %{javaless}
	--with-ant-home="%{antpath}" \
%endif
	--with-lang=%{langs} \
	--without-myspell-dicts \
	--with-system-dicts \
	--with-external-dict-dir=%{_datadir}/dict/ooo \
	--with-external-hyph-dir=%{_datadir}/dict/ooo \
	--with-external-thes-dir=%{_datadir}/dict/ooo \
	--with-system-libs \
	--with-system-ucpp \
%if !%extensionenabled
	--disable-ext-presenter-minimizer \
%else
	--enable-ext-wiki-publisher \
	--with-servlet-api-jar=/usr/share/java/tomcat6-servlet-2.5-api.jar \
%endif
%if %{use_ccache} && !%{use_icecream}
	--with-gcc-speedup=ccache \
%else
 %if !%{use_ccache} && %{use_icecream}
	--with-gcc-speedup=icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
 %else
  %if %{use_ccache} && %{use_icecream}
	--with-gcc-speedup=ccache,icecream \
	--with-max-jobs=10 \
	--with-icecream-bindir=%{_libdir}/icecc/bin
  %endif
 %endif
%endif

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
%if %{javaless}
ln -sf %{SOURCE30} src/
ln -sf %{SOURCE31} src/
ln -sf %{SOURCE32} src/
ln -sf %{SOURCE33} src/
%endif
ln -sf %{SOURCE40} src/
touch src.downloaded

make \
	ARCH_FLAGS="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="%{optflags} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="%{optflags} -O2" 

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

# # (Review)
# # desktop files
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --add-mime-type="application/vnd.ms-works;application/x-msworks-wp;zz-application/zz-winassoc-wps" \
#   --add-mime-type="application/vnd.openxmlformats-officedocument.wordprocessingml.document" \
#   --add-mime-type="application/vnd.ms-word.document.macroEnabled.12" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/writer*desktop
# 
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --add-mime-type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
#   --add-mime-type="application/vnd.ms-excel.sheet.macroEnabled.12" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/calc*desktop
# 
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --remove-category="Graphics" \
#   --remove-category="VectorGraphics" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/draw*desktop
# 
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --add-mime-type="application/vnd.openxmlformats-officedocument.presentationml.presentation" \
#   --add-mime-type="application/vnd.ms-powerpoint.presentation.macroEnabled.12" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/impress*desktop
# 
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/math*desktop
# 
# # desktop-file-install --vendor="" \
# #   --remove-category="Application" \
# #   --remove-category="Network" \
# #   --remove-category="WebDevelopment" \
# #   --add-category="Office" \
# #   --add-category="X-MandrivaLinux-CrossDesktop" \
# #   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/web*desktop
# # #  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/web*desktop
# 
# # libre
# # desktop-file-install --vendor="" \
# #   --remove-category="Application" \
# #   --add-category="Office" \
# #   --add-category="X-MandrivaLinux-CrossDesktop" \
# #   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/template*desktop
# # #  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/template*desktop
# 
# desktop-file-install --vendor="" \
#   --remove-category="Application" \
#   --remove-category="Database" \
#   --add-category="Office" \
#   --add-category="X-MandrivaLinux-CrossDesktop" \
#   --dir %{buildroot}%{_datadir}/applications %{buildroot}%{ooodir}/share/xdg/base*desktop

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

%if %extensionenabled
# # copy extensions 
# install -d -m755 %{buildroot}%{ooodir}/extensions
# cp %{_builddir}/libreoffice-%{version}/solver/unxlng*/bin/pdfimport/pdfimport.oxt %{buildroot}%{ooodir}/extensions/
# cp %{_builddir}/libreoffice-%{version}/solver/unxlng*/bin/presenter/presenter-screen.oxt %{buildroot}%{ooodir}/extensions/
# cp %{_builddir}/libreoffice-%{version}/solver/unxlng*/bin/wiki-publisher.oxt %{buildroot}%{ooodir}/extensions/
# cp %{_builddir}/libreoffice-%{version}/solver/unxlng*/bin/minimizer/presentation-minimizer.oxt %{buildroot}%{ooodir}/extensions/
%endif

## Installation fixes
## remove fix wrong manpages files, extension gz->xz
for p in common base calc writer impress draw math; do
	sed -i '/^.*man.*\.gz$/d' file-lists/${p}_list.txt 
done;

## drop GTK dependency from -core
sed -i -e '/^.*libqstart_gtklo.so$/d' file-lists/core_list.txt
sed -i -e '/^.*pluginapp.bin$/d' file-lists/core_list.txt
echo '%{ooodir}/program/libqstart_gtklo.so' >>file-lists/gnome_list.txt
echo '%{ooodir}/program/pluginapp.bin' >>file-lists/gnome_list.txt
## GConf too
sed -i -e '/^.*gconfbe1.uno.so$/d' file-lists/core_list.txt
echo '%{ooodir}/program/gconfbe1.uno.so' >>file-lists/gnome_list.txt

## sort removing duplicates
sort -u file-lists/gnome_list.txt > file-lists/gnome_list.uniq.sorted.txt 
sort -u file-lists/sdk_list.txt   > file-lists/sdk_list.uniq.sorted.txt 

# Fix weirdo filenames wreaking havoc because they're regular expressions
sed -i -e 's/\[/?/g;s/\]/?/g' file-lists/sdk*.txt

## oxygen should be in the style
sed -i '/^.*images_oxygen\.zip$/d' file-lists/common_list.txt 
## merge en-US with common
cat file-lists/lang_en_US_list.txt >> file-lists/common_list.txt
sort -u file-lists/common_list.txt >  file-lists/common_list.uniq.sorted.txt 

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

%if %extensionenabled
# %post pdfimport
# # upgrade 
# if [ $1 -ge 2 ];then
# 	# removes old installed pdfimport extension 
# 	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
# 	if [ "z$idpdfimport" != "z" ]; then
# 		%unopkg remove --shared $idpdfimport 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
# 
# #install new pdfimport version
# %unopkg add --shared %{ooodir}/extensions/pdfimport.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 
# 
# #uninstall
# %preun pdfimport 
# if [ $1 -eq 0 ];then
# 	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
# 	if [ "z$idpdfimport" != "z" ]; then
# 		%unopkg remove --shared $idpdfimport 2> /dev/null
# 		#clean footprint cache
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
# 
# %post presenter-screen
# # upgrade 
# if [ $1 -ge 2 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
# #install 
# %unopkg add --shared %{ooodir}/extensions/presenter-screen.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 
# 
# 
# %preun presenter-screen
# if [ $1 -eq 0 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi

# %post wiki-publisher
# # upgrade 
# if [ $1 -ge 2 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi	
# #install 
# %unopkg add --shared %{ooodir}/extensions/wiki-publisher.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 
# 
# %preun wiki-publisher
# if [ $1 -eq 0 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
# 
# %post presentation-minimizer
# # upgrade 
# if [ $1 -ge 2 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
# #install 
# %unopkg add --shared %{ooodir}/extensions/sun-presentation-minimizer.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 
# 
# %preun presentation-minimizer
# if [ $1 -eq 0 ];then
# 	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
# 	if [ "z$idextension" != "z" ]; then
# 		%unopkg remove --shared $idextension 2> /dev/null
# 		%unopkg list --shared &> /dev/null
# 	fi
# fi
%endif

%files

%files base -f file-lists/base_list.txt
%{_mandir}/man1/lobase*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-base_72.svg

%files calc -f file-lists/calc_list.txt
%{_mandir}/man1/localc*
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-calc_72.svg

%files common -f file-lists/common_list.uniq.sorted.txt 
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo_72.svg
%{_mandir}/man1/loffice*
%{_mandir}/man1/lofromtemplate*
%{_mandir}/man1/libreoffice*
%{_mandir}/man1/unopkg.1*

%files core -f file-lists/core_list.txt

%files devel -f file-lists/sdk_list.uniq.sorted.txt

%files devel-doc -f file-lists/sdk_doc_list.txt

%files draw -f file-lists/draw_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-draw_72.svg
%{_mandir}/man1/lodraw*

%files dtd-officedocument1.0 -f file-lists/dtd_list.txt

%files gnome -f file-lists/gnome_list.uniq.sorted.txt

%files impress -f file-lists/impress_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-impress_72.svg
%{_mandir}/man1/loimpress*

%files java-common -f file-lists/java_common_list.txt
%{_libdir}/libreoffice/program/classes/ScriptProviderForBeanShell.jar
#{_libdir}/libreoffice/program/classes/bsh.jar
%{_libdir}/libreoffice/program/services/scriptproviderforbeanshell.rdb

%files kde4 -f file-lists/kde4_list.txt

%files math -f file-lists/math_list.txt
%{_iconsdir}/hicolor/scalable/apps/mandriva-rosa-lo-math_72.svg
%{_mandir}/man1/lomath*

%files openclipart -f file-lists/gallery_list.txt

%files pyuno -f file-lists/pyuno_list.txt

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

%if %extensionenabled
%files pdfimport
%{ooodir}/share/extensions/pdfimport

%files presenter-screen
%{ooodir}/share/extensions/presenter-screen

%files report-builder
%{ooodir}/share/extensions/report-builder

%files wiki-publisher
%{ooodir}/share/extensions/wiki-publisher

%files presentation-minimizer
%{ooodir}/share/extensions/presentation-minimizer

%endif

%files postgresql
%{ooodir}/program/postgresql-sdbc.uno.so
%{ooodir}/program/postgresql-sdbc-impl.uno.so
%{ooodir}/program/postgresql-sdbc.ini
%{ooodir}/program/services/postgresql-sdbc.rdb
%{ooodir}/share/registry/postgresqlsdbc.xcd

%if %l10n
%files l10n-it -f file-lists/lang_it_list.txt

%files l10n-af -f file-lists/lang_af_list.txt

%files l10n-ar -f file-lists/lang_ar_list.txt

%files l10n-as -f file-lists/lang_as_list.txt

%files l10n-bg -f file-lists/lang_bg_list.txt

%files l10n-bn -f file-lists/lang_bn_list.txt

%files l10n-br -f file-lists/lang_br_list.txt

%files l10n-bs -f file-lists/lang_bs_list.txt

%files l10n-ca -f file-lists/lang_ca_list.txt

%files l10n-cs -f file-lists/lang_cs_list.txt

%files l10n-cy -f file-lists/lang_cy_list.txt

%files l10n-da -f file-lists/lang_da_list.txt

%files l10n-de -f file-lists/lang_de_list.txt

%files l10n-dz -f file-lists/lang_dz_list.txt

%files l10n-el -f file-lists/lang_el_list.txt

%files l10n-en_GB -f file-lists/lang_en_GB_list.txt

%files l10n-es -f file-lists/lang_es_list.txt

%files l10n-et -f file-lists/lang_et_list.txt

%files l10n-eu -f file-lists/lang_eu_list.txt

%files l10n-fa -f file-lists/lang_fa_list.txt

%files l10n-fi -f file-lists/lang_fi_list.txt

%files l10n-fr -f file-lists/lang_fr_list.txt

%files l10n-ga -f file-lists/lang_ga_list.txt

%files l10n-gl -f file-lists/lang_gl_list.txt

%files l10n-gu -f file-lists/lang_gu_list.txt

%files l10n-he -f file-lists/lang_he_list.txt

%files l10n-hi -f file-lists/lang_hi_list.txt

%files l10n-hr -f file-lists/lang_hr_list.txt

%files l10n-hu -f file-lists/lang_hu_list.txt

%files l10n-ja -f file-lists/lang_ja_list.txt

%files l10n-kn -f file-lists/lang_kn_list.txt

%files l10n-ko -f file-lists/lang_ko_list.txt

%files l10n-lt -f file-lists/lang_lt_list.txt

%files l10n-lv -f file-lists/lang_lv_list.txt

%files l10n-mai -f file-lists/lang_mai_list.txt

%files l10n-ml -f file-lists/lang_ml_list.txt

%files l10n-mk -f file-lists/lang_mk_list.txt

%files l10n-mr -f file-lists/lang_mr_list.txt

%files l10n-nb -f file-lists/lang_nb_list.txt

%files l10n-nl -f file-lists/lang_nl_list.txt

%files l10n-nn -f file-lists/lang_nn_list.txt

%files l10n-nr -f file-lists/lang_nr_list.txt

%files l10n-nso -f file-lists/lang_nso_list.txt

%files l10n-or -f file-lists/lang_or_list.txt

%files l10n-pa_IN -f file-lists/lang_pa_IN_list.txt

%files l10n-pl -f file-lists/lang_pl_list.txt

%files l10n-pt -f file-lists/lang_pt_list.txt

%files l10n-pt_BR -f file-lists/lang_pt_BR_list.txt

%files l10n-qtz -f file-lists/lang_qtz_list.txt

%files l10n-ro -f file-lists/lang_ro_list.txt

%files l10n-ru -f file-lists/lang_ru_list.txt

%files l10n-shs -f file-lists/lang_sh_list.txt

%files l10n-si -f file-lists/lang_si_list.txt

%files l10n-sk -f file-lists/lang_sk_list.txt

%files l10n-sl -f file-lists/lang_sl_list.txt

%files l10n-sr -f file-lists/lang_sr_list.txt

%files l10n-ss -f file-lists/lang_ss_list.txt

%files l10n-st -f file-lists/lang_st_list.txt

%files l10n-sv -f file-lists/lang_sv_list.txt

%files l10n-ta -f file-lists/lang_ta_list.txt

%files l10n-te -f file-lists/lang_te_list.txt

%files l10n-th -f file-lists/lang_th_list.txt

%files l10n-tn -f file-lists/lang_tn_list.txt

%files l10n-tr -f file-lists/lang_tr_list.txt

%files l10n-ts -f file-lists/lang_ts_list.txt

%files l10n-uk -f file-lists/lang_uk_list.txt

%files l10n-ve -f file-lists/lang_ve_list.txt

%files l10n-xh -f file-lists/lang_xh_list.txt

%files l10n-zh_CN -f file-lists/lang_zh_CN_list.txt

%files l10n-zh_TW -f file-lists/lang_zh_TW_list.txt

%files l10n-zu -f file-lists/lang_zu_list.txt

%files help-bg -f file-lists/help_bg_list.txt

%files help-bn -f file-lists/help_bn_list.txt

%files help-bs -f file-lists/help_bs_list.txt

%files help-ca -f file-lists/help_ca_list.txt

%files help-cs -f file-lists/help_cs_list.txt

%files help-da -f file-lists/help_da_list.txt

%files help-de -f file-lists/help_de_list.txt

%files help-dz -f file-lists/help_dz_list.txt

%files help-el -f file-lists/help_el_list.txt

%files help-en_GB -f file-lists/help_en_GB_list.txt

%files help-es -f file-lists/help_es_list.txt

%files help-et -f file-lists/help_et_list.txt

%files help-eu -f file-lists/help_eu_list.txt

%files help-fi -f file-lists/help_fi_list.txt

%files help-fr -f file-lists/help_fr_list.txt

%files help-gl -f file-lists/help_gl_list.txt

%files help-gu -f file-lists/help_gu_list.txt

%files help-he -f file-lists/help_he_list.txt

%files help-hi -f file-lists/help_hi_list.txt

%files help-hr -f file-lists/help_hr_list.txt

%files help-hu -f file-lists/help_hu_list.txt

%files help-it -f file-lists/help_it_list.txt

%files help-ja -f file-lists/help_ja_list.txt

%files help-ko -f file-lists/help_ko_list.txt

%files help-mk -f file-lists/help_mk_list.txt

%files help-nb -f file-lists/help_nb_list.txt

%files help-nl -f file-lists/help_nl_list.txt

%files help-nn -f file-lists/help_nn_list.txt

%files help-pl -f file-lists/help_pl_list.txt

%files help-pt -f file-lists/help_pt_list.txt

%files help-pt_BR -f file-lists/help_pt_BR_list.txt

%files help-qtz -f file-lists/help_qtz_list.txt

%files help-ro -f file-lists/help_ro_list.txt

%files help-ru -f file-lists/help_ru_list.txt

%files help-si -f file-lists/help_si_list.txt

%files help-sk -f file-lists/help_sk_list.txt

%files help-sl -f file-lists/help_sl_list.txt

%files help-sv -f file-lists/help_sv_list.txt

%files help-tr -f file-lists/help_tr_list.txt

%files help-uk -f file-lists/help_uk_list.txt

%files help-zh_CN -f file-lists/help_zh_CN_list.txt

%files help-zh_TW -f file-lists/help_zh_TW_list.txt

%files help-en_US -f file-lists/help_en_US_list.txt
%endif

