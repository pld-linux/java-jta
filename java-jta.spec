Summary:	Java Transaction API
Summary(pl):	API transakcji do Javy
Name:		jta
Version:	1.0.1a
Release:	2
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
#Source0:	%{name}-1_0_1a.zip
Source0:	http://student.ing-steen.se/java/jakarta/%{name}-%{version}.zip
URL:		http://java.sun.com/products/jat/
NoSource:	0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Java Transaction API.

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
