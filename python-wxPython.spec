%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl.UTF-8):   Wieloplatformowe narzędzie GUI dla Pythona
Name:		python-%{module}
Version:	2.8.0.1
Release:	1
License:	wxWindows Library v3.1 (LGPL derivative)
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/wxpython/%{module}-src-%{version}.tar.bz2
# Source0-md5:	5d4000fa5fc330519e882e6cc115b000
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
URL:		http://wxpython.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.8.0
# optional: libgnomeprint >= 2.8 (if wx uses it), gstreamer 0.8
%pyrequires_eq	python-modules
Requires:	wxGTK2-unicode-gl >= 2.8.0
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

%package examples
Summary:	wxPython example programs
Summary(pl.UTF-8):   Przykładowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
wxPython example programs.

%description examples -l pl.UTF-8
Przykładowe programy w wxPythonie.

%prep
%setup -q -n %{module}-src-%{version}
%patch0 -p1

# old version, not lib64-aware; use the one which comes with python.
rm -rf wxPython/distutils

%build
cd wxPython
CFLAGS="%{rpmcflags}" python setup.py build \
	WX_CONFIG=%{_bindir}/wx-gtk2-unicode-config \
	UNICODE=1

%install
rm -rf $RPM_BUILD_ROOT
cd wxPython

python setup.py install \
	WX_CONFIG=%{_bindir}/wx-gtk2-unicode-config \
	INSTALL_MULTIVERSION=0 \
	UNICODE=1 \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{py_sitedir}/wxversion.py

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded
rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/samples/embedded/embedded.o

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wxPython/docs/{CHANGES.txt,MigrationGuide.txt,README.txt}
#don't remove this files, because this is licensing information
%doc docs/{licence.txt,licendoc.txt,preamble.txt}
%attr(755,root,root) %{_bindir}/*

%{py_sitedir}/wxversion.py[co]

%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py[co]
%dir %{py_sitedir}/%{module}/lib/colourchooser
%{py_sitedir}/%{module}/lib/colourchooser/*.py[co]
%dir %{py_sitedir}/%{module}/lib/editor
%{py_sitedir}/%{module}/lib/editor/*.py[co]
%dir %{py_sitedir}/%{module}/lib/mixins
%{py_sitedir}/%{module}/lib/mixins/*.py[co]
%dir %{py_sitedir}/%{module}/tools
%{py_sitedir}/%{module}/tools/*.py[co]

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
%dir %{py_sitedir}/wx/lib/masked
%{py_sitedir}/wx/lib/masked/*.py[co]
%dir %{py_sitedir}/wx/lib/mixins
%{py_sitedir}/wx/lib/mixins/*.py[co]
%dir %{py_sitedir}/wx/lib/ogl
%{py_sitedir}/wx/lib/ogl/*.py[co]
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

%dir %{py_sitescriptdir}/wxaddons
%{py_sitescriptdir}/wxaddons/*.py[co]

%{py_sitedir}/*.egg-info
%{py_sitescriptdir}/*.egg-info

# -devel?
#%{_includedir}/wx-2.6/wx/wxPython

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
