# bconds:
# _with_gtk2

%include	/usr/lib/rpm/macros.python

%define		module	wxPython

Summary:	Cross platform GUI toolkit for Python
Summary(pl):	Wielo-platformowe narzêdzie GUI dla Pythona
Name:		python-%{module}
Version:	2.4.0.7
Release:	0.3
License:	wxWindows Library v. 3 (LGPL derivative)
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/wxpython/%{module}Src-%{version}.tar.gz
Patch0:		%{module}-contrib.patch
URL:		http://wxpython.org/
Prereq:         /sbin/ldconfig
BuildRequires:  rpm-pythonprov
%pyrequires_eq	python-modules
BuildRequires:	glib-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	python >= 2.2.1
%if 0%{?_with_gtk2:1}
BuildRequires:	wxGTK2-unicode-devel >= 2.4.0
BuildRequires:	wxGTK2-unicode-gl-devel >= 2.4.0
%else
BuildRequires:	wxGTK-devel >= 2.4.0
BuildRequires:	wxGTK-gl-devel >= 2.4.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxPython is a GUI toolkit for Python that is a wrapper around the
wxWindows C++ GUI library. wxPython provides a large variety of window
types and controls, all implemented with a native look and feel (and
native runtime speed) on the platforms it is supported on.

%description -l pl
wxPython jest narzêdziem GUI dla Pythona bêd±cym nak³adk± na
bibliotekê GUI napisan± w C++ o nazwie wxWindows. wxPython dostarcza
du¿± liczbê typów okien, kontrolek.

%package examples
Summary:	wxPython example programs
Summary(pl):	Przyk³adowe programy wxPython
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description examples
wxPython example programs

%description examples -l pl
Przyk³adowe programy wxPython

%prep
%setup -q -n %{module}Src-%{version}
%patch0 -p1

%build
cd wxPython
CFLAGS="%{rpmcflags}" python setup.py build \
	IN_CVS_TREE=1 \
	WXPORT=gtk%{?_with_gtk2:2} \
	UNICODE=%(expr 0 + 0%{?_with_gtk2:1}) 

%install
cd wxPython
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	IN_CVS_TREE=1 \
	WXPORT=gtk%{?_with_gtk2:2} \
	UNICODE=%(expr 0 + 0%{?_with_gtk2:1}) \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT 

install wxPython/tools/XRCed/*.txt $RPM_BUILD_ROOT%{py_sitedir}/%{module}/tools/XRCed/
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc wxPython/{CHANGES.txt,README.txt}
#don't remove this files, because this is licensing information
%doc docs/{licence.txt,licendoc.txt,preamble.txt}
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/%{module}/lib
%dir %{py_sitedir}/%{module}/lib/PyCrust
%dir %{py_sitedir}/%{module}/lib/PyCrust/wxd
%dir %{py_sitedir}/%{module}/lib/colourchooser
%dir %{py_sitedir}/%{module}/lib/editor
%dir %{py_sitedir}/%{module}/lib/mixins
%dir %{py_sitedir}/%{module}/tools
%dir %{py_sitedir}/%{module}/tools/XRCed
%{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/lib/*.py[co]
%{py_sitedir}/%{module}/lib/PyCrust/*.py[co]
%{py_sitedir}/%{module}/lib/PyCrust/wxd/*.py[co]
%{py_sitedir}/%{module}/lib/colourchooser/*.py[co]
%{py_sitedir}/%{module}/lib/editor/*.py[co]
%{py_sitedir}/%{module}/lib/mixins/*.py[co]
%{py_sitedir}/%{module}/tools/*.py[co]
%{py_sitedir}/%{module}/tools/XRCed/*.py[co]
%{py_sitedir}/%{module}/tools/XRCed/*.txt

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
