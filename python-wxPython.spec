# TODO: move Editra locale (.mo) files to system LC_MESSAGES dirs
%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl.UTF-8):	Wieloplatformowe narzędzie GUI dla Pythona
Name:		python-%{module}
Version:	3.0.2.0
Release:	4
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		Libraries/Python
Source0:	https://downloads.sourceforge.net/wxpython/%{module}-src-%{version}.tar.bz2
# Source0-md5:	922b02ff2c0202a7bf1607c98bbbbc04
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-format.patch
URL:		https://wxpython.org/
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.8.11
# optional: libgnomeprint >= 2.8 (if wx uses it), gstreamer 0.8
Requires:	python-modules
Requires:	wxGTK2-unicode-gl >= 2.8.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWidgets C++ GUI library. wxPython provides a large variety of window
types and controls, all implemented with a native look and feel (and
native runtime speed) on the platforms it is supported on.

%description -l pl.UTF-8
wxPython jest narzędziem GUI dla Pythona będącym nakładką na
bibliotekę GUI napisaną w C++ o nazwie wxWidgets. wxPython dostarcza
dużą liczbę typów okien, kontrolek.

%package devel
Summary:	Header and SWIG files for wxPython
Summary(pl.UTF-8):	Pliki nagłówkowe i SWIG dla wxPythona
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	wxWidgets-devel >= 2.8.7

%description devel
Header and SWIG files for wxPython.

%description devel -l pl.UTF-8
Pliki nagłówkowe i SWIG dla wxPythona.

%package editra
Summary:	Editra editor
Summary(pl.UTF-8):	Edytor Editra
Group:		Development/Tools
URL:		http://editra.org/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	%{name} = %{version}-%{release}

%description editra
Editra is a multi-platform text editor with an implementation that
focuses on creating an easy to use interface and features that aid in
code development. Currently it supports syntax highlighting and
variety of other useful features for over 50 programming languages.

%description editra -l pl.UTF-8
Editra to wieloplatformowy edytor tekstu, którego implementacja skupia
się na stworzeniu łatwego w użyciu interfejsu i możliwościach
pomagających w tworzeniu kodu. Aktualnie obsługuje podświetlanie
składni i różne przydatne ułatwienia dla ponad 50 języków
programowania.

%package xrced
Summary:	XRCed - XRC files editor
Summary(pl.UTF-8):	XRCed - edytor plików XRC
License:	BSD
Group:		Development/Tools
URL:		http://xrced.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	%{name} = %{version}-%{release}

%description xrced
XRCed is a simple resource editor for wxWidgets/wxPython GUI
development which supports creating and editing files in XRC format.
It is written in Python and uses wxPython GUI toolkit.

%description xrced -l pl.UTF-8
XRCed to prosty edytor zasobów do programowania w środowisku
graficznym wxWidgets/wxPython, pozwalający na tworzenie i
modyfikowanie plików w formacie XRC. Został napisany w Pythonie i
wykorzystuje toolkit graficzny wxPython.

%package examples
Summary:	wxPython example programs
Summary(pl.UTF-8):	Przykładowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description examples
wxPython example programs.

%description examples -l pl.UTF-8
Przykładowe programy w wxPythonie.

%prep
%setup -q -n %{module}-src-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
cd wxPython
%py_build \
	WX_CONFIG=%{_bindir}/wx-gtk2-unicode-config \
	UNICODE=1

%install
rm -rf $RPM_BUILD_ROOT
cd wxPython

%py_install \
	WX_CONFIG=%{_bindir}/wx-gtk2-unicode-config \
	INSTALL_MULTIVERSION=0 \
	UNICODE=1 \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{py_sitedir}/wxversion.py

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded.o

%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/editor/README.txt README.editor.txt
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/wx/tools/Editra/{AUTHORS,CHANGELOG,COPYING,FAQ,INSTALL,MANIFEST.in,NEWS,README,THANKS,TODO,docs/*.txt,setup.py*,tests,plugins/*.egg}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wxPython/docs/{CHANGES.txt,MigrationGuide.txt,README.txt} wxPython/README.editor.txt
#don't remove these files, because this is licensing information
%doc docs/{licence.txt,licendoc.txt,preamble.txt}
%attr(755,root,root) %{_bindir}/helpviewer
%attr(755,root,root) %{_bindir}/img2png
%attr(755,root,root) %{_bindir}/img2py
%attr(755,root,root) %{_bindir}/img2xpm
%attr(755,root,root) %{_bindir}/pyalacarte
%attr(755,root,root) %{_bindir}/pyalamode
%attr(755,root,root) %{_bindir}/pycrust
%attr(755,root,root) %{_bindir}/pyshell
%attr(755,root,root) %{_bindir}/pywrap
%attr(755,root,root) %{_bindir}/pywxrc

%{py_sitedir}/wxversion.py[co]

%dir %{py_sitedir}/wx
%attr(755,root,root) %{py_sitedir}/wx/*.so
%{py_sitedir}/wx/*.py[co]
%dir %{py_sitedir}/wx/build
%{py_sitedir}/wx/build/*.py[co]
%dir %{py_sitedir}/wx/lib
%{py_sitedir}/wx/lib/*.py[co]
%dir %{py_sitedir}/wx/lib/analogclock
%{py_sitedir}/wx/lib/analogclock/*.py[co]
%dir %{py_sitedir}/wx/lib/analogclock/lib_setup
%{py_sitedir}/wx/lib/analogclock/lib_setup/*.py[co]
%dir %{py_sitedir}/wx/lib/art
%{py_sitedir}/wx/lib/art/*.py[co]
%dir %{py_sitedir}/wx/lib/colourchooser
%{py_sitedir}/wx/lib/colourchooser/*.py[co]
%dir %{py_sitedir}/wx/lib/editor
%{py_sitedir}/wx/lib/editor/*.py[co]
%dir %{py_sitedir}/wx/lib/floatcanvas
%{py_sitedir}/wx/lib/floatcanvas/*.py[co]
%dir %{py_sitedir}/wx/lib/floatcanvas/Utilities
%{py_sitedir}/wx/lib/floatcanvas/Utilities/*.py[co]
%dir %{py_sitedir}/wx/lib/masked
%{py_sitedir}/wx/lib/masked/*.py[co]
%dir %{py_sitedir}/wx/lib/mixins
%{py_sitedir}/wx/lib/mixins/*.py[co]
%dir %{py_sitedir}/wx/lib/ogl
%{py_sitedir}/wx/lib/ogl/*.py[co]
%dir %{py_sitedir}/wx/lib/agw
%{py_sitedir}/wx/lib/agw/*.py[co]
%{py_sitedir}/wx/lib/agw/data
%dir %{py_sitedir}/wx/lib/agw/aui
%{py_sitedir}/wx/lib/agw/aui/*.py[co]
%dir %{py_sitedir}/wx/lib/agw/persist
%{py_sitedir}/wx/lib/agw/persist/*.py[co]
%dir %{py_sitedir}/wx/lib/agw/ribbon
%{py_sitedir}/wx/lib/agw/ribbon/*.py[co]
%dir %{py_sitedir}/wx/lib/pdfviewer
%{py_sitedir}/wx/lib/pdfviewer/*.py[co]
%dir %{py_sitedir}/wx/lib/pubsub
%{py_sitedir}/wx/lib/pubsub/*.py[co]
%dir %{py_sitedir}/wx/lib/pubsub/core
%{py_sitedir}/wx/lib/pubsub/core/*.py[co]
%dir %{py_sitedir}/wx/lib/pubsub/core/arg1
%{py_sitedir}/wx/lib/pubsub/core/arg1/*.py[co]
%dir %{py_sitedir}/wx/lib/pubsub/core/kwargs
%{py_sitedir}/wx/lib/pubsub/core/kwargs/*.py[co]
%dir %{py_sitedir}/wx/lib/pubsub/utils
%{py_sitedir}/wx/lib/pubsub/utils/*.py[co]
%dir %{py_sitedir}/wx/py
%{py_sitedir}/wx/py/*.ico
%{py_sitedir}/wx/py/*.py[co]
%doc %{py_sitedir}/wx/py/*.txt
%dir %{py_sitedir}/wx/tools
%{py_sitedir}/wx/tools/*.py[co]
%dir %{py_sitedir}/wx/tools/XRCed
%{py_sitedir}/wx/tools/XRCed/*.py[co]
%doc %{py_sitedir}/wx/tools/XRCed/*.txt
%{py_sitedir}/wx/tools/XRCed/*.xrc

%{py_sitedir}/wxPython-*.egg-info

%files devel
%defattr(644,root,root,755)
%{_includedir}/wx-3.0/wx/wxPython

%files editra
%defattr(644,root,root,755)
%doc wxPython/wx/tools/Editra/{AUTHORS,CHANGELOG,COPYING,FAQ,NEWS,README,THANKS,TODO,docs/*.txt}
%attr(755,root,root) %{_bindir}/editra
%dir %{py_sitedir}/wx/tools/Editra
%{py_sitedir}/wx/tools/Editra/__init__.py[co]
%{py_sitedir}/wx/tools/Editra/launcher.py[co]
%{py_sitedir}/wx/tools/Editra/Editra.pyw
%dir %{py_sitedir}/wx/tools/Editra/locale
%lang(ca) %{py_sitedir}/wx/tools/Editra/locale/ca_ES@valencia
%lang(cs) %{py_sitedir}/wx/tools/Editra/locale/cs_CZ
%lang(da) %{py_sitedir}/wx/tools/Editra/locale/da_DK
%lang(de) %{py_sitedir}/wx/tools/Editra/locale/de_DE
%lang(en) %{py_sitedir}/wx/tools/Editra/locale/en_US
%lang(es) %{py_sitedir}/wx/tools/Editra/locale/es_ES
%lang(fr) %{py_sitedir}/wx/tools/Editra/locale/fr_FR
%lang(gl) %{py_sitedir}/wx/tools/Editra/locale/gl_ES
%lang(hr) %{py_sitedir}/wx/tools/Editra/locale/hr_HR
%lang(hu) %{py_sitedir}/wx/tools/Editra/locale/hu_HU
%lang(it) %{py_sitedir}/wx/tools/Editra/locale/it_IT
%lang(ja) %{py_sitedir}/wx/tools/Editra/locale/ja_JP
%lang(lv) %{py_sitedir}/wx/tools/Editra/locale/lv_LV
%lang(nl) %{py_sitedir}/wx/tools/Editra/locale/nl_NL
%lang(nn) %{py_sitedir}/wx/tools/Editra/locale/nn_NO
%lang(pl) %{py_sitedir}/wx/tools/Editra/locale/pl_PL
%lang(pt_BR) %{py_sitedir}/wx/tools/Editra/locale/pt_BR
%lang(ro) %{py_sitedir}/wx/tools/Editra/locale/ro_RO
%lang(ru) %{py_sitedir}/wx/tools/Editra/locale/ru_RU
%lang(sk) %{py_sitedir}/wx/tools/Editra/locale/sk_SK
%lang(sl) %{py_sitedir}/wx/tools/Editra/locale/sl_SI
%lang(sr) %{py_sitedir}/wx/tools/Editra/locale/sr_RS
%lang(sv) %{py_sitedir}/wx/tools/Editra/locale/sv_SE
%lang(tr) %{py_sitedir}/wx/tools/Editra/locale/tr_TR
%lang(uk) %{py_sitedir}/wx/tools/Editra/locale/uk_UA
%lang(zh_CN) %{py_sitedir}/wx/tools/Editra/locale/zh_CN
%lang(zh_TW) %{py_sitedir}/wx/tools/Editra/locale/zh_TW
%{py_sitedir}/wx/tools/Editra/pixmaps
%dir %{py_sitedir}/wx/tools/Editra/src
%{py_sitedir}/wx/tools/Editra/src/*.py[co]
%dir %{py_sitedir}/wx/tools/Editra/src/autocomp
%{py_sitedir}/wx/tools/Editra/src/autocomp/*.py[co]
%dir %{py_sitedir}/wx/tools/Editra/src/eclib
%{py_sitedir}/wx/tools/Editra/src/eclib/*.py[co]
%dir %{py_sitedir}/wx/tools/Editra/src/extern
%{py_sitedir}/wx/tools/Editra/src/extern/*.py[co]
%dir %{py_sitedir}/wx/tools/Editra/src/syntax
%{py_sitedir}/wx/tools/Editra/src/syntax/*.py[co]
%dir %{py_sitedir}/wx/tools/Editra/src/ebmlib
%{py_sitedir}/wx/tools/Editra/src/ebmlib/*.py[co]
%{py_sitedir}/wx/tools/Editra/styles

%files xrced
%defattr(644,root,root,755)
%doc wxPython/wx/tools/XRCed/{CHANGES.txt,ChangeLog,README.txt,TODO.txt,license.txt}
%attr(755,root,root) %{_bindir}/xrced
%dir %{py_sitedir}/wx/tools/XRCed
%{py_sitedir}/wx/tools/XRCed/misc
%dir %{py_sitedir}/wx/tools/XRCed/plugins
%{py_sitedir}/wx/tools/XRCed/plugins/*.py[co]
%{py_sitedir}/wx/tools/XRCed/plugins/bitmaps
%{py_sitedir}/wx/tools/XRCed/plugins/gizmos.crx
%{py_sitedir}/wx/tools/XRCed/xrced.htb

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
