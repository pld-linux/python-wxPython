%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl):	Wieloplatformowe narzêdzie GUI dla Pythona
Name:		python-%{module}
Version:	2.6.2.1
Release:	0.1
License:	wxWindows Library v3.1 (LGPL derivative)
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/wxpython/%{module}-src-%{version}.tar.gz
# Source0-md5:	aae333c806acd5e5227a7afd2505286a
Source1:	%{name}-wxversion-null.py
Patch0:		%{name}-CFLAGS.patch
URL:		http://wxpython.org/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.3
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	wxGTK2-unicode-devel >= 2.6.1
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.6.1
# optional: libgnomeprint >= 2.8 (if wx uses it), gstreamer 0.8
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWidgets C++ GUI library. wxPython provides a large variety of window
types and controls, all implemented with a native look and feel (and
native runtime speed) on the platforms it is supported on.

%description -l pl
wxPython jest narzêdziem GUI dla Pythona bêd±cym nak³adk± na
bibliotekê GUI napisan± w C++ o nazwie wxWidgets. wxPython dostarcza
du¿± liczbê typów okien, kontrolek.

%package examples
Summary:	wxPython example programs
Summary(pl):	Przyk³adowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description examples
wxPython example programs.

%description examples -l pl
Przyk³adowe programy w wxPythonie.

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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
