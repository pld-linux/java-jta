Summary:	Java Transaction API
Name:		jta
Version:	1.0.1a
Release:	1
License:	Sun Microsystems, Inc. Binary Code License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	jta-1_0_1a.zip
URL:		http://java.sun.com/products/jat
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
Java Transaction API

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp *.jar $RPM_BUILD_ROOT/%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_javalibdir}
%{_javalibdir}/*.jar
