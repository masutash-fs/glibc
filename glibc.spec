#
# You can define min_kernel macro by "rpm --define 'min_kernel version'"
# default is 2.2.0 (no changes up to 2.3.25)
#
# Conditional build:
%bcond_without	fp		# build without frame pointer (pass \--enable-omitfp)
%bcond_without	memusage	# don't build memusage utility
%bcond_with	kernelheaders	# use headers from kernel-headers instead of
				# glibc-kernel-headers (evil, breakage etc., don't use)
%bcond_without	dist_kernel	# for above, allow non-distribution kernel
%bcond_with	idn		# build with included libidn
#
# TODO:
# - localedb-gen man pages(?)
# - fix what trojan broke while upgreading (getaddrinfo-workaround)
#
# WARNING:
#	posix zoneinfo dir removed, /etc/rc.d/init.d/timezone must be changed
#	in order to use this version!
#
%{!?min_kernel:%global		min_kernel	2.2.0}
%define	gkh_version	1:2.6.0.2
Summary:	GNU libc
Summary(de):	GNU libc
Summary(es):	GNU libc
Summary(fr):	GNU libc
Summary(ja):	GNU libc �饤�֥��
Summary(pl):	GNU libc
Summary(ru):	GNU libc ������ 2.3
Summary(tr):	GNU libc
Summary(uk):	GNU libc ���Ӧ� 2.3
Name:		glibc
Version:	2.3.2
Release:	13
Epoch:		6
License:	LGPL
Group:		Libraries
Source0:	ftp://sources.redhat.com/pub/glibc/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ede969aad568f48083e413384f20753c
Source1:	ftp://sources.redhat.com/pub/glibc/releases/%{name}-linuxthreads-%{version}.tar.bz2
# Source1-md5:	894b8969cfbdf787c73e139782167607
Source2:	nscd.init
Source3:	nscd.sysconfig
Source4:	nscd.logrotate
Source5:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-man-pages.tar.bz2
# Source5-md5:	ddba280857330dabba4d8c16d24a6dfd
Source6:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source6-md5:	2e3992c2e1bc94212c2cd33236de6058
# borrowed from util-linux
Source7:	sln.8
Source8:	%{name}-localedb-gen
Source10:	http://josefsson.org/libidn/releases/libidn-0.3.0rc3.tar.gz
# Source10-md5:	ded0b439efe16dd29ce5a24d3d3dcebf
Patch0:		%{name}-info.patch
Patch1:		%{name}-initgroups-overflow.patch
Patch2:		%{name}-pld.patch
Patch3:		%{name}-crypt-blowfish.patch
Patch4:		%{name}-string2-pointer-arith.patch
Patch5:		%{name}-linuxthreads-lock.patch
Patch6:		%{name}-pthread_create-manpage.patch
Patch9:		%{name}-paths.patch
Patch10:	%{name}-vaargs.patch
Patch11:	%{name}-getaddrinfo-workaround.patch
Patch12:	%{name}-postshell.patch
Patch13:	%{name}-pl.po-update.patch
Patch14:	%{name}-missing-nls.patch
Patch16:	%{name}-java-libc-wait.patch
Patch17:	%{name}-morelocales.patch
Patch18:	%{name}-lthrds_noomit.patch
Patch19:	%{name}-no_opt_override.patch
Patch20:	%{name}-gcc33.patch
#Patch21:	%{name}-sanity.patch
Patch22:	%{name}-secureexec.patch
Patch23:	%{name}-kernel_includes.patch
Patch24:	%{name}-sparc64_pause.patch
Patch25:	%{name}-linuxthreads.patch
Patch26:	%{name}-alpha-fix-as-syntax.patch
Patch27:	%{name}-soinit-EH_FRAME.patch
Patch28:	%{name}-alpha-pwrite.patch
Patch29:	%{name}-alpha-tv64.patch
URL:		http://www.gnu.org/software/libc/
BuildRequires:	automake
BuildRequires:	binutils >= 2.13.90.0.2
BuildRequires:	gcc >= 3.2
%{?with_memusage:BuildRequires:	gd-devel >= 2.0.1}
BuildRequires:	gettext-devel >= 0.10.36
%if %{with kernelheaders}
%{?with_dist_kernel:BuildRequires:	kernel-headers < 2.5}
%else
BuildRequires:	glibc-kernel-headers >= %{gkh_version}
%endif
BuildRequires:	perl-base
BuildRequires:	rpm-build >= 4.3-0.20030610.28
BuildRequires:	rpm-perlprov
BuildRequires:	sed >= 4.0.5
BuildRequires:	texinfo
PreReq:		basesystem
Provides:	ld.so.2
Provides:	ldconfig
Provides:	/sbin/ldconfig
Obsoletes:	%{name}-common
Obsoletes:	%{name}-debug
Obsoletes:	ldconfig
AutoReq:	false
Requires:	glibc-misc = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kernel < %{min_kernel}
Conflicts:	ld.so < 1.9.9-10
Conflicts:	man-pages < 1.43
Conflicts:	rc-scripts < 0.3.1-13
Conflicts:	rpm < 4.1

%define		debugcflags	-O1 -g
%ifarch sparc64
%undefine	with_memusage
%define 	specflags_sparc64	-mvis -fcall-used-g6
%define		_libdir			/usr/lib64
%endif
# hack: don't depend on rpmlib(PartialHardlinkSets) for easier upgrade from Ra
# (hardlinks here are unlikely to be "partial"... and rpm 4.0.2 from Ra was
# patched not to crash on partial hardlinks too)
%define		_hack_dontneed_PartialHardlinkSets	1

%description
Contains the standard libraries that are used by multiple programs on
the system. In order to save disk space and memory, as well as to ease
upgrades, common system code is kept in one place and shared between
programs. This package contains the most important sets of shared
libraries, the standard C library and the standard math library.
Without these, a Linux system will not function. It also contains
national language (locale) support and timezone databases.

Can be used on: Linux kernel >= %{min_kernel}.

%description -l es
Contiene las bibliotecas est�ndared que son usadas por varios programas
del sistema. Para ahorrar el espacio en el disco y la memoria, igual que
para facilitar actualizaciones, c�digo com�n del sistema se guarda en un
sitio y es compartido entre los programas. Este paquete contiene las
bibliotecas compartidas m�s importantes, es decir la biblioteca C est�ndar
y la biblioteca est�ndar de matem�tica. Sin �stas, un sistema Linux no
podr� funcionar. Tambi�n est� incluido soporte de idiomas nacionales
(locale) y bases de datos de zona de tiempo.

Puede usarse con: n�cleo Linux >= %{min_kernel}.

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

Can be used on: Linux kernel >= %{min_kernel}.

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

Can be used on: Linux kernel >= %{min_kernel}.

%description -l ja
glibc
�ѥå������ϥ����ƥ���ʣ���Υץ����ǻȤ���ɸ��饤�֥���
�դ��ߤޤ����ǥ��������ڡ����ȥ�������󤷤��ꡢ���åץ��졼�ɤ�
�Ѱդˤ��뤿��ˡ����̤Υ����ƥॳ���ɤϰ�Ĥξ��ˤ����졢�ץ����
�֤Ƕ�ͭ����ޤ���������ʬŪ�ʥѥå������ϥ������ɥ饤�֥��Τ��ʤ�
���פʥ��åȤ�դ��ߤޤ�: ɸ�� C �饤�֥���ɸ����ͥ饤�֥��Ǥ���
������ĤΥ饤�֥��ȴ���Ǥϡ�Linux �����ƥ�ϵ�ǽ���ޤ��� glibc
�ѥå������Ϥޤ��ϰ���� (locale) ���ݡ��Ȥȥ����ॾ����ǡ����١���
���ݡ��Ȥ�դ��ߤޤ���

Can be used on: Linux kernel >= %{min_kernel}.

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

Przeznaczony dla j�dra Linux >= %{min_kernel}.

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

Can be used on: Linux kernel >= %{min_kernel}.

%description -l tr
Bu paket, bir�ok program�n kulland��� standart kitapl�klar� i�erir.
Disk alan� ve bellek kullan�m�n� azaltmak ve ayn� zamanda g�ncelleme
i�lemlerini kolayla�t�rmak i�in ortak sistem kodlar� tek bir yerde
tutulup programlar aras�nda payla�t�r�l�r. Bu paket en �nemli ortak
kitapl�klar�, standart C kitapl���n� ve standart matematik kitapl���n�
i�erir. Bu kitapl�klar olmadan Linux sistemi �al��mayacakt�r. Yerel
dil deste�i ve zaman dilimi veri taban� da bu pakette yer al�r.

Can be used on: Linux kernel >= %{min_kernel}.

%description -l uk
������ ��������Φ ¦�̦�����, ���Ҧ ���������������� ����������
���������� � �����ͦ. ��� ����, ��� �������� �������� ����Ԧ� ��
���'���, � ����� ��� �������� ���������� �������, ��������� ���,
�Ц����� ��� �Ӧ� �������, ���Ҧ������� � ������ ͦ�æ � ����������
����������դ���� �Ӧ�� ����������. ��� ����� ͦ����� ���¦��� �����צ
� ����ͦ���� ¦�̦���� - ���������� ¦�̦����� � �� ����������
¦�̦����� ����������. ��� ��� ¦�̦���� Linux ����æ������� �� ����.
����� ����� ͦ����� Ц������� ��æ�������� ��� (locale) �� ���� ������
������� ��� (timezone databases).

Can be used on: Linux kernel >= %{min_kernel}.

%package misc
Summary:	Utilities and data used by glibc
Summary(pl):	Narz�dzia i dane u�ywane przez glibc
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description misc
Utilities and data used by glibc.

%description misc -l pl
Narz�dzia i dane u�ywane przez glibc.

%package devel
Summary:	Additional libraries required to compile
Summary(de):	Weitere Libraries zum Kompilieren
Summary(es):	Bibliotecas adicionales necesarias para la compilaci�n
Summary(fr):	Librairies suppl�mentaires n�cessaires � la compilation
Summary(ja):	ɸ�� C �饤�֥��ǻȤ���إå����ȥ��֥������ȥե�����
Summary(pl):	Dodatkowe biblioteki wymagane podczas kompilacji
Summary(ru):	�������������� ����������, ����������� ��� ����������
Summary(tr):	Geli�tirme i�in gerekli di�er kitapl�klar
Summary(uk):	�������צ ¦�̦�����, ���Ҧ�Φ ��� ���Ц��æ�
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%{!?with_kernelheaders:Requires:	glibc-kernel-headers >= %{gkh_version}}

%description devel
To develop programs which use the standard C libraries (which nearly
all programs do), the system needs to have these standard header files
and object files available for creating the executables.

%description devel -l de
Bei der Entwicklung von Programmen, die die Standard-C-Libraries
verwenden (also fast alle), ben�tigt das System diese Standard-Header-
und Objektdateien zum Erstellen der ausf�hrbaren Programme.

%description devel -l es
Para desarrollar programas que utilizan las bibliotecas C est�ndar
(lo cual hacen pr�cticamente todos los programas), el sistema necesita
disponer de estos ficheros de cabecera y de objetos para crear los
ejecutables.

%description devel -l fr
Pour d�velopper des programmes utilisant les biblioth�ques standard du
C (ce que presque tous les programmes font), le syst�me doit poss�der
ces fichiers en-t�tes et objets standards pour cr�er les ex�cutables.

%description devel -l ja
glibc-devel �ѥå�������(�ۤȤ�ɤ��٤ƤΥץ����ǻȤ���)ɸ�� C
�饤�֥�����Ѥ����ץ�����ȯ���뤿��Υإå����ȥ��֥�������
�ե������ޤߤޤ����⤷ɸ�� C
�饤�֥�����Ѥ���ץ�����ȯ����ʤ�
�¹ԥե���������������Ū�Ǥ�����ɸ��إå��ȥ��֥������ȥե�����
�����ѤǤ��ޤ���

%description devel -l pl
Pakiet ten jest niezb�dny przy tworzeniu w�asnych program�w
korzystaj�cych ze standardowej biblioteki C. Znajduj� si� tutaj pliki
nag��wkowe oraz pliki obiektowe, niezb�dne do kompilacji program�w
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
Summary(es):	Demonio de cach� del servicio de nombres
Summary(ja):	�͡��ॵ���ӥ�����å��󥰥ǡ���� (nacd)
Summary(pl):	Demon zapami�tuj�cy odpowiedzi serwis�w nazw
Summary(ru):	���������� ����� �������� ����
Summary(uk):	�������� ����� ��צӦ� ����
Group:		Networking/Daemons
PreReq:		rc-scripts >= 0.2.0
Requires(post,preun):	/sbin/chkconfig
Requires(post):	fileutils
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nscd
nscd caches name service lookups; it can dramatically improve
performance with NIS+, and may help with DNS as well. You cannot use
nscd with 2.0 kernels, due to bugs in the kernel-side thread support.
nscd happens to hit these bugs particularly hard.

%description -n nscd -l es
nscd guarda las peticiones del servicio de nombres en una cach�; eso puede
aumentar dr�sticamente las prestaciones de NIS+, y tambi�n puede ayudar
con DNS. No puede usar nscd con n�cleos 2.0, por contener �stos errores
en el soporte de hilos. Resulta que estos errores impactan el nscd de manera
realmente grave.

%description -n nscd -l ja
Nscd �ϥ͡��ॵ���ӥ����Ȥ򥭥�å��夷��NIS+ �Υѥե����ޥ󥹤�
�ɥ�ޥƥ��å��˲������뤳�Ȥ��Ǥ���DNS ��Ʊ�ͤ�������ޤ��� 2.0
�����ͥ�� nscd ����Ѥ��뤳�ȤϤǤ��ʤ����Ȥ���դ��Ƥ���������
����ϡ������ͥ�¦�Υ���åɥ��ݡ��Ȥ˥Х������뤫��Ǥ����Թ��ʤ��Ȥˡ�
nscd �Ϥ����ΥХ����äˤϤ����������äƤ��ޤ��ޤ���

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
Summary(es):	C�digo fuente de la base de datos de los locales
Summary(pl):	Kod �r�d�owy bazy locale
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n localedb-src
This add-on package contains the data needed to build the locale data
files to use the internationalization features of the GNU libc.

%description -n localedb-src -l es
Este paquete adicional contiene los datos necesarios para construir
los ficheros de locale, imprescindibles para usar las cualidades de
internacionalizaci�n de GNU libc.

%description -n localedb-src -l pl
Pakiet ten zawiera dane niezb�dne do zbudowania binarnych plik�w
lokalizacyjnych, by m�c wykorzysta� mo�liwo�ci oferowane przez GNU
libc.

%package localedb-all
Summary:	locale database for all locales supported by glibc
Summary(es):	Base de datos de todos los locales soportados por glibc
Summary(pl):	Baza danych locale dla wszystkich lokalizacji obs�ugiwanych przez glibc
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description localedb-all
This package contains locale database for all locales supported by
glibc. In glibc 2.3.x it's one large file (about 19MB) - if you want
something smaller with support for chosen locales only, consider
installing localedb-src and regenerating database using localedb-gen
script (when database is generated, localedb-src can be uninstalled).

%description localedb-all -l es
Este paquete contiene una base de datos de todos los locales soportados
por glibc. En glibc 2.3.x �se es un fichero grande (aprox. 19 MB) -- si
prefiere algo m�s peque�o, s�lo con soporte de unos locales elegidos,
consid�rese instalar localedb-src y regenerar la base de datos usando
el escript localedb-gen (una vez que la base de datos est� creada,
localedb-src se podr� desinstalar).

%description localedb-all -l pl
Ten pakiet zawiera baz� danych locale dla wszystkich lokalizacji
obs�ugiwanych przez glibc. W glibc 2.3.x jest to jeden du�y plik
(oko�o 19MB); aby mie� co� mniejszego, z obs�ug� tylko wybranych
lokalizacji, nale�y zainstalowa� pakiet localedb-src i przegenerowa�
baz� danych przy u�yciu skryptu localedb-gen (po wygenerowaniu bazy
pakiet localedb-src mo�na odinstalowa�).

%package -n iconv
Summary:	Convert encoding of given files from one encoding to another
Summary(es):	Convierte entre varias codificaciones de los ficheros dados
Summary(pl):	Program do konwersji plik�w tekstowych z jednego kodowania do innego
Group:		Applications/Text
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n iconv
Convert encoding of given files from one encoding to another. You need
this package if you want to convert some document from one encoding to
another or if you have installed some programs which use Generic
Character Set Conversion Interface.

%description -n iconv -l es
Convierte la codificaci�n de dados ficheros. Necesita este paquete si
quiere convertir un documento entre una codificaci�n (juego de
caracteres) y otra, o si tiene instalado alg�n programa que usa el
Generic Character Set Conversion Interface (interfaz gen�rica de
conversi�n de juegos de caracteres).

%description -n iconv -l pl
Program do konwersji plik�w tekstowych z jednego kodowania do innego.
Musisz mie� zainstalowany ten pakiet je�eli wykonujesz konwersj�
dokument�w z jednego kodowania do innego lub je�eli masz zainstalowane
jakie� programy, kt�re korzystaj� z Generic Character Set Conversion
Interface w glibc, czyli z zestawu funkcji z tej biblioteki, kt�re
umo�liwiaj� konwersj� kodowania danych z poziomu dowolnego programu.

%package static
Summary:	Static libraries
Summary(es):	Bibliotecas est�ticas
Summary(pl):	Biblioteki statyczne
Summary(ru):	����������� ���������� glibc
Summary(uk):	������Φ ¦�̦����� glibc
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
GNU libc static libraries.

%description static -l es
Bibliotecas est�ticas de GNU libc.

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
Summary(es):	glibc con soporte de perfilamiento
Summary(fr):	glibc avec support pour profiling
Summary(pl):	glibc ze wsparciem dla profilowania
Summary(ru):	GNU libc � ���������� ����������
Summary(tr):	�l��m deste�i olan glibc
Summary(uk):	GNU libc � Ц�������� ����������
Group:		Development/Libraries/Libc
Obsoletes:	libc-profile
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description profile
When programs are being profiled using gprof, they must use these
libraries instead of the standard C libraries for gprof to be able to
profile them correctly.

%description profile -l de
Damit Programmprofile mit gprof richtig erstellt werden, m�ssen diese
Libraries anstelle der �blichen C-Libraries verwendet werden.

%description profile -l es
Cuando programas son perfilidas usando gprof, tienen que usar estas
biblioteces en vez de las est�ndares para que gprof pueda perfilarlas
correctamente.

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
Summary(es):	Archivo PIC de glibc
Summary(pl):	Archiwum PIC glibc
Group:		Development/Libraries/Libc
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description pic
GNU C Library PIC archive contains an archive library (ar file)
composed of individual shared objects. This is used for creating a
library which is a smaller subset of the standard libc shared library.

%description pic -l es
El archivo PIC de la biblioteca glibc contiene una biblioteca archivada
(un fichero ar) compuesta de individuales objetos compartidos. Es usado
para crear una biblioteca que sea un subconjunto m�s peque�o de la
biblioteca libc compartida est�ndar.

%description pic -l pl
Archiwum PIC biblioteki GNU C zawiera archiwaln� bibliotek� (plik ar)
z�o�on� z pojedy�czych obiekt�w wsp�dzielonych. U�ywana jest do
tworzenia biblioteki b�d�cej mniejszym podzestawem standardowej
biblioteki wsp�dzielonej libc.

%package -n nss_compat
Summary:	Old style NYS NSS glibc module
Summary(es):	El antiguo m�dulo NYS NSS de glibc
Summary(pl):	Stary modu� NYS NSS glibc
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_compat
Old style NYS NSS glibc module.

%description -n nss_compat -l es
El antiguo m�dulo NYS NSS de glibc

%description -n nss_compat -l pl
Stary modu� NYS NSS glibc.

%package -n nss_dns
Summary:	BIND NSS glibc module
Summary(es):	M�dulo BIND NSS de glibc
Summary(pl):	Modu� BIND NSS glibc
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_dns
BIND NSS glibc module.

%description -n nss_dns -l es
M�dulo BIND NSS de glibc.

%description -n nss_dns -l pl
Modu� BIND NSS glibc.

%package -n nss_files
Summary:	Traditional files databases NSS glibc module
Summary(es):	M�dulo de tradicionales bases de datos en ficheros para glibc
Summary(pl):	Modu� tradycyjnych plikowych baz danych NSS glibc
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_files
Traditional files databases NSS glibc module.

%description -n nss_files -l es
M�dulo de tradicionales bases de datos en ficheros para glibc.

%description -n nss_files -l pl
Modu� tradycyjnych plikowych baz danych NSS glibc.

%package -n nss_hesiod
Summary:	hesiod NSS glibc module
Summary(es):	M�dulo hesiod NSS de glibc
Summary(pl):	Modu� hesiod NSS glibc
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_hesiod
glibc NSS (Name Service Switch) module for databases access.

%description -n nss_hesiod -l es
M�dulo hesiod NSS de glibc.

%description -n nss_hesiod -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych.

%package -n nss_nis
Summary:	NIS(YP) NSS glibc module
Summary(es):	M�dulo NIS(YP) NSS de glibc
Summary(pl):	Modu� NIS(YP) NSS glibc
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_nis
glibc NSS (Name Service Switch) module for NIS(YP) databases access.

%description -n nss_nis -l es
M�dulo NSS de glibc para acceder las bases de datos NIS(YP).

%description -n nss_nis -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych NIS(YP).

%package -n nss_nisplus
Summary:	NIS+ NSS module
Summary(es):	M�dulo NIS+ NSS
Summary(pl):	Modu� NIS+ NSS
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n nss_nisplus
glibc NSS (Name Service Switch) module for NIS+ databases access.

%description -n nss_nisplus -l es
M�dulo NSS (Name Service Switch) de glibc para acceder las bases de datos NIS+.

%description -n nss_nisplus -l pl
Modu� glibc NSS (Name Service Switch) dost�pu do baz danych NIS+.

%package memusage
Summary:	A toy
Summary(es):	Un juguete
Summary(pl):	Zabawka
Group:		Applications
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gd

%description memusage
A toy.

%description memusage -l es
Un juguete.

%description memusage -l pl
Zabawka.

%package zoneinfo_right
Summary:	Non-POSIX (real) time zones
Summary(es):	Zonas de tiempo reales (no de POSIX)
Summary(pl):	Nie-POSIX-owe (prawdziwe) strefy czasowe
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description zoneinfo_right
You don't want this. Details at:
http://sources.redhat.com/ml/libc-alpha/2000-12/msg00068.html

%description zoneinfo_right -l es
No lo necesita. Encontrar� los detalles en:
http://sources.redhat.com/ml/libc-alpha/2000-12/msg00068.html

%description zoneinfo_right -l pl
Nie potrzebujesz tego. Szczeg�y pod:
http://sources.redhat.com/ml/libc-alpha/2000-12/msg00068.html

%package -n %{name}64
Summary:	GNU libc - 64-bit libraries
Summary(es):	GNU libc - bibliotecas de 64 bits
Summary(pl):	GNU libc - biblioteki 64-bitowe
Group:		Libraries
%ifarch amd64
Provides:	glibc = %{epoch}:%{version}-%{release}
%else
Requires:	%{name} = %{epoch}:%{version}-%{release}
%endif

%description -n %{name}64
64-bit GNU libc libraries for sparc64 architecture.

%description -n %{name}64 -l es
Bibliotecas GNU libc de 64 bits para la arquitectura sparc64.

%description -n %{name}64 -l pl
Biblioteki 64-bitowe GNU libc dla architektury sparc64.

%package -n %{name}64-devel
Summary:	Development files for 64-bit GNU libc libraries
Summary(es):	Ficheros de desarrollo para bibliotecas GNU libc de 64 bits
Summary(pl):	Pliki do programowania z u�yciem 64-bitowych bibliotek GNU libc
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description -n %{name}64-devel
Development files for 64-bit GNU libc libraries for sparc64
architecture.

%description -n %{name}64-devel -l es
Ficheros de desarrollo para las bibliotecas GNU libc de 64 bits para la
arquitectura sparc64.

%description -n %{name}64-devel -l pl
Pliki do programowania z u�yciem 64-bitowych bibliotek GNU libc dla
architektury sparc64.

%package -n %{name}64-static
Summary:	Static 64-bit GNU libc libraries
Summary(es):	Bibliotecas est�ticas GNU libc de 64 bits
Summary(pl):	Statyczne 64-bitowe biblioteki GNU libc
Group:		Development/Libraries
Requires:	%{name}64-devel = %{epoch}:%{version}-%{release}

%description -n %{name}64-static
Static 64-bit GNU libc libraries.

%description -n %{name}64-static -l es
Bibliotecas est�ticas GNU libc de 64 bits.

%description -n %{name}64-static -l pl
Statyczne 64-bitowe biblioteki GNU libc.

%prep
%setup -q -a 1 -a 10
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch9 -p1
%patch10 -p1
#%%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
# don't know, if it is good idea, for brave ones
#%patch19 -p1
%patch20 -p1
#%patch21 -p1
%patch22 -p1
%{?with_kernelheaders:%patch23}
%patch24 -p1
# updated - lt
%ifnarch alpha
%patch25 -p1
%endif
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p0

chmod +x scripts/cpp

# standardize name
mv -f localedata/locales/{lug_UG,lg_UG}

%if %{with idn}
cp -r libidn-*/lib libidn
cp libidn-*/libc/{Makefile,configure,Banner,Versions} libidn
cp libidn-*/lib/*.{c,h} libidn
sed -e 's/idn-int.h/stdint.h/g' libidn-*/lib/idna.h > libidn/idna.h
ln -sf ../libidn/idna.h include/idna.h
sed -e 's/idn-int.h/stdint.h/g' libidn-*/lib/stringprep.h > libidn/stringprep.h
sed -e 's/idn-int.h/stdint.h/g' libidn-*/lib/punycode.h > libidn/punycode.h
sed -e 's/stringprep_generic/rfc3454/g' libidn-*/libc/Makefile > libidn/Makefile

#cp libidn-*/libc/getaddrinfo.c sysdeps/posix/
#cp libidn-*/libc/netdb.h resolv/

cp libidn-*/libc/*.patch libc-idn.patch
patch -p0 < libc-idn.patch

touch libidn/libidn.texi
%endif

#make proper symlink for asm in headers
#cd usr/include
#%ifarch %{ix86}
#ln -s asm-i386 asm
#%endif
#cd ../..

%build
# Build glibc
cp /usr/share/automake/config.sub .
cp /usr/share/automake/config.sub scripts
cp /usr/share/automake/config.sub libidn-*
[ -d builddir ] || mkdir builddir
cd builddir
# avoid stripping ld.so by -s in rpmldflags
LDFLAGS=" " ; export LDFLAGS
../%configure \
	--enable-add-ons=linuxthreads%{?with_idn:,libidn} \
	--enable-kernel="%{min_kernel}" \
	--enable-profile \
	--%{!?with_fp:en}%{?with_fp:dis}able-omitfp \
%if %{with kernelheaders}
	CPPFLAGS="-I%{_kernelsrcdir}/include" \
	--with-headers=%{_kernelsrcdir}/include
%else
	CPPFLAGS="-I%{_includedir}" \
	--with-headers=%{_includedir}
%endif

# problem compiling with --enable-bounded (must be reported to libc-alpha)

%{__make} %{?parallelmkflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{logrotate.d,rc.d/init.d,sysconfig},%{_mandir}/man{3,8},/var/log}

cd builddir

env LANGUAGE=C LC_ALL=C \
%{__make} install \
	%{?parallelmkflags} \
	install_root=$RPM_BUILD_ROOT \
	infodir=%{_infodir} \
	mandir=%{_mandir}

env LANGUAGE=C LC_ALL=C \
%{__make} localedata/install-locales \
	%{?parallelmkflags} \
	install_root=$RPM_BUILD_ROOT

PICFILES="libc_pic.a libc.map
	math/libm_pic.a libm.map
	resolv/libresolv_pic.a"

install $PICFILES				$RPM_BUILD_ROOT%{_libdir}
install elf/soinit.os				$RPM_BUILD_ROOT%{_libdir}/soinit.o
install elf/sofini.os				$RPM_BUILD_ROOT%{_libdir}/sofini.o

install elf/postshell				$RPM_BUILD_ROOT/%{_lib}
mv $RPM_BUILD_ROOT/sbin/ldconfig 		$RPM_BUILD_ROOT/%{_lib}
ln -s /%{_lib}/ldconfig 			$RPM_BUILD_ROOT/sbin

%{?with_memusage:mv -f $RPM_BUILD_ROOT/%{_lib}/libmemusage.so	$RPM_BUILD_ROOT%{_libdir}}
%ifnarch sparc64
mv -f $RPM_BUILD_ROOT/%{_lib}/libpcprofile.so	$RPM_BUILD_ROOT%{_libdir}
%endif

%{__make} -C ../linuxthreads/man
install ../linuxthreads/man/*.3thr			$RPM_BUILD_ROOT%{_mandir}/man3

rm -rf $RPM_BUILD_ROOT%{_datadir}/zoneinfo/{localtime,posixtime,posixrules,posix/*}

#cd $RPM_BUILD_ROOT%{_datadir}/zoneinfo
#for i in [A-Z]*; do
#	ln -s ../$i posix
#done
#cd -

ln -sf %{_sysconfdir}/localtime	$RPM_BUILD_ROOT%{_datadir}/zoneinfo/localtime
ln -sf localtime		$RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixtime
ln -sf localtime		$RPM_BUILD_ROOT%{_datadir}/zoneinfo/posixrules
ln -sf libbsd-compat.a		$RPM_BUILD_ROOT%{_libdir}/libbsd.a

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/localtime

# make symlinks across top-level directories absolute
for l in anl BrokenLocale crypt dl m nsl pthread resolv rt thread_db util ; do
	rm -f $RPM_BUILD_ROOT%{_libdir}/lib${l}.so
	ln -sf /%{_lib}/`cd $RPM_BUILD_ROOT/%{_lib} ; echo lib${l}.so.*` $RPM_BUILD_ROOT%{_libdir}/lib${l}.so
done

install %{SOURCE2}		$RPM_BUILD_ROOT/etc/rc.d/init.d/nscd
install %{SOURCE3}		$RPM_BUILD_ROOT/etc/sysconfig/nscd
install %{SOURCE4}		$RPM_BUILD_ROOT/etc/logrotate.d/nscd
install ../nscd/nscd.conf	$RPM_BUILD_ROOT%{_sysconfdir}
install ../nss/nsswitch.conf	$RPM_BUILD_ROOT%{_sysconfdir}

bzip2 -dc %{SOURCE5} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
bzip2 -dc %{SOURCE6} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
> $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.cache
> $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf
rm -f $RPM_BUILD_ROOT%{_mandir}/hu/man7/man.7

:> $RPM_BUILD_ROOT/var/log/nscd

rm -rf ../documentation
install -d ../documentation

cp -f ../linuxthreads/ChangeLog ../documentation/ChangeLog.threads
cp -f ../linuxthreads/Changes ../documentation/Changes.threads
cp -f ../linuxthreads/README ../documentation/README.threads
cp -f ../crypt/README.ufc-crypt ../documentation/

cp -f ../ChangeLog* ../documentation

rm -f $RPM_BUILD_ROOT%{_libdir}/libnss_*.so

# strip ld.so with --strip-debug only (other ELFs are stripped by rpm):
%ifnarch sparc64
%{!?debug:strip -g -R .comment -R .note $RPM_BUILD_ROOT/%{_lib}/ld-%{version}.so}
%endif

# Collect locale files and mark them with %%lang()
rm -f ../glibc.lang
echo '%defattr(644,root,root,755)' > ../glibc.lang
for i in $RPM_BUILD_ROOT%{_datadir}/locale/* $RPM_BUILD_ROOT%{_libdir}/locale/* ; do
	if [ -d $i ]; then
		lang=`echo $i | sed -e 's/.*locale\///' -e 's/\/.*//'`
		twochar=1
		# list of long %%lang values we do support
		for j in de_AT de_BE de_CH de_LU es_AR es_MX ja_JP.SJIS ko_KR.utf8 pt_BR \
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
		echo "%lang($lang) $dir" >> ../glibc.lang
	fi
done
# XXX: to be added when become supported by glibc
# am,bn,ml (present in sources, but incomplete and disabled) (used by GNOME)
# ia,kn,li,mn,sr@Latn (used by GNOME)
#	note: GNOME2 uses sr as cyrillic!
# nso,ss,ven,xh,zu (used by KDE)
for i in af ar az be bg br bs cy de_AT el en en_AU eo es_AR es_MX et eu fa fi \
	 ga gr he hi hr hu id is ja_JP.SJIS ka lg lt lv mk ms mt nn pt ro ru \
	 se sl sq sr sr@cyrillic ta tg th uk uz vi wa yi zh_CN ; do
	if [ ! -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES ]; then
		install -d $RPM_BUILD_ROOT%{_datadir}/locale/$i/LC_MESSAGES
		lang=`echo $i | sed -e 's/_.*//'`
		echo "%lang($lang) %{_datadir}/locale/$i" >> ../glibc.lang
	fi
done
install %{SOURCE7} $RPM_BUILD_ROOT%{_mandir}/man8

# localedb-gen infrastructure
install %{SOURCE8} $RPM_BUILD_ROOT%{_bindir}/localedb-gen
install ../localedata/SUPPORTED $RPM_BUILD_ROOT%{_datadir}/i18n

# shutup check-files
rm -f $RPM_BUILD_ROOT%{_mandir}/README.*
rm -f $RPM_BUILD_ROOT%{_mandir}/diff.*
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# we don't support kernel without ptys support
rm -f $RPM_BUILD_ROOT%{_libdir}/pt_chown


%clean
rm -rf $RPM_BUILD_ROOT

# don't run iconvconfig in %%postun -n iconv because iconvconfig doesn't exist
# when %%postun is run

%ifnarch sparc64
%ifarch amd64
%post	-n %{name}64 -p /%{_lib}/postshell
%else
%post	-p /%{_lib}/postshell
%endif
/%{_lib}/ldconfig
-/sbin/telinit u

%ifarch amd64
%postun	-n %{name}64 -p /%{_lib}/postshell
%else
%postun	-p /%{_lib}/postshell
%endif
/%{_lib}/ldconfig
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
touch /var/log/nscd
chmod 000 /var/log/nscd
chown root:root /var/log/nscd
chmod 640 /var/log/nscd
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
%endif

%ifnarch sparc64
%ifarch amd64
%files -n glibc64
%else
%files 
%endif
%defattr(644,root,root,755)
%doc README NEWS FAQ BUGS
# ld* and libc.so.6 SONAME symlinks must be in package because of
# chicken-egg problem (postshell is dynamically linked with libc);
# ld-*.so SONAME is ld.so.1 on ppc, ld-linux.so.2 on other archs
%attr(755,root,root) /%{_lib}/postshell
%attr(755,root,root) /%{_lib}/ld*
%attr(755,root,root) /%{_lib}/libanl*
%attr(755,root,root) /%{_lib}/libdl*
%attr(755,root,root) /%{_lib}/libnsl*
%attr(755,root,root) /%{_lib}/lib[BScmprtu]*
%dir %{_libdir}/locale

#%files -n nss_dns
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_dns*.so*

#%files -n nss_files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_files*.so*


%files misc -f %{name}.lang
%defattr(644,root,root,755)

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
%ifnarch alpha ppc sparc64 amd64
%attr(755,root,root) %{_bindir}/lddlibc4
%endif
%attr(755,root,root) %{_bindir}/locale
%attr(755,root,root) %{_bindir}/rpcgen
%attr(755,root,root) %{_bindir}/tzselect

%attr(755,root,root) %{_sbindir}/rpcinfo
%attr(755,root,root) %{_sbindir}/zdump
%attr(755,root,root) %{_sbindir}/zic

%dir %{_datadir}/locale
%{_datadir}/locale/locale.alias
%{_datadir}/zoneinfo
%exclude %{_datadir}/zoneinfo/right


%{_mandir}/man1/[!lsg]*
%{_mandir}/man1/getent.1*
%{_mandir}/man1/locale.1*
%{_mandir}/man1/ldd.1*
%{_mandir}/man5/???[!d]*
%{_mandir}/man7/*
%{_mandir}/man8/[!n]*
%lang(cs) %{_mandir}/cs/man[578]/*
%lang(de) %{_mandir}/de/man[578]/*
%lang(es) %{_mandir}/es/man[578]/*
%lang(fi) %{_mandir}/fi/man1/ldd.1*
%lang(fr) %{_mandir}/fr/man1/ldd.1*
%lang(fr) %{_mandir}/fr/man[578]/*
%lang(hu) %{_mandir}/hu/man1/ldd.1*
%lang(hu) %{_mandir}/hu/man[578]/*
%lang(it) %{_mandir}/it/man[578]/*
%lang(ja) %{_mandir}/ja/man1/[!lsg]*
%lang(ja) %{_mandir}/ja/man1/ldd.1*
%lang(ja) %{_mandir}/ja/man5/???[!d]*
%lang(ja) %{_mandir}/ja/man7/*
%lang(ja) %{_mandir}/ja/man8/[!n]*
%lang(ko) %{_mandir}/ko/man[578]/*
# %lang(nl) %{_mandir}/nl/man[578]/*
%lang(pl) %{_mandir}/pl/man1/ldd.1*
%lang(pl) %{_mandir}/pl/man[578]/*
%lang(pt) %{_mandir}/pt/man5/???[!d]*
%lang(pt) %{_mandir}/pt/man7/*
%lang(pt) %{_mandir}/pt/man8/[!n]*
%lang(pt_BR) %{_mandir}/pt_BR/man5/???[!d]*
%lang(pt_BR) %{_mandir}/pt_BR/man7/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/[!n]*
%lang(ru) %{_mandir}/ru/man[578]/*

%files zoneinfo_right
%defattr(644,root,root,755)
%{_datadir}/zoneinfo/right

%files -n nss_compat
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_compat*.so*

%files -n nss_hesiod
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_hesiod*.so*

%files -n nss_nis
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_nis.so.*
%attr(755,root,root) /%{_lib}/libnss_nis-*.so

%files -n nss_nisplus
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/libnss_nisplus*.so*

%if %{with memusage}
%files memusage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/memusage*
%attr(755,root,root) %{_libdir}/libmemusage.so
%endif

%files devel
%defattr(644,root,root,755)
%doc documentation/* NOTES PROJECTS
%attr(755,root,root) %{_bindir}/gencat
%attr(755,root,root) %{_bindir}/getconf
%attr(755,root,root) %{_bindir}/*prof*
%attr(755,root,root) %{_bindir}/*trace

%{_includedir}/*.h
%ifarch alpha
%{_includedir}/alpha
%endif
%{_includedir}/arpa
%{_includedir}/bits
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

%{_infodir}/libc.info*

%attr(755,root,root) %{_libdir}/lib[!m]*.so
%attr(755,root,root) %{_libdir}/libm.so
%attr(755,root,root) %{_libdir}/*crt*.o
%{_libdir}/libbsd-compat.a
%{_libdir}/libbsd.a
%{_libdir}/libc_nonshared.a
%{_libdir}/libg.a
%{_libdir}/libieee.a
%{_libdir}/libpthread_nonshared.a
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
%attr(755,root,root) %{_bindir}/localedb-gen
%{_datadir}/i18n
%{_mandir}/man1/localedef*

%files localedb-all
%defattr(644,root,root,755)
%{_libdir}/locale/locale-archive

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

%else

%files -n glibc64
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ld-*
%attr(755,root,root) %{_libdir}/libanl*
%attr(755,root,root) %{_libdir}/libdl*
%attr(755,root,root) %{_libdir}/libnsl*
%attr(755,root,root) %{_libdir}/lib[BScmprtu]*
%attr(755,root,root) %{_libdir}/libnss_dns*.so*
%attr(755,root,root) %{_libdir}/libnss_files*.so*

%files -n glibc64-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib[!m]*.so
%attr(755,root,root) %{_libdir}/libm.so
%attr(755,root,root) %{_libdir}/*crt*.o
%{_libdir}/libbsd-compat.a
%{_libdir}/libbsd.a
%{_libdir}/libc_nonshared.a
%{_libdir}/libg.a
%{_libdir}/libieee.a
%{_libdir}/libpthread_nonshared.a
%{_libdir}/librpcsvc.a

%files -n glibc64-static
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
%endif
