%include	/usr/lib/rpm/macros.python

%define		module	wxPython

Summary:	Cross platform GUI toolkit for Python
Summary(pl):	Wielo-platformowe narzêdzie GUI dla Pythona
Name:		python-%{module}
Version:	2.3.2.1
Release:	6
Source0:	http://prdownloads.sourceforge.net/wxpython/%{module}-%{version}.tar.gz
Patch0:		%{module}-no_gizmos.patch
License:	wxWindows (LGPL derivative)
Group:		Libraries/Python
BuildRequires:  rpm-pythonprov
%pyrequires_eq	python-modules
BuildRequires:	glib-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	wxGTK-devel >= 2.3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://wxpython.org/

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
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT 

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt licence/*.txt
%dir %{py_sitedir}/%{module}/lib
%dir %{py_sitedir}/%{module}/lib/PyCrust
%dir %{py_sitedir}/%{module}/lib/editor
%dir %{py_sitedir}/%{module}/lib/mixins
%{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]
%{py_sitedir}/%{module}/lib/*.py[co]
%{py_sitedir}/%{module}/lib/PyCrust/*.py[co]
%{py_sitedir}/%{module}/lib/editor/*.py[co]
%{py_sitedir}/%{module}/lib/mixins/*.py[co]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
