%define _enable_debug_packages %{nil}
%define debug_package          %{nil}
%undefine debug_package_and_restore

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

%define version	        3.4.3
%define release		%mkrel 2

%define buildver     	3.4.3.2
%define basis           basis3.4
%define jdkver		1_5_0_11
%define ooodir		%{_libdir}/libreoffice
%define libdbver	4.2
%if %l10n
%define langs	"en-US af ar as bg bn br bs ca cs cy da de dz el en-GB es et eu fa fi fr ga gl gu he hi hr hu it ja ko kn lt lv mai mk ml mr nb nl nn nr nso or pa-IN pl pt pt-BR ro ru sh si sk sl sr ss st sv ta te th tn tr ts uk ve xh zh-TW zh-CN zu"
%else
%define langs	"en-US"
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

# main cleanup
%define use_openclipart	0
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
Epoch:		1
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
# Provides:       openoffice.org = 1:3.3-1:2011.0

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
BuildRequires:	imagemagick
BuildRequires:	db1-devel
%if %{use_systemdb}
%if %mdkversion < 201020
# this is pulled by db-devel >= 4.8, and libdbcxx?.? does not provide libdbcxx at all
BuildRequires:	libdbcxx >= 4.2.5-4mdk
%endif
BuildRequires:	db-devel >= 4.2.5-4mdk
%else
BuildConflicts: libdbjava4.2
%endif
# BuildRequires:	bsh
BuildRequires:	curl-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libsvg-devel
BuildRequires:	libgstreamer-plugins-base-devel
BuildRequires:	xaw-devel
BuildRequires:	openldap-devel
BuildRequires:	portaudio0-devel >= 18.1
BuildRequires:	sndfile-devel
BuildRequires:	unixODBC-devel
BuildRequires:	libxp-devel
BuildRequires:	libxslt-proc >= 1.0.19
BuildRequires:	libxslt-devel
BuildRequires:	libxml2-devel >= 2.4.23
%if %{use_mono}
BuildRequires:	mono-devel
BuildRequires:	mono-data-sqlite
%endif
# dev 300 (retirar essa require)
# BuildRequires:	mozilla-firefox-devel
BuildRequires:	nss-devel
BuildRequires:	nspr-devel
BuildRequires:	nas-devel
BuildRequires:	neon-devel >= 0.27
BuildRequires:	pam-devel
BuildRequires:	perl
BuildRequires:	perl-Archive-Zip
BuildRequires:	perl-MDK-Common
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	python-devel
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
BuildRequires:	hsqldb
%if %mdkversion >=201100
BuildRequires:	libwpd-devel >= 0.9.0
%else
BuildRequires:	libwpd-devel
%endif
BuildRequires:	libwpg-devel
BuildRequires:	libwps-devel
BuildRequires:	icu
BuildRequires:  icu-devel

# main cleanup
# BuildRequires:	libmdbtools-devel

# BuildRequires:  ant-apache-regexp
BuildRequires:  xulrunner-devel
BuildRequires:  libvigra-devel
BuildRequires:  hunspell-devel
#pdfimport extension
BuildRequires:	libpoppler-devel
BuildRequires:	libxtst-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mesaglu-devel
BuildRequires:  qt4-devel
BuildRequires:  task-kde4-devel
BuildRequires:  cppunit-devel
BuildRequires:  redland-devel
BuildRequires:  jakarta-commons-codec
BuildRequires:  jakarta-commons-lang
BuildRequires:  jakarta-commons-httpclient
BuildRequires:  graphite2-devel
BuildRequires:  textcat-devel
BuildRequires:	python-translate >= 1.9.0
# STLport-devel 4.5 + private patches are needed
BuildConflicts:	STLport-devel

# BuildRequires:  jakarta-commons-logging

####################################################################
#
# Sources
#
####################################################################
Source0:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-artwork-%{buildver}.tar.%{oootarext}
Source1:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-base-%{buildver}.tar.%{oootarext}
Source2:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-bootstrap-%{buildver}.tar.%{oootarext}
Source3:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-calc-%{buildver}.tar.%{oootarext}
Source4:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-components-%{buildver}.tar.%{oootarext}
Source5: 	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-extensions-%{buildver}.tar.%{oootarext}
Source6:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-extras-%{buildver}.tar.%{oootarext}
Source7:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-filters-%{buildver}.tar.%{oootarext}
Source8:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-help-%{buildver}.tar.%{oootarext}
Source9:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-impress-%{buildver}.tar.%{oootarext}
Source10:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-core-%{buildver}.tar.%{oootarext}
Source11:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-extern-%{buildver}.tar.%{oootarext}
Source12:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-extern-sys-%{buildver}.tar.%{oootarext}
Source13:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-libs-gui-%{buildver}.tar.%{oootarext}
Source14:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-postprocess-%{buildver}.tar.%{oootarext}
Source15:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-sdk-%{buildver}.tar.%{oootarext}
Source16:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-testing-%{buildver}.tar.%{oootarext}
Source17:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-ure-%{buildver}.tar.%{oootarext}
Source18:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-writer-%{buildver}.tar.%{oootarext}
Source19:	 http://download.documentfoundation.org/libreoffice/src/%{ooname}-translations-%{buildver}.tar.%{oootarext}

Source20: 	Mandriva-Rosa_Icons.tar.bz2

Source31:       http://download.go-oo.org/DEV300/ooo_oxygen_images-2009-06-17.tar.gz
Source32: 	http://hg.services.openoffice.org/binaries/fdb27bfe2dbe2e7b57ae194d9bf36bab-SampleICC-1.3.2.tar.gz
Source36: 	http://download.go-oo.org/src/0ff7d225d087793c8c2c680d77aac3e7-mdds_0.5.3.tar.bz2
Source37: 	http://download.go-oo.org/src/0f63ee487fda8f21fafa767b3c447ac9-ixion-0.2.0.tar.gz
Source38:	http://hg.services.openoffice.org/binaries/067201ea8b126597670b5eff72e1f66c-mythes-1.2.0.tar.gz
Source39: 	http://download.go-oo.org/extern/185d60944ea767075d27247c3162b3bc-unowinreg.dll
Source40: 	http://hg.services.openoffice.org/binaries/48d8169acc35f97e05d8dcdfd45be7f2-lucene-2.3.2.tar.gz
Source42:	http://hg.services.openoffice.org/binaries/2a177023f9ea8ec8bd00837605c5df1b-jakarta-tomcat-5.0.30-src.tar.gz
Source43: 	http://hg.services.openoffice.org/binaries/284e768eeda0e2898b0d5bf7e26a016e-raptor-1.4.18.tar.gz
Source44:	http://hg.services.openoffice.org/binaries/fca8706f2c4619e2fa3f8f42f8fc1e9d-rasqal-0.9.16.tar.gz 
Source45:	http://hg.services.openoffice.org/binaries/1756c4fa6c616ae15973c104cd8cb256-Adobe-Core35_AFMs-314.tar.gz
Source46:	http://hg.services.openoffice.org/binaries/1f24ab1d39f4a51faf22244c94a6203f-xmlsec1-1.2.14.tar.gz	
Source47:	http://hg.services.openoffice.org/binaries/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
Source48:	http://hg.services.openoffice.org/binaries/798b2ffdc8bcfe7bca2cf92b62caf685-rhino1_5R5.zip
Source49:	http://hg.services.openoffice.org/binaries/35c94d2df8893241173de1d16b6034c0-swingExSrc.zip
Source50:	http://hg.services.openoffice.org/binaries/48a9f787f43a09c0a9b7b00cd1fddbbf-hyphen-2.7.1.tar.gz
Source51:	http://hg.services.openoffice.org/binaries/26b3e95ddf3d9c077c480ea45874b3b8-lp_solve_5.5.tar.gz
Source52:	http://hg.services.openoffice.org/binaries/3c219630e4302863a9a83d0efde889db-commons-logging-1.1.1-src.tar.gz	
Source54:	http://hg.services.openoffice.org/binaries/ada24d37d8d638b3d8a9985e80bc2978-source-9.0.0.7-bj.zip
Source55:	http://download.go-oo.org/src/ea570af93c284aa9e5621cd563f54f4d-bsh-2.0b1-src.tar.gz
Source56:	http://hg.services.openoffice.org/binaries/18f577b374d60b3c760a3a3350407632-STLport-4.5.tar.gz

Patch4:		xulrunner-to-mozila-plugin.pc.diff
Patch5:		mdv-sysui-disableslack.diff
Patch9:		vbahelper.visibility.patch 
Patch10:    	disable-qtunixeventloop.patch

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
Suggests: %{name}-java-common = %{EVRD}
# Due to the split
Conflicts: openoffice.org <= 2.2.1
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-base < 1:3.3-1:2011.0 
# Provides:  openoffice.org-base = 1:3.3-1:2011.0
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
# Provides:  openoffice.org-calc = 1:3.3-1:2011.0
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
Suggests: %{name}-java-common = %{EVRD}
Suggests: %{name}-help-en_US = %{EVRD}
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
# Provides:  openoffice.org-common = 1:3.3-1:2011.0
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.1.0
Conflicts: openoffice.org64-devel <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-math <= 2.3.0.5-1mdv
Conflicts: openoffice.org64-core <= 2.3.99.4-1mdv
Conflicts: openoffice.org64-gnome < 3.0svn13581-2mdv
Obsoletes: openoffice.org64-common <= 1:3.1-4
%endif
Conflicts: %{name}-common = 1:3.2-rc4.0

# Upstream dropped this packages in 3.4
Obsoletes: %{name}-l10n-pt_AO = 1:3.3.2-1
Obsoletes: %{name}-help-pt_AO = 1:3.3.2-1
Obsoletes: %{name}-help-ta    = 1:3.3.2-1
Obsoletes: %{name}-help-zu    = 1:3.3.2-1
Obsoletes: %{name}-help-cy    = 1:3.3.2-1
Obsoletes: %{name}-help-ar    = 1:3.3.2-1
Obsoletes: %{name}-help-af    = 1:3.3.2-1
Obsoletes: %{name}-help-br    = 1:3.3.2-1

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
# Provides:  openoffice.org-core = 1:3.3-1:2011.0
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
Obsoletes: openoffice.org-devel < 1:3.3-1:2011.0 

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
Obsoletes: openoffice.org-devel-doc < 1:3.3-1:2011.0 

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
# Provides:  openoffice.org-draw = 1:3.3-1:2011.0
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
Obsoletes: openoffice.org-filter-binfilter < 1:3.3-1:2011.0 
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
# Provides:  openoffice.org-gnome = 1:3.3-1:2011.0
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
# Provides:  openoffice.org-impress = 1:3.3-1:2011.0
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
# Provides:  openoffice.org-kde4 = 1:3.3-1:2011.0
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
#Provides:  openoffice.org-java-common = 1:3.3-1:2011.0
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
#Provides:  openoffice.org-math = 1:3.3-1:2011.0
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
Conflicts: openoffice.org <= 2.2.1
Obsoletes: openoffice.org-galleries <= 2.2.1
Obsoletes: openoffice.org-openclipart < 1:3.3-1:2011.0 
%ifarch x86_64
Conflicts: openoffice.org64 <= 2.2.1
Obsoletes: openoffice.org64-galleries <= 2.2.1
Obsoletes: openoffice.org64-openclipart <= 1:3.1-4
%endif

%description openclipart
LibreOffice is a full-featured office productivity suite that provides a
near drop-in replacement for Microsoft(R) Office.

This package contains the LibreOffice Open Clipart data, including images
and sounds.

%package pyuno
Group: Office
Summary: Python bindings for UNO library
Requires: %{name}-core = %{EVRD}
Requires: %{name}-common = %{EVRD}
Conflicts: openoffice.org-common <= 2.3.0.5-1mdv
Obsoletes: openoffice.org-pyuno < 1:3.3-1:2011.0 
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
Obsoletes: openoffice.org-testtool < 1:3.3-1:2011.0 
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
#Provides:  openoffice.org-style-galaxy = 1:3.3-1:2011.0
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
#Provides:  openoffice.org-style-crystal = 1:3.3-1:2011.0
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
#Provides:  openoffice.org-style-hicontrast = 1:3.3-1:2011.0
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
# Provides:  openoffice.org-style-industrial = 1:3.3-1:2011.0
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
# Provides:  openoffice.org-style-tango = 1:3.3-1:2011.0
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
#Provides:  openoffice.org-style-oxygen = 1:3.3-1:2011.0

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
#Provides:  openoffice.org-writer = 1:3.3-1:2011.0
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
Obsoletes:	openoffice.org-mono < 1:3.3-1:2011.0 
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
#Provides:  openoffice.org-pdfimport = 1:3.3-1:2011.0
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
Obsoletes: openoffice.org-presenter-screen < 1:3.3-1:2011.0 
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
Obsoletes: openoffice.org-wiki-publisher < 1:3.3-1:2011.0 
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
Obsoletes: openoffice.org-presentation-minimizer < 1:3.3-1:2011.0 
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

%package l10n-af
Summary:	Afrikaans language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-af
Requires:	urw-fonts
Requires:	myspell-af
Obsoletes:  	OpenOffice.org-l10n-af
Provides: 	LibreOffice-l10n-af
Obsoletes:	openoffice.org-go-ooo-l10n-af <= %{version}
Suggests:	%{ooname}-help-af = %{EVRD} 
Obsoletes:	openoffice.org-l10n-af < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-ar = %{EVRD}
Obsoletes:	openoffice.org-l10n-ar < 1:3.3-1:2011.0 
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

%package l10n-as
Summary:	Assamese language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-as
Provides: 	LibreOffice-l10n-as

%description l10n-as
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  	OpenOffice.org-l10n-bg
Provides: 	LibreOffice-l10n-bg
Obsoletes:	openoffice.org-go-ooo-l10n-bg <= %{version}
Suggests:	%{ooname}-help-bg = %{EVRD}
Obsoletes:	openoffice.org-l10n-bg < 1:3.3-1:2011.0 
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


%package l10n-bn
Summary:	Bengali language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-bn
Provides: 	LibreOffice-l10n-bn
Suggests:	%{ooname}-help-bn = %{EVRD}

%description l10n-bn
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-br
Provides: 	LibreOffice-l10n-br
Obsoletes:	openoffice.org-go-ooo-l10n-br <= %{version}
Suggests:	%{ooname}-help-br = %{EVRD}
Obsoletes:	openoffice.org-l10n-br < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-bs = %{EVRD}
Obsoletes:	openoffice.org-l10n-bs < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-ca = %{EVRD}
Obsoletes:	openoffice.org-l10n-ca < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-cs = %{EVRD}
Obsoletes:	openoffice.org-l10n-cs < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-cy = %{EVRD}
Obsoletes:	openoffice.org-l10n-cy < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-da = %{EVRD}
Obsoletes:	openoffice.org-l10n-da < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-de = %{EVRD} 
Obsoletes:	openoffice.org-l10n-de < 1:3.3-1:2011.0 
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

%package l10n-dz
Summary:	Dzongkha language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-dz
Provides: 	LibreOffice-l10n-dz
Suggests:	%{ooname}-help-dz = %{EVRD} 

%description l10n-dz
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-el
Provides: 	LibreOffice-l10n-el
Obsoletes:	openoffice.org-go-ooo-l10n-el <= %{version}
Suggests:	%{ooname}-help-el = %{EVRD} 
Obsoletes:	openoffice.org-l10n-el < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-en_GB = %{EVRD} 
Obsoletes:	openoffice.org-l10n-en_GB < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-es = %{EVRD} 
Obsoletes:	openoffice.org-l10n-es < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-et = %{EVRD} 
Obsoletes:	openoffice.org-l10n-et < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-eu = %{EVRD} 
Obsoletes:	openoffice.org-l10n-eu < 1:3.3-1:2011.0 
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

%package l10n-fa
Summary:	Farsi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-fa
Provides: 	LibreOffice-l10n-fa

%description l10n-fa
LibreOffice is an Open Source, community-developed, office suite.

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
Requires:	%{ooname}-voikko
Obsoletes:  OpenOffice.org-l10n-fi
Provides: 	LibreOffice-l10n-fi
Obsoletes:	openoffice.org-go-ooo-l10n-fi <= %{version}
Suggests:	%{ooname}-help-fi = %{EVRD} 
Obsoletes:	openoffice.org-l10n-fi < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-fr = %{EVRD} 
Obsoletes:	openoffice.org-l10n-fr < 1:3.3-1:2011.0 
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


%package l10n-ga
Summary:	Irish language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ga
Provides: 	LibreOffice-l10n-ga

%description l10n-ga
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-gl
Suggests:	%{ooname}-help-gl = %{EVRD} 

%description l10n-gl
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-gu
Suggests:	%{ooname}-help-gu = %{EVRD} 

%description l10n-gu
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-he
Provides: 	LibreOffice-l10n-he
Obsoletes:	openoffice.org-go-ooo-l10n-he <= %{version}
Suggests:	%{ooname}-help-he = %{EVRD} 
Obsoletes:	openoffice.org-l10n-he < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-hi = %{EVRD} 
Obsoletes:	openoffice.org-l10n-hi < 1:3.3-1:2011.0 
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


%package l10n-hr
Summary:	Croatian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-hr
Provides: 	LibreOffice-l10n-hr
Suggests:	%{ooname}-help-hr = %{EVRD} 

%description l10n-hr
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-hu
Provides: 	LibreOffice-l10n-hu
Obsoletes:	openoffice.org-go-ooo-l10n-hu <= %{version}
Suggests:	%{ooname}-help-hu = %{EVRD} 
Obsoletes:	openoffice.org-l10n-hu < 1:3.3-1:2011.0 
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


%package l10n-it
Summary:	Italian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	fonts-ttf-dejavu
Requires:	urw-fonts
Requires:	myspell-it
Requires:	myspell-hyph-it
Obsoletes:  OpenOffice.org-l10n-it
Provides: 	LibreOffice-l10n-it
Obsoletes:	openoffice.org-go-ooo-l10n-it <= %{version}
Suggests:	%{ooname}-help-it = %{EVRD}
Obsoletes:	openoffice.org-l10n-it < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-ja = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ja < 1:3.3-1:2011.0 
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


%package l10n-kn
Summary:	Kannada language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-kn
Provides: 	LibreOffice-l10n-kn

%description l10n-kn
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-ko
Provides: 	LibreOffice-l10n-ko
Obsoletes:	openoffice.org-go-ooo-l10n-ko <= %{version}
Suggests:	%{ooname}-help-ko = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ko < 1:3.3-1:2011.0 
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


%package l10n-lt
Summary:	Lithuanian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-lt
Provides: 	LibreOffice-l10n-lt

%description l10n-lt
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-lv

%description l10n-lv
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-mai

%description l10n-mai
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-ml

%description l10n-ml
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-mk
Provides: 	LibreOffice-l10n-mk
Obsoletes:	openoffice.org-go-ooo-l10n-mk <= %{version}
Suggests:	%{ooname}-help-mk = %{EVRD} 
Obsoletes:	openoffice.org-l10n-mk < 1:3.3-1:2011.0 
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


%package l10n-mr
Summary:	Marathi language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-mr
Provides: 	LibreOffice-l10n-mr

%description l10n-mr
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-nb
Provides: 	LibreOffice-l10n-nb
Obsoletes:	openoffice.org-go-ooo-l10n-nb <= %{version}
Suggests:	%{ooname}-help-nb = %{EVRD} 
Obsoletes:	openoffice.org-l10n-nb < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-nl = %{EVRD} 
Obsoletes:	openoffice.org-l10n-nl < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-nn = %{EVRD} 
Obsoletes:	openoffice.org-l10n-nn < 1:3.3-1:2011.0 
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


%package l10n-nr
Summary:	Ndebele language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-nr
Provides: 	LibreOffice-l10n-nr

%description l10n-nr
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-nso
Suggests:	%{ooname}-help-nso = %{EVRD} 

%description l10n-nso
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-or

%description l10n-or
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-pa_IN
Provides: 	LibreOffice-l10n-pa

%description l10n-pa_IN
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-pl
Provides: 	LibreOffice-l10n-pl
Obsoletes:	openoffice.org-go-ooo-l10n-pl <= %{version}
Suggests:	%{ooname}-help-pl = %{EVRD} 
Obsoletes:	openoffice.org-l10n-pl < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-pt = %{EVRD} 
Obsoletes:	openoffice.org-l10n-pt < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-pt_BR = %{EVRD} 
Obsoletes:	openoffice.org-l10n-pt_BR < 1:3.3-1:2011.0 
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


# %package l10n-pt_AO
# Summary:    Portuguese Angola language support for LibreOffice
# Group:      Office
# Provides:	%{ooname}-l10n = %{EVRD}
# # Due to alternatives setup, we must have -release here. (BrOffice)
# Requires:	%{ooname}-common = %{EVRD}
# Requires:   locales-pt
# Requires:   urw-fonts
# Obsoletes:  OpenOffice.org-l10n-pt_AO
# Provides: 	LibreOffice-l10n-pt_AO
# Suggests:	%{ooname}-help-pt_AO = %{EVRD} 
# Obsoletes:	openoffice.org-l10n-pt_AO < 1:3.3-1:2011.0 
# 
# %description l10n-pt_AO
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localization of LibreOffice in Portuguese
# Angola.
# It contains the user interface, the templates and the autotext
# features. Please note that not all of these are available for all
# possible language. You can switch user interface language using the
# standard locales system.
# 

%package l10n-ro
Summary:	Romanian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ro
Provides: 	LibreOffice-l10n-ro

%description l10n-ro
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-ru
Provides: 	LibreOffice-l10n-ru
Obsoletes:	openoffice.org-go-ooo-l10n-ru <= %{version}
Suggests:	%{ooname}-help-ru = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ru < 1:3.3-1:2011.0 
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


%package l10n-sh
Summary:	Secwepemctsin language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sh
Provides: 	LibreOffice-l10n-sh
Suggests:	%{ooname}-help-sh = %{EVRD} 

%description l10n-sh
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-si
Suggests:	%{ooname}-help-si = %{EVRD} 

%description l10n-si
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-sk
Provides: 	LibreOffice-l10n-sk
Obsoletes:	openoffice.org-go-ooo-l10n-sk <= %{version}
Suggests:	%{ooname}-help-sk = %{EVRD} 
Obsoletes:	openoffice.org-l10n-sk < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-sl = %{EVRD} 
Obsoletes:	openoffice.org-l10n-sl < 1:3.3-1:2011.0 
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


%package l10n-sr
Summary:	Serbian language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-sr
Provides: 	LibreOffice-l10n-sr

%description l10n-sr
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-st

%description l10n-st
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-ss

%description l10n-ss
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-sv
Provides: 	LibreOffice-l10n-sv
Obsoletes:	openoffice.org-go-ooo-l10n-sv <= %{version}
Suggests:	%{ooname}-help-sv = %{EVRD} 
Obsoletes:	openoffice.org-l10n-sv < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-ta = %{EVRD} 
Obsoletes:	openoffice.org-l10n-ta < 1:3.3-1:2011.0 
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


%package l10n-te
Summary:	Telugu language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-te
Provides: 	LibreOffice-l10n-te

%description l10n-te
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-th

%description l10n-th
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-tn

%description l10n-tn
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-tr
Provides: 	LibreOffice-l10n-tr
Obsoletes:	openoffice.org-go-ooo-l10n-tr <= %{version}
Suggests:	%{ooname}-help-tr = %{EVRD} 
Obsoletes:	openoffice.org-l10n-tr < 1:3.3-1:2011.0 
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


%package l10n-ts
Summary:	Tsonga language support for LibreOffice
Group:		Office
Provides:	%{ooname}-l10n = %{EVRD}
Requires:	%{ooname}-common = %{EVRD}
Requires:	locales-ts
Provides: 	LibreOffice-l10n-ts

%description l10n-ts
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-uk
Suggests:	%{ooname}-help-uk = %{EVRD} 

%description l10n-uk
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-ve

%description l10n-ve
LibreOffice is an Open Source, community-developed, office suite.

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
Provides: 	LibreOffice-l10n-xh

%description l10n-xh
LibreOffice is an Open Source, community-developed, office suite.

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
Obsoletes:  OpenOffice.org-l10n-zh_CN
Provides: 	LibreOffice-l10n-zh_CN
Obsoletes:	openoffice.org-go-ooo-l10n-zh_CN <= %{version}
Suggests:	%{ooname}-help-zh_CN = %{EVRD} 
Obsoletes:	openoffice.org-l10n-zh_CN < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-zh_TW = %{EVRD}
Obsoletes:	openoffice.org-l10n-zh_TW < 1:3.3-1:2011.0 
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
Suggests:	%{ooname}-help-zu = %{EVRD}
Obsoletes:	openoffice.org-l10n-zu < 1:3.3-1:2011.0 
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


# %package help-af
# Summary:	Afrikaans help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-af = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-af <= 1:3.1-4
# %endif
# Obsoletes:  OpenOffice.org-help-af
# Provides:	LibreOffice-help-af
# Obsoletes:  openoffice.org-help-af < 1:3.3-1:2011.0 
# 
# %description help-af
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Afrikaans.


# %package help-ar
# Summary:	Arabic help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-ar = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-ar <= 1:3.1-4
# %endif
# Obsoletes:  OpenOffice.org-help-ar
# Provides:	LibreOffice-help-ar
# Obsoletes:  openoffice.org-help-ar < 1:3.3-1:2011.0 
# 
# %description help-ar
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Arabic.


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
Obsoletes:  openoffice.org-help-bg < 1:3.3-1:2011.0 

%description help-bg
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Bulgarian.

%package help-bn
Summary:	Bengali help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-bn = %{EVRD}
Provides:	LibreOffice-help-bn

%description help-bn
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Bengali.


# %package help-br
# Summary:	Breton help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-br = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-br <= 1:3.1-4
# %endif
# Obsoletes:  OpenOffice.org-help-br
# Provides:	LibreOffice-help-br
# Obsoletes:  openoffice.org-help-br < 1:3.3-1:2011.0 
# 
# %description help-br
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Breton.


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
Obsoletes:  openoffice.org-help-bs < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-ca < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-cs < 1:3.3-1:2011.0 

%description help-cs
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Czech.


# %package help-cy
# Summary:	Welsh help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-cy = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-cy <= 1:3.1-4
# %endif
# Obsoletes:	OpenOffice.org-help-cy
# Provides:	LibreOffice-help-cy
# Obsoletes:  openoffice.org-help-cy < 1:3.3-1:2011.0 
# 
# %description help-cy
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Welsh.


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
Obsoletes:  openoffice.org-help-da < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-de < 1:3.3-1:2011.0 

%description help-de
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in German.

%package help-dz
Summary:	Dzongkha help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-dz = %{EVRD}
Provides:	LibreOffice-help-dz

%description help-dz
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Dzongkha.


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
Obsoletes:  openoffice.org-help-el < 1:3.3-1:2011.0 


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
Obsoletes:  openoffice.org-help-en_GB < 1:3.3-1:2011.0 

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
#Provides:  openoffice.org-help-en_US = 1:3.3-1:2011.0

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
Obsoletes:  openoffice.org-help-es < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-et < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-eu < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-fi < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-fr < 1:3.3-1:2011.0 

%description help-fr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in French.


%package help-gu
Summary:	Gujarati help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gu = %{EVRD}
Provides:	LibreOffice-help-gu

%description help-gu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Gujarati.


%package help-gl
Summary:	Galician help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-gl = %{EVRD}
Provides:	LibreOffice-help-gl

%description help-gl
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Galician.


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
Obsoletes:  openoffice.org-help-he < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-hi < 1:3.3-1:2011.0 

%description help-hi
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Hindi.


%package help-hr
Summary:	Croatian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-hr = %{EVRD}
Provides:	LibreOffice-help-hr

%description help-hr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Croatian.


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
Obsoletes:  openoffice.org-help-hu < 1:3.3-1:2011.0 

%description help-hu
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Hungarian.


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
Obsoletes:  openoffice.org-help-it < 1:3.3-1:2011.0 

%description help-it
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Italian.


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
Obsoletes:  openoffice.org-help-ja < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-ko < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-mk < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-nb < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-nl < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-nn < 1:3.3-1:2011.0 

%description help-nn
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Norwegian
Nynorsk.


%package help-nso
Summary:	Northern Sotho help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-nso = %{EVRD}
Provides:	LibreOffice-help-nso

%description help-nso
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Northern Sotho.


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
Obsoletes:  openoffice.org-help-pl < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-pt < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-pt_BR < 1:3.3-1:2011.0 

%description help-pt_BR
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Portuguese
Brazilian.


# %package help-pt_AO
# Summary:	Portuguese Angola help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-pt_AO = %{EVRD}
# Provides:	LibreOffice-help-pt_AO
# Obsoletes:  openoffice.org-help-pt_AO < 1:3.3-1:2011.0 
# 
# %description help-pt_AO
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Portuguese
# Angola.


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
Obsoletes:  openoffice.org-help-ru < 1:3.3-1:2011.0 

%description help-ru
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Russian.


%package help-si
Summary:	Sinhalese help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-si = %{EVRD}
Provides:	LibreOffice-help-si

%description help-si
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Sinhalese.


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
Obsoletes:  openoffice.org-help-sk < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-sl < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-sv < 1:3.3-1:2011.0 

%description help-sv
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Swedish.


# %package help-ta
# Summary:	Tamil help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-ta = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-ta <= 1:3.1-4
# %endif
# Obsoletes:	OpenOffice.org-help-ta
# Provides:	LibreOffice-help-ta
# Obsoletes:  openoffice.org-help-ta < 1:3.3-1:2011.0 
# 
# %description help-ta
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Tamil.


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
Obsoletes:  openoffice.org-help-tr < 1:3.3-1:2011.0 

%description help-tr
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Turkish.


%package help-uk
Summary:	Ukrainian help for LibreOffice
Group:		Office
Provides:	%{ooname}-help = %{EVRD}
Requires:	%{ooname}-l10n-uk = %{EVRD}
Provides:	LibreOffice-help-uk

%description help-uk
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Ukrainian.


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
Obsoletes:  openoffice.org-help-zn_CN < 1:3.3-1:2011.0 

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
Obsoletes:  openoffice.org-help-zn_CT < 1:3.3-1:2011.0 

%description help-zh_TW
LibreOffice is an Open Source, community-developed, office suite.

This package contains the localized help files of LibreOffice in Chinese
Traditional.

# %package help-zu
# Summary:	Zulu help for LibreOffice
# Group:		Office
# Provides:	%{ooname}-help = %{EVRD}
# Requires:	%{ooname}-l10n-zu = %{EVRD}
# %ifarch x86_64
# Obsoletes:     openoffice.org64-help-zu <= 1:3.1-4
# %endif
# Obsoletes:	OpenOffice.org-help-zu
# Provides:	LibreOffice-help-zu
# Obsoletes:  openoffice.org-help-zu < 1:3.3-1:2011.0 
# 
# %description help-zu
# LibreOffice is an Open Source, community-developed, office suite.
# 
# This package contains the localized help files of LibreOffice in Zulu.

%endif

%prep
%setup -q -c -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19
for a in */*; do mv `pwd`/$a .; done

%patch4 -p0 -b .xul
%patch5 -p0 -b .sysui
%patch9 -p0 -b .vba
%patch10 -p0 -b .vclkde

# Add lzma support (REVIEW)
%if %{oootarext} == "lzma"
%patch1 -p1 -b .lzma
%endif

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


# Force KDE3 support instead of KDE4 (dev 300)
# %ifarch x86_64 
# export KDEDIR=/opt/kde
# %endif

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

ENVCFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing" \
ENVCXXFLAGS="%{optflags} %{optsafe} -g0 -fno-omit-frame-pointer -fno-strict-aliasing -fpermissive -fvisibility-inlines-hidden " \
%configure2_5x \
	--with-distro=%{distroname} \
	--with-vendor=Mandriva \
	--with-build-version="%{buildver}" \
	--with-system-stdlibs \
	--disable-qadevooo \
	--enable-lockdown \
	--enable-opengl \
	--enable-odk \
	--enable-split-app-modules \
  	--enable-split-opt-features \
	--enable-binfilter \
	--with-system-mozilla=xulrunner \
	--with-system-hsqldb \
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
	--with-system-libtextcat \
	--with-external-libtextcat-data \
	--with-system-libwpd \
	--with-system-libwps \
	--with-system-libwpg \
	--with-system-graphite \
        --with-system-apache-commons \
	--with-system-translate-toolkit \
	--without-junit \
	--with-system-cppunit \
	--enable-broffice \
	--with-system-redland \
	--with-openldap \
	--disable-kde \
	--enable-kde4 \
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
	--with-lang=%{langs} \
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
    	--enable-ext-pdfimport \
	--enable-ext-presenter-minimizer \
	--enable-ext-presenter-console \
    	--enable-ext-wiki-publisher \
    	--without-fonts \
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

mkdir -p src
ln -sf %{SOURCE31} src/
ln -sf %{SOURCE32} src/
#ln -sf %{SOURCE33} src/
#ln -sf %{SOURCE34} src/
#ln -sf %{SOURCE35} src/
ln -sf %{SOURCE36} src/
ln -sf %{SOURCE37} src/
ln -sf %{SOURCE38} src/
ln -sf %{SOURCE39} src/
ln -sf %{SOURCE40} src/
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
ln -sf %{SOURCE54} src/
ln -sf %{SOURCE55} src/
ln -sf %{SOURCE56} src/
touch src.downloaded

#. ./*[Ee]nv.[Ss]et.sh
./bootstrap

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

rm -rf %{buildroot}
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
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
tar -xjvf %{SOURCE20} -C %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/

sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-calc_72/'    %{buildroot}%{ooodir}/share/xdg/calc.desktop
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-writer_72/'  %{buildroot}%{ooodir}/share/xdg/writer.desktop 
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-impress_72/' %{buildroot}%{ooodir}/share/xdg/impress.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-draw_72/'    %{buildroot}%{ooodir}/share/xdg/draw.desktop  
sed -i 's/^Icon=.*$/Icon=mandriva-rosa-lo-base_72/'    %{buildroot}%{ooodir}/share/xdg/base.desktop  

# fix permissions for stripping
find %{buildroot} -type f -exec chmod u+rw '{}' \;

# fix permission of .so libraries
find %{buildroot} -type f \( -name '*.so' -o -name '*.so.*' \) -exec chmod a+x '{}' \;

# Anssi patch
# remove /usr/bin/soffice (made with update-alternatives)
# rm -f %{buildroot}%{_bindir}/soffice

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
%{buildroot}%{ooodir}/program/unopkg add --shared %{_builddir}/libreoffice-%version/solver/340/unxlng*/bin/pdfimport/pdfimport.oxt
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

#libre 
# remove icons we dont have these sizes yet
# rm -rf %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/*
# rm -rf %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/*

#libre 
# remove scalables icons since we dont have yet
# rm -rf %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*

# libre
# Fixes japanese translations on desktop files
## patch -p0 -d %{buildroot} < %{SOURCE102}

# libre
# # templates for kde "create new" context menu
# # tar xjf %{SOURCE31} -C %{buildroot}%{_datadir}

# copy extensions 
install -d -m755 %{buildroot}%{ooodir}/extensions
cp %{_builddir}/libreoffice-%version/solver/340/unxlng*/bin/pdfimport/pdfimport.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-%version/solver/340/unxlng*/bin/presenter/presenter-screen.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-%version/solver/340/unxlng*/bin/swext/wiki-publisher.oxt %{buildroot}%{ooodir}/extensions/
cp %{_builddir}/libreoffice-%version/solver/340/unxlng*/bin/minimizer/presentation-minimizer.oxt %{buildroot}%{ooodir}/extensions/

# libre
# #fixes #56439
# sed -i 's/^Icon=.*$/Icon=ooo-calc/' %{buildroot}%{_datadir}/templates/ooo-spreadsheet.desktop
# sed -i 's/^Icon=.*$/Icon=ooo-writer/' %{buildroot}%{_datadir}/templates/ooo-text.desktop
# sed -i 's/^Icon=.*$/Icon=ooo-impress/' %{buildroot}%{_datadir}/templates/ooo-presentation.desktop
# sed -i 's/^Icon=.*$/Icon=ooo-draw/' %{buildroot}%{_datadir}/templates/ooo-drawing.desktop

## Libre (Temporary), will better handled inside (bin/distro-install-file-lists) 
## Installation fixes
## remove fix wrong manpages files, extension gz->xz
for p in common base calc writer impress draw math; do
	sed -i '/^.*man.*\.gz$/d' file-lists/${p}_list.txt 
done;

## sort removing duplicates
sort -u file-lists/gnome_list.txt > file-lists/gnome_list.uniq.sorted.txt 
sort -u file-lists/sdk_list.txt   > file-lists/sdk_list.uniq.sorted.txt 

## oxygen should be in the style
sed -i '/^.*images_oxygen\.zip$/d' file-lists/common_list.txt 

## merge en-US with common
cat file-lists/lang_en_US_list.txt >> file-lists/common_list.txt
sort -u file-lists/common_list.txt >  file-lists/common_list.uniq.sorted.txt 

# # does not package lo original desktop files (Review)
# sed -i '/^.*libreoffice-writer.desktop$/d'  file-lists/writer_list.txt 
# sed -i '/^.*libreoffice-calc.desktop$/d'    file-lists/calc_list.txt 
# sed -i '/^.*libreoffice-impress.desktop$/d' file-lists/impress_list.txt 
# sed -i '/^.*libreoffice-draw.desktop$/d'    file-lists/draw_list.txt 
# sed -i '/^.*libreoffice-base.desktop$/d'    file-lists/base_list.txt 
# sed -i '/^.*libreoffice-math.desktop$/d'    file-lists/math_list.txt 

%clean
rm -rf %{buildroot}

%post common

%{update_desktop_database}
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
%{clean_desktop_database}
%clean_icon_cache gnome
%clean_icon_cache hicolor

# Firefox plugin
if [ $1 -eq 0 ]
then
  update-alternatives --remove %{firefox_plugin} \
  %{ooodir}/program/libnpsoplugin.so
fi

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

%files base -f file-lists/base_list.txt
%{_mandir}/man1/lobase*
# %{_datadir}/applications/base.desktop
%{_datadir}/icons/hicolor/scalable/apps/mandriva-rosa-lo-base_72.svg

%files calc -f file-lists/calc_list.txt
#libre 
# %{_datadir}/templates/ooo-spreadsheet.desktop
# %{_datadir}/templates/.source/ooo-spreadsheet.ods
%{_mandir}/man1/localc*
# %{_datadir}/applications/calc.desktop
%{_datadir}/icons/hicolor/scalable/apps/mandriva-rosa-lo-calc_72.svg

%files common -f file-lists/common_list.uniq.sorted.txt 

# libre
# %{_sysconfdir}/bash_completion.d/libreoffice3.3.sh
# %{_sysconfdir}/profile.d/openoffice.org.*
# %{_bindir}/ooconfig3.3
# %{_bindir}/ootool3.3

# libre
# %{_datadir}/applications/template*.desktop

# new icons
# %{_datadir}/icons/hicolor/*/apps/openofficeorg3-*.png
# moved to mandriva-kde-config 
#%{_datadir}/icons/hicolor/*/mimetypes/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/apps/openofficeorg3-*.png
# %{_datadir}/icons/gnome/*/mimetypes/openofficeorg3-*.png


# libre
# %{_datadir}/pixmaps/ooo-base3.3.png
# %{_datadir}/pixmaps/ooo-calc3.3.png
# %{_datadir}/pixmaps/ooo-draw3.3.png
# %{_datadir}/pixmaps/ooo-gulls3.3.png
# %{_datadir}/pixmaps/ooo-impress3.3.png
# %{_datadir}/pixmaps/ooo-math3.3.png
# %{_datadir}/pixmaps/ooo-template3.3.png
# %{_datadir}/pixmaps/ooo-web3.3.png
# %{_datadir}/pixmaps/ooo-writer3.3.png

%{_mandir}/man1/loffice*
%{_mandir}/man1/lofromtemplate*
%{_mandir}/man1/libreoffice*
%{_datadir}/mime

#dev300 
# %ghost %{ooodir}/share/uno_packages
# %ghost %{ooodir}/program/bootstraprc
# %ghost %{ooodir}/program/versionrc
# %ghost %{ooodir}/%basis/share/registry/data/org/openoffice/Setup.xcu

%{_mandir}/man1/unopkg.1*

# libre
# %{_datadir}/applications/ooo-extension-manager*.desktop

# Anssi 
%dir %{ooodir}/extensions

%files core -f file-lists/core_list.txt

%files devel -f file-lists/sdk_list.uniq.sorted.txt

%files devel-doc -f file-lists/sdk_doc_list.txt

%files draw -f file-lists/draw_list.txt
# %{_datadir}/applications/draw.desktop
# libre
# %{_datadir}/templates/ooo-drawing.desktop
# %{_datadir}/templates/.source/ooo-drawing.odg
%{_mandir}/man1/lodraw*
%{_datadir}/icons/hicolor/scalable/apps/mandriva-rosa-lo-draw_72.svg

# dev300: 
# %files dtd-officedocument1.0 -f build/dtd_list.txt

# dev300: 
%files filter-binfilter -f file-lists/filter-binfilter_list.txt

%files gnome -f file-lists/gnome_list.uniq.sorted.txt

%files impress -f file-lists/impress_list.txt
# %{_datadir}/applications/impress.desktop
# libre 
# %{_datadir}/templates/ooo-presentation.desktop
# %{_datadir}/templates/.source/ooo-presentation.odp
%{_mandir}/man1/loimpress*
%{_datadir}/icons/hicolor/scalable/apps/mandriva-rosa-lo-impress_72.svg

%files java-common -f file-lists/java_common_list.txt

%files kde4 -f file-lists/kde4_list.txt

%files math -f file-lists/math_list.txt
# %{_datadir}/applications/math.desktop
%{_mandir}/man1/lomath*

%files openclipart -f file-lists/gallery_list.txt

%files pyuno -f file-lists/pyuno_list.txt

#%files qa-api-tests
#%{ooodir}/qadevOOo

%files testtool -f file-lists/testtool_list.txt

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

%files writer -f file-lists/writer_list.txt
# %{_datadir}/applications/writer.desktop
# libre
#%{_datadir}/applications/web.desktop
# libre
# %{_datadir}/templates/ooo-text.desktop
# %{_datadir}/templates/.source/ooo-text.odt
%{_mandir}/man1/loweb*
%{_mandir}/man1/lowriter*
%{_datadir}/icons/hicolor/scalable/apps/mandriva-rosa-lo-writer_72.svg

%if %{use_mono}
%files mono -f file-lists/mono_list.txt
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
%files l10n-it -f file-lists/lang_it_list.txt
%defattr(-,root,root)

%files l10n-af -f file-lists/lang_af_list.txt
%defattr(-,root,root)

%files l10n-ar -f file-lists/lang_ar_list.txt
%defattr(-,root,root)

%files l10n-as -f file-lists/lang_as_list.txt
%defattr(-,root,root)

%files l10n-bg -f file-lists/lang_bg_list.txt
%defattr(-,root,root)

%files l10n-bn -f file-lists/lang_bn_list.txt
%defattr(-,root,root)

%files l10n-br -f file-lists/lang_br_list.txt
%defattr(-,root,root)

%files l10n-bs -f file-lists/lang_bs_list.txt
%defattr(-,root,root)

%files l10n-ca -f file-lists/lang_ca_list.txt
%defattr(-,root,root)

%files l10n-cs -f file-lists/lang_cs_list.txt
%defattr(-,root,root)

%files l10n-cy -f file-lists/lang_cy_list.txt
%defattr(-,root,root)

%files l10n-da -f file-lists/lang_da_list.txt
%defattr(-,root,root)

%files l10n-de -f file-lists/lang_de_list.txt
%defattr(-,root,root)

%files l10n-dz -f file-lists/lang_dz_list.txt
%defattr(-,root,root)

%files l10n-el -f file-lists/lang_el_list.txt
%defattr(-,root,root)

%files l10n-en_GB -f file-lists/lang_en_GB_list.txt
%defattr(-,root,root)

%files l10n-es -f file-lists/lang_es_list.txt
%defattr(-,root,root)

%files l10n-et -f file-lists/lang_et_list.txt
%defattr(-,root,root)

%files l10n-eu -f file-lists/lang_eu_list.txt
%defattr(-,root,root)

%files l10n-fa -f file-lists/lang_fa_list.txt
%defattr(-,root,root)

%files l10n-fi -f file-lists/lang_fi_list.txt
%defattr(-,root,root)

%files l10n-fr -f file-lists/lang_fr_list.txt
%defattr(-,root,root)

%files l10n-ga -f file-lists/lang_ga_list.txt
%defattr(-,root,root)

%files l10n-gl -f file-lists/lang_gl_list.txt
%defattr(-,root,root)

%files l10n-gu -f file-lists/lang_gu_list.txt
%defattr(-,root,root)

%files l10n-he -f file-lists/lang_he_list.txt
%defattr(-,root,root)

%files l10n-hi -f file-lists/lang_hi_list.txt
%defattr(-,root,root)

%files l10n-hr -f file-lists/lang_hr_list.txt
%defattr(-,root,root)

%files l10n-hu -f file-lists/lang_hu_list.txt
%defattr(-,root,root)

%files l10n-ja -f file-lists/lang_ja_list.txt
%defattr(-,root,root)

%files l10n-kn -f file-lists/lang_kn_list.txt
%defattr(-,root,root)

%files l10n-ko -f file-lists/lang_ko_list.txt
%defattr(-,root,root)

%files l10n-lt -f file-lists/lang_lt_list.txt
%defattr(-,root,root)

%files l10n-lv -f file-lists/lang_lv_list.txt
%defattr(-,root,root)

%files l10n-mai -f file-lists/lang_mai_list.txt
%defattr(-,root,root)

%files l10n-ml -f file-lists/lang_ml_list.txt
%defattr(-,root,root)

%files l10n-mk -f file-lists/lang_mk_list.txt
%defattr(-,root,root)

%files l10n-mr -f file-lists/lang_mr_list.txt
%defattr(-,root,root)

%files l10n-nb -f file-lists/lang_nb_list.txt
%defattr(-,root,root)

%files l10n-nl -f file-lists/lang_nl_list.txt
%defattr(-,root,root)

%files l10n-nn -f file-lists/lang_nn_list.txt
%defattr(-,root,root)

%files l10n-nr -f file-lists/lang_nr_list.txt
%defattr(-,root,root)

%files l10n-nso -f file-lists/lang_nso_list.txt
%defattr(-,root,root)

%files l10n-or -f file-lists/lang_or_list.txt
%defattr(-,root,root)

%files l10n-pa_IN -f file-lists/lang_pa_IN_list.txt
%defattr(-,root,root)

%files l10n-pl -f file-lists/lang_pl_list.txt
%defattr(-,root,root)

%files l10n-pt -f file-lists/lang_pt_list.txt
%defattr(-,root,root)

%files l10n-pt_BR -f file-lists/lang_pt_BR_list.txt
%defattr(-,root,root)

# %files l10n-pt_AO -f file-lists/lang_pt_AO_list.txt
# %defattr(-,root,root)

%files l10n-ro -f file-lists/lang_ro_list.txt
%defattr(-,root,root)

%files l10n-ru -f file-lists/lang_ru_list.txt
%defattr(-,root,root)

%files l10n-sh -f file-lists/lang_sh_list.txt
%defattr(-,root,root)

%files l10n-si -f file-lists/lang_si_list.txt
%defattr(-,root,root)

%files l10n-sk -f file-lists/lang_sk_list.txt
%defattr(-,root,root)

%files l10n-sl -f file-lists/lang_sl_list.txt
%defattr(-,root,root)

%files l10n-sr -f file-lists/lang_sr_list.txt
%defattr(-,root,root)

%files l10n-ss -f file-lists/lang_ss_list.txt
%defattr(-,root,root)

%files l10n-st -f file-lists/lang_st_list.txt
%defattr(-,root,root)

%files l10n-sv -f file-lists/lang_sv_list.txt
%defattr(-,root,root)

%files l10n-ta -f file-lists/lang_ta_list.txt
%defattr(-,root,root)

%files l10n-te -f file-lists/lang_te_list.txt
%defattr(-,root,root)

%files l10n-th -f file-lists/lang_th_list.txt
%defattr(-,root,root)

%files l10n-tn -f file-lists/lang_tn_list.txt
%defattr(-,root,root)

%files l10n-tr -f file-lists/lang_tr_list.txt
%defattr(-,root,root)

%files l10n-ts -f file-lists/lang_ts_list.txt
%defattr(-,root,root)

%files l10n-uk -f file-lists/lang_uk_list.txt
%defattr(-,root,root)

%files l10n-ve -f file-lists/lang_ve_list.txt
%defattr(-,root,root)

%files l10n-xh -f file-lists/lang_xh_list.txt
%defattr(-,root,root)

%files l10n-zh_CN -f file-lists/lang_zh_CN_list.txt
%defattr(-,root,root)

%files l10n-zh_TW -f file-lists/lang_zh_TW_list.txt
%defattr(-,root,root)

%files l10n-zu -f file-lists/lang_zu_list.txt
%defattr(-,root,root)


# %files help-af -f file-lists/help_af_list.txt
# %defattr(-,root,root)

# %files help-ar -f file-lists/help_ar_list.txt
# %defattr(-,root,root)

%files help-bg -f file-lists/help_bg_list.txt
%defattr(-,root,root)

%files help-bn -f file-lists/help_bn_list.txt
%defattr(-,root,root)

# %files help-br -f file-lists/help_br_list.txt
# %defattr(-,root,root)

%files help-bs -f file-lists/help_bs_list.txt
%defattr(-,root,root)

%files help-ca -f file-lists/help_ca_list.txt
%defattr(-,root,root)

%files help-cs -f file-lists/help_cs_list.txt
%defattr(-,root,root)

# %files help-cy -f file-lists/help_cy_list.txt
# %defattr(-,root,root)

%files help-da -f file-lists/help_da_list.txt
%defattr(-,root,root)

%files help-de -f file-lists/help_de_list.txt
%defattr(-,root,root)

%files help-dz -f file-lists/help_dz_list.txt
%defattr(-,root,root)

%files help-el -f file-lists/help_el_list.txt
%defattr(-,root,root)

%files help-en_GB -f file-lists/help_en_GB_list.txt
%defattr(-,root,root)

%files help-es -f file-lists/help_es_list.txt
%defattr(-,root,root)

%files help-et -f file-lists/help_et_list.txt
%defattr(-,root,root)

%files help-eu -f file-lists/help_eu_list.txt
%defattr(-,root,root)

%files help-fi -f file-lists/help_fi_list.txt
%defattr(-,root,root)

%files help-fr -f file-lists/help_fr_list.txt
%defattr(-,root,root)

%files help-gl -f file-lists/help_gl_list.txt
%defattr(-,root,root)

%files help-gu -f file-lists/help_gu_list.txt
%defattr(-,root,root)

%files help-he -f file-lists/help_he_list.txt
%defattr(-,root,root)

%files help-hi -f file-lists/help_hi_list.txt
%defattr(-,root,root)

%files help-hr -f file-lists/help_hr_list.txt
%defattr(-,root,root)

%files help-hu -f file-lists/help_hu_list.txt
%defattr(-,root,root)

%files help-it -f file-lists/help_it_list.txt
%defattr(-,root,root)

%files help-ja -f file-lists/help_ja_list.txt
%defattr(-,root,root)

%files help-ko -f file-lists/help_ko_list.txt
%defattr(-,root,root)

%files help-mk -f file-lists/help_mk_list.txt
%defattr(-,root,root)

%files help-nb -f file-lists/help_nb_list.txt
%defattr(-,root,root)

%files help-nl -f file-lists/help_nl_list.txt
%defattr(-,root,root)

%files help-nn -f file-lists/help_nn_list.txt
%defattr(-,root,root)

%files help-nso -f file-lists/help_nso_list.txt
%defattr(-,root,root)

%files help-pl -f file-lists/help_pl_list.txt
%defattr(-,root,root)

%files help-pt -f file-lists/help_pt_list.txt
%defattr(-,root,root)

%files help-pt_BR -f file-lists/help_pt_BR_list.txt
%defattr(-,root,root)

# %files help-pt_AO -f file-lists/help_pt_AO_list.txt
# %defattr(-,root,root)

%files help-ru -f file-lists/help_ru_list.txt
%defattr(-,root,root)

%files help-si -f file-lists/help_si_list.txt
%defattr(-,root,root)

%files help-sk -f file-lists/help_sk_list.txt
%defattr(-,root,root)

%files help-sl -f file-lists/help_sl_list.txt
%defattr(-,root,root)

%files help-sv -f file-lists/help_sv_list.txt
%defattr(-,root,root)

# %files help-ta -f file-lists/help_ta_list.txt
# %defattr(-,root,root)

%files help-tr -f file-lists/help_tr_list.txt
%defattr(-,root,root)

%files help-uk -f file-lists/help_uk_list.txt
%defattr(-,root,root)

%files help-zh_CN -f file-lists/help_zh_CN_list.txt
%defattr(-,root,root)

%files help-zh_TW -f file-lists/help_zh_TW_list.txt
%defattr(-,root,root)

# %files help-zu -f file-lists/help_zu_list.txt
# %defattr(-,root,root)

%files help-en_US -f file-lists/help_en_US_list.txt
%defattr(-,root,root)
%endif

#removed --with-system-hsqldb
# BuildRequires:  ant-apache-regexp
