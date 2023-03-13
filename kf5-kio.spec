#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.104
%define		qtver		5.15.2
%define		kfname		kio

Summary:	Network transparent access to files and data
Name:		kf5-%{kfname}
Version:	5.104.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	bafdfade24ea7fa78e8ac3e617e87530
Patch0:		kio_help-fallback-to-kde4-docs.patch
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Qml-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5X11Extras-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	acl-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	heimdal-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kcrash-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kded-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwallet-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	libblkid-devel
BuildRequires:	libmount-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	Qt5Core >= %{qtver}
Requires:	Qt5DBus >= %{qtver}
Requires:	Qt5Gui >= %{qtver}
Requires:	Qt5Network >= %{qtver}
Requires:	Qt5Qml >= %{qtver}
Requires:	Qt5Widgets >= %{qtver}
Requires:	Qt5X11Extras >= %{qtver}
Requires:	Qt5Xml >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-karchive >= %{version}
Requires:	kf5-kauth >= %{version}
Requires:	kf5-kbookmarks >= %{version}
Requires:	kf5-kcompletion >= %{version}
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kconfigwidgets >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-kcrash >= %{version}
Requires:	kf5-kdbusaddons >= %{version}
Requires:	kf5-kdoctools >= %{version}
Requires:	kf5-ki18n >= %{version}
Requires:	kf5-kiconthemes >= %{version}
Requires:	kf5-kitemviews >= %{version}
Requires:	kf5-kjobwidgets >= %{version}
Requires:	kf5-knotifications >= %{version}
Requires:	kf5-kservice >= %{version}
Requires:	kf5-ktextwidgets >= %{version}
Requires:	kf5-kwallet >= %{version}
Requires:	kf5-kwidgetsaddons >= %{version}
Requires:	kf5-kwindowsystem >= %{version}
Requires:	kf5-kxmlgui >= %{version}
Requires:	kf5-solid >= %{version}
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

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Concurrent-devel >= %{qtver}
Requires:	Qt5DBus-devel >= %{qtver}
Requires:	Qt5Network-devel >= %{qtver}
Requires:	cmake >= 3.16
Requires:	kf5-kbookmarks-devel >= %{version}
Requires:	kf5-kcompletion-devel >= %{version}
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-kcoreaddons-devel >= %{version}
Requires:	kf5-kitemviews-devel >= %{version}
Requires:	kf5-kjobwidgets-devel >= %{version}
Requires:	kf5-kservice-devel >= %{version}
Requires:	kf5-kwindowsystem-devel >= %{version}
Requires:	kf5-kxmlgui-devel >= %{version}
Requires:	kf5-solid-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}
%patch0 -p1

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
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
%ghost %{_libdir}/libKF5KIOCore.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOCore.so.*.*
%ghost %{_libdir}/libKF5KIOFileWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOFileWidgets.so.*.*
%ghost %{_libdir}/libKF5KIONTLM.so.5
%attr(755,root,root) %{_libdir}/libKF5KIONTLM.so.*.*
%ghost %{_libdir}/libKF5KIOWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOWidgets.so.*.*
%ghost %{_libdir}/libKF5KIOGui.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOGui.so.*.*
%attr(755,root,root) %{qt5dir}/plugins/kcm_trash.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_webshortcuts.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/kcookiejar.so
%attr(755,root,root) %{qt5dir}/plugins/designer/kio5widgets.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/proxyscout.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/remotenotifier.so
%dir %{qt5dir}/plugins/kf5/kio
%dir %{qt5dir}/plugins/kf5/kiod
%attr(755,root,root) %{qt5dir}/plugins/kcm_proxy.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_file.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_ftp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_ghelp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_help.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_http.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_remote.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/kio_trash.so
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
%lang(ca) %{_mandir}/ca/man8/kcookiejar5.8*
%lang(de) %{_mandir}/de/man8/kcookiejar5.8*
%lang(es) %{_mandir}/es/man8/kcookiejar5.8*
%lang(it) %{_mandir}/it/man8/kcookiejar5.8*
%lang(nl) %{_mandir}/nl/man8/kcookiejar5.8*
%lang(pt) %{_mandir}/pt/man8/kcookiejar5.8*
%lang(pt_BR) %{_mandir}/pt_BR/man8/kcookiejar5.8*
%lang(sv) %{_mandir}/sv/man8/kcookiejar5.8*
%lang(uk) %{_mandir}/uk/man8/kcookiejar5.8*
%{_desktopdir}/ktelnetservice5.desktop
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
%{_datadir}/kservices5/searchproviders/backports.desktop
%{_datadir}/kservices5/searchproviders/baidu.desktop
%{_datadir}/kservices5/searchproviders/beolingus.desktop
%{_datadir}/kservices5/searchproviders/bing.desktop
%{_datadir}/kservices5/searchproviders/call.desktop
%{_datadir}/kservices5/searchproviders/cia.desktop
%{_datadir}/kservices5/searchproviders/citeseer.desktop
%{_datadir}/kservices5/searchproviders/cpan.desktop
%{_datadir}/kservices5/searchproviders/ctan.desktop
%{_datadir}/kservices5/searchproviders/ctan_cat.desktop
%{_datadir}/kservices5/searchproviders/dbug.desktop
%{_datadir}/kservices5/searchproviders/de2en.desktop
%{_datadir}/kservices5/searchproviders/de2fr.desktop
%{_datadir}/kservices5/searchproviders/deb.desktop
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
%{_datadir}/kservices5/searchproviders/it2en.desktop
%{_datadir}/kservices5/searchproviders/jamendo.desktop
%{_datadir}/kservices5/searchproviders/jeeves.desktop
%{_datadir}/kservices5/searchproviders/kde.desktop
%{_datadir}/kservices5/searchproviders/kde_apps.desktop
%{_datadir}/kservices5/searchproviders/kde_forums.desktop
%{_datadir}/kservices5/searchproviders/kde_techbase.desktop
%{_datadir}/kservices5/searchproviders/kde_userbase.desktop
%{_datadir}/kservices5/searchproviders/leo.desktop
%{_datadir}/kservices5/searchproviders/magnatune.desktop
%{_datadir}/kservices5/searchproviders/metacrawler.desktop
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
%{_datadir}/kservices5/searchproviders/pgpkeys.desktop
%{_datadir}/kservices5/searchproviders/php.desktop
%{_datadir}/kservices5/searchproviders/python.desktop
%{_datadir}/kservices5/searchproviders/qwant.desktop
%{_datadir}/kservices5/searchproviders/qwant_images.desktop
%{_datadir}/kservices5/searchproviders/qwant_news.desktop
%{_datadir}/kservices5/searchproviders/qwant_shopping.desktop
%{_datadir}/kservices5/searchproviders/qwant_social.desktop
%{_datadir}/kservices5/searchproviders/qwant_videos.desktop
%{_datadir}/kservices5/searchproviders/rae.desktop
%{_datadir}/kservices5/searchproviders/rag.desktop
%{_datadir}/kservices5/searchproviders/rfc.desktop
%{_datadir}/kservices5/searchproviders/rpmfind.desktop
%{_datadir}/kservices5/searchproviders/ruby_application_archive.desktop
%{_datadir}/kservices5/searchproviders/soundcloud.desktop
%{_datadir}/kservices5/searchproviders/sourceforge.desktop
%{_datadir}/kservices5/searchproviders/technorati.desktop
%{_datadir}/kservices5/searchproviders/technoratitags.desktop
%{_datadir}/kservices5/searchproviders/thesaurus.desktop
%{_datadir}/kservices5/searchproviders/tvtome.desktop
%{_datadir}/kservices5/searchproviders/urbandictionary.desktop
%{_datadir}/kservices5/searchproviders/uspto.desktop
%{_datadir}/kservices5/searchproviders/vimeo.desktop
%{_datadir}/kservices5/searchproviders/voila.desktop
%{_datadir}/kservices5/searchproviders/webster.desktop
%{_datadir}/kservices5/searchproviders/wikia.desktop
%{_datadir}/kservices5/searchproviders/wikipedia.desktop
%{_datadir}/kservices5/searchproviders/wiktionary.desktop
%{_datadir}/kservices5/searchproviders/wolfram_alpha.desktop
%{_datadir}/kservices5/searchproviders/wordref.desktop
%{_datadir}/kservices5/searchproviders/yahoo.desktop
%{_datadir}/kservices5/searchproviders/yahoo_image.desktop
%{_datadir}/kservices5/searchproviders/yahoo_local.desktop
%{_datadir}/kservices5/searchproviders/yahoo_shopping.desktop
%{_datadir}/kservices5/searchproviders/yahoo_video.desktop
%{_datadir}/kservices5/searchproviders/youtube.desktop
%{_datadir}/kservices5/smb.desktop
%{_datadir}/kservices5/webshortcuts.desktop
%{_datadir}/kservicetypes5/kfileitemactionplugin.desktop
%{_datadir}/kservicetypes5/konqpopupmenuplugin.desktop
%{_datadir}/kservicetypes5/kpropertiesdialogplugin.desktop
%{_datadir}/kservicetypes5/searchprovider.desktop
%{_mandir}/man8/kcookiejar5.8*
%{_datadir}/kservices5/searchproviders/archwiki.desktop
%{_datadir}/kservices5/searchproviders/bug.desktop
%{_datadir}/kservices5/searchproviders/deepl.desktop
%{_mandir}/fr/man8/kcookiejar5.8*
%{_datadir}/qlogging-categories5/kio.renamecategories
%{_datadir}/kservices5/searchproviders/invent.desktop
%{_datadir}/kservices5/searchproviders/invent_repo.desktop
%{_desktopdir}/kcm_trash.desktop
%{_datadir}/kservices5/searchproviders/cplusplus.desktop
%{_datadir}/kservices5/searchproviders/cppreference.desktop
%{_datadir}/kservices5/searchproviders/flatpak.desktop
%{_datadir}/kservices5/searchproviders/invent_issues.desktop
%{_datadir}/kservices5/searchproviders/invent_mr.desktop
%{_datadir}/kservices5/searchproviders/kde_store.desktop
%{_datadir}/kservices5/searchproviders/kreddit.desktop
%{_datadir}/kservices5/searchproviders/krita.desktop
%{_datadir}/kservices5/searchproviders/learncpp.desktop
%{_datadir}/kservices5/searchproviders/linguee.desktop
%{_datadir}/kservices5/searchproviders/microsoft_cpp.desktop
%{_datadir}/kservices5/searchproviders/opensuse.desktop
%{_datadir}/kservices5/searchproviders/protondb.desktop
%{_datadir}/kservices5/searchproviders/qt5.desktop
%{_datadir}/kservices5/searchproviders/qt6.desktop
%{_datadir}/kservices5/searchproviders/reddit.desktop
%{_datadir}/kservices5/searchproviders/rust.desktop
%{_datadir}/kservices5/searchproviders/ubuntu.desktop
%{_datadir}/kservices5/searchproviders/wine.desktop
%{_datadir}/kservices5/searchproviders/yandex.desktop
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_smb.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_cookies.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_datadir}/kdevappwizard/templates/kioworker.tar.bz2


%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIO
%{_includedir}/KF5/KIOCore
%{_includedir}/KF5/KIOFileWidgets
%{_includedir}/KF5/KIOWidgets
%{_includedir}/KF5/KIOGui
%dir %{_includedir}/KF5/kio
%{_includedir}/KF5/kio/kntlm.h
%{_includedir}/KF5/kio/kntlm_export.h
%{_libdir}/cmake/KF5KIO
%{_libdir}/libKF5KIOCore.so
%{_libdir}/libKF5KIOFileWidgets.so
%{_libdir}/libKF5KIOGui.so
%{_libdir}/libKF5KIONTLM.so
%{_libdir}/libKF5KIOWidgets.so
%{qt5dir}/mkspecs/modules/qt_KIOCore.pri
%{qt5dir}/mkspecs/modules/qt_KIOFileWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KIOGui.pri
%{qt5dir}/mkspecs/modules/qt_KIOWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KNTLM.pri
