%define		module	wxPython
Summary:	Cross platform GUI toolkit for Python
Summary(pl):	Wielo-platformowe narz�dzie GUI dla Pythona
Name:		python-%{module}
Version:	2.5.5.1
Release:	1
License:	wxWindows Library v. 3 (LGPL derivative)
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/wxpython/%{module}-src-%{version}.tar.gz
# Source0-md5:	050602f803814a1a458634cf07ab6984
URL:		http://wxpython.org/
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	wxGTK2-unicode-devel >= 2.5.5
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.5.5
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWindows C++ GUI library. wxPython provides a large variety of window
types and controls, all implemented with a native look and feel (and
native runtime speed) on the platforms it is supported on.

%description -l pl
wxPython jest narz�dziem GUI dla Pythona b�d�cym nak�adk� na
bibliotek� GUI napisan� w C++ o nazwie wxWindows. wxPython dostarcza
du�� liczb� typ�w okien, kontrolek.

%package examples
Summary:	wxPython example programs
Summary(pl):	Przyk�adowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description examples
wxPython example programs

%description examples -l pl
Przyk�adowe programy wxPython

%prep
%setup -q -n %{module}-src-%{version}

# kill precompiled x86 binaries
rm -f wxPython/demo/dllwidget/test_dll.{o,so}

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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc wxPython/docs/{CHANGES.txt,MigrationGuide.txt,README.txt}
#don't remove this files, because this is licensing information
%doc docs/{licence.txt,licendoc.txt,preamble.txt}
%attr(755,root,root) %{_bindir}/*
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
