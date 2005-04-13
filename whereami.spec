Summary:	A simple command that displays your location on a server
Summary(pl):	Prosty program pokazuj±cy twoja lokacje na serwerze
Name:		whereami
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://jkcool.com/whereami/%{name}-%{version}.tar.gz
# Source0-md5:	bac6d761d6d66e07649b6b8ed68b6f81
URL:		http://jkcool.com/whereami/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whereami is a program that allows you to help you figure out where
your located on servers. It really helps if you are SSHed multiple
times.

%description -l pl
Whereami to program, który pozwala pomóc w odnalezieniu gdzie jeste¶
zlokalizowany na serwerach. To naprawdê pomaga je¿eli jeste¶
zalogowany przez SSH wielokrotnie.

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
