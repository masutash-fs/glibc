Summary:	GNU libc
Summary(de):	GNU libc
Summary(fr):	GNU libc
Summary(pl):	GNU libc
Summary(tr):	GNU libc
name:		glibc
Version:	2.1.1
Release:	1
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://sourceware.cygnus.com/pub/glibc/%{name}-%{version}.tar.gz
Source1:	ftp://sourceware.cygnus.com/pub/glibc/%{name}-linuxthreads-%{version}.tar.gz
Source2:	http://www.ozemail.com.au/~geoffk/glibc-crypt/%{name}-crypt-2.1.tar.gz
Source3:	utmpd.init
Source4:	nscd.init
Patch0:		glibc-info.patch
URL:		http://www.gnu.org/software/libc/
Provides:	ld.so.2
Obsoletes:	%{name}-profile
Obsoletes:	%{name}-debug
Autoreq:	false
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Contains the standard libraries that are used by multiple programs on the
system. In order to save disk space and memory, as well as to ease upgrades,
common system code is kept in one place and shared between programs. This
package contains the most important sets of shared libraries, the standard C
library and the standard math library. Without these, a Linux system will
not function. It also contains national language (locale) support and
timezone databases.

%description -l de
Enth�lt die Standard-Libraries, die von verschiedenen Programmen im System
benutzt werden. Um Festplatten- und Arbeitsspeicher zu sparen und zur
Vereinfachung von Upgrades ist der gemeinsame Systemcode an einer einzigen
Stelle gespeichert und wird von den Programmen gemeinsam genutzt. Dieses
Paket enth�lt die wichtigsten Sets der shared Libraries, die
Standard-C-Library und die Standard-Math-Library, ohne die das Linux-System
nicht funktioniert. Ferner enth�lt es den Support f�r die verschiedenen
Sprachgregionen (locale) und die Zeitzonen-Datenbank.

%description -l fr
Contient les biblioth�ques standards utilis�es par de nombreux programmes
du syst�me. Afin d'�conomiser l'espace disque et m�moire, et de faciliter
les mises � jour, le code commun au syst�me est mis � un endroit et partag�
entre les programmes. Ce paquetage contient les biblioth�ques partag�es les
plus importantes, la biblioth�que standard du C et la biblioth�que
math�matique standard. Sans celles-ci, un syst�me Linux ne peut fonctionner.
Il contient aussi la gestion des langues nationales (locales) et les bases
de donn�es des zones horaires.

%description -l pl
W pakiecie znajduj� si� podstawowe biblioteki, u�ywane przez r�ne programy
w Twoim systemie. U�ywanie przez programy bibliotek z tego pakietu oszcz�dza
miejsce na dysku i pami��. Wiekszo�� kodu systemowego jest usytuowane w
jednym miejscu i dzielone mi�dzy wieloma programami. Pakiet ten zawiera
bardzo wa�ny zbi�r bibliotek standardowych wsp�dzielonych (dynamicznych)
bibliotek C i matematycznych. Bez glibc system Linux nie jest w stanie
funkcjonowa�. Znajduj� si� tutaj r�wnie� definicje r�nych informacji dla
wielu j�zyk�w (locale) oraz definicje stref czasowych.

%description -l tr
Bu paket, bir�ok program�n kulland��� standart kitapl�klar� i�erir. Disk
alan� ve bellek kullan�m�n� azaltmak ve ayn� zamanda g�ncelleme i�lemlerini
kolayla�t�rmak i�in ortak sistem kodlar� tek bir yerde tutulup programlar
aras�nda payla�t�r�l�r. Bu paket en �nemli ortak kitapl�klar�, standart
C kitapl���n� ve standart matematik kitapl���n� i�erir. Bu kitapl�klar olmadan
Linux sistemi �al��mayacakt�r. Yerel dil deste�i ve zaman dilimi veri taban�
da bu pakette yer al�r.

%package devel
Summary:	Additional libraries required to compile
Summary(de):	Weitere Libraries zum Kompilieren
Summary(fr):	Librairies suppl�mentaires n�cessaires � la compilation.
Summary(pl):	Dodatkowe biblioteki wymagane podczas kompilacji
Summary(tr):	Geli�tirme i�in gerekli di�er kitapl�klar
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Prereq:		/sbin/install-info
Requires:	%{name} = %{version}

%description devel
To develop programs which use the standard C libraries (which nearly all
programs do), the system needs to have these standard header files and object
files available for creating the executables.

%description -l de devel
Bei der Entwicklung von Programmen, die die Standard-C-Libraries verwenden
(also fast alle), ben�tigt das System diese Standard-Header- und Objektdateien
zum Erstellen der ausf�hrbaren Programme.

%description -l fr devel
Pour d�velopper des programmes utilisant les biblioth�ques standard du C
(ce que presque tous les programmes font), le syst�me doit poss�der ces
fichiers en-t�tes et objets standards pour cr�er les ex�cutables.

%description -l pl devel
Pakiet ten jest niezb�dny przy tworzeniu w�asnych program�w korzystaj�cych
ze standardowej biblioteki C. Znajduj� si� tutaj pliki nag��wkowe oraz pliki 
objektowe, niezb�dne do kompilacji program�w wykonywalnych i innych bibliotek.

%description -l tr devel
C kitapl���n� kullanan (ki hemen hemen hepsi kullan�yor) programlar
geli�tirmek i�in gereken standart ba�l�k dosyalar� ve statik kitapl�klar.

%package static
Summary:	Additional libraries required to compile
Summary(pl):	Dodatkowe biblioteki wymagane podczas kompilacji
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-static-base = %{version}

%description static
Additional libraries required to compile static programs.

%description static -l pl
Dodatkowe biblioteki wymagane podczas kompilacji program�w w wersji statycznej.
Potrzebne tylko przy kompilacji niekt�rych program�w.

%package static-base
Summary:	Static libc.a and libm.a
Summary(pl):	Statyczne libc.a i libm.a
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static-base
Base library in static version.

%description static-base -l pl
Dwie podstawowe (libc.a i libcm.a) biblioteki w wersji statycznej.
Potrzebne tylko przy kompilacji niekt�rych program�w.

%package -n nscd
Summary:	Name Service Caching Daemon
Summary(pl):	-
Group:		Networnikng/Daemons
Group:		Sieciowe/Serwery
Prereq:		/sbin/chkconfig
Conflicts:	kernel < 2.2.0

%description -n nscd
nscd caches name service lookups; it can dramatically improve performance
with NIS+, and may help with DNS as well.

You cannot use nscd with 2.0 kernels, due to bugs in the kernel-side thread
support. nscd happens to hit these bugs particularly hard.

%description -n nscd -l pl
nscd zapmi�tuje zapytania i odpowiedzi NIS oraz DNS. Pozwala drastycznie 
poprawi� szybko�� dzia�ania NIS+.

Nie jest mo�liwe u�ywanie nscd z j�drami serii 2.0.x z powodu b�ad�w
po stronie j�dra w ods�udze w�tk�w.

%package -n utmpd
Summary:	utmp and utmpx synchronizer for libc5 applications.
Summary(pl):	Synchrnonizuje pliki utmp i utmpx.
Group:		Daemons
Group(pl):	Serwery
Prereq:         /sbin/chkconfig

%description -n utmpd
utmpd is a utmp and utmpx synchronizer. Is only needed for libc5 based 
program with utmp access.

%description -n utmpd -l pl
utmpd stara si� utrzyma� tak� sam� zawarto�� plik�w 
/var/run/utmp i /var/run/utmpx. Potrzebny jest tylko w przypadku korzystania
ze starszych program�w (bazuj�cych na libc5).

%prep 
%setup  -q -a 1 -a 2
%patch0 -p1

%build
%configure \
	--enable-add-ons=crypt,linuxthreads \
	--disable-profile \
	--disable-omitfp 
make  

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/rc.d/init.d,%{_mandir}/man3,var/db}
make install \
	install_root=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	mandir=%{_mandir}
make install-locales -C localedata \
	install_root=$RPM_BUILD_ROOT

make -C linuxthreads/man
install linuxthreads/man/*.3thr $RPM_BUILD_ROOT%{_mandir}/man3

rm -rf $RPM_BUILD_ROOT/usr/share/zoneinfo/{localtime,posixtime,posixrules}

ln -sf ../../../etc/localtime $RPM_BUILD_ROOT%{_datadir}/zoneinfo/localtime
ln -sf localtime $RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixtime
ln -sf localtime $RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixrules
ln -sf ../../usr/lib/libbsd-compat.a $RPM_BUILD_ROOT%{_libdir}/libbsd.a

rm -f $RPM_BUILD_ROOT/etc/localtime

install %{SOURCE3} $RPM_BUILD_ROOT/etc/nsswitch.conf

install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/nscd
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/utmpd

install nscd/nscd.conf		$RPM_BUILD_ROOT/etc
install nss/nsswitch.conf	$RPM_BUILD_ROOT/etc

install nss/db-Makefile $RPM_BUILD_ROOT/var/db

cat << EOF > $RPM_BUILD_ROOT/usr/bin/create-db
#!/bin/sh
/usr/bin/make -f /var/db/db-Makefile
EOF

ln -sf create-db $RPM_BUILD_ROOT%{_bindir}/update-db 

rm -rf documentation
install -d documentation

cp linuxthreads/ChangeLog  documentation/ChangeLog.threads
cp linuxthreads/Changes documentation/Changes.threads
cp linuxthreads/README documentation/README.threads
cp login/README.utmpd documentation/
cp crypt/README documentation/README.crypt

cp ChangeLog ChangeLog.8 documentation

gzip -9fn README NEWS FAQ BUGS NOTES PROJECTS \
	$RPM_BUILD_ROOT{%{_mandir}/man*/*,%{_infodir}/libc*} \
	documentation/*

ls $RPM_BUILD_ROOT%{_libdir}/lib*.a \
	|egrep -v '(libc.a|libc.a|libc_nonshared.a)' \
	|sed -e "s#$RPM_BUILD_ROOT##g" >static.libs

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/libc.info.gz /etc/info-dir

%preun devel
if [ "$1" = 0 ]; then
	/sbin/install-info --delete %{_infodir}/libc.info.gz /etc/info-dir
fi

%post -n nscd
/sbin/chkconfig --add nscd
if test -r /var/run/nscd.pid; then
	/etc/rc.d/init.d/nscd stop >&2
	/etc/rc.d/init.d/nscd start >&2
else
	echo "Run \"/etc/rc.d/init.d/nscd start\" to start nscd daemon."
fi

%preun -n nscd
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del nscd
	/etc/rc.d/init.d/nscd stop >&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,NEWS,FAQ,BUGS}.gz

%config(noreplace) %verify(not mtime md5 size) /etc/nsswitch.conf
%config /etc/rpc

%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/rpcinfo
%attr(755,root,root) %{_sbindir}/zdump
%attr(755,root,root) %{_sbindir}/zic

%attr(755,root,root) /lib/ld-*
%attr(755,root,root) /lib/lib*

%dir %{_libdir}/gconv
%{_libdir}/gconv/gconv-modules

%{_datadir}/i18n
%{_datadir}/locale
%{_datadir}/zoneinfo

%dir /var/db
%config /var/db/db-*

%files devel
%defattr(644,root,root,755)
%doc documentation/* {NOTES,PROJECTS}.gz

%{_includedir}/*.h
%{_includedir}/arpa
%{_includedir}/bits
%{_includedir}/db1
%{_includedir}/gnu
%{_includedir}/net
%{_includedir}/netash
%{_includedir}/netatalk
%{_includedir}/netax25
%{_includedir}/neteconet
%{_includedir}/netinet
%{_includedir}/netipx
%{_includedir}/netpacket
%{_includedir}/netrom
%{_includedir}/netrose
%{_includedir}/nfs
%{_includedir}/protocols
%{_includedir}/rpc
%{_includedir}/rpcsvc
%{_includedir}/scsi
%{_includedir}/sys

%{_infodir}/libc.inf*.gz

%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.o
%{_libdir}/lib*.a

%attr(755,root,root) /usr/lib/gconv/*.so
%{_mandir}/man3/*

%files static-base
%defattr(644,root,root,755)
%{_libdir}/libc.a
%{_libdir}/libm.a
%{_libdir}/libc_nonshared.a

%files static -f static.libs
%defattr(644,root,root,755)

%files -n nscd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not mtime md5 size) /etc/nscd.*
%attr(754,root,root) /etc/rc.d/init.d/nscd
%attr(755,root,root) %{_sbindir}/nscd

%files -n utmpd
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/utmpd
%attr(755,root,root) %{_sbindir}/utmpd

%changelog
* Wed May 19 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
- macro %{_target_platform},
- some macros,
- updated to version pre3,
- FHS 2.0

* Sun Mar 14 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.1-6]
- updated glibc-crypt to version-2.1

* Sat Mar 06 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.1-5]
- removed striping of shared libraries -- no debug info in this libs,
- fixed /etc/rc.d/init.d/* -- Tomek, never again 754 on start scripts... 
- fixed permission of /var/db directory -- should be 755...

* Mon Feb 22 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.1-4]
- removed man group from man pages,
- standarized {un}registering info pages (added libc-info.patch),
- changed base source url to ftp://sourceware.cygnus.com/pub/glibc/,
- changed URL,
- siplifications in %files devel,
- Group in devel changed to Development/Libraries,
- removed some %doc (INSTALL and outdated ChangeLog),
- removed %config and %verify rules fromn /etc/rc.d/init.d/* files,
- changed permission to 754 on /etc/rc.d/init.d/*,
- added striping shared libraries.

* Sun Feb 14 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.1-3d]
- updated to stable version,
- fixed stripping ELF binaries,
- removed obsoletes /usr/include/{asm,linux}

* Fri Jan 29 1999 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.0.111-1d]
- updated to latest snapshoot,
- added utmpd.init, (don't run this piece of ... by default)
- added /var/db, (don't generate a data base by default)
- removed unused /usr/libexec/pt_ch*
- other changes.

* Sat Nov 07 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.0.100-1d]
- updated to latest snapshoot,
- added install-locales,
- minor changes.

* Tue Oct 13 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [2.0.99-1d]
- updated to 2.0.99,
- added Obsoletes: glibc-debug, glibc-profile

* Thu Aug 06 1998 Wojtek �lusarczyk <wojtek@SHADOW.EU.ORG>
  [2.0.96-1d]
- updated to 2.0.96,
- translation modified for pl, 
  (follow the suggestions Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>)
- major changes.
      (rewrote invalid spec file -- follow the PLD policy)

* Wed Jul 16 1998 Wojtek �lusarczyk <wojtek@SHADOW.EU.ORG>
  [2.0.94-2d]
- added nscd.init and config
- fixed permision of pt_chown to 4711 
- added %defattr
- moved linux include links from kernel-headers to glibc-devel

* Tue Jun 2 1998 Wojtek Slusarczyk <wojtek@SHADOW.EU.ORG>
  [2.0.94-1d]
- updated to glibc 2.0.94

* Sun May 24 1998 Marcin Korzonek <mkorz@euler.mat.univ.szczecin.pl>
  [2.0.93-1d]
- updated for glibc 2.0.93
- build prepare for PLD-1.1 Tornado
- removed glibc-debug and glibc-profile packages generation (it took too
  long to compile the full featured version on my home linux box ;)
- compilation is now performed in compile directory as advised 
  in Glibc HOWTO,
- start at invalid RH spec file.
  [2.1.1-1]
- based on RH spec,
- spec rewrited by PLD team,
  we start at GNU libc 2.0.92 one year ago ...
- pl translation by Wojtek �lusarczyk <wojtek@shadow.eu.org>.
