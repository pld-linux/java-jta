
Summary:	Java Transaction API
Summary(es):	API de transacciones para Java
Summary(pl):	API transakcji do Javy
Name:		jta
Version:	1.0.1a
%define _ver	%(echo %{version} | tr . _)
Release:	2
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
#Source0:	%{name}-%{_ver}.zip
Source0:	http://student.ing-steen.se/java/jakarta/%{name}-%{_ver}.zip
URL:		http://java.sun.com/products/jat/
NoSource:	0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Java Transaction API.

%description -l es
API de transacciones para Java.

%description -l pl
API transakcji do Javy.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install *.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
