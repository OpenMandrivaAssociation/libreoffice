%define debug_package  %{nil}

%define l10n   1
%{?_with_l10n: %global l10n 1}
%{?_without_l10n: %global l10n 0}

%define	ooname		libreoffice
%define name		libreoffice

#define _binary_payload w1.gzdio
#define _binary_payload w9.bzdio
#define _binary_payload w9.lzdio
#define _source_payload w9.bzdio
%define _binary_payload w1.gzdio
%define _source_payload w1.gzdio

%define version	        3.3
%define release		%mkrel 1

%define buildver     	3.3.0.4
%define basis           basis3.3
%define jdkver		1_5_0_11
%define ooodir		%{_libdir}/ooo
%define libdbver	4.2
%if l10n
%define ooolangs	"en-US af ar bg br bs ca cs cy da de el en-GB es et eu fi fr he hi hu it ja ko mk nb nl nn pl pt pt-BR pt-AO ru sk sl sv ta tr zh-TW zh-CN zu"
%else
%define ooolangs	"en-US"
%endif

%define firefox_plugin  libnpsoplugin.so

%define oootarext	bz2

%ifarch x86_64
%define distroname      Mandriva64
%define jdkver          1.4.2
%else
%define distroname      Mandriva
%define jdkver          1_5_0_11
%endif

%ifarch x86_64
%define use_gcj		1
%else
%if %mdkversion >= 200800
%define	use_gcj		1
%else
%define	use_gcj		0
%endif
%endif
%{?_with_gcj: %global use_gcj 1}
%{?_without_gcj: %global use_gcj 0}

%define use_icecream    0	
%{?_with_icecream: %global use_icecream 1}
%{?_without_icecream: %global use_icecream 0}

%define use_ccache	0
%define ccachedir	~/.ccache-OOo
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}

%define use_smp		1
%{?_with_smp: %global use_smp 1}
%{?_without_smp: %global use_smp 0}

%define use_mono	0
%{?_with_mono: %global use_mono 1}
%{?_without_mono: %global use_mono 0}

%define use_openclipart	1
%{?_with_clipart: %global use_openclipart 1}
%{?_without_clipart: %global use_openclipart 0}

%define use_systemdb	1
%{?_with_systemdb: %global use_systemdb 1}
%{?_without_systemdb: %global use_systemdb 0}

%define use_systemboost 1
%{?_with_systemboost: %global use_systemboost 1}
%{?_without_systemboost: %global use_systemboost 0}

# (fix to avoid gcc 4.0.2 produces segfaulting javaldx bin which breaks
# building process)
%define optsafe	""
%define _requires_exceptions libjawt.so\\|libmyspell.so\\|libstlport_gcc.so\\|libmono.so\\|mono
%define _provides_exceptions libsndfile.so\\|libportaudio.so\\|libdb-4.2.so\\|libdb_java-4.2.so\\|libmyspell.so\\|libstlport_gcc.so\\|librdf.so.0\\|libraptor.so.1\\|libxmlsec1-nss.so.1\\|libxmlsec1.so.1

%define unopkg  %{_bindir}/unopkg

Summary:	Office suite 
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.libreoffice.org
License:	LGPL
Group:		Office
Vendor:		Mandriva
Packager:	Rafael da Veiga Cabral <cabral@mandriva.com>
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
# Requres to all our packages
Requires:	%{name}-base = %{EVRD}
Requires:	%{name}-calc = %{EVRD}
Requires:	%{name}-draw = %{EVRD}
Requires:	%{name}-impress = %{EVRD}
Requires:	%{name}-math = %{EVRD}
Requires:	%{name}-writer = %{EVRD}
# Suggests:	%{name}-dtd-officedocument1.0 = %{version}
Suggests: 	%{name}-pdfimport = %{EVRD}
Obsoletes:	OpenOffice.org
Obsoletes:	OpenOffice.org-libs
Obsoletes:	%{ooname}-go-ooo <= %{version}
%ifarch x86_64
Obsoletes:     openoffice.org64 <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo < 3.1-4
%endif
Provides:	LibreOffice
Provides:	LibreOffice-libs
Obsoletes:      openoffice.org < 1:3.3-1:2011.0 
Provides:       openoffice.org = 1:3.3-1:2011.0
# echo %rename openoffice.org
# exit
#Obsoletes: 	openoffice.org < 1:3.2.2
# Provides: 	openoffice.org = %{EVRD}
#
# Requirements for building
#
%if %{use_icecream}
BuildRequires:	icecream
%endif
%if %{use_ccache}
BuildRequires:	ccache
%endif
#
BuildRequires:	automake1.8
BuildRequires:	autoconf
%if %{use_systemboost}
BuildRequires:	boost-devel
%endif
BuildRequires:	bison >= 1.32-2mdk
%if %{use_openclipart}
BuildRequires:	clipart-openclipart
%endif
BuildRequires:	cups-devel
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	ed
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype2-devel >= 2.1.3-3mdk
BuildRequires:	gcc >= 3.2-0.3mdk
BuildRequires:	gcc-c++ >= 3.2-0.3mdk
BuildRequires:	glitz-devel
BuildRequires:	gnutls-devel
BuildRequires:	gnome-vfsmm2.6-devel
BuildRequires:	gperf
BuildRequires:	ImageMagick
BuildRequires:	db1-devel
%if %{use_systemdb}
%if %mdkversion < 201100
# this is pulled by db-devel >= 5.1, and libdbcxx5.1 does not provide libdbcxx at all
BuildRequires:	libdbcxx >= 4.2.5-4mdk
%endif
BuildRequires:	db-devel >= 4.2.5-4mdk
%else
BuildConflicts: libdbjava4.2
%endif
BuildRequires:	bsh
BuildRequires:	libcurl-devel
BuildRequires:	libgtk+2-devel
BuildRequires:	libsvg-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	libxaw-devel
BuildRequires:	libldap-devel
BuildRequires:	libportaudio-devel
BuildConflicts: %{mklibname libportaudio 2}-devel
BuildRequires:	libsndfile-devel
BuildRequires:	unixODBC-devel
BuildRequires:	libwpd-devel
BuildRequires:	libxp-devel
BuildRequires:	libxslt-proc >= 1.0.19
BuildRequires:	libxslt-devel
BuildRequires:	libxml2 >= 2.4.23
%if %{use_mono}
BuildRequires:	mono-devel
BuildRequires:	mono-data-sqlite
%endif
# dev 300 (retirar essa require)
# BuildRequires:	mozilla-firefox-devel
BuildRequires:	nss-devel
BuildRequires:	nas-devel
BuildRequires:	neon-devel >= 0.27
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	python-devel
# BuildRequires:	qt3-devel
BuildRequires:	readline-devel
BuildRequires:	recode
BuildRequires:	sane-devel
BuildRequires:	sharutils
BuildRequires:	startup-notification-devel
%if %{oootarext} == "lzma"
BuildRequires:	lzma
BuildRequires:	tar >= 1.15.1-7mdk
%endif
BuildRequires:	tcsh >= 6.12-2mdk
BuildRequires:	unzip
BuildRequires:	XFree86
BuildRequires:	x11-server-xvfb
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
BuildRequires:	zip
#
# java
%if %{use_gcj}
BuildRequires:	ant
%if %mdkversion >= 200810
BuildRequires:	java-rpmbuild
%else
BuildRequires:	java-1.7.0-icedtea-devel
%define java_home %{_jvmdir}/java-icedtea
%endif
#
BuildRequires:	xml-commons-apis
%else
BuildRequires:	jdk >= %{jdkver}
BuildRequires:	jre >= %{jdkver}
BuildRequires:	j2sdk-ant
BuildConflicts:	gcc-java
BuildConflicts:	gcj-tools
BuildConflicts: java-kaffe
%endif
BuildConflicts:	STLport-devel
BuildRequires:	hsqldb
BuildRequires:	libwpg-devel
BuildRequires:	libwps-devel
BuildRequires:	icu
BuildRequires:	icu-devel
BuildRequires:	libmdbtools-devel
BuildRequires:  ant-apache-regexp
BuildRequires:  xulrunner-devel
BuildRequires:	libvigra-devel
BuildRequires:  hunspell-devel
#pdfimport extension
BuildRequires:	libpoppler-devel
BuildRequires:	libxtst-devel
BuildRequires:  desktop-file-utils
BuildRequires:	mesaglu-devel
BuildRequires:  qt4-devel 
BuildRequires:  task-kde4-devel 
BuildRequires:  cppunit-devel
BuildRequires:  redland-devel
BuildRequires:  jakarta-commons-codec
BuildRequires:  jakarta-commons-lang
BuildRequires:  jakarta-commons-httpclient

####################################################################
#
# Sources
#
####################################################################
Source0:	http://download.documentfoundation.org/libreoffice/src/%{ooname}-build-%{buildver}.tar.%{oootarext}
Source5:	http://download.documentfoundation.org/libreoffice/src/%{ooname}-sdk-%{buildver}.tar.%{oootarext}
Source71:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-ure-%{buildver}.tar.%{oootarext}
Source72:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-base-%{buildver}.tar.%{oootarext}
Source73:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-calc-%{buildver}.tar.%{oootarext}
Source74:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-impress-%{buildver}.tar.%{oootarext}
Source75:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-writer-%{buildver}.tar.%{oootarext}
Source76:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-l10n-%{buildver}.tar.%{oootarext}
Source77:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-artwork-%{buildver}.tar.%{oootarext}
Source78:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-filters-%{buildver}.tar.%{oootarext}
Source79:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-testing-%{buildver}.tar.%{oootarext}
Source80:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-bootstrap-%{buildver}.tar.%{oootarext}
Source81:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-gui-%{buildver}.tar.%{oootarext}
Source82:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-core-%{buildver}.tar.%{oootarext}
Source83:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-extern-%{buildver}.tar.%{oootarext}
Source84:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-extern-sys-%{buildver}.tar.%{oootarext}
Source85:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-components-%{buildver}.tar.%{oootarext}
Source86:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-postprocess-%{buildver}.tar.%{oootarext}
Source91:        http://download.go-oo.org/DEV300/ooo_oxygen_images-2009-06-17.tar.gz
Source104: 	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-extensions-%{buildver}.tar.%{oootarext}
Source106:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-help-%{buildver}.tar.%{oootarext}
Source107:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-extras-%{buildver}.tar.%{oootarext}


Source13:	http://download.go-oo.org/SRC680/extras-3.1.tar.bz2
Source17:	http://download.go-oo.org/SRC680/mdbtools-0.6pre1.tar.gz

Source20:       http://download.go-oo.org//DEV300/ooo-cli-prebuilt-3.3.tar.bz2
Source21:       http://download.go-oo.org/OOO300/cairo-1.4.10.tar.gz
Source22: 	http://download.go-oo.org/OOO300/libwpd-0.8.14.tar.gz
Source3: 	http://download.go-oo.org/OOO300/libwps-0.1.2.tar.gz
Source4:        http://download.go-oo.org/OOO300/libwpg-0.1.3.tar.gz

Source25:	http://download.go-oo.org/SRC680/biblio.tar.bz2
Source26:	http://tools.openoffice.org/unowinreg_prebuild/680/unowinreg.dll



# splash screens and about images
Source27:	openintro_mandriva.bmp
Source28:	openabout_mandriva.bmp

Source102:	mdv-desktop-japanese.patch
Source30: 	icons.tar.bz2

# templates for kde "create new" context menu
Source31: kde-context-menu-templates.tar.bz2

Source32: 	http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source33:       http://download.go-oo.org/src/86e390f015e505dd71a66f0123c62f09-libwpd-0.9.0.tar.bz2
Source34:	http://download.go-oo.org/src/9e436bff44c60dc8b97cba0c7fc11a5c-libwps-0.2.0.tar.bz2
Source35:	http://download.go-oo.org/src/5ba6a61a2f66dfd5fee8cdd4cd262a37-libwpg-0.2.0.tar.bz2
Source36:	http://hg.services.openoffice.org/binaries/cf8a6967f7de535ae257fa411c98eb88-mdds_0.3.0.tar.bz2
Source37: 	http://download.go-oo.org/src/0f63ee487fda8f21fafa767b3c447ac9-ixion-0.2.0.tar.gz
Source38:	http://hg.services.openoffice.org/binaries/067201ea8b126597670b5eff72e1f66c-mythes-1.2.0.tar.gz
Source39: 	http://download.go-oo.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll
Source40: 	http://hg.services.openoffice.org/binaries/48d8169acc35f97e05d8dcdfd45be7f2-lucene-2.3.2.tar.gz
Source41: 	http://hg.services.openoffice.org/binaries/d35724900f6a4105550293686688bbb3-silgraphite-2.3.1.tar.gz
Source42:	http://hg.services.openoffice.org/binaries/2a177023f9ea8ec8bd00837605c5df1b-jakarta-tomcat-5.0.30-src.tar.gz
Source43: 	http://hg.services.openoffice.org/binaries/284e768eeda0e2898b0d5bf7e26a016e-raptor-1.4.18.tar.gz
Source44:	http://hg.services.openoffice.org/binaries/fca8706f2c4619e2fa3f8f42f8fc1e9d-rasqal-0.9.16.tar.gz 
Source45:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz
Source46:	http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz	
Source47:	http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source48:	http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source49:	http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source50:	http://hg.services.openoffice.org/binaries/d0b5af6e408b8d2958f3d83b5244f5e8-hyphen-2.4.tar.gz
Source51:	http://hg.services.openoffice.org/binaries/26b3e95ddf3d9c077c480ea45874b3b8-lp_solve_5.5.tar.gz
Source52:	http://hg.services.openoffice.org/binaries/3c219630e4302863a9a83d0efde889db-commons-logging-1.1.1-src.tar.gz	
Source53:	http://hg.services.openoffice.org/binaries/128cfc86ed5953e57fe0f5ae98b62c2e-libtextcat-2.2.tar.gz

Source60:	openoffice.org.csh
Source61:	openoffice.org.sh

Patch1:	 	build-fmtstrings.diff		 
Patch2:		mdv-package-ooo.patch	
Patch3: 	mdv-build-apply.patch
Patch4:		xulrunner-to-mozila-plugin.pc.diff

%description
LibreOffice is an Open Source, community-developed, multi-platform
office productivity suite. It includes the key desktop applications,
such as a word processor, spreadsheet, presentation manager, formula
editing and drawing program, with a user interface and feature set
similar to other office suites. Sophisticated and flexible,
OpenOffice.org also works transparently with a variety of file
formats, including Microsoft Office.

%package base
Group: Office
Summary: LibreOffice office suite - database
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Heavy java deps
Requires: hsqldb
Suggests: %{name}-java-common = %{version}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-base < 1:3.3-1:2011.0 
Provides:  openoffice.org-base = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-base <= 1:3.1-4
%endif

%description base
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

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
Group: Office
Summary: LibreOffice office suite - spreadsheet
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-calc < 1:3.3-1:2011.0 
Provides:  openoffice.org-calc = 1:3.3-1:2011.0
# Provides:  openoffice.org-calc = %{EVRD}
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-calc <= 1:3.1-4
%endif

%description calc
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the spreadsheet component for LibreOffice.

%package common
Group: Office
Summary: LibreOffice office suite architecture independent files
%if %mdkversion < 200810
# On upgrades, we can't split that way or we will loose functionality.
# Requires: %{name}-gnome
# Requires: %{name}-kde
Requires: %{name}-openclipart
Requires: %{name}-style-galaxy 
Requires: %{name}-style-crystal
Requires: %{name}-style-hicontrast
Requires: %{name}-style-industrial
Requires: %{name}-style-tango
%endif
# Require the architecture dependant stuff
Requires: %{name}-core = %{EVRD}
# Require at least one style to be installed
Requires: %{name}-style = %{EVRD}
# And suggest the galaxy one
# dev 300
# Suggests: %{name}-style-galaxy = %{version}
# Also suggest java-common, as it may be used by some macros
Suggests: %{name}-java-common
Suggests: %{name}-help-en_US
# And then general requires for OOo follows
Requires: ghostscript
Requires: fonts-ttf-liberation
Requires: desktop-common-data >= 2008
# rpm will automatically grab the require for libsane1, but there are some
# configs needed at this package, so we must require it too.
Requires: sane-backends
# Due to %{_bindir}/paperconf
# Requires: paper-utils
Requires(post): desktop-file-utils update-alternatives
Requires(postun): desktop-file-utils update-alternatives

# Due to the split
Conflicts: openoffice.org <= 2.1.0
Conflicts: openoffice.org-devel <= 2.3.0.5-1mdv
Conflicts: openoffice.org-math <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.99.4-1mdv
Conflicts: openoffice.org-gnome < 3.0svn13581-2mdv
Obsoletes: openoffice.org-common < 1:3.3-1:2011.0 
Provides:  openoffice.org-common = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.1.0
Conflicts: openoffice.org64-devel <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-math <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.99.4-1mdv
Conflicts: openoffice.org64-gnome < 3.0svn13581-2mdv
Obsoletes: openoffice.org64-common <= 1:3.1-4
%endif
Conflicts: %{name}-common = 1:3.2-rc4.0

%description common
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of LibreOffice.

%package core
Group: Office
Summary: LibreOffice office suite architecture dependent files
# Due to the split
Conflicts: openoffice.org <= 2.1.0
Conflicts: openoffice.org-base <= 2.3.0.5-1mdv
Conflicts: openoffice.org-common <= 2.3.1-1mdv
Conflicts: openoffice.org-devel <= 2.3.0.5-1mdv
Conflicts: openoffice.org-draw <= 2.3.0.5-1mdv
Conflicts: openoffice.org-impress <= 2.3.0.5-1mdv
Conflicts: openoffice.org-kde <= 2.3.0.5-1mdv
Conflicts: openoffice.org-writer <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-core < 1:3.3-1:2011.0 
Provides:  openoffice.org-core = 1:3.3-1:2011.0
# Provides:  openoffice.org-core = %{EVRD}
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.1.0
Conflicts: openoffice.org64-base <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-common <= 2.3.1-1mdv
Conflicts: openoffice.org64-devel <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-draw <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-impress <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-writer <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-core <= 1:3.1-4
%endif

%description core
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-dependent core files of LibreOffice.
See the libreoffice package for more information.

%package devel
Group: Office
Summary: LibreOffice SDK - development files
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
%description devel
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the files needed to build plugins/add-ons for
LibreOffice (includes, IDL files, build tools, ...). It also contains the
zipped source of the UNO Java libraries for use in IDEs like eclipse.

%package devel-doc
Group: Office
Summary: LibreOffice SDK - documentation
Requires: %{name}-devel = %{version}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-devel-doc
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-devel-doc <= 1:3.1-4
%endif

%description devel-doc
LibreOffice is a full-featured office productivity suite that provides
a near drop-in replacement for Microsoft(R) Office.

This package contains the documentation of the LibreOffice SDK:

 * C++/Java API reference
 * IDL reference
 * C++/Java/Basic examples

It also contains the gsicheck utility.

%package draw
Group: Office
Summary: LibreOffice office suite - drawing
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-impress <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-draw < 1:3.3-1:2011.0 
Provides:  openoffice.org-draw = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-impress <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-draw <= 1:3.1-4
%endif

%description draw
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the drawing component for LibreOffice.

# package dtd-officedocument1.0
# Group: Office
# Summary: OfficeDocument 1.0 DTD (OpenOffice.org 1.x)
## due to the split
#Conflicts: %{name} <= 2.2.1
## no need to require -core or -common, see #37559

#%description dtd-officedocument1.0
#LibreOffice is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.

# This package contains the Document Type Definition (DTD) of the OpenOffice.org
# 1.x(!) XML file format.

%package filter-binfilter
Group: Office
Summary: Legacy filters (e.g. StarOffice 5.2) for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-filter-mobiledev <= 2.3.0.5
Conflicts: openoffice.org-filter-mobiledev <= 2.3.0.5
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-filter-binfilter
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-filter-mobiledev <= 2.3.0.5
Obsoletes: openoffice.org64-filter-binfilter <= 1:3.1-4
%endif


%description filter-binfilter
LibreOffice is a full-featured office productivity suite that provides
 a near drop-in replacement for Microsoft(R) Office.

This package contains the "binfilters", legacy filters for
 - the old StarOffice 5.2 formats
 - StarWriter 1.0/2.0
 - StarWriter/DOS
 - *Writer* filters for
   + Excel
   + Lotus

%package gnome
Group: Office
Summary: GNOME Integration for OpenOffice.org (VFS, GConf)
Requires: %{name}-common = %{EVRD}
Requires: %{name}-core = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-gtk <= 2.3.0.5
Conflicts: openoffice.org-gtk <= 2.3.0.5
Obsoletes: openoffice.org-qstart <= 2.3.0.5
Conflicts: openoffice.org-qstart <= 2.3.0.5
Obsoletes: openoffice.org-evolution <= 2.3.0.5
Conflicts: openoffice.org-evolution <= 2.3.0.5
# Suggests: %{name}-style-tango = %{version}
Obsoletes: openoffice.org-gnome < 1:3.3-1:2011.0 
Provides:  openoffice.org-gnome = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-gtk <= 2.3.0.5
Obsoletes: openoffice.org64-qstart <= 2.3.0.5
Obsoletes: openoffice.org64-evolution <= 2.3.0.5
Obsoletes: openoffice.org64-gnome <= 1:3.1-4
%endif

%description gnome
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the GNOME VFS support and a GConf backend.

You can extend the functionality of this by installing these packages:

 * openoffice.org-evolution: Evolution addressbook support
 * evolution

%package impress
Group: Office
Summary: LibreOffice office suite - presentation
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD} 
Requires: %{name}-draw = %{EVRD}
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-impress < 1:3.3-1:2011.0 
Provides:  openoffice.org-impress = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-impress <= 1:3.1-4
%endif

%description impress
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the presentation component for LibreOffice.

%package kde4
Group: Office
Summary: KDE4 Integration for LibreOffice (Widgets, Dialogs, Addressbook)
Requires: %{name}-common = %{EVRD}
Requires: %{name}-core = %{EVRD}
Suggests: %{name}-style-oxygen = %{EVRD} 
Obsoletes: openoffice.org-kde4 < 1:3.3-1:2011.0 
Provides:  openoffice.org-kde4 = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-kde <= 1:3.1-4
%endif
Conflicts: openoffice.org-core <= %{version}-beta1.0mdv

%description kde4
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the KDE4 plugin for drawing OOo's widgets with KDE4/Qt4.5 and 
a KDEish File Picker when running under KDE4.
 
%package java-common
Group: Office
Summary: LibreOffice office suite Java support arch. independent files
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Requires: java
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-java-common < 1:3.3-1:2011.0 
Provides:  openoffice.org-java-common = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-java-common <= 1:3.1-4
%endif

%description java-common
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the architecture-independent files of the Java support
for OpenOffice.org (Java classes, scripts, config snippets).

Also contains the OpenOffice.org Office Bean for embedding OpenOffice.org in
custom Java applications.

%package math
Group: Office
Summary: LibreOffice office suite - equation editor
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-math < 1:3.3-1:2011.0 
Provides:  openoffice.org-math = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-math <= 1:3.1-4
%endif

%description math
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the equation editor component for LibreOffice.

%package openclipart
Group: Office
Summary: LibreOffice Open Clipart data
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Requires: clipart-openclipart
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-galleries <= 2.2.1
Obsoletes: openoffice.org-openclipart
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-galleries <= 2.2.1
Obsoletes: openoffice.org64-openclipart <= 1:3.1-4
%endif

%description openclipart
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the OpenOffice.org Open Clipart data, including images
and sounds.

%package pyuno
Group: Office
Summary: Python bindings for UNO library
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-pyuno
%ifarch x86_64
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-pyuno <= 1:3.1-4
%endif

%description pyuno
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the Python bindings for the UNO library.

#%package qa-api-tests
#Group: Office
#Summary: LibreOffice API Test Data
#Requires: %{name}-common = %{version}-%{release}
## Due to the split
#Conflicts: %{name} <= 2.2.1
#
#%description qa-api-tests
#LibreOffice is a full-featured office productivity suite that provides a
#near drop-in replacement for Microsoft(R) Office.
#
#This package contains the test data for the OpenOffice.org Java and Basic APIs.

%package testtool
Group: Office
Summary: LibreOffice Automatic Test Programs
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-testtool
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-testtool <= 1:3.1-4
%endif

%description testtool
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the test tools to automatically test the OpenOffice.org
programs.

%package style-galaxy
Group: Office
Summary: Default symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-style-andromeda <= %{version}
Obsoletes: openoffice.org-style-galaxy < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-galaxy = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-style-galaxy <= 1:3.1-4
%endif

%description style-galaxy
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "Galaxy" symbol style from Sun, normally used on
MS Windows (tm) and when not using GNOME or KDE. Needs to be manually enabled
in the OpenOffice.org option menu.

%package style-crystal
Group: Office
Summary: Crystal symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-style-crystal < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-crystal = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-style-crystal <= 1:3.1-4
%endif

%description style-crystal
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "crystal" symbol style, default style for KDE.

%package style-hicontrast
Group: Office
Summary: Hicontrast symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-style-hicontrast < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-hicontrast = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-style-hicontrast <= 1:3.1-4
%endif

%description style-hicontrast
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "hicontrast" symbol style, needs to be manually
enabled in the OpenOffice.org option menu.

%package style-industrial
Group: Office
Summary: Industrial symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-style-industrial < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-industrial = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-style-industrial <= 1:3.1-4
%endif

%description style-industrial
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "industrial" symbol style.

%package style-tango
Group: Office
Summary: Tango symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-style-tango < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-tango = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-style-tango <= 1:3.1-4
%endif

%description style-tango
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "tango" symbol style, default style for GTK/Gnome.

%package style-oxygen
Group: Office
Summary: Oxygen symbol style for LibreOffice
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Provides: %{name}-style = %{EVRD}
# Due to the split
Conflicts: openoffice.org = 2.2.1
Obsoletes: openoffice.org-style-oxygen < 1:3.3-1:2011.0 
Provides:  openoffice.org-style-oxygen = 1:3.3-1:2011.0

%description style-oxygen
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the "oxygen" symbol style, default style for KDE4.

%package writer
Group: Office
Summary: LibreOffice office suite - word processor
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-writer < 1:3.3-1:2011.0 
Provides:  openoffice.org-writer = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-writer <= 1:3.1-4
%endif

%description writer
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the wordprocessor component for LibreOffice.

%package mono
Summary:	Mono UNO Bridge for LibreOffice
Group:		Office
Requires:	%{ooname} = %{version}
Obsoletes:	openoffice.org-go-ooo-mono <= %{version}
Obsoletes:	openoffice.org-mono
%ifarch x86_64
Obsoletes: openoffice.org64-mono <= 1:3.1-4
%endif

%description mono
The Mono/UNO binding allows a Mono application to access the complete
set of APIs exposed by OpenOffice.org via UNO.

Currently the use of Mono for add-ins & scripting inside OO.o itself is
not supported.

%package pdfimport
Group: Office
Summary: LibreOffice office suite - PDF Import extension
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Requires: %{name}-draw = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-pdfimport < 1:3.3-1:2011.0 
Provides:  openoffice.org-pdfimport = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-pdfimport <= 1:3.1-4
%endif
Conflicts: openoffice.org-pdfimport <= 1:3.2-rc4.0

%description pdfimport
PDF import extension enables PDF documments importing and basic editing of PDF
documments by using OpenOffice.org-draw application.

%package presenter-screen
Group: Office
Summary: LibreOffice office suite - Presenter Screen extension
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Requires: %{name}-impress = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-presenter-screen
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-presenter-screen <= 1:3.1-4
%endif
Conflicts: %{name}-presenter-screen <= 1:3.2-rc4.0

%description presenter-screen
Presenter Screen extension helps users to see upcoming slides and slide notes
of presentations inside a second view not visible for the spectators.

# %package report-builder
# Group: Office
# Summary: LibreOffice office suite - Report Builder extension
# Requires: %{name}-core = %{version}-%{release}
# Requires: %{name}-common = %{version}-%{release}
# Requires: %{name}-base = %{version}
# Due to the split
# Conflicts: %{name} <= 2.2.1
# Conflicts: %{name}-common <= 2.3.0.5-1mdv
# Conflicts: %{name}-core <= 2.3.0.5-1mdv
# %ifarch x86_64
# Conflicts: %{name}64 <= 2.2.1
# Conflicts: %{name}64-common <= 2.3.0.5-1mdv
# Conflicts: %{name}64-core <= 2.3.0.5-1mdv
# Obsoletes: openoffice.org64-report-builder < 1:3.1-4
# %endif

# %description report-builder
# By using %{name}-base the Report Builder extesion enables creating of smart and 
# professional looking reports. Further the reports can be exported to PDF or 
# OpenDocuments formats.

%package wiki-publisher
Group: Office
Summary: LibreOffice office suite - Wiki Publisher extension
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Requires: %{name}-writer = %{EVRD}
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-wiki-publisher
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-wiki-publisher <= 1:3.1-4
%endif
Conflicts: openoffice.org-wiki-publisher <= 1:3.2-rc4.0

%description wiki-publisher
With Wiki Publisher extesion is possible by using %{name}-writer to create 
wiki page articles on MediaWiki servers without having to know the syntax of 
MediaWiki markup language. This extension also enables publishing of the
wiki pages.

%package presentation-minimizer
Group: Office
Summary: LibreOffice office suite - Presentation Minimizer extension
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Requires: %{name}-impress = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-presentation-minimizer
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Conflicts: openoffice.org64-common <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.0.5-1mdv
Obsoletes: openoffice.org64-presentation-minimizer <= 1:3.1-4
%endif
Conflicts: openoffice.org-presentation-minimizer <= 1:3.2-rc4.0

%description presentation-minimizer
With Presentation Minimizer extesion is possible to reduce the file size of the 
presentation by compressing images and removing data not needed in a automatizated
way.

Note: The Presentation Minimizer also works on Microsoft PowerPoint presentations. 

%if %l10n
%package l10n-it
Summary:	Italian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{version}-%{release}
Requires:	%{ooname}-common = %{EVRD}
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-it
Requires:	myspell-hyph-it
Obsoletes:  OpenOffice.org-l10n-it
Provides: 	LibreOffice-l10n-it
Obsoletes:	openoffice.org-go-ooo-l10n-it <= %{version}
Suggests:	%{ooname}-help-it
Obsoletes:	openoffice.org-l10n-it
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-it <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-it <= 3.1-4
%endif

%description l10n-it
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Italian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package l10n-af
Summary:	Afrikaans language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-af
Requires:	urw-fonts
Requires:	myspell-af
Obsoletes:  OpenOffice.org-l10n-af
Provides: 	LibreOffice-l10n-af
Obsoletes:	openoffice.org-go-ooo-l10n-af <= %{version}
Suggests:	%{ooname}-help-af
Obsoletes:	openoffice.org-l10n-af
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-af <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-af <= 3.1-4
%endif

%description l10n-af
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-ar
Provides: 	LibreOffice-l10n-ar
Obsoletes:	openoffice.org-go-ooo-l10n-ar <= %{version}
Suggests:	%{ooname}-help-ar
Obsoletes:	openoffice.org-l10n-ar
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ar <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ar <= 3.1-4
%endif

%description l10n-ar
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Arabic.
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
Obsoletes:  OpenOffice.org-l10n-bg
Provides: 	LibreOffice-l10n-bg
Obsoletes:	openoffice.org-go-ooo-l10n-bg <= %{version}
Suggests:	%{ooname}-help-bg
Obsoletes:	openoffice.org-l10n-bg
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-bg <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-bg <= 3.1-4
%endif

%description l10n-bg
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Bulgarian.
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
Obsoletes:  OpenOffice.org-l10n-br
Provides: 	LibreOffice-l10n-br
Obsoletes:	openoffice.org-go-ooo-l10n-br <= %{version}
Suggests:	%{ooname}-help-br
Obsoletes:	openoffice.org-l10n-br
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-br <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-br <= 3.1-4
%endif

%description l10n-br
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-bs
Provides: 	LibreOffice-l10n-bs
Obsoletes:	openoffice.org-go-ooo-l10n-bs <= %{version}
Suggests:	%{ooname}-help-bs
Obsoletes:	openoffice.org-l10n-bs
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-bs <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-bs <= 3.1-4
%endif

%description l10n-bs
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-ca
Provides: 	LibreOffice-l10n-ca
Obsoletes:	openoffice.org-go-ooo-l10n-ca <= %{version}
Suggests:	%{ooname}-help-ca
Obsoletes:	openoffice.org-l10n-ca
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ca <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ca <= 3.1-4
%endif

%description l10n-ca
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-cs
Provides: 	LibreOffice-l10n-cs
Obsoletes:	openoffice.org-go-ooo-l10n-cs <= %{version}
Suggests:	%{ooname}-help-cs
Obsoletes:	openoffice.org-l10n-cs
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-cs <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-cs <= 3.1-4
%endif

%description l10n-cs
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-cy
Provides: 	LibreOffice-l10n-cy
Obsoletes:	openoffice.org-go-ooo-l10n-cy <= %{version}
Suggests:	%{ooname}-help-cy
Obsoletes:	openoffice.org-l10n-cy
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-cy <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-cy <= 3.1-4
%endif

%description l10n-cy
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-da
Provides: 	LibreOffice-l10n-da
Obsoletes:	openoffice.org-go-ooo-l10n-da <= %{version}
Suggests:	%{ooname}-help-da
Obsoletes:	openoffice.org-l10n-da
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-da <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-da <= 3.1-4
%endif

%description l10n-da
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-de
Provides: 	LibreOffice-l10n-de
Obsoletes:	openoffice.org-go-ooo-l10n-de <= %{version}
Suggests:	%{ooname}-help-de
Obsoletes:	openoffice.org-l10n-de
%ifarch x86_64
Obsoletes:  openoffice.org64-l10n-de <= 1:3.1-4
Obsoletes:  openoffice.org64-go-ooo-l10n-de <= 3.1-4
%endif

%description l10n-de
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in German.
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
Obsoletes:  OpenOffice.org-l10n-el
Provides: 	LibreOffice-l10n-el
Obsoletes:	openoffice.org-go-ooo-l10n-el <= %{version}
Suggests:	%{ooname}-help-el
Obsoletes:	openoffice.org-l10n-el
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-el <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-el <= 3.1-4
%endif

%description l10n-el
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-en_GB
Provides: 	LibreOffice-l10n-en_GB
Obsoletes:	openoffice.org-go-ooo-l10n-en_GB <= %{version}
Suggests:	%{ooname}-help-en_GB
Obsoletes:	openoffice.org-l10n-en_GB
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-en_GB <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-en_GB <= 3.1-4
%endif

%description l10n-en_GB
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-es
Provides: 	LibreOffice-l10n-es
Obsoletes:	openoffice.org-go-ooo-l10n-es <= %{version}
Suggests:	%{ooname}-help-es
Obsoletes:	openoffice.org-l10n-es
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-es <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-es <= 3.1-4
%endif

%description l10n-es
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-et
Provides: 	LibreOffice-l10n-et
Obsoletes:	openoffice.org-go-ooo-l10n-et <= %{version}
Suggests:	%{ooname}-help-et
Obsoletes:	openoffice.org-l10n-et
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-et <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-et <= 3.1-4
%endif

%description l10n-et
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-eu
Provides: 	LibreOffice-l10n-eu
Obsoletes:	openoffice.org-go-ooo-l10n-eu <= %{version}
Suggests:	%{ooname}-help-eu
Obsoletes:	openoffice.org-l10n-eu
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-eu <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-eu <= 3.1-4
%endif

%description l10n-eu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Basque.
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
Requires:	%{ooname}-voikko
Obsoletes:  OpenOffice.org-l10n-fi
Provides: 	LibreOffice-l10n-fi
Obsoletes:	openoffice.org-go-ooo-l10n-fi <= %{version}
Suggests:	%{ooname}-help-fi
Obsoletes:	openoffice.org-l10n-fi
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-fi <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-fi <= 3.1-4
%endif

%description l10n-fi
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-fr
Provides: 	LibreOffice-l10n-fr
Obsoletes:	openoffice.org-go-ooo-l10n-fr <= %{version}
Suggests:	%{ooname}-help-fr
Obsoletes:	openoffice.org-l10n-fr
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-fr <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-fr <= 3.1-4
%endif

%description l10n-fr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in French.
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
Obsoletes:  OpenOffice.org-l10n-he
Provides: 	LibreOffice-l10n-he
Obsoletes:	openoffice.org-go-ooo-l10n-he <= %{version}
Suggests:	%{ooname}-help-he
Obsoletes:	openoffice.org-l10n-he
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-he <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-he <= 3.1-4
%endif

%description l10n-he
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-hi
Provides: 	LibreOffice-l10n-hi
Obsoletes:	openoffice.org-go-ooo-l10n-hi <= %{version}
Suggests:	%{ooname}-help-hi
Obsoletes:	openoffice.org-l10n-hi
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-hi <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-hi <= 3.1-4
%endif

%description l10n-hi
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Hindi.
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
Obsoletes:  OpenOffice.org-l10n-hu
Provides: 	LibreOffice-l10n-hu
Obsoletes:	openoffice.org-go-ooo-l10n-hu <= %{version}
Suggests:	%{ooname}-help-hu
Obsoletes:	openoffice.org-l10n-hu
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-hu <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-hu <= 3.1-4
%endif

%description l10n-hu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Hungarian.
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
Requires:	fonts-ttf-japanese >= 0.20020727-1mdk
Obsoletes:  OpenOffice.org-l10n-ja
Provides: 	LibreOffice-l10n-ja
Obsoletes:	openoffice.org-go-ooo-l10n-ja <= %{version}
Suggests:	%{ooname}-help-ja
Obsoletes:	openoffice.org-l10n-ja
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ja <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ja <= 3.1-4
%endif

%description l10n-ja
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Japanese.
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
Obsoletes:  OpenOffice.org-l10n-ko
Provides: 	LibreOffice-l10n-ko
Obsoletes:	openoffice.org-go-ooo-l10n-ko <= %{version}
Suggests:	%{ooname}-help-ko
Obsoletes:	openoffice.org-l10n-ko
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ko <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ko <= 3.1-4
%endif

%description l10n-ko
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Korean.
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
Obsoletes:  OpenOffice.org-l10n-mk
Provides: 	LibreOffice-l10n-mk
Obsoletes:	openoffice.org-go-ooo-l10n-mk <= %{version}
Suggests:	%{ooname}-help-mk
Obsoletes:	openoffice.org-l10n-mk
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-mk <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-mk <= 3.1-4
%endif

%description l10n-mk
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Macedonian.
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
Obsoletes:  OpenOffice.org-l10n-nb
Provides: 	LibreOffice-l10n-nb
Obsoletes:	openoffice.org-go-ooo-l10n-nb <= %{version}
Suggests:	%{ooname}-help-nb
Obsoletes:	openoffice.org-l10n-nb
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-nb <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-nb <= 3.1-4
%endif

%description l10n-nb
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-nl
Provides: 	LibreOffice-l10n-nl
Obsoletes:	openoffice.org-go-ooo-l10n-nl <= %{version}
Suggests:	%{ooname}-help-nl
Obsoletes:	openoffice.org-l10n-nl
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-nl <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-nl <= 3.1-4
%endif

%description l10n-nl
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-nn
Provides: 	LibreOffice-l10n-nn
Obsoletes:	openoffice.org-go-ooo-l10n-nn <= %{version}
Suggests:	%{ooname}-help-nn
Obsoletes:	openoffice.org-l10n-nn
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-nn <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-nn <= 3.1-4
%endif

%description l10n-nn
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Norwegian Nynorsk.
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
Obsoletes:  OpenOffice.org-l10n-pl
Provides: 	LibreOffice-l10n-pl
Obsoletes:	openoffice.org-go-ooo-l10n-pl <= %{version}
Suggests:	%{ooname}-help-pl
Obsoletes:	openoffice.org-l10n-pl
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-pl <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-pl <= 3.1-4
%endif

%description l10n-pl
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-pt
Provides: 	LibreOffice-l10n-pt
Obsoletes:	openoffice.org-go-ooo-l10n-pt <= %{version}
Suggests:	%{ooname}-help-pt
Obsoletes:	openoffice.org-l10n-pt
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-pt <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-pt <= 3.1-4
%endif

%description l10n-pt
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Portuguese.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-pt_BR
Summary:	Portuguese Brazilian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
# Due to alternatives setup, we must have -release here. (BrOffice)
Requires:	%{ooname}-common = %{EVRD}
Requires(post): update-alternatives %{ooname}-common
Requires(postun): update-alternatives %{ooname}-common
Requires:	locales-pt
Requires:	urw-fonts
Requires:	myspell-pt_BR
Obsoletes:  OpenOffice.org-l10n_pt_BR
Provides: 	LibreOffice-l10n_pt_BR
Obsoletes:	openoffice.org-go-ooo-l10n-pt_BR <= %{version}
Suggests:	%{ooname}-help-pt_BR
Obsoletes:	openoffice.org-l10n-pt_BR
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-pt_BR <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-pt_BR <= 3.1-4
%endif

%description l10n-pt_BR
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Portuguese
Brazilian.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.


%package l10n-pt_AO
Summary:    Portuguese Angola language support for LibreOffice
Group:      Office
Provides:	%{ooname}-l10n = %{EVRD}
# Due to alternatives setup, we must have -release here. (BrOffice)
Requires:	%{ooname}-common = %{EVRD}
Requires:   locales-pt
Requires:   urw-fonts
Obsoletes:  OpenOffice.org-l10n-pt_AO
Provides: 	LibreOffice-l10n-pt_AO
Suggests:	%{ooname}-help-pt_AO
Obsoletes:	openoffice.org-l10n-pt_AO

%description l10n-pt_AO
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Portuguese
Angola.
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
Obsoletes:  OpenOffice.org-l10n-ru
Provides: 	LibreOffice-l10n-ru
Obsoletes:	openoffice.org-go-ooo-l10n-ru <= %{version}
Suggests:	%{ooname}-help-ru
Obsoletes:	openoffice.org-l10n-ru
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ru <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ru <= 3.1-4
%endif

%description l10n-ru
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Russian.
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
Obsoletes:  OpenOffice.org-l10n-sk
Provides: 	LibreOffice-l10n-sk
Obsoletes:	openoffice.org-go-ooo-l10n-sk <= %{version}
Suggests:	%{ooname}-help-sk
Obsoletes:	openoffice.org-l10n-sk
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-sk <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-sk <= 3.1-4
%endif

%description l10n-sk
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-sl
Provides: 	LibreOffice-l10n-sl
Obsoletes:	openoffice.org-go-ooo-l10n-sl <= %{version}
Suggests:	%{ooname}-help-sl
Obsoletes:	openoffice.org-l10n-sl
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-sl <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-sl <= 3.1-4
%endif

%description l10n-sl
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Slovenian.
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
Obsoletes:  OpenOffice.org-l10n-sv
Provides: 	LibreOffice-l10n-sv
Obsoletes:	openoffice.org-go-ooo-l10n-sv <= %{version}
Suggests:	%{ooname}-help-sv
Obsoletes:	openoffice.org-l10n-sv
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-sv <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-sv <= 3.1-4
%endif

%description l10n-sv
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-ta
Provides: 	LibreOffice-l10n-ta
Obsoletes:	openoffice.org-go-ooo-l10n-ta <= %{version}
Suggests:	%{ooname}-help-ta
Obsoletes:	openoffice.org-l10n-ta
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-ta <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-ta <= 3.1-4
%endif

%description l10n-ta
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Tamil.
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
Obsoletes:  OpenOffice.org-l10n-tr
Provides: 	LibreOffice-l10n-tr
Obsoletes:	openoffice.org-go-ooo-l10n-tr <= %{version}
Suggests:	%{ooname}-help-tr
Obsoletes:	openoffice.org-l10n-tr
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-tr <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-tr <= 3.1-4
%endif

%description l10n-tr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Turkish.
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
Obsoletes:  OpenOffice.org-l10n-zh_CN
Provides: 	LibreOffice-l10n-zh_CN
Obsoletes:	openoffice.org-go-ooo-l10n-zh_CN <= %{version}
Suggests:	%{ooname}-help-zh_CN
Obsoletes:	openoffice.org-l10n-zh_CN
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-zh_CN <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-zh_CN <= 3.1-4
%endif

%description l10n-zh_CN
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-zh_TW
Provides: 	LibreOffice-l10n-zh_TW
Obsoletes:	openoffice.org-go-ooo-l10n-zh_TW <= %{version}
Suggests:	%{ooname}-help-zh_TW
Obsoletes:	openoffice.org-l10n-zh_TW
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-zh_TW <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-zh_TW <= 3.1-4
%endif

%description l10n-zh_TW
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-zu
Provides: 	LibreOffice-l10n-zu
Obsoletes:	openoffice.org-go-ooo-l10n-zu <= %{version}
Suggests:	%{ooname}-help-zu
Obsoletes:	openoffice.org-l10n-zu
%ifarch x86_64
Obsoletes:     openoffice.org64-l10n-zu <= 1:3.1-4
Obsoletes:     openoffice.org64-go-ooo-l10n-zu <= 3.1-4
%endif

%description l10n-zu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localization of LibreOffice in Zulu.
It contains the user interface, the templates and the autotext
features. Please note that not all of these are available for all
possible language. You can switch user interface language using the
standard locales system.

%package help-it
Summary:	Italian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-it = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-it <= 1:3.1-4
%endif
Obsoletes:  OpenOffice.org-help-it
Provides:	LibreOffice-help-it
Obsoletes:  openoffice.org-help-it

%description help-it
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Italian.

%package help-af
Summary:	Afrikaans help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-af = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-af <= 1:3.1-4
%endif
Obsoletes:  OpenOffice.org-help-af
Provides:	LibreOffice-help-af
Obsoletes:  openoffice.org-help-af

%description help-af
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Afrikaans.


%package help-ar
Summary:	Arabic help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ar = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ar <= 1:3.1-4
%endif
Obsoletes:  OpenOffice.org-help-ar
Provides:	LibreOffice-help-ar
Obsoletes:  openoffice.org-help-ar

%description help-ar
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Arabic.


%package help-bg
Summary:	Bulgarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bg = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-bg <= 1:3.1-4
%endif
Obsoletes:  OpenOffice.org-help-bg
Provides:	LibreOffice-help-bg
Obsoletes:  openoffice.org-help-bg

%description help-bg
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Bulgarian.


%package help-br
Summary:	Breton help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-br = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-br <= 1:3.1-4
%endif
Obsoletes:  OpenOffice.org-help-br
Provides:	LibreOffice-help-br
Obsoletes:  openoffice.org-help-br

%description help-br
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Breton.


%package help-bs
Summary:	Bosnian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bs = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-br <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-bs
Provides:	LibreOffice-help-bs
Obsoletes:  openoffice.org-help-bs

%description help-bs
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Bosnian.


%package help-ca
Summary:	Catalan help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ca = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ca <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-ca
Provides:	LibreOffice-help-ca
Obsoletes:  openoffice.org-help-ca

%description help-ca
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Catalan.


%package help-cs
Summary:	Czech help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-cs = %{EVRD}
Obsoletes:	OpenOffice.org-help-cs
%ifarch x86_64
Obsoletes:     openoffice.org64-help-cs <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-cs
Provides:	LibreOffice-help-cs
Obsoletes:  openoffice.org-help-cs

%description help-cs
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Czech.


%package help-cy
Summary:	Welsh help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-cy = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-cy <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-cy
Provides:	LibreOffice-help-cy
Obsoletes:  openoffice.org-help-cy

%description help-cy
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Welsh.


%package help-da
Summary:	Danish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-da = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-da <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-da
Provides:	LibreOffice-help-da
Obsoletes:  openoffice.org-help-da

%description help-da
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Danish.


%package help-de
Summary:	German help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-de = %{EVRD}
Obsoletes:	OpenOffice.org-help-de
%ifarch x86_64
Obsoletes:     openoffice.org64-help-de <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-de
Provides:	LibreOffice-help-de
Obsoletes:  openoffice.org-help-de

%description help-de
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in German.


%package help-el
Summary:	Greek help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-el = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-el <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-el
Provides:	LibreOffice-help-el
Obsoletes:  openoffice.org-help-el


%description help-el
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Greek.


%package help-en_GB
Summary:	British help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-en_GB = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-en_GB <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-en_GB
Provides:	LibreOffice-help-en_GB
Obsoletes:  openoffice.org-help-en_GB

%description help-en_GB
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in British.


%package help-en_US 
Summary:	American English help for LibreOffice 
Group:		Office 
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-en_US <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-en_US
Provides:	LibreOffice-help-en_US
Obsoletes: openoffice.org-help-en_US < 1:3.3-1:2011.0 
Provides:  openoffice.org-help-en_US = 1:3.3-1:2011.0

%description help-en_US
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in American English.


%package help-es
Summary:	Spanish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-es = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-es <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-es
Provides:	LibreOffice-help-es
Obsoletes:  openoffice.org-help-es

%description help-es
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Spanish.


%package help-et
Summary:	Estonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-et = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-et <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-et
Provides:	LibreOffice-help-et
Obsoletes:  openoffice.org-help-et

%description help-et
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Estonian.


%package help-eu
Summary:	Basque help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-eu = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-eu <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-eu
Provides:	LibreOffice-help-eu
Obsoletes:  openoffice.org-help-eu

%description help-eu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Basque.


%package help-fi
Summary:	Finnish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fi = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-fi <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-fi
Provides:	LibreOffice-help-fi
Obsoletes:  openoffice.org-help-fi

%description help-fi
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Finnish.


%package help-fr
Summary:	French help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-fr = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-fr <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-fr
Provides:	LibreOffice-help-fr
Obsoletes:  openoffice.org-help-fr

%description help-fr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in French.


%package help-he
Summary:	Hebrew help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-he = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-he <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-he
Provides:	LibreOffice-help-he
Obsoletes:  openoffice.org-help-he

%description help-he
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Hebrew.


%package help-hi
Summary:	Hindi help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hi = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-hi <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-hi
Provides:	LibreOffice-help-hi
Obsoletes:  openoffice.org-help-hi

%description help-hi
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Hindi.


%package help-hu
Summary:	Hungarian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hu = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-hu <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-hu
Provides:	LibreOffice-help-hu
Obsoletes:  openoffice.org-help-hu

%description help-hu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Hungarian.


%package help-ja
Summary:	Japanese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ja = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ja <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-ja
Provides:	LibreOffice-help-ja
Obsoletes:  openoffice.org-help-ja

%description help-ja
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Japanese.


%package help-ko
Summary:	Korean help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ko = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ko <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-ko
Provides:	LibreOffice-help-ko
Obsoletes:  openoffice.org-help-ko

%description help-ko
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Korean.


%package help-mk
Summary:	Macedonian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-mk = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-mk <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-mk
Provides:	LibreOffice-help-mk
Obsoletes:  openoffice.org-help-mk

%description help-mk
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Macedonian.


%package help-nb
Summary:	Norwegian Bokmal help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nb = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-nb <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-nb
Provides:	LibreOffice-help-nb
Obsoletes:  openoffice.org-help-nb

%description help-nb
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Norwegian
Bokmal.


%package help-nl
Summary:	Dutch help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nl = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-nl <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-nl
Provides:	LibreOffice-help-nl
Obsoletes:  openoffice.org-help-nl

%description help-nl
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Dutch.


%package help-nn
Summary:	Norwegian Nynorsk help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nn = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-nn <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-nn
Provides:	LibreOffice-help-nn
Obsoletes:  openoffice.org-help-nn

%description help-nn
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Norwegian
Nynorsk.

%package help-pl
Summary:	Polish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pl = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-pl <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-pl
Provides:	LibreOffice-help-pl
Obsoletes:  openoffice.org-help-pl

%description help-pl
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Polish.


%package help-pt
Summary:	Portuguese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-pt <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-pt
Provides:	LibreOffice-help-pt
Obsoletes:  openoffice.org-help-pt

%description help-pt
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Portuguese.


%package help-pt_BR
Summary:	Portuguese Brazilian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt_BR = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-pt_BR <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-pt_BR
Provides:	LibreOffice-help-pt_BR
Obsoletes:  openoffice.org-help-pt_BR

%description help-pt_BR
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Portuguese
Brazilian.


%package help-pt_AO
Summary:	Portuguese Angola help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-pt_AO = %{EVRD}
Provides:	LibreOffice-help-pt_AO
Obsoletes:  openoffice.org-help-pt_AO

%description help-pt_AO
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Portuguese
Angola.


%package help-ru
Summary:        Russian help for LibreOffice
Group:          Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ru = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ru <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-ru
Provides:	LibreOffice-help-ru
Obsoletes:  openoffice.org-help-ru

%description help-ru
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Russian.


%package help-sk
Summary:	Slovak help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sk = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-sk <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-sk
Provides:	LibreOffice-help-sk
Obsoletes:  openoffice.org-help-sk

%description help-sk
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Slovak.


%package help-sl
Summary:	Slovenian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sl = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-sl <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-sl
Provides:	LibreOffice-help-sl
Obsoletes:  openoffice.org-help-sl

%description help-sl
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Slovenian.


%package help-sv
Summary:	Swedish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-sv = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-sv <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-sv
Provides:	LibreOffice-help-sv
Obsoletes:  openoffice.org-help-sv

%description help-sv
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Swedish.


%package help-ta
Summary:	Tamil help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-ta = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-ta <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-ta
Provides:	LibreOffice-help-ta
Obsoletes:  openoffice.org-help-ta

%description help-ta
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Tamil.


%package help-tr
Summary:	Turkish help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-tr = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-tr <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-tr
Provides:	LibreOffice-help-tr
Obsoletes:  openoffice.org-help-tr

%description help-tr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Turkish.


%package help-zh_CN
Summary:	Chinese Simplified help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_CN = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-zh_CN <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-zh_CN
Provides:	LibreOffice-help-zn_CN
Obsoletes:  openoffice.org-help-zn_CN

%description help-zh_CN
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Chinese
Simplified.


%package help-zh_TW
Summary:	Chinese Traditional help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zh_TW = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-zh_TW <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-zh_CT
Provides:	LibreOffice-help-zn_CT
Obsoletes:  openoffice.org-help-zn_CT

%description help-zh_TW
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Chinese
Traditional.


%package help-zu
Summary:	Zulu help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-zu = %{EVRD}
%ifarch x86_64
Obsoletes:     openoffice.org64-help-zu <= 1:3.1-4
%endif
Obsoletes:	OpenOffice.org-help-zu
Provides:	LibreOffice-help-zu
Obsoletes:  openoffice.org-help-zu

%description help-zu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Zulu.
%endif

%prep
%setup -q -n libreoffice-build-%{buildver}

# mdv fixes for the building stuff 
cp %{P:1} %{_builddir}/libreoffice-build-%{buildver}/patches/hotfixes/
cp %{P:4} %{_builddir}/libreoffice-build-%{buildver}/patches/hotfixes/
%patch3 -p0 -b .apply-mdv #disable mono at all

# mdv fixes for the packaging stuff
%patch2 -p0 -b .pkg-mdv

# Add lzma support (REVIEW)
%if %{oootarext} == "lzma"
%patch1 -p1 -b .lzma
%endif


# We want odk
# sed -i /disable-odk/d distro-configs/Mandriva*

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


# Force KDE3 support instead of KDE4 (dev 300)
#%ifarch x86_64 
#export KDEDIR=/opt/kde
#%endif




%if !%{use_gcj}
if [ -z $JAVA_HOME ]; then
	. /etc/profile.d/jdk-%{jdkver}.sh
fi
%endif

# add moc in PATH
# if [ ! -z $QTDIR ]; then
#	export QTPATH=$QTDIR/bin
#	export PATH=$PATH:$QTPATH
#else
#	export PATH=$PATH:%{_prefix}/lib/qt3

# fi

%if %{use_gcj}
if [ "`readlink -f %{_bindir}/java`" = "%{_bindir}/jamvm" ]; then
	echo "Warning: Alternatives for java-1.4.2-gcj-compat are not installed properly."
	echo "Warning: Try running \"update-alternatives --config java\" before building this package."
	exit 1
fi
%endif

%if !%{use_icecream}
# sbin due to icu stuff there
#PATH=/bin:/usr/bin:/usr/X11R6/bin:$QTPATH:/usr/sbin:$PATH
PATH=$PATH:/usr/sbin
export PATH
%endif


mkdir -p src/clone

ln -sf %{SOURCE3} src/
ln -sf %{SOURCE4} src/
ln -sf %{SOURCE5} src/
ln -sf %{SOURCE13} src/
ln -sf %{SOURCE17} src/
%if %{use_mono}
ln -sf %{SOURCE20} src/
%endif

ln -sf %{SOURCE21} src/
ln -sf %{SOURCE22} src/

# ooo-build requests this even with mono off
ln -sf %{SOURCE26} src/
ln -sf %{SOURCE25} src/

# splash screen
ln -sf %{SOURCE27} src/
ln -sf %{SOURCE28} src/

# icons
ln -sf %{SOURCE30} src/

# templates for kde context menu
ln -sf %{SOURCE31} src/

ln -sf %{SOURCE32} src/
ln -sf %{SOURCE33} src/
ln -sf %{SOURCE34} src/
ln -sf %{SOURCE35} src/
ln -sf %{SOURCE36} src/
ln -sf %{SOURCE37} src/
ln -sf %{SOURCE38} src/
ln -sf %{SOURCE39} src/
ln -sf %{SOURCE40} src/
ln -sf %{SOURCE41} src/
ln -sf %{SOURCE42} src/
ln -sf %{SOURCE43} src/
ln -sf %{SOURCE44} src/
ln -sf %{SOURCE45} src/
ln -sf %{SOURCE46} src/
ln -sf %{SOURCE47} src/
ln -sf %{SOURCE48} src/
ln -sf %{SOURCE49} src/
ln -sf %{SOURCE50} src/
ln -sf %{SOURCE51} src/
ln -sf %{SOURCE52} src/
ln -sf %{SOURCE53} src/

ln -sf %{SOURCE71} src/
ln -sf %{SOURCE72} src/
ln -sf %{SOURCE73} src/
ln -sf %{SOURCE74} src/
ln -sf %{SOURCE75} src/
ln -sf %{SOURCE76} src/
ln -sf %{SOURCE77} src/
ln -sf %{SOURCE78} src/
ln -sf %{SOURCE79} src/
ln -sf %{SOURCE80} src/
ln -sf %{SOURCE81} src/
ln -sf %{SOURCE82} src/
ln -sf %{SOURCE83} src/
ln -sf %{SOURCE84} src/
ln -sf %{SOURCE85} src/
ln -sf %{SOURCE86} src/
ln -sf %{SOURCE91} src/
ln -sf %{SOURCE104} src/
ln -sf %{SOURCE106} src/
ln -sf %{SOURCE107} src/

if [ -x ./autogen.sh ]; then
	./autogen.sh --with-distro=%{distroname}
fi

%if %{use_ccache}
export CCACHE_DIR=%{ccachedir}
%endif

export ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing"
export ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden"
export ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"

%if %use_gcj
export JAVA=%java
export JAVAC=%javac
export ANT="%ant"
%endif

echo "Configure start at: "`date` >> ooobuildtime.log 
# --with-jdk-home=%java_home \

CFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing" \
CXXFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
%configure2_5x \
	--with-distro=%{distroname} \
	--with-vendor=Mandriva \
	--with-build-version="%{buildver}" \
	--disable-qadevooo \
	--enable-lockdown \
	--enable-opengl \
	--enable-odk \
	--enable-split-app-modules \
  	--enable-split-opt-features \
	--enable-binfilter \
	--with-system-mozilla=xulrunner \
	--with-system-hsqldb \
	--with-system-beanshell \
	--with-system-icu \
	--with-system-xrender-headers \
        --with-system-jpeg \
        --with-system-hunspell \
	--with-system-zlib \
	--with-system-openssl \
	--with-system-expat \
	--with-system-libxml \
	--with-system-python \
	--with-system-xslt \
	--with-system-curl \
	--with-system-vigra \
	--with-system-neon \
	--with-system-agg \
	--without-junit \
	--with-system-cppunit \
	--enable-broffice \
	--with-system-redland \
	--with-system-apache-commons \
	--disable-kde \
	--enable-kde4 \
	--with-git=no \
	--with-intro-bitmaps="%{SOURCE27}" \
	--with-about-bitmaps="%{SOURCE28}" \
%if %use_gcj
	--with-java-target-version=1.5 \
%else
	--with-jdk-home=$JAVA_HOME \
%endif
%if %{use_systemdb}
	--with-system-db \
%endif
%if %{use_systemboost}
	--with-system-boost \
%endif
	--with-lang=%{ooolangs} \
        --with-installed-ooo-dirname=ooo \
        --with-docdir=%{_datadir}/doc/packages/ooo \
	--with-system-sane-header \
	--with-system-cairo \
	--without-myspell-dicts \
	--with-system-dicts \
	--with-external-dict-dir=%{_datadir}/dict/ooo \
        --with-external-hyph-dir=%{_datadir}/dict/ooo \
        --with-external-thes-dir=%{_datadir}/dict/ooo \
	--with-system-poppler \
        --enable-pdfimport \
	--enable-minimizer \
	--enable-presenter-console \
        --enable-wiki-publisher \
%if %{use_openclipart}
        --with-openclipart=%{_datadir}/images/openclipart \
%endif
%if %{use_mono}
# dev300
	--enable-mono \
#	--with-mono-gac-root=%{_libdir} \
%endif
%if %{use_smp}
#dev300: (--with-num-cpus command not found  )
#	--with-num-cpus=${RPM_BUILD_NCPUS:-1}
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

# %make 
make \
	ARCH_FLAGS="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CC="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing" \
	ARCH_FLAGS_CXX="%{optflags} %{optsafe} -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden" \
	ARCH_FLAGS_OPT="%{optflags} -O2 %{optsafe}"

echo "Make end at: "`date` >> ooobuildtime.log 
echo "Install start at: "`date` >> ooobuildtime.log 

%install

# sbin due to icu stuff there
PATH=$PATH:/usr/sbin

# clear lists in case of short-circuiting:
rm -f build/*_list.txt

rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}/opt
# FIXME: there are template/<locale>wizard/letter already
#rm -rf %{buildroot}%{ooodir}/share/template/wizard/letter/

# use the dicts from myspell-<lang>
# rm -rf %{buildroot}%{ooodir}/share/dict/ooo
# ln -s %{_datadir}/dict/ooo %{buildroot}%{ooodir}/share/dict

# desktop files
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --add-mime-type="application/vnd.ms-works;application/x-msworks-wp;zz-application/zz-winassoc-wps" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/writer*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/calc*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Graphics" \
  --remove-category="VectorGraphics" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/draw*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/impress*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/math*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Network" \
  --remove-category="WebDevelopment" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/web*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/template*desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Database" \
  --add-category="Office" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/base*desktop

## MS OOXML (#36465)
desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.wordprocessingml.document" \
  --add-mime-type="application/vnd.ms-word.document.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/writer*desktop

desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  --add-mime-type="application/vnd.ms-excel.sheet.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/calc*desktop

desktop-file-install \
  --add-mime-type="application/vnd.openxmlformats-officedocument.presentationml.presentation" \
  --add-mime-type="application/vnd.ms-powerpoint.presentation.macroEnabled.12" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/impress*desktop

# fix permissions for stripping
find %{buildroot} -type f -exec chmod u+rw '{}' \;

# fix permission of .so libraries
find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod a+x '{}' \;

# Anssi patch
# remove /usr/bin/soffice (made with update-alternatives)
# rm -f %{buildroot}%{_bindir}/soffice

# Fix sdk listing
sort -u build/sdk_list.txt > build/sdk_list_fixed.txt

# Anssi patch
# Versionify bash_completion (ooo-wrapper.sh)
# if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh ]; then
# mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper.sh \
# 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooo-wrapper%{mdvsuffix}
# fi

# Versionify bash_completion (ooffice.sh)
# if [ -f %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice*.sh ]; then
# mv %{buildroot}%{_sysconfdir}/bash_completion.d/ooffice*.sh \
# 	%{buildroot}%{_sysconfdir}/bash_completion.d/ooffice%{mdvsuffix}
# fi

# dev 300 2.3 ???
# %if %{use_mono}
# Versionify mono-ooo.pc
# mv %{buildroot}%{_libdir}/pkgconfig/mono-ooo-%{mdvsuffix}.pc \
#   %{buildroot}%{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
# %endif

# Install versioned profile.d/ files (#33475)
# Profiles for set PYTHONPATH variables (Python Integration)
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.csh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org.csh
sed 's@%%{ooodir}@%{ooodir}@g' \
	%{_sourcedir}/openoffice.org.sh > \
	%{buildroot}%{_sysconfdir}/profile.d/openoffice.org.sh
# Anssi 
# Install a random UNO extension into BUILDROOT and remove it, so that unopkg
# creates the cache directories and files that can then be ghostified.
# Simple "list" would create everything but files inside
# "com.sun.star.comp.deployment.component.PackageRegistryBackend".
# Note that this has to be run before below bro calls below that rename needed
# files and thus disable unopkg for the rest of install stage.
# First make sure there is no actual data pre-existing in this directory,
# as that will be lost due to the ghostification:
[ $(find %{buildroot}%{ooodir}/share/uno_packages/cache | wc -l) -eq 1 ]
%{buildroot}%{ooodir}/program/unopkg add --shared %{_builddir}/libreoffice-build-%{buildver}/build/libreoffice-%{buildver}/solver/330/unxlng*/bin/pdfimport/pdfimport.oxt
%{buildroot}%{ooodir}/program/unopkg remove --shared pdfimport.oxt
# clean cache
%{buildroot}%{ooodir}/program/unopkg list --shared
# # there should be more files now:
# [ $(find %{buildroot}%{ooodir}/share/uno_packages/cache | wc -l) -ge 5 ]
# for path in $(find %{buildroot}%{ooodir}/share/uno_packages/cache/); do
#       if [ -d $path ]; then
#               echo "%%dir ${path#%{buildroot}}" >> build/common_list.txt
#       else
#               echo "%%ghost ${path#%{buildroot}}" >> build/common_list.txt
#       fi
# done

## libreoffice provided with feature --enable-broffice
#  # BrOffice.org Support (install)
#  function bro() {
#     exp="$1"
#     f="$2"
#     mv "%{buildroot}$f" "%{buildroot}$f.ooo"
#     echo -n > "%{buildroot}$f"
#    %if %l10n
#     sed "$exp" "%{buildroot}$f.ooo" > "%{buildroot}$f.bro"
#    %endif
#    sed -i "s@$f\$@$f.ooo@" %{_builddir}/libreoffice-build-%{buildver}/build/*.txt
#  }
#  
#  ## Change suite name in the program itself
#  bro "s/OpenO/BrO/;s/openo/bro/" %{ooodir}/program/bootstraprc
#  bro "s/en-US/pt-BR/;s/openo/bro/" %{ooodir}/program/versionrc
#  bro "s/OpenO/BrO/" %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu
#  
#  # Change the suite name in .desktop files for pt_BR locale
#  sed -i '/pt_BR/{s/OpenO/BrO/}' %{buildroot}%{_datadir}/applications/*.desktop
#  
#  # Place symlinks br<app> -> oo<app>
#  %if %l10n
#  cd %{buildroot}%{_bindir}
#  # fix me wrong brffice symb link name 
#  for i in oo*; do
#  	ln -s $i ${i/oo/br}
#  done
#  cd -
#  %endif
#  # End of BrOffice support (install)

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

# new icons
tar xjf %{SOURCE30} -C %{buildroot}%{_datadir}

# remove icons we dont have these sizes yet
rm -rf %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/*
rm -rf %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/*

# remove scalables icons since we dont have yet
rm -rf %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*

# XXX disable the menu entries for these
# besides not being real apps, we don't have new-style icons for them
# see #26311#c33
for f in %{buildroot}%{_datadir}/applications/template*desktop \
	%{buildroot}%{_datadir}/applications/web*desktop; do
	echo 'NoDisplay=true' >> $f
done

# libre
# Fixes japanese translations on desktop files
## patch -p0 -d %{buildroot} < %{SOURCE102}

# templates for kde "create new" context menu
tar xjf %{SOURCE31} -C %{buildroot}%{_datadir}

# copy extensions 
install -d -m755 %{buildroot}%{ooodir}/extensions
cp %{_builddir}/libreoffice-build-%{buildver}/build/libreoffice-%{buildver}/solver/330/unxlng*/bin/pdfimport/pdfimport.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-build-%{buildver}/build/libreoffice-%{buildver}/solver/330/unxlng*/bin/presenter/presenter-screen.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-build-%{buildver}/build/libreoffice-%{buildver}/solver/330/unxlng*/bin/swext/wiki-publisher.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-build-%{buildver}/build/libreoffice-%{buildver}/solver/330/unxlng*/bin/minimizer/presentation-minimizer.oxt %{buildroot}%{ooodir}/extensions/

#fixes #56439
sed -i 's/^Icon=.*$/Icon=ooo-calc/' %{buildroot}%{_datadir}/templates/ooo-spreadsheet.desktop
sed -i 's/^Icon=.*$/Icon=ooo-writer/' %{buildroot}%{_datadir}/templates/ooo-text.desktop
sed -i 's/^Icon=.*$/Icon=ooo-impress/' %{buildroot}%{_datadir}/templates/ooo-presentation.desktop
sed -i 's/^Icon=.*$/Icon=ooo-draw/' %{buildroot}%{_datadir}/templates/ooo-drawing.desktop

# Remove version on names so better position on menu 
# and to give consistency under old links #43922, #57700
for dskt in base calc draw impress math template web writer ooo-extension-manager startcenter; do 
     mv %{buildroot}%{_datadir}/applications/${dskt}3.3.desktop %{buildroot}%{_datadir}/applications/${dskt}.desktop
done;

# Get rid of the version at the name of unopkg script #57700
mv %{buildroot}%{_bindir}/unopkg3.3 %{buildroot}%{_bindir}/unopkg
mv %{buildroot}%{_mandir}/man1/unopkg3.3.1 %{buildroot}%{_mandir}/man1/unopkg.1
# for m in %{buildroot}%{_mandir}/man1/unopkg%version.1*; do
#      mv $m `echo $m | sed 's/unopkg%version/unopkg/'`
# done; 

#temp 
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/writer.desktop
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/calc.desktop
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/base.desktop
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/impress.desktop
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/draw.desktop
sed -i 's/^Exec=oo/Exec=lo/' %{buildroot}%{_datadir}/applications/math.desktop

%clean
rm -rf %{buildroot}

%post common
# <mrl> Bogus versioning in previous alternatives setup forces us to do this
# We can safelly remove it, as we are obsoleting that version anyway.
/usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice2.1 || :
# We changed the master name here.
/usr/sbin/update-alternatives --remove ooffice %{_bindir}/ooffice2.3 || :

#dev300: including basis3.0 before program
# alternatives names follows oobr_<filename> mark, making it explicit.
 /usr/sbin/update-alternatives \
	--install %{ooodir}/program/bootstraprc oobr_bootstraprc \
		%{ooodir}/program/bootstraprc.ooo 1 \
	--slave %{ooodir}/program/versionrc oobr_versionrc \
		%{ooodir}/program/versionrc.ooo
#	--slave %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu \
#		%{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu.ooo
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post

%{update_desktop_database}
%update_icon_cache gnome
%update_icon_cache hicolor

# Remove ooobuildtime.log misplaced file
if [ -f /ooobuildtime.log ]; then
      mkdir -p /tmp/ooo.tmp.mdv.rc2/
      mv /ooobuildtime.log /tmp/ooo.tmp.mdv.rc2/
      rm -r /tmp/ooo.tmp.mdv.rc2/
fi

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

# BrOffice support %postun common
 if [ ! -e "%{ooodir}/program/bootstraprc.ooo" ]; then
       /usr/sbin/update-alternatives --remove oobr_bootstraprc %{ooodir}/program/bootstraprc.ooo
 fi
# End of BrOffice support %postun common
%{clean_desktop_database}
%clean_icon_cache gnome
%clean_icon_cache hicolor

# Firefox plugin
if [ $1 -eq 0 ]
then
  update-alternatives --remove %{firefox_plugin} \
  %{ooodir}/program/libnpsoplugin.so
fi

%if %l10n
%post l10n-pt_BR
# BrOffice support %post l10n-pt_BR
# alternatives names follows oobr_<filename> mark, making it explicit.
 /usr/sbin/update-alternatives \
	--install %{ooodir}/program/bootstraprc oobr_bootstraprc \
		%{ooodir}/program/bootstraprc.bro 2 \
	--slave %{ooodir}/program/versionrc oobr_versionrc \
		%{ooodir}/program/versionrc.bro \
	--slave %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu oobr_Setup.xcu \
		%{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu.bro
# Always do this configuration, as the switch should be transparent.
/usr/sbin/update-alternatives --auto oobr_bootstraprc
# End of BrOffice support %post l10n-pt_BR

# %{update_desktop_database}

%postun l10n-pt_BR
# BrOffice support %postun l10n-pt_BR
 if [ ! -e "%{ooodir}/program/bootstraprc.bro" ]; then
        /usr/sbin/update-alternatives --remove oobr_bootstraprc %{ooodir}/program/bootstraprc.bro
 fi
# End of BrOffice support %postun l10n-pt_BR

%{clean_desktop_database}
%endif

%post base
%{update_desktop_database}
%postun base
%{clean_desktop_database}
%post calc
%{update_desktop_database}
%postun calc
%{clean_desktop_database}
%post draw
%{update_desktop_database}
%postun draw
%{clean_desktop_database}
%post impress
%{update_desktop_database}
%postun impress
%{clean_desktop_database}
%post math
%{update_desktop_database}
%postun math
%{clean_desktop_database}
%post writer
%{update_desktop_database}
%postun writer
%{clean_desktop_database}

%post pdfimport
# upgrade 
if [ $1 -ge 2 ];then
	# removes old installed pdfimport extension 
	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
	if [ "z$idpdfimport" != "z" ]; then
		%unopkg remove --shared $idpdfimport 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

#install new pdfimport version
%unopkg add --shared %{ooodir}/extensions/pdfimport.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

#uninstall
%preun pdfimport 
if [ $1 -eq 0 ];then
	idpdfimport=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PDFImport-linux.*\)/\1/p');
	if [ "z$idpdfimport" != "z" ]; then
		%unopkg remove --shared $idpdfimport 2> /dev/null
		#clean footprint cache
		%unopkg list --shared &> /dev/null
	fi
fi

%post presenter-screen
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi
#install 
%unopkg add --shared %{ooodir}/extensions/presenter-screen.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 


%preun presenter-screen  
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.PresenterScreen-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

# %post report-builder
# upgrade 
# if [ $1 -ge 1 ];then
#	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.reportdesigner\)/\1/p');
#	if [ "z$idextension" != "z" ]; then
#		%unopkg remove --shared $idextension 2> /dev/null
#		%unopkg list --shared &> /dev/null
#	fi
# fi
#install 
# %unopkg add --shared %{ooodir}/sun-report-builder.oxt 2> /dev/null
# %unopkg list --shared &> /dev/null 

#uninstall
# %preun report-builder
# if [ $1 -eq 0 ];then
#	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.reportdesigner\)/\1/p');
#	if [ "z$idextension" != "z" ]; then
#		%unopkg remove --shared $idextension 2> /dev/null
#		%unopkg list --shared &> /dev/null
#	fi
# fi

%post wiki-publisher
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi	
#install 
%unopkg add --shared %{ooodir}/extensions/wiki-publisher.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

%preun wiki-publisher
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.wiki-publisher\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

%post presentation-minimizer
# upgrade 
if [ $1 -ge 2 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi
#install 
%unopkg add --shared %{ooodir}/extensions/sun-presentation-minimizer.oxt 2> /dev/null
%unopkg list --shared &> /dev/null 

%preun presentation-minimizer
if [ $1 -eq 0 ];then
	idextension=$(%unopkg list --shared 2> /dev/null | sed -ne 's/^Identifier: \(com.sun.star.PresentationMinimizer-linux.*\)/\1/p');
	if [ "z$idextension" != "z" ]; then
		%unopkg remove --shared $idextension 2> /dev/null
		%unopkg list --shared &> /dev/null
	fi
fi

%files

%files base -f build/base_list.txt
%{_bindir}/lobase3.3
%{_mandir}/man1/lobase3.3.1*
%{_datadir}/applications/base.desktop

%files calc -f build/calc_list.txt
%{_bindir}/localc3.3
%{_datadir}/templates/ooo-spreadsheet.desktop
%{_datadir}/templates/.source/ooo-spreadsheet.ods
%{_mandir}/man1/localc3.3.1*
%{_datadir}/applications/calc.desktop

%files common -f build/common_list.txt 
%{_sysconfdir}/bash_completion.d/libreoffice3.3.sh
%{_sysconfdir}/profile.d/openoffice.org.*
%{_bindir}/ooconfig3.3
%{_bindir}/libreoffice3.3
%{_bindir}/lofromtemplate3.3
%{_bindir}/ootool3.3
%{_bindir}/soffice3.3
#ooo3.2
## %{ooodir}/%basis/program/OGLTrans.uno.so
## %{ooodir}/%basis/share/config/soffice.cfg/simpress/transitions-ogl.xml
## %{ooodir}/%basis/share/registry/modules/org/openoffice/Office/Impress/Impress-ogltrans.xcu

%{_datadir}/applications/template*.desktop
%{_datadir}/applications/startcenter.desktop

%{_datadir}/icons/hicolor/*/apps/ooo-base3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-calc3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-draw3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-gulls3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-impress3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-math3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-printeradmin3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-template3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-web3.3.*
%{_datadir}/icons/hicolor/*/apps/ooo-writer3.3.*

%{_datadir}/icons/hicolor/*/apps/ooo-base.*
%{_datadir}/icons/hicolor/*/apps/ooo-calc.*
%{_datadir}/icons/hicolor/*/apps/ooo-draw.*
%{_datadir}/icons/hicolor/*/apps/ooo-impress.*
%{_datadir}/icons/hicolor/*/apps/ooo-math.*
%{_datadir}/icons/hicolor/*/apps/ooo-printeradmin.*
%{_datadir}/icons/hicolor/*/apps/ooo-writer.*

%{_datadir}/icons/hicolor/*/apps/ooo-main.*

# new icons
# %{_datadir}/icons/hicolor/*/apps/openofficeorg3-*.png
# moved to mandriva-kde-config 
#%{_datadir}/icons/hicolor/*/mimetypes/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/apps/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/mimetypes/openofficeorg3-*.png
%{_datadir}/pixmaps/ooo-base3.3.png
%{_datadir}/pixmaps/ooo-calc3.3.png
%{_datadir}/pixmaps/ooo-draw3.3.png
%{_datadir}/pixmaps/ooo-gulls3.3.png
%{_datadir}/pixmaps/ooo-impress3.3.png
%{_datadir}/pixmaps/ooo-math3.3.png
%{_datadir}/pixmaps/ooo-template3.3.png
%{_datadir}/pixmaps/ooo-web3.3.png
%{_datadir}/pixmaps/ooo-writer3.3.png
# %{_mandir}/man1/looffice3.3.1*
%{_mandir}/man1/lofromtemplate3.3.1*
%{_mandir}/man1/libreoffice3.3.1*
%{_datadir}/mime
# XXX Due to alternatives upgrade from 2.3.0.5-1mdv to -2mdv
# (.desktop files are not included because they are in their
# respective subpackages already (#38412))

#dev300 
# %ghost %{ooodir}/share/uno_packages
# %ghost %{ooodir}/program/bootstraprc
# %ghost %{ooodir}/program/versionrc
# %ghost %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu

%{_bindir}/unopkg
%{_mandir}/man1/unopkg.1*
%{_datadir}/applications/ooo-extension-manager*.desktop

# Anssi 
%dir %{ooodir}/extensions

%files core -f build/core_list.txt

%files devel -f build/sdk_list_fixed.txt

%files devel-doc -f build/sdk_doc_list.txt

%files draw -f build/draw_list.txt
%{_bindir}/lodraw3.3
%{_datadir}/applications/draw.desktop

%{_datadir}/templates/ooo-drawing.desktop
%{_datadir}/templates/.source/ooo-drawing.odg
%{_mandir}/man1/lodraw3.3.1*

# dev300: 
# %files dtd-officedocument1.0 -f build/dtd_list.txt

# dev300: 
%files filter-binfilter -f build/filter-binfilter_list.txt

%files gnome -f build/gnome_list.txt

%files impress -f build/impress_list.txt
%{_bindir}/loimpress3.3
%{_datadir}/applications/impress.desktop
%{_datadir}/templates/ooo-presentation.desktop
%{_datadir}/templates/.source/ooo-presentation.odp
%{_mandir}/man1/loimpress3.3.1*

%files java-common -f build/java_common_list.txt

%files kde4 -f build/kde4_list.txt

%files math -f build/math_list.txt
%{_bindir}/lomath3.3
%{_datadir}/applications/math.desktop
%{_mandir}/man1/lomath3.3.1*

%files openclipart -f build/gallery_list.txt

%files pyuno -f build/pyuno_list.txt

#%files qa-api-tests
#%{ooodir}/qadevOOo

%files testtool -f build/testtool_list.txt

%files style-galaxy
%{ooodir}/%basis/share/config/images.zip

%files style-crystal
%{ooodir}/%basis/share/config/images_crystal.zip

%files style-hicontrast
%{ooodir}/%basis/share/config/images_hicontrast.zip
#libre
# %files style-industrial
# %{ooodir}/%basis/share/config/images_industrial.zip

%files style-tango
%{ooodir}/%basis/share/config/images_tango.zip

%files style-oxygen
%{ooodir}/%basis/share/config/images_oxygen.zip

%files writer -f build/writer_list.txt
%{_bindir}/loweb3.3
%{_bindir}/lowriter3.3
%{_datadir}/applications/writer.desktop
%{_datadir}/applications/web.desktop
%{_datadir}/templates/ooo-text.desktop
%{_datadir}/templates/.source/ooo-text.odt
%{_mandir}/man1/loweb3.3.1*
%{_mandir}/man1/lowriter3.3.1*

%if %{use_mono}
%files mono -f build/mono_list.txt
%defattr(-,root,root)
%{_libdir}/pkgconfig/mono-ooo.pc
# %{_libdir}/pkgconfig/mono-ooo%{mdvsuffix}-2.3.pc
# %{_libdir}/mono/*/*/*
# %{_libdir}/mono/ooo-%{mdvsuffix}
%endif

%files pdfimport
%defattr(-,root,root,-)
%{ooodir}/extensions/pdfimport.oxt

%files presenter-screen
%defattr(-,root,root,-)
%{ooodir}/extensions/presenter-screen.oxt

# %files report-builder
# %defattr(-,root,root,-)
# %{ooodir}/sun-report-builder.oxt

%files wiki-publisher
%defattr(-,root,root,-)
%{ooodir}/extensions/wiki-publisher.oxt

%files presentation-minimizer
%defattr(-,root,root,-)
%{ooodir}/extensions/presentation-minimizer.oxt

%if %l10n
%files l10n-it -f build/lang_it_list.txt
%defattr(-,root,root)

%files l10n-af -f build/lang_af_list.txt
%defattr(-,root,root)

%files l10n-ar -f build/lang_ar_list.txt
%defattr(-,root,root)

%files l10n-bg -f build/lang_bg_list.txt
%defattr(-,root,root)

%files l10n-br -f build/lang_br_list.txt
%defattr(-,root,root)

%files l10n-bs -f build/lang_bs_list.txt
%defattr(-,root,root)

%files l10n-ca -f build/lang_ca_list.txt
%defattr(-,root,root)

%files l10n-cs -f build/lang_cs_list.txt
%defattr(-,root,root)

%files l10n-cy -f build/lang_cy_list.txt
%defattr(-,root,root)

%files l10n-da -f build/lang_da_list.txt
%defattr(-,root,root)

%files l10n-de -f build/lang_de_list.txt
%defattr(-,root,root)

%files l10n-el -f build/lang_el_list.txt
%defattr(-,root,root)

%files l10n-en_GB -f build/lang_en_GB_list.txt
%defattr(-,root,root)

%files l10n-es -f build/lang_es_list.txt
%defattr(-,root,root)

%files l10n-et -f build/lang_et_list.txt
%defattr(-,root,root)

%files l10n-eu -f build/lang_eu_list.txt
%defattr(-,root,root)

%files l10n-fi -f build/lang_fi_list.txt
%defattr(-,root,root)

%files l10n-fr -f build/lang_fr_list.txt
%defattr(-,root,root)

%files l10n-he -f build/lang_he_list.txt
%defattr(-,root,root)

%files l10n-hi -f build/lang_hi_list.txt
%defattr(-,root,root)

%files l10n-hu -f build/lang_hu_list.txt
%defattr(-,root,root)

%files l10n-ja -f build/lang_ja_list.txt
%defattr(-,root,root)

%files l10n-ko -f build/lang_ko_list.txt
%defattr(-,root,root)

%files l10n-mk -f build/lang_mk_list.txt
%defattr(-,root,root)

%files l10n-nb -f build/lang_nb_list.txt
%defattr(-,root,root)

%files l10n-nl -f build/lang_nl_list.txt
%defattr(-,root,root)

%files l10n-nn -f build/lang_nn_list.txt
%defattr(-,root,root)

%files l10n-pl -f build/lang_pl_list.txt
%defattr(-,root,root)

%files l10n-pt -f build/lang_pt_list.txt
%defattr(-,root,root)

%files l10n-pt_BR -f build/lang_pt_BR_list.txt
%defattr(-,root,root)
# BrOffice support
# XXX Yes, by this way there will be broken symlinks if you don't make a full suite
# installation.
# %{_bindir}/br*
# %{ooodir}/program/bootstraprc.bro
# %{ooodir}/program/versionrc.bro
# %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu.bro
# %ghost %{ooodir}/program/bootstraprc
# %ghost %{ooodir}/program/versionrc
# %ghost %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu

%files l10n-pt_AO -f build/lang_pt_AO_list.txt
%defattr(-,root,root)

%files l10n-ru -f build/lang_ru_list.txt
%defattr(-,root,root)

%files l10n-sk -f build/lang_sk_list.txt
%defattr(-,root,root)

%files l10n-sl -f build/lang_sl_list.txt
%defattr(-,root,root)

%files l10n-sv -f build/lang_sv_list.txt
%defattr(-,root,root)

%files l10n-ta -f build/lang_ta_list.txt
%defattr(-,root,root)

%files l10n-tr -f build/lang_tr_list.txt
%defattr(-,root,root)

%files l10n-zh_CN -f build/lang_zh_CN_list.txt
%defattr(-,root,root)

%files l10n-zh_TW -f build/lang_zh_TW_list.txt
%defattr(-,root,root)

%files l10n-zu -f build/lang_zu_list.txt
%defattr(-,root,root)

%files help-it -f build/help_it_list.txt
%defattr(-,root,root)

%files help-af -f build/help_af_list.txt
%defattr(-,root,root)

%files help-ar -f build/help_ar_list.txt
%defattr(-,root,root)

%files help-bg -f build/help_bg_list.txt
%defattr(-,root,root)

%files help-br -f build/help_br_list.txt
%defattr(-,root,root)

%files help-bs -f build/help_bs_list.txt
%defattr(-,root,root)

%files help-ca -f build/help_ca_list.txt
%defattr(-,root,root)

%files help-cs -f build/help_cs_list.txt
%defattr(-,root,root)

%files help-cy -f build/help_cy_list.txt
%defattr(-,root,root)

%files help-da -f build/help_da_list.txt
%defattr(-,root,root)

%files help-de -f build/help_de_list.txt
%defattr(-,root,root)

%files help-el -f build/help_el_list.txt
%defattr(-,root,root)

%files help-en_GB -f build/help_en_GB_list.txt
%defattr(-,root,root)

%files help-es -f build/help_es_list.txt
%defattr(-,root,root)

%files help-et -f build/help_et_list.txt
%defattr(-,root,root)

%files help-eu -f build/help_eu_list.txt
%defattr(-,root,root)

%files help-fi -f build/help_fi_list.txt
%defattr(-,root,root)

%files help-fr -f build/help_fr_list.txt
%defattr(-,root,root)

%files help-he -f build/help_he_list.txt
%defattr(-,root,root)

%files help-hi -f build/help_hi_list.txt
%defattr(-,root,root)

%files help-hu -f build/help_hu_list.txt
%defattr(-,root,root)

%files help-ja -f build/help_ja_list.txt
%defattr(-,root,root)

%files help-ko -f build/help_ko_list.txt
%defattr(-,root,root)

%files help-mk -f build/help_mk_list.txt
%defattr(-,root,root)

%files help-nb -f build/help_nb_list.txt
%defattr(-,root,root)

%files help-nl -f build/help_nl_list.txt
%defattr(-,root,root)

%files help-nn -f build/help_nn_list.txt
%defattr(-,root,root)

%files help-pl -f build/help_pl_list.txt
%defattr(-,root,root)

%files help-pt -f build/help_pt_list.txt
%defattr(-,root,root)

%files help-pt_BR -f build/help_pt_BR_list.txt
%defattr(-,root,root)

%files help-pt_AO -f build/help_pt_AO_list.txt
%defattr(-,root,root)

%files help-ru -f build/help_ru_list.txt
%defattr(-,root,root)

%files help-sk -f build/help_sk_list.txt
%defattr(-,root,root)

%files help-sl -f build/help_sl_list.txt
%defattr(-,root,root)

%files help-sv -f build/help_sv_list.txt
%defattr(-,root,root)

%files help-ta -f build/help_ta_list.txt
%defattr(-,root,root)

%files help-tr -f build/help_tr_list.txt
%defattr(-,root,root)

%files help-zh_CN -f build/help_zh_CN_list.txt
%defattr(-,root,root)

%files help-zh_TW -f build/help_zh_TW_list.txt
%defattr(-,root,root)

%files help-zu -f build/help_zu_list.txt
%defattr(-,root,root)

%files help-en_US -f build/help_en_US_list.txt
%defattr(-,root,root)
%endif

