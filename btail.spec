Summary:	Bayesian log filter
Summary(pl.UTF-8):	Filtr beyesiański do logów
Name:		btail
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.vanheusden.com/btail/%{name}-%{version}.tgz
# Source0-md5:	08f785b77f559b3d4e86fe2dbf4ec752
URL:		http://www.vanheusden.com/btail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Btail monitors a logfile for specific events. To do this it uses a
bayesian filter to determine what events are worth passing through and
which should be suppressed. So it filters out all of the routine
stuff, but passes through anything important or out of the ordinary.

%description -l pl.UTF-8
Btail monitoruje plik z logami na wypadek niestandardowych wydarzeń.
Wykorzystuje filtr bayesiański do określenia które wydarzenia są warte
pokazania, a które należy opuścić. Wszystkie rutynowe komunikaty są
więc odfiltrowane, natomiast nieregularne i ważne wydarzenia zostają
przepuszczone przez filtr

%prep
%setup -q
sed -i -e  's/ncurses.h/ncurses\/ncurses.h/' error.cpp
sed -i -e 's/\(\/usr\/local\/bin\)/\$\(DESTDIR\)\/usr\/bin/' Makefile

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
