#
# TODO:
#		- update to 1.0.1B (and pack classe into jar).
#
Summary:	Java Transaction API
Summary(es):	API de transacciones para Java
Summary(pl):	API transakcji do Javy
Name:		jta
Version:	1.0.1a
Release:	2
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Development/Languages/Java
Source0:	%{name}-%(echo %{version} | tr . _).zip
URL:		http://java.sun.com/products/jta/
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
