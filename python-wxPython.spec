#
# Conditional build:
%bcond_with	system_wx	# system wxWidgets (3.0.x)

%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl.UTF-8):	Wieloplatformowe narzędzie GUI dla Pythona
Name:		python-%{module}
# keep 4.0.x here for python2 support
Version:	4.0.7.post2
Release:	1
License:	wxWindows Library Licence 3.1 (LGPL v2+ with exception)
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wxpython/
Source0:	https://files.pythonhosted.org/packages/source/w/wxPython/%{module}-%{version}.tar.gz
# Source0-md5:	e10f59d8e1565b034c4933334ea1eb19
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
Patch1:		%{name}-setup.patch
URL:		https://wxpython.org/
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with system_wx}
BuildRequires:	wxGTK3-unicode-devel >= 3.0.0
BuildRequires:	wxGTK3-unicode-gl-devel >= 3.0.0
BuildRequires:	wxGTK3-unicode-devel < 3.2
BuildRequires:	wxGTK3-unicode-gl-devel < 3.2
%endif
# optional: libgnomeprint >= 2.8 (if wx uses it), gstreamer 0.8
Requires:	python-modules >= 1:2.7
%if %{with system_wx}
Requires:	wxGTK3-unicode >= 3.0.0
Requires:	wxGTK3-unicode-gl >= 2.8.9
%endif
Obsoletes:	python-wxPython-editra < 4
Obsoletes:	python-wxPython-xrced < 4
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
%setup -q -n %{module}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' demo/{__main__,demo,run}.py samples/mainloop/mainloop.py

%build
%if %{with system_wx}
export WX_CONFIG=%{_bindir}/wx-gtk3-unicode-config
%endif
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%if %{with system_wx}
export WX_CONFIG=%{_bindir}/wx-gtk3-unicode-config
%endif

%py_install

for bin in $RPM_BUILD_ROOT%{_bindir}/* ; do
	%{__mv} "$bin" "${bin}-2"
done

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{py_sitedir}/wxversion.py

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/editor/README.txt README.editor.txt
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/plot/CHANGELOG.md CHANGELOG.plot.md
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/plot/README.md README.plot.md
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/pubsub/LICENSE_BSD_Simple.txt LICENSE_BSD_Simple.pubsub.txt
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/pubsub/README_WxPython.txt README_WxPython.pubsub.txt
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/pubsub/RELEASE_NOTES.txt RELEASE_NOTES.pubsub.txt
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/wx/lib/plot/examples
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/wx/py/tests

%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/locale/{gl_ES,gl}
%{__mv} $RPM_BUILD_ROOT%{py_sitedir}/wx/locale/{ko_KR,ko}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst TODO.rst docs/{MigrationGuide,classic_vs_phoenix}.rst README.editor.txt CHANGELOG.plot.md README.plot.md LICENSE_BSD_Simple.pubsub.txt README_WxPython.pubsub.txt RELEASE_NOTES.pubsub.txt
%attr(755,root,root) %{_bindir}/helpviewer-2
%attr(755,root,root) %{_bindir}/img2png-2
%attr(755,root,root) %{_bindir}/img2py-2
%attr(755,root,root) %{_bindir}/img2xpm-2
%attr(755,root,root) %{_bindir}/pycrust-2
%attr(755,root,root) %{_bindir}/pyshell-2
%attr(755,root,root) %{_bindir}/pyslices-2
%attr(755,root,root) %{_bindir}/pyslicesshell-2
%attr(755,root,root) %{_bindir}/pywxrc-2
%attr(755,root,root) %{_bindir}/wxdemo-2
%attr(755,root,root) %{_bindir}/wxdocs-2
%attr(755,root,root) %{_bindir}/wxget-2
%{py_sitedir}/wxversion.py[co]
%dir %{py_sitedir}/wx
%if %{without system_wx}
%{py_sitedir}/wx/libwx_baseu*-3.0.so*
%{py_sitedir}/wx/libwx_gtk3u*-3.0.so*
%dir %{py_sitedir}/wx/locale
# wxstd domain for wxWidgets 3.0.x
%lang(af) %{py_sitedir}/wx/locale/af
%lang(an) %{py_sitedir}/wx/locale/an
%lang(ar) %{py_sitedir}/wx/locale/ar
%lang(ca) %{py_sitedir}/wx/locale/ca
%lang(ca@valencia) %{py_sitedir}/wx/locale/ca@valencia
%lang(cs) %{py_sitedir}/wx/locale/cs
%lang(da) %{py_sitedir}/wx/locale/da
%lang(de) %{py_sitedir}/wx/locale/de
%lang(el) %{py_sitedir}/wx/locale/el
%lang(es) %{py_sitedir}/wx/locale/es
%lang(eu) %{py_sitedir}/wx/locale/eu
%lang(fi) %{py_sitedir}/wx/locale/fi
%lang(fr) %{py_sitedir}/wx/locale/fr
%lang(gl) %{py_sitedir}/wx/locale/gl
%lang(hi) %{py_sitedir}/wx/locale/hi
%lang(hu) %{py_sitedir}/wx/locale/hu
%lang(id) %{py_sitedir}/wx/locale/id
%lang(it) %{py_sitedir}/wx/locale/it
%lang(ja) %{py_sitedir}/wx/locale/ja
%lang(ko) %{py_sitedir}/wx/locale/ko
%lang(lt) %{py_sitedir}/wx/locale/lt
%lang(lv) %{py_sitedir}/wx/locale/lv
%lang(ms) %{py_sitedir}/wx/locale/ms
%lang(nb) %{py_sitedir}/wx/locale/nb
%lang(ne) %{py_sitedir}/wx/locale/ne
%lang(nl) %{py_sitedir}/wx/locale/nl
%lang(pl) %{py_sitedir}/wx/locale/pl
%lang(pt) %{py_sitedir}/wx/locale/pt
%lang(pt_BR) %{py_sitedir}/wx/locale/pt_BR
%lang(ro) %{py_sitedir}/wx/locale/ro
%lang(ru) %{py_sitedir}/wx/locale/ru
%lang(sk) %{py_sitedir}/wx/locale/sk
%lang(sl) %{py_sitedir}/wx/locale/sl
%lang(sq) %{py_sitedir}/wx/locale/sq
%lang(sv) %{py_sitedir}/wx/locale/sv
%lang(ta) %{py_sitedir}/wx/locale/ta
%lang(tr) %{py_sitedir}/wx/locale/tr
%lang(uk) %{py_sitedir}/wx/locale/uk
%lang(vi) %{py_sitedir}/wx/locale/vi
%lang(zh_CN) %{py_sitedir}/wx/locale/zh_CN
%lang(zh_TW) %{py_sitedir}/wx/locale/zh_TW
%endif
%{py_sitedir}/wx/_*.so
%{py_sitedir}/wx/siplib.so
%{py_sitedir}/wx/*.py[co]
%{py_sitedir}/wx/*.pyi
%dir %{py_sitedir}/wx/lib
%{py_sitedir}/wx/lib/*.py[co]
%{py_sitedir}/wx/lib/myole4ax.idl
%{py_sitedir}/wx/lib/myole4ax.tlb
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
%dir %{py_sitedir}/wx/lib/gizmos
%{py_sitedir}/wx/lib/gizmos/*.py[co]
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
%{py_sitedir}/wx/lib/pdfviewer/bitmaps
%dir %{py_sitedir}/wx/lib/plot
%{py_sitedir}/wx/lib/plot/*.py[co]
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
%dir %{py_sitedir}/wx/lib/wxcairo
%{py_sitedir}/wx/lib/wxcairo/*.py[co]
%dir %{py_sitedir}/wx/py
%{py_sitedir}/wx/py/*.ico
%{py_sitedir}/wx/py/*.png
%{py_sitedir}/wx/py/*.py[co]
%doc %{py_sitedir}/wx/py/*.txt
%dir %{py_sitedir}/wx/tools
%{py_sitedir}/wx/tools/*.py[co]
%{py_sitedir}/wxPython-%{version}-py*.egg-info

%files devel
%defattr(644,root,root,755)
%{py_sitedir}/wx/include

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
