#
# You can define min_kernel macro by "rpm --define 'min_kernel version'"
# default is 2.2.0 (no changes up to 2.3.25)

%{!?min_kernel:%define		min_kernel	2.2.0}

Summary:	GNU libc
Summary(de):	GNU libc
Summary(fr):	GNU libc
Summary(pl):	GNU libc
Summary(ru):	GNU libc ������ 2.2
Summary(tr):	GNU libc
Summary(uk):	GNU libc ���Ӧ� 2.2
Name:		glibc
Version:	2.2.5
Release:	25
Epoch:		6
License:	LGPL
Group:		Libraries
#ftp://sources.redhat.com/pub/glibc/releases/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	5be613d02b934d8e305dd2f93062fa6c
Source1:	ftp://sources.redhat.com/pub/glibc/releases/%{name}-linuxthreads-%{version}.tar.bz2
# Source1-md5:	33b9ae01d51263867d338adfba105278
Source2:	nscd.init
Source3:	nscd.sysconfig
Source4:	nscd.logrotate
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source5-md5:	ddba280857330dabba4d8c16d24a6dfd
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source6-md5:	2e3992c2e1bc94212c2cd33236de6058
Source7:	postshell.c
# borrowed from util-linux
Source8:	sln.8
Patch0:		%{name}-info.patch
Patch1:		%{name}-versions.awk_fix.patch
Patch2:		%{name}-pld.patch
Patch3:		%{name}-crypt-blowfish.patch
Patch4:		%{name}-string2-pointer-arith.patch
Patch5:		%{name}-linuxthreads-lock.patch
Patch6:		%{name}-pthread_create-manpage.patch
Patch7:		%{name}-sparc-linux-chown.patch
Patch8:		%{name}-ldconfig-bklinks.patch
Patch9:		%{name}-paths.patch
Patch10:	%{name}-vaargs.patch
Patch11:	%{name}-getaddrinfo-workaround.patch
Patch12:	%{name}-use-int-not-arpa.patch
Patch13:	%{name}-divdi3.patch
Patch14:	%{name}-nss_dns-overflow.patch
Patch15:	%{name}-sunrpc-overflow.patch
Patch16:	%{name}-calloc-overflow.patch
Patch17:	%{name}-gcc32.patch
Patch18:	%{name}-maxpacket.patch
Patch19:	%{name}-setrlimit.patch
Patch20:	%{name}-2.2.5-xdrmem.patch
Patch21:	%{name}-initgroups-overflow.patch
URL:		http://www.gnu.org/software/libc/
BuildRequires:	gd-devel >= 2.0.1
BuildRequires:	gettext-devel >= 0.10.36
BuildRequires:	libpng-devel
BuildRequires:	perl
BuildRequires:	rpm-build >= 4.0.2-46
BuildRequires:	texinfo
Provides:	ld.so.2
Provides:	ldconfig
Provides:	/sbin/ldconfig
Obsoletes:	%{name}-common
Obsoletes:	%{name}-debug
Obsoletes:	ldconfig
Autoreq:	false
PreReq:		basesystem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kernel < %{min_kernel}
Conflicts:	man-pages < 1.43
Conflicts:	ld.so < 1.9.9-10

%define		debugcflags	-O1 -g

%description
Contains the standard libraries that are used by multiple programs on
the system. In order to save disk space and memory, as well as to ease
upgrades, common system code is kept in one place and shared between
programs. This package contains the most important sets of shared
libraries, the standard C library and the standard math library.
Without these, a Linux system will not function. It also contains
national language (locale) support and timezone databases.

%description -l de
Enth�lt die Standard-Libraries, die von verschiedenen Programmen im
System benutzt werden. Um Festplatten- und Arbeitsspeicher zu sparen
und zur Vereinfachung von Upgrades ist der gemeinsame Systemcode an
einer einzigen Stelle gespeichert und wird von den Programmen
gemeinsam genutzt. Dieses Paket enth�lt die wichtigsten Sets der
shared Libraries, die Standard-C-Library und die
Standard-Math-Library, ohne die das Linux-System nicht funktioniert.
Ferner enth�lt es den Support f�r die verschiedenen Sprachgregionen
(locale) und die Zeitzonen-Datenbank.

%description -l fr
Contient les biblioth�ques standards utilis�es par de nombreux
programmes du syst�me. Afin d'�conomiser l'espace disque et m�moire,
et de faciliter les mises � jour, le code commun au syst�me est mis �
un endroit et partag� entre les programmes. Ce paquetage contient les
biblioth�ques partag�es les plus importantes, la biblioth�que standard
du C et la biblioth�que math�matique standard. Sans celles-ci, un
syst�me Linux ne peut fonctionner. Il contient aussi la gestion des
langues nationales (locales) et les bases de donn�es des zones
horaires.

%description -l pl
W pakiecie znajduj� si� podstawowe biblioteki, u�ywane przez r�ne
programy w Twoim systemie. U�ywanie przez programy bibliotek z tego
pakietu oszcz�dza miejsce na dysku i pami��. Wiekszo�� kodu
systemowego jest usytuowane w jednym miejscu i dzielone mi�dzy wieloma
programami. Pakiet ten zawiera bardzo wa�ny zbi�r bibliotek
standardowych, wsp�dzielonych (dynamicznych) bibliotek C i
matematycznych. Bez glibc system Linux nie jest w stanie funkcjonowa�.
Znajduj� si� tutaj r�wnie� definicje r�nych informacji dla wielu
j�zyk�w (locale) oraz definicje stref czasowych.

%description -l ru
�������� ����������� ����������, ������������ ���������������
����������� � �������. ��� ����, ����� ��������� �������� ������������
� ������, � ����� ��� �������� ����������, ��������� ���, ����� ���
���� ��������, �������� � ����� ����� � ����������� ������������ �����
�����������. ���� ����� �������� �������� ������ �� �����������
��������� - ����������� ���������� C � ����������� ����������
����������. ��� ���� ��������� Linux ��������������� �� �����. �����
����� �������� ��������� ������������ ������ (locale) � ���� ������
��������� ��� (timezone databases).

%description -l tr
Bu paket, bir�ok program�n kulland��� standart kitapl�klar� i�erir.
Disk alan� ve bellek kullan�m�n� azaltmak ve ayn� zamanda g�ncelleme
i�lemlerini kolayla�t�rmak i�in ortak sistem kodlar� tek bir yerde
tutulup programlar aras�nda payla�t�r�l�r. Bu paket en �nemli ortak
kitapl�klar�, standart C kitapl���n� ve standart matematik kitapl���n�
i�erir. Bu kitapl�klar olmadan Linux sistemi �al��mayacakt�r. Yerel
dil deste�i ve zaman dilimi veri taban� da bu pakette yer al�r.

%description -l uk
������� ��������Φ ¦�̦�����, ���Ҧ ���������������� ����������
���������� � �����ͦ. ��� ����, ��� �������� �������� ����Ԧ� ��
���'���, � ����� ��� �������� ���������� �������, ��������� ���,
�Ц����� ��� �Ӧ� �������, ���Ҧ������� � ������ ͦ�æ � ����������
����������դ���� �Ӧ�� ����������. ��� ����� ͦ����� ���¦��� �����צ
� ����ͦ���� ¦�̦���� - ���������� ¦�̦����� � �� ����������
¦�̦����� ����������. ��� ��� ¦�̦���� Linux ����æ������� �� ����.
����� ����� ͦ����� Ц������� ��æ�������� ��� (locale) �� ���� ������
������� ��� (timezone databases).

%package devel
Summary:	Additional libraries required to compile
Summary(de):	Weitere Libraries zum Kompilieren
Summary(fr):	Librairies suppl�mentaires n�cessaires � la compilation.
Summary(pl):	Dodatkowe biblioteki wymagane podczas kompilacji
Summary(ru):	�������������� ����������, ����������� ��� ����������
Summary(tr):	Geli�tirme i�in gerekli di�er kitapl�klar
Summary(uk):	�������צ ¦�̦�����, ���Ҧ�Φ ��� ���Ц��æ�
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
To develop programs which use the standard C libraries (which nearly
all programs do), the system needs to have these standard header files
and object files available for creating the executables.

%description devel -l de
Bei der Entwicklung von Programmen, die die Standard-C-Libraries
verwenden (also fast alle), ben�tigt das System diese Standard-Header-
und Objektdateien zum Erstellen der ausf�hrbaren Programme.

%description devel -l fr
Pour d�velopper des programmes utilisant les biblioth�ques standard du
C (ce que presque tous les programmes font), le syst�me doit poss�der
ces fichiers en-t�tes et objets standards pour cr�er les ex�cutables.

%description devel -l pl
Pakiet ten jest niezb�dny przy tworzeniu w�asnych program�w
korzystaj�cych ze standardowej biblioteki C. Znajduj� si� tutaj pliki
nag��wkowe oraz pliki objektowe, niezb�dne do kompilacji program�w
wykonywalnych i innych bibliotek.

%description devel -l ru
��� ���������� ��������, ������������ ����������� ���������� C (�
����������� ��� ��������� �� ����������), ������� ���������� ������ �
��������� �����, ������������ � ���� ������, ����� ���������
����������� �����.

%description devel -l tr
C kitapl���n� kullanan (ki hemen hemen hepsi kullan�yor) programlar
geli�tirmek i�in gereken standart ba�l�k dosyalar� ve statik
kitapl�klar.

%description devel -l uk
��� �������� �������, �� �������������� ��������Φ ¦�̦����� C
(��������� �Ӧ �������� �� ��������������), �����ͦ ������� ������
�� ��'���Φ �����, �� ͦ������� � ����� ����Ԧ, ��� ����������
��������Φ �����.

%package -n nscd
Summary:	Name Service Caching Daemon
Summary(pl):	Demon zapami�tuj�cy odpowiedzi serwis�w nazw
Summary(ru):	���������� ����� �������� ����
Summary(uk):	�������� ����� ��צӦ� ����
Group:		Networking/Daemons
PreReq:		/sbin/chkconfig
PreReq:		rc-scripts >= 0.2.0
Requires:	%{name} = %{version}
Requires(post):	fileutils

%description -n nscd
nscd caches name service lookups; it can dramatically improve
performance with NIS+, and may help with DNS as well. You cannot use
nscd with 2.0 kernels, due to bugs in the kernel-side thread support.
nscd happens to hit these bugs particularly hard.

%description -n nscd -l pl
nscd zapami�tuje zapytania i odpowiedzi NIS oraz DNS. Pozwala
drastycznie poprawi� szybko�� dzia�ania NIS+. Nie jest mo�liwe
u�ywanie nscd z j�drami serii 2.0.x z powodu b��d�w po stronie j�dra w
obs�udze w�tk�w.

%description -n nscd -l ru
nscd �������� ���������� �������� � �������� ����; ��� ����� �����
��������� ������������������ ������ � NIS+ �, �����, ����� ������ �
DNS.

%description -n nscd -l uk
nscd ���դ ���������� �����Ӧ� �� ���צӦ� ����; �� ���� ������
�¦������ ����˦��� ������ � NIS+ �, �����, ���� ��������� � DNS.

%package -n localedb-src
Summary:	locale database source code
Summary(pl):	Kod �r�d�owy bazy locale
Group:		Daemons
Requires:	%{name} = %{version}

%description -n localedb-src
This add-on package contains the data needed to build the locale data
files to use the internationalization features of the GNU libc. glibc
package contains standard set of locale binary database so you need
this package only when you want to build some non-standard locale
database.

%description -n localedb-src -l pl
Pakiet ten zawiera dane niezb�dne do zbudowania binarnych plik�w
lokalizacyjnych, by m�c wykorzysta� mo�liwo�ci oferowane przez GNU
libc. glibc zawiera standardowy zestaw binarnych baz lokalizacyjnych,
w zwi�zku z czym ten pakiet jest potrzebny tylko w sytuacji budowania
jakiej� niestandardowej bazy.

%package -n iconv
Summary:	Convert encoding of given files from one encoding to another
Summary(pl):	Program do konwersji plik�w tekstowych z jednego kodowania do innego
Group:		Applications/Text
Requires:	%{name} = %{version}

%description -n iconv
Convert encoding of given files from one encoding to another. You need
this package if you want to convert some documet from one encoding to
another or if you have installed some programs which use Generic
Character Set Conversion Interface.

%description -n iconv -l pl
Program do konwersji plik�w tekstowych z jednego kodowania do innego.
Musisz mie� zainstalowany ten pakiet je�eli wykonujesz konwersj�
dokument�w z jednego kodowania do innego lub je�eli masz zainstalowane
jakie� programy, kt�re korzystaj� z Generic Character Set Conversion
Interface w glibc, czyli z zestawu funkcji z tej biblioteki, kt�re
umo�liwiaj� konwersj� kodowania danych z poziomu dowolnego programu.

%package static
Summary:	Static libraries
Summary(pl):	Biblioteki statyczne
Summary(ru):	����������� ���������� glibc
Summary(uk):	������Φ ¦�̦����� glibc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNU libc static libraries.

%description static -l pl
Biblioteki statyczne GNU libc.

%description static -l ru
��� ��������� ����� �� ������������ ������������, ������� ������ ��
������ � glibc-devel.

%description static -l uk
�� ������� ����� ڦ ���������� ¦�̦�������, �� ¦���� �� ������� �
����� glibc-devel.

%package profile
Summary:	glibc with profiling support
Summary(de):	glibc mit Profil-Unterst�tzung
Summary(fr):	glibc avec support pour profiling
Summary(pl):	glibc ze wsparciem dla profilowania
Summary(ru):	GNU libc � ���������� ����������
Summary(tr):	�l��m deste�i olan glibc
Summary(uk):	GNU libc � Ц�������� ����������
Group:		Development/Libraries/Libc
Obsoletes:	libc-profile
Requires:	%{name}-devel = %{version}

%description profile
When programs are being profiled used gprof, they must use these
libraries instead of the standard C libraries for gprof to be able to
profile them correctly.

%description profile -l de
Damit Programmprofile mit gprof richtig erstellt werden, m�ssen diese
Libraries anstelle der �blichen C-Libraries verwendet werden.

%description profile -l pl
Programy profilowane za pomoc� gprof musz� u�ywa� tych bibliotek
zamiast standardowych bibliotek C, aby gprof m�g� odpowiednio je
wyprofilowa�.

%description profile -l uk
���� �������� ���̦�������� ����������� gprof, ���� �����Φ
��������������� ��ͦ��� ����������� ¦�̦���� ¦�̦�����, �� ͦ�������
� ����� ����Ԧ. ��� ����������Φ ����������� ¦�̦���� gprof ��ͦ���
�������� ��������Ԧ� ���� ���������� æ�� �� ������ � �������� �
������������ ��æ...

%description profile -l tr
gprof kullan�larak �l��len programlar standart C kitapl��� yerine bu
kitapl��� kullanmak zorundad�rlar.

%description profile -l ru
����� ��������� ����������� ����������� gprof, ��� ������
������������, ������ ����������� ���������, ����������, ���������� �
���� �����. ��� ������������� ����������� ��������� gprof ������
�������� ����������� ����� ���������� ���� �� ������ � �������� �
����������� ����...

%package pic
Summary:	glibc PIC archive
Summary(pl):	archiwum PIC glibc
Group:		Development/Libraries/Libc
Requires:	%{name}-devel = %{version}

%description pic
GNU C Library PIC archive contains an archive library (ar file)
composed of individual shared objects. This is used for creating a
library which is a smaller subset of the standard libc shared library.

%description pic -l pl
Archiwum PIC biblioteki GNU C zawiera archiwaln� bibliotek� (plik ar)
z�o�on� z pojedy�czych obiekt�w wsp�dzielonych. U�ywana jest do
tworzenia biblioteki b�d�cej mniejszym podzestawem standardowej
biblioteki wsp�dzielonej libc.

%package -n nss_compat
Summary:	Old style NYS NSS glibc module
Summary(pl):	Stary modu� NYS NSS glibc
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_compat
Old style NYS NSS glibc module.

%description -n nss_compat -l pl
Stary modu� NYS NSS glibc.

%package -n nss_dns
Summary:	BIND NSS glibc module
Summary(pl):	Modu� BIND NSS glibc
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_dns
BIND NSS glibc module.

%description -n nss_dns -l pl
Modu� BIND NSS glibc.

%package -n nss_files
Summary:	Traditional files databases NSS glibc module
Summary(pl):	Modu� tradycyjnych plikowych baz danych NSS glibc
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_files
Traditional files databases NSS glibc module.

%description -n nss_files -l pl
Modu� tradycyjnych plikowych baz danych NSS glibc.

%package -n nss_hesiod
Summary:	Hesiod NSS glibc module
Summary(pl):	Modu� hesiod NSS glibc
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_hesiod
glibc NSS (Name Service Switch) module for databases access.

%description -n nss_hesiod -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych.

%package -n nss_nis
Summary:	NIS(YP) NSS glibc module
Summary(pl):	Modu� NIS(YP) NSS glibc
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_nis
glibc NSS (Name Service Switch) module for NIS(YP) databases access.

%description -n nss_nis -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych NIS(YP).

%package -n nss_nisplus
Summary:	NIS+ NSS module
Summary(pl):	Modu� NIS+ NSS
Group:		Base
Requires:	%{name} = %{version}

%description -n nss_nisplus
glibc NSS (Name Service Switch) module for NIS+ databases accesa.

%description -n nss_nisplus -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych NIS+.

%package memusage
Summary:	A toy
Summary(pl):	Zabawka
Group:		Applications
Requires:	%{name} = %{version}
Requires:	gd

%description memusage
A toy.

%description memusage -l pl
Zabawka.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
#%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1

chmod +x scripts/cpp

%build
# avoid stripping ld.so by -s in rpmldflags
LDFLAGS=" " ; export LDFLAGS
%configure2_13 \
	--enable-add-ons=linuxthreads \
	--enable-kernel="%{?kernel:%{kernel}}%{!?kernel:%{min_kernel}}" \
	--enable-profile \
	--disable-omitfp

%{__make}

# this need improvements (like building agains new builded glibc) but works
%{__cc} -o postshell %{rpmcflags} %{rpmldflags} %{SOURCE7}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{logrotate.d,rc.d/init.d,sysconfig},%{_mandir}/man{3,8},/var/log}

env LANGUAGE=C LC_ALL=C \
%{__make} install \
	install_root=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	mandir=%{_mandir}

env LANGUAGE=C LC_ALL=C \
%{__make} install-locales -C localedata \
	install_root=$RPM_BUILD_ROOT

PICFILES="libc_pic.a libc.map
	math/libm_pic.a libm.map
	resolv/libresolv_pic.a"

install $PICFILES				$RPM_BUILD_ROOT%{_libdir}
install elf/soinit.os				$RPM_BUILD_ROOT%{_libdir}/soinit.o
install elf/sofini.os				$RPM_BUILD_ROOT%{_libdir}/sofini.o

mv -f $RPM_BUILD_ROOT/lib/libmemusage.so	$RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT/lib/libpcprofile.so	$RPM_BUILD_ROOT%{_libdir}

%{__make} -C linuxthreads/man
install linuxthreads/man/*.3thr			$RPM_BUILD_ROOT%{_mandir}/man3

rm -rf $RPM_BUILD_ROOT%{_datadir}/zoneinfo/{localtime,posixtime,posixrules}

ln -sf ../../..%{_sysconfdir}/localtime		$RPM_BUILD_ROOT%{_datadir}/zoneinfo/localtime
ln -sf localtime				$RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixtime
ln -sf localtime				$RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixrules
ln -sf ../..%{_libdir}/libbsd-compat.a		$RPM_BUILD_ROOT%{_libdir}/libbsd.a

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/localtime

install %{SOURCE2}		$RPM_BUILD_ROOT/etc/rc.d/init.d/nscd
install %{SOURCE3}		$RPM_BUILD_ROOT/etc/sysconfig/nscd
install %{SOURCE4}		$RPM_BUILD_ROOT/etc/logrotate.d/nscd
install nscd/nscd.conf		$RPM_BUILD_ROOT%{_sysconfdir}
install nss/nsswitch.conf	$RPM_BUILD_ROOT%{_sysconfdir}

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
bzip2 -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
> $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.cache
> $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf
rm -f %{_mandir}/hu/man7/man.7

:> $RPM_BUILD_ROOT/var/log/nscd

rm -rf documentation
install -d documentation

cp -f linuxthreads/ChangeLog documentation/ChangeLog.threads
cp -f linuxthreads/Changes documentation/Changes.threads
cp -f linuxthreads/README documentation/README.threads
cp -f crypt/README.ufc-crypt documentation/

cp -f ChangeLog documentation

rm -f $RPM_BUILD_ROOT%{_libdir}/libnss_*.so

# strip ld.so with --strip-debug only (other ELFs are stripped by rpm):
%{!?debug:strip -g -R .comment -R .note $RPM_BUILD_ROOT/lib/ld-%{version}.so}

# Collect locale files and mark them with %%lang()
rm -f glibc.lang
for i in $RPM_BUILD_ROOT%{_datadir}/locale/* $RPM_BUILD_ROOT%{_libdir}/locale/* ; do
	if [ -d $i ]; then
		lang=`echo $i | sed -e 's/.*locale\///' -e 's/\/.*//'`
		twochar=1
		# list of long %%lang values we do support
		for j in de_AT de_BE de_CH de_LU ja_JP.SJIS ko_KR.utf8 pt_BR \
			 zh_CN zh_CN.gbk zh_HK zh_TW ; do
			if [ $j = "$lang" ]; then
				twochar=
			fi
		done
		if [ -n "$twochar" ]; then
			if [ `echo $lang | sed "s,_.*,,"` = "zh" ]; then
				lang=`echo $lang | sed "s,\..*,,"`
			else
				lang=`echo $lang | sed "s,_.*,,"`
			fi
		fi	
		dir=`echo $i | sed "s#$RPM_BUILD_ROOT##"`
		echo "%lang($lang) $dir" >> glibc.lang
	fi
done
for i in af ar az be bg cy de_AT el en eo es_ES et eu fi ga gr he hi hr hu id \
	 is ja_JP.SJIS ka lt lv ms nn pt ro ru sl sq sr ta tg th uk uz vi wa \
	 zh_CN ; do
	if [ ! -d $i ]; then
		install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES
		lang=`echo $i | sed -e 's/_.*//'`
		echo "%lang($lang) %{_datadir}/locale/$i" >> glibc.lang
	fi
done
install %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/man8

install -m755 postshell $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

# don't run iconvconfig in %%postun -n iconv because iconvconfig doesn't exist
# when %%postun is run

%post	-p /sbin/postshell
/sbin/ldconfig
-/sbin/telinit u

%postun -p /sbin/postshell
/sbin/ldconfig
-/sbin/telinit u

%post	memusage -p /sbin/ldconfig
%postun memusage -p /sbin/ldconfig

%post -n iconv -p %{_sbindir}/iconvconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post -n nscd
/sbin/chkconfig --add nscd
touch /var/log/nscd && (chmod 000 /var/log/nscd; chown root.root /var/log/nscd; chmod 640 /var/log/nscd)
if [ -f /var/lock/subsys/nscd ]; then
	/etc/rc.d/init.d/nscd restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/nscd start\" to start nscd daemon." 1>&2
fi

%preun -n nscd
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/nscd ]; then
		/etc/rc.d/init.d/nscd stop 1>&2
	fi
	/sbin/chkconfig --del nscd
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS FAQ BUGS

%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/ld.so.conf
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/nsswitch.conf
%config %{_sysconfdir}/rpc
%ghost %{_sysconfdir}/ld.so.cache

%attr(755,root,root) /sbin/*
%attr(755,root,root) %{_bindir}/catchsegv
%attr(755,root,root) %{_bindir}/getent
%attr(755,root,root) %{_bindir}/glibcbug
%attr(755,root,root) %{_bindir}/iconv
%attr(755,root,root) %{_bindir}/ldd
%ifnarch alpha sparc sparc64 ppc
%attr(755,root,root) %{_bindir}/lddlibc4
%endif
%attr(755,root,root) %{_bindir}/locale
%attr(755,root,root) %{_bindir}/rpcgen
%attr(755,root,root) %{_bindir}/tzselect

%attr(755,root,root) %{_sbindir}/rpcinfo
%attr(755,root,root) %{_sbindir}/zdump
%attr(755,root,root) %{_sbindir}/zic

%attr(755,root,root) /lib/ld-*
%attr(755,root,root) /lib/libanl*
%attr(755,root,root) /lib/libdl*
%attr(755,root,root) /lib/libnsl*
%attr(755,root,root) /lib/lib[BScmprtu]*

%dir %{_datadir}/locale
%{_datadir}/locale/locale.alias
%{_datadir}/zoneinfo

%dir %{_libdir}/locale

%{_mandir}/man1/[^lsg]*
%{_mandir}/man1/getent.1*
%{_mandir}/man1/locale.1*
%{_mandir}/man1/ldd.1*
%{_mandir}/man5/???[^d]*
%{_mandir}/man7/*
%{_mandir}/man8/[^n]*
%lang(cs) %{_mandir}/cs/man[578]/*
%lang(de) %{_mandir}/de/man[578]/*
%lang(es) %{_mandir}/es/man[578]/*
%lang(fi) %{_mandir}/fi/man1/ldd.1*
%lang(fr) %{_mandir}/fr/man1/ldd.1*
%lang(fr) %{_mandir}/fr/man[578]/*
%lang(hu) %{_mandir}/hu/man1/ldd.1*
%lang(hu) %{_mandir}/hu/man[578]/*
%lang(it) %{_mandir}/it/man[578]/*
%lang(ja) %{_mandir}/ja/man1/[^lsg]*
%lang(ja) %{_mandir}/ja/man1/ldd.1*
%lang(ja) %{_mandir}/ja/man5/???[^d]*
%lang(ja) %{_mandir}/ja/man7/*
%lang(ja) %{_mandir}/ja/man8/[^n]*
%lang(ko) %{_mandir}/ko/man[578]/*
# %lang(nl) %{_mandir}/nl/man[578]/*
%lang(pl) %{_mandir}/pl/man1/ldd.1*
%lang(pl) %{_mandir}/pl/man[578]/*
%lang(pt) %{_mandir}/pt/man5/???[^d]*
%lang(pt) %{_mandir}/pt/man7/*
%lang(pt) %{_mandir}/pt/man8/[^n]*
%lang(pt_BR) %{_mandir}/pt_BR/man5/???[^d]*
%lang(pt_BR) %{_mandir}/pt_BR/man7/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/[^n]*
%lang(ru) %{_mandir}/ru/man[578]/*

#%files -n nss_dns
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_dns*.so*

#%files -n nss_files
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_files*.so*

%files -n nss_compat
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_compat*.so*

%files -n nss_hesiod
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_hesiod*.so*

%files -n nss_nis
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_nis.so.*
%attr(755,root,root) /lib/libnss_nis-*.so

%files -n nss_nisplus
%defattr(644,root,root,755)
%attr(755,root,root) /lib/libnss_nisplus*.so*

%files memusage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/memusage*
%attr(755,root,root) %{_libdir}/libmemusage*

%files devel
%defattr(644,root,root,755)
%doc documentation/* NOTES PROJECTS
%attr(755,root,root) %{_bindir}/gencat
%attr(755,root,root) %{_bindir}/getconf
%attr(755,root,root) %{_bindir}/*prof*
%attr(755,root,root) %{_bindir}/*trace

%{_includedir}/*

%{_infodir}/libc.info*

%attr(755,root,root) %{_libdir}/lib[^m]*.so
%attr(755,root,root) %{_libdir}/libm.so
%attr(755,root,root) %{_libdir}/*crt*.o
%{_libdir}/libbsd-compat.a
%{_libdir}/libbsd.a
%{_libdir}/libc_nonshared.a
%{_libdir}/libg.a
%{_libdir}/libieee.a
%{_libdir}/librpcsvc.a

%{_mandir}/man1/getconf*
%{_mandir}/man1/sprof*
%{_mandir}/man3/*
%lang(cs) %{_mandir}/cs/man3/*
%lang(de) %{_mandir}/de/man3/*
%lang(es) %{_mandir}/es/man3/*
%lang(fr) %{_mandir}/fr/man3/*
%lang(hu) %{_mandir}/hu/man3/*
# %lang(it) %{_mandir}/it/man3/*
%lang(ja) %{_mandir}/ja/man3/*
%lang(ko) %{_mandir}/ko/man3/*
%lang(nl) %{_mandir}/nl/man3/*
%lang(pl) %{_mandir}/pl/man3/*
%lang(pt) %{_mandir}/pt/man3/*
%lang(pt_BR) %{_mandir}/pt_BR/man3/*
%lang(ru) %{_mandir}/ru/man3/*

%files -n nscd
%defattr(644,root,root,755)
%attr(640,root,root) %config %verify(not md5 size mtime) /etc/sysconfig/nscd
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/nscd.*
%attr(754,root,root) /etc/rc.d/init.d/nscd
%attr(755,root,root) %{_sbindir}/nscd*
%attr(640,root,root) /etc/logrotate.d/nscd
%attr(640,root,root) %ghost /var/log/nscd
%{_mandir}/man5/nscd.conf*
%{_mandir}/man8/nscd*
%lang(ja) %{_mandir}/ja/man5/nscd.conf*
%lang(ja) %{_mandir}/ja/man8/nscd*
%lang(pt) %{_mandir}/pt/man5/nscd.conf*
%lang(pt) %{_mandir}/pt/man8/nscd*
%lang(pt_BR) %{_mandir}/pt_BR/man5/nscd.conf*
%lang(pt_BR) %{_mandir}/pt_BR/man8/nscd*

%files -n localedb-src
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/localedef
%{_datadir}/i18n
%{_mandir}/man1/localedef*

%files -n iconv
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/iconvconfig
%dir %{_libdir}/gconv
%{_libdir}/gconv/gconv-modules
%attr(755,root,root) %{_libdir}/gconv/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libanl.a
%{_libdir}/libBrokenLocale.a
%{_libdir}/libc.a
%{_libdir}/libcrypt.a
%{_libdir}/libdl.a
%{_libdir}/libm.a
%{_libdir}/libmcheck.a
%{_libdir}/libnsl.a
%{_libdir}/libpthread.a
%{_libdir}/libresolv.a
%{_libdir}/librt.a
%{_libdir}/libutil.a

%files profile
%defattr(644,root,root,755)
%{_libdir}/lib*_p.a

%files pic
%defattr(644,root,root,755)
%{_libdir}/lib*_pic.a
%{_libdir}/lib*.map
%{_libdir}/soinit.o
%{_libdir}/sofini.o
