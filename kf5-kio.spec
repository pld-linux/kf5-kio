# TODO: SwitcherooControl?
#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeframever	5.116
%define		kf_ver		%{version}
%define		qt_ver		5.15.2
%define		kfname		kio

Summary:	Network transparent access to files and data
Summary(pl.UTF-8):	Przezroczysty sieciowo dostęp do plików i danych
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	684597aefb1b7d17f4297edf931a3b49
Patch0:		kio_help-fallback-to-kde4-docs.patch
URL:		https://kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	acl-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	heimdal-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf5-karchive-devel >= %{kf_ver}
BuildRequires:	kf5-kauth-devel >= %{kf_ver}
BuildRequires:	kf5-kbookmarks-devel >= %{kf_ver}
BuildRequires:	kf5-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-kdbusaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kded-devel >= %{kf_ver}
BuildRequires:	kf5-kdoctools-devel >= %{kf_ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel >= %{kf_ver}
BuildRequires:	kf5-kiconthemes-devel >= %{kf_ver}
BuildRequires:	kf5-kitemviews-devel >= %{kf_ver}
BuildRequires:	kf5-kjobwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-knotifications-devel >= %{kf_ver}
BuildRequires:	kf5-kservice-devel >= %{kf_ver}
BuildRequires:	kf5-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf5-kwallet-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	kf5-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf5-solid-devel >= %{kf_ver}
BuildRequires:	libblkid-devel
BuildRequires:	libmount-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
# to allow parallel install with ka6-kio-extras
Requires:	%{name}-apps >= %{version}-%{release}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5DBus >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5Qml >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
Requires:	kf5-dirs
Requires:	kf5-karchive >= %{kf_ver}
Requires:	kf5-kauth >= %{kf_ver}
Requires:	kf5-kbookmarks >= %{kf_ver}
Requires:	kf5-kcompletion >= %{kf_ver}
Requires:	kf5-kconfig >= %{kf_ver}
Requires:	kf5-kconfigwidgets >= %{kf_ver}
Requires:	kf5-kcoreaddons >= %{kf_ver}
Requires:	kf5-kcrash >= %{kf_ver}
Requires:	kf5-kdbusaddons >= %{kf_ver}
Requires:	kf5-kdoctools >= %{kf_ver}
Requires:	kf5-kguiaddons >= %{kf_ver}
Requires:	kf5-ki18n >= %{kf_ver}
Requires:	kf5-kiconthemes >= %{kf_ver}
Requires:	kf5-kitemviews >= %{kf_ver}
Requires:	kf5-kjobwidgets >= %{kf_ver}
Requires:	kf5-knotifications >= %{kf_ver}
Requires:	kf5-kservice >= %{kf_ver}
Requires:	kf5-ktextwidgets >= %{kf_ver}
Requires:	kf5-kwallet >= %{kf_ver}
Requires:	kf5-kwidgetsaddons >= %{kf_ver}
Requires:	kf5-kwindowsystem >= %{kf_ver}
Requires:	kf5-kxmlgui >= %{kf_ver}
Requires:	kf5-solid >= %{kf_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This framework implements almost all the file management functions you
will ever need. In fact, the KDE file manager (Dolphin) and the KDE
file dialog also uses this to provide its network-enabled file
management.

It supports accessing files locally as well as via HTTP and FTP out of
the box and can be extended by plugins to support other protocols as
well. There is a variety of plugins available, e.g. to support access
via SSH.

The framework can also be used to bridge a native protocol to a
file-based interface. This makes the data accessible in all
applications using the KDE file dialog or any other KIO enabled
infrastructure.

%description -l pl.UTF-8
Ten szkielet implementuje prawie wszystkie funkcje zarządzania
plikami, jakie mogą być kiedykolwiek potrzebne. W rzeczywistości
zarządca plików KDE (Dolphin) oraz okno dialogowe KDE także go
wykorzystują w celu zapewnienia zarządzania plikami obsługującego
sieć.

Szkielet obsługuje dostęp do plików lokalnie, jak i przez HTTP i FTP;
może być rozszerzany przez wtyczki, aby obsłużyć także inne protokoły.
Dostępne są różne wtyczki, np. do obsługi dostępu przez SSH.

Szkielet może być używany także aby połączyć protokół natywny z
interfejsem opartym na plikach. Pozwala to na dostęp do danych we
wszystkich aplikacjach wykorzystujących okno dialogowe KDE albo
dowolną inną infrastrukturę obsługującą KIO.

%package apps
Summary:	KIO provided applications
Summary(pl.UTF-8):	Aplikacje dostarczane wraz z KIO
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Conflicts:	ka6-kio-extras
BuildArch:	noarch

%description apps
KIO provided applications.

%description apps -l pl.UTF-8
Aplikacje dostarczane wraz z KIO.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Concurrent-devel >= %{qt_ver}
Requires:	Qt5DBus-devel >= %{qt_ver}
Requires:	Qt5Gui-devel >= %{qt_ver}
Requires:	Qt5Network-devel >= %{qt_ver}
Requires:	cmake >= 3.16
Requires:	kf5-kbookmarks-devel >= %{kf_ver}
Requires:	kf5-kcompletion-devel >= %{kf_ver}
Requires:	kf5-kconfig-devel >= %{kf_ver}
Requires:	kf5-kcoreaddons-devel >= %{kf_ver}
Requires:	kf5-kitemviews-devel >= %{kf_ver}
Requires:	kf5-kjobwidgets-devel >= %{kf_ver}
Requires:	kf5-kservice-devel >= %{kf_ver}
Requires:	kf5-kwindowsystem-devel >= %{kf_ver}
Requires:	kf5-kxmlgui-devel >= %{kf_ver}
Requires:	kf5-solid-devel >= %{kf_ver}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}
%patch -P0 -p1

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{qt5dir}/plugins/kf5/{kfileitemaction,kio_dnd}
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr@latin

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,tok}

%find_lang %{kfname}5 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/accept-languages.codes
/etc/xdg/kshorturifilterrc
%{_datadir}/qlogging-categories5/kio.categories
%attr(755,root,root) %{_bindir}/kcookiejar5
%attr(755,root,root) %{_bindir}/ktelnetservice5
%attr(755,root,root) %{_bindir}/ktrash5
%attr(755,root,root) %{_bindir}/protocoltojson
%attr(755,root,root) %{_libexecdir}/kf5/kio_http_cache_cleaner
%attr(755,root,root) %{_libexecdir}/kf5/kiod5
%attr(755,root,root) %{_libexecdir}/kf5/kioexec
%attr(755,root,root) %{_libexecdir}/kf5/kioslave5
%attr(755,root,root) %{_libexecdir}/kf5/kpac_dhcp_helper
%attr(755,root,root) %{_libdir}/libKF5KIOCore.so.*.*
%ghost %{_libdir}/libKF5KIOCore.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOFileWidgets.so.*.*
%ghost %{_libdir}/libKF5KIOFileWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIONTLM.so.*.*
%ghost %{_libdir}/libKF5KIONTLM.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOWidgets.so.*.*
%ghost %{_libdir}/libKF5KIOWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOGui.so.*.*
%ghost %{_libdir}/libKF5KIOGui.so.5
%attr(755,root,root) %{qt5dir}/plugins/kcm_proxy.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_trash.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_webshortcuts.so
%attr(755,root,root) %{qt5dir}/plugins/designer/kio5widgets.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/kcookiejar.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/proxyscout.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/remotenotifier.so
%dir %{qt5dir}/plugins/kf5/kio
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_file.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_ftp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_ghelp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_help.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_http.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_remote.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_trash.so
%dir %{qt5dir}/plugins/kf5/kiod
%attr(755,root,root) %{qt5dir}/plugins/kf5/kiod/kioexecd.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kiod/kssld.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kiod/kpasswdserver.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/fixhosturifilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kshorturifilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kuriikwsfilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kurisearchfilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/localdomainurifilter.so
%dir %{qt5dir}/plugins/kf5/kfileitemaction
%dir %{qt5dir}/plugins/kf5/kio_dnd
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_smb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cookies.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KCookieServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KDirNotify.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KPasswdServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KSlaveLauncher.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kio.FileUndoManager.xml
%{_datadir}/dbus-1/services/org.kde.kiod5.service
%{_datadir}/dbus-1/services/org.kde.kioexecd.service
%{_datadir}/dbus-1/services/org.kde.kcookiejar5.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver.service
%{_datadir}/dbus-1/services/org.kde.kssld5.service
%{_datadir}/kconf_update/filepicker.upd
%{_datadir}/kf5/kcookiejar/domain_info
%{_datadir}/knotifications5/proxyscout.notifyrc
%{_datadir}/kservices5/cookies.desktop
%{_datadir}/kservices5/http_cache_cleaner.desktop
%{_datadir}/kservices5/kcmtrash.desktop
%{_datadir}/kservices5/netpref.desktop
%{_datadir}/kservices5/proxy.desktop
%{_datadir}/kservices5/searchproviders/7digital.desktop
%{_datadir}/kservices5/searchproviders/acronym.desktop
%{_datadir}/kservices5/searchproviders/amazon.desktop
%{_datadir}/kservices5/searchproviders/amazon_mp3.desktop
%{_datadir}/kservices5/searchproviders/amg.desktop
%{_datadir}/kservices5/searchproviders/archpkg.desktop
%{_datadir}/kservices5/searchproviders/archwiki.desktop
%{_datadir}/kservices5/searchproviders/backports.desktop
%{_datadir}/kservices5/searchproviders/baidu.desktop
%{_datadir}/kservices5/searchproviders/beolingus.desktop
%{_datadir}/kservices5/searchproviders/bing.desktop
%{_datadir}/kservices5/searchproviders/bug.desktop
%{_datadir}/kservices5/searchproviders/call.desktop
%{_datadir}/kservices5/searchproviders/cia.desktop
%{_datadir}/kservices5/searchproviders/citeseer.desktop
%{_datadir}/kservices5/searchproviders/cpan.desktop
%{_datadir}/kservices5/searchproviders/cplusplus.desktop
%{_datadir}/kservices5/searchproviders/cppreference.desktop
%{_datadir}/kservices5/searchproviders/ctan.desktop
%{_datadir}/kservices5/searchproviders/ctan_cat.desktop
%{_datadir}/kservices5/searchproviders/dbug.desktop
%{_datadir}/kservices5/searchproviders/de2en.desktop
%{_datadir}/kservices5/searchproviders/de2fr.desktop
%{_datadir}/kservices5/searchproviders/deb.desktop
%{_datadir}/kservices5/searchproviders/deepl.desktop
%{_datadir}/kservices5/searchproviders/dictfr.desktop
%{_datadir}/kservices5/searchproviders/docbook.desktop
%{_datadir}/kservices5/searchproviders/doi.desktop
%{_datadir}/kservices5/searchproviders/duckduckgo.desktop
%{_datadir}/kservices5/searchproviders/duckduckgo_info.desktop
%{_datadir}/kservices5/searchproviders/duckduckgo_shopping.desktop
%{_datadir}/kservices5/searchproviders/ecosia.desktop
%{_datadir}/kservices5/searchproviders/en2de.desktop
%{_datadir}/kservices5/searchproviders/en2es.desktop
%{_datadir}/kservices5/searchproviders/en2fr.desktop
%{_datadir}/kservices5/searchproviders/en2it.desktop
%{_datadir}/kservices5/searchproviders/es2en.desktop
%{_datadir}/kservices5/searchproviders/facebook.desktop
%{_datadir}/kservices5/searchproviders/feedster.desktop
%{_datadir}/kservices5/searchproviders/flatpak.desktop
%{_datadir}/kservices5/searchproviders/flickr.desktop
%{_datadir}/kservices5/searchproviders/flickrcc.desktop
%{_datadir}/kservices5/searchproviders/foldoc.desktop
%{_datadir}/kservices5/searchproviders/fr2de.desktop
%{_datadir}/kservices5/searchproviders/fr2en.desktop
%{_datadir}/kservices5/searchproviders/freecode.desktop
%{_datadir}/kservices5/searchproviders/freedb.desktop
%{_datadir}/kservices5/searchproviders/fsd.desktop
%{_datadir}/kservices5/searchproviders/github.desktop
%{_datadir}/kservices5/searchproviders/gitlab.desktop
%{_datadir}/kservices5/searchproviders/google.desktop
%{_datadir}/kservices5/searchproviders/google_advanced.desktop
%{_datadir}/kservices5/searchproviders/google_code.desktop
%{_datadir}/kservices5/searchproviders/google_groups.desktop
%{_datadir}/kservices5/searchproviders/google_images.desktop
%{_datadir}/kservices5/searchproviders/google_lucky.desktop
%{_datadir}/kservices5/searchproviders/google_maps.desktop
%{_datadir}/kservices5/searchproviders/google_movie.desktop
%{_datadir}/kservices5/searchproviders/google_news.desktop
%{_datadir}/kservices5/searchproviders/google_shopping.desktop
%{_datadir}/kservices5/searchproviders/grec.desktop
%{_datadir}/kservices5/searchproviders/hyperdictionary.desktop
%{_datadir}/kservices5/searchproviders/hyperdictionary_thesaurus.desktop
%{_datadir}/kservices5/searchproviders/identica_groups.desktop
%{_datadir}/kservices5/searchproviders/identica_notices.desktop
%{_datadir}/kservices5/searchproviders/identica_people.desktop
%{_datadir}/kservices5/searchproviders/imdb.desktop
%{_datadir}/kservices5/searchproviders/invent.desktop
%{_datadir}/kservices5/searchproviders/invent_issues.desktop
%{_datadir}/kservices5/searchproviders/invent_mr.desktop
%{_datadir}/kservices5/searchproviders/invent_repo.desktop
%{_datadir}/kservices5/searchproviders/it2en.desktop
%{_datadir}/kservices5/searchproviders/jamendo.desktop
%{_datadir}/kservices5/searchproviders/jeeves.desktop
%{_datadir}/kservices5/searchproviders/kde.desktop
%{_datadir}/kservices5/searchproviders/kde_apps.desktop
%{_datadir}/kservices5/searchproviders/kde_forums.desktop
%{_datadir}/kservices5/searchproviders/kde_store.desktop
%{_datadir}/kservices5/searchproviders/kde_techbase.desktop
%{_datadir}/kservices5/searchproviders/kde_userbase.desktop
%{_datadir}/kservices5/searchproviders/kreddit.desktop
%{_datadir}/kservices5/searchproviders/krita.desktop
%{_datadir}/kservices5/searchproviders/learncpp.desktop
%{_datadir}/kservices5/searchproviders/leo.desktop
%{_datadir}/kservices5/searchproviders/linguee.desktop
%{_datadir}/kservices5/searchproviders/magnatune.desktop
%{_datadir}/kservices5/searchproviders/metacrawler.desktop
%{_datadir}/kservices5/searchproviders/microsoft_cpp.desktop
%{_datadir}/kservices5/searchproviders/msdn.desktop
%{_datadir}/kservices5/searchproviders/multitran-deru.desktop
%{_datadir}/kservices5/searchproviders/multitran-enru.desktop
%{_datadir}/kservices5/searchproviders/multitran-esru.desktop
%{_datadir}/kservices5/searchproviders/multitran-frru.desktop
%{_datadir}/kservices5/searchproviders/multitran-itru.desktop
%{_datadir}/kservices5/searchproviders/multitran-nlru.desktop
%{_datadir}/kservices5/searchproviders/netcraft.desktop
%{_datadir}/kservices5/searchproviders/nl-telephone.desktop
%{_datadir}/kservices5/searchproviders/nl-teletekst.desktop
%{_datadir}/kservices5/searchproviders/opendesktop.desktop
%{_datadir}/kservices5/searchproviders/opensuse.desktop
%{_datadir}/kservices5/searchproviders/pgpkeys.desktop
%{_datadir}/kservices5/searchproviders/php.desktop
%{_datadir}/kservices5/searchproviders/protondb.desktop
%{_datadir}/kservices5/searchproviders/python.desktop
%{_datadir}/kservices5/searchproviders/qt5.desktop
%{_datadir}/kservices5/searchproviders/qt6.desktop
%{_datadir}/kservices5/searchproviders/qwant.desktop
%{_datadir}/kservices5/searchproviders/qwant_images.desktop
%{_datadir}/kservices5/searchproviders/qwant_news.desktop
%{_datadir}/kservices5/searchproviders/qwant_shopping.desktop
%{_datadir}/kservices5/searchproviders/qwant_social.desktop
%{_datadir}/kservices5/searchproviders/qwant_videos.desktop
%{_datadir}/kservices5/searchproviders/rae.desktop
%{_datadir}/kservices5/searchproviders/rag.desktop
%{_datadir}/kservices5/searchproviders/reddit.desktop
%{_datadir}/kservices5/searchproviders/rfc.desktop
%{_datadir}/kservices5/searchproviders/rpmfind.desktop
%{_datadir}/kservices5/searchproviders/ruby_application_archive.desktop
%{_datadir}/kservices5/searchproviders/rust.desktop
%{_datadir}/kservices5/searchproviders/soundcloud.desktop
%{_datadir}/kservices5/searchproviders/sourceforge.desktop
%{_datadir}/kservices5/searchproviders/technorati.desktop
%{_datadir}/kservices5/searchproviders/technoratitags.desktop
%{_datadir}/kservices5/searchproviders/thesaurus.desktop
%{_datadir}/kservices5/searchproviders/tvtome.desktop
%{_datadir}/kservices5/searchproviders/ubuntu.desktop
%{_datadir}/kservices5/searchproviders/urbandictionary.desktop
%{_datadir}/kservices5/searchproviders/uspto.desktop
%{_datadir}/kservices5/searchproviders/vimeo.desktop
%{_datadir}/kservices5/searchproviders/voila.desktop
%{_datadir}/kservices5/searchproviders/webster.desktop
%{_datadir}/kservices5/searchproviders/wikia.desktop
%{_datadir}/kservices5/searchproviders/wikipedia.desktop
%{_datadir}/kservices5/searchproviders/wiktionary.desktop
%{_datadir}/kservices5/searchproviders/wine.desktop
%{_datadir}/kservices5/searchproviders/wolfram_alpha.desktop
%{_datadir}/kservices5/searchproviders/wordref.desktop
%{_datadir}/kservices5/searchproviders/yahoo.desktop
%{_datadir}/kservices5/searchproviders/yahoo_image.desktop
%{_datadir}/kservices5/searchproviders/yahoo_local.desktop
%{_datadir}/kservices5/searchproviders/yahoo_shopping.desktop
%{_datadir}/kservices5/searchproviders/yahoo_video.desktop
%{_datadir}/kservices5/searchproviders/yandex.desktop
%{_datadir}/kservices5/searchproviders/youtube.desktop
%{_datadir}/kservices5/smb.desktop
%{_datadir}/kservices5/webshortcuts.desktop
%{_datadir}/kservicetypes5/kfileitemactionplugin.desktop
%{_datadir}/kservicetypes5/konqpopupmenuplugin.desktop
%{_datadir}/kservicetypes5/kpropertiesdialogplugin.desktop
%{_datadir}/kservicetypes5/searchprovider.desktop
%{_datadir}/qlogging-categories5/kio.renamecategories
%{_desktopdir}/ktelnetservice5.desktop
%{_mandir}/man8/kcookiejar5.8*
%lang(ca) %{_mandir}/ca/man8/kcookiejar5.8*
%lang(de) %{_mandir}/de/man8/kcookiejar5.8*
%lang(es) %{_mandir}/es/man8/kcookiejar5.8*
%lang(fr) %{_mandir}/fr/man8/kcookiejar5.8*
%lang(it) %{_mandir}/it/man8/kcookiejar5.8*
%lang(nl) %{_mandir}/nl/man8/kcookiejar5.8*
%lang(pt) %{_mandir}/pt/man8/kcookiejar5.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/kcookiejar5.8*
%lang(sv) %{_mandir}/sv/man8/kcookiejar5.8*
%lang(uk) %{_mandir}/uk/man8/kcookiejar5.8*

%files apps
%defattr(644,root,root,755)
%{_desktopdir}/kcm_trash.desktop

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKF5KIOCore.so
%{_libdir}/libKF5KIOFileWidgets.so
%{_libdir}/libKF5KIOGui.so
%{_libdir}/libKF5KIONTLM.so
%{_libdir}/libKF5KIOWidgets.so
%{_includedir}/KF5/KIO
%{_includedir}/KF5/KIOCore
%{_includedir}/KF5/KIOFileWidgets
%{_includedir}/KF5/KIOWidgets
%{_includedir}/KF5/KIOGui
%dir %{_includedir}/KF5/kio
%{_includedir}/KF5/kio/kntlm.h
%{_includedir}/KF5/kio/kntlm_export.h
%{_libdir}/cmake/KF5KIO
%{qt5dir}/mkspecs/modules/qt_KIOCore.pri
%{qt5dir}/mkspecs/modules/qt_KIOFileWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KIOGui.pri
%{qt5dir}/mkspecs/modules/qt_KIOWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KNTLM.pri
%{_datadir}/kdevappwizard/templates/kioworker.tar.bz2
