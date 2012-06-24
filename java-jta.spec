# NOTE:
# - it seems to be an open source JTA implementation:
#   http://www.atomikos.com/Main/TransactionsEssentials
%define	_ver	%(echo %{version} | tr . _)
%define		srcname	jta
%include	/usr/lib/rpm/macros.java
Summary:	Java Transaction API
Summary(es.UTF-8):	API de transacciones para Java
Summary(pl.UTF-8):	API transakcji do Javy
Name:		java-jta
Version:	1.0.1B
Release:	0.1
License:	restricted, non-distributable (Sun Binary Code License - see URL)
Group:		Libraries/Java
Source0:	%{srcname}-%{_ver}-classes.zip
# NoSource0-md5:	c6e3e528816227b97f6b21f709641f8f
NoSource:	0
URL:		http://java.sun.com/products/jta/
BuildRequires:	unzip
Requires:	jre
Provides:	java(jta) = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java Transaction API.

%description -l es.UTF-8
API de transacciones para Java.

%description -l pl.UTF-8
API transakcji do Javy.

%prep
%setup -q -c

%build
jar cf %{srcname}-%{version}.jar javax/

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javadir}
install *.jar $RPM_BUILD_ROOT%{_javadir}
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
