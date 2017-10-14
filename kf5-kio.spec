%define		kdeframever	5.39
%define		qtver		5.4.0
%define		kfname		kio

Summary:	Network transparent access to files and data
Name:		kf5-%{kfname}
Version:	5.39.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	31c865a351ace1b987fd40f9fd176cd4
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= %{qtver}
BuildRequires:	Qt5Script-devel >= %{qtver}
BuildRequires:	Qt5Test-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	acl-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	heimdal-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= 1.0.0
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
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
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf5-dirs
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
Requires:	Qt5Network-devel >= %{qtver}
Requires:	cmake >= 2.6.0
Requires:	kf5-kbookmarks-devel >= %{version}
Requires:	kf5-kcompletion-devel >= %{version}
Requires:	kf5-kconfig-devel >= %{version}
Requires:	kf5-kcoreaddons-devel >= %{version}
Requires:	kf5-kitemviews-devel >= %{version}
Requires:	kf5-kjobwidgets-devel >= %{version}
Requires:	kf5-kservice-devel >= %{version}
Requires:	kf5-kxmlgui-devel >= %{version}
Requires:	kf5-solid-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
/etc/xdg/accept-languages.codes
/etc/xdg/kshorturifilterrc
%attr(755,root,root) %{_bindir}/kcookiejar5
#%%attr(755,root,root) %{_bindir}/kmailservice5
%attr(755,root,root) %{_bindir}/ktelnetservice5
%attr(755,root,root) %{_bindir}/ktrash5
%attr(755,root,root) %{_bindir}/protocoltojson
%attr(755,root,root) %{_libdir}/kf5/kio_http_cache_cleaner
%attr(755,root,root) %{_libdir}/kf5/kiod5
%attr(755,root,root) %{_libdir}/kf5/kioexec
%attr(755,root,root) %{_libdir}/kf5/kioslave
%attr(755,root,root) %{_libdir}/kf5/kpac_dhcp_helper
%attr(755,root,root) %ghost %{_libdir}/libKF5KIOCore.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOCore.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KIOFileWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOFileWidgets.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KIONTLM.so.5
%attr(755,root,root) %{_libdir}/libKF5KIONTLM.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KIOWidgets.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOWidgets.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5KIOGui.so.5
%attr(755,root,root) %{_libdir}/libKF5KIOGui.so.*.*
%attr(755,root,root) %{qt5dir}/plugins/kcm_kio.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_trash.so
%attr(755,root,root) %{qt5dir}/plugins/kcm_webshortcuts.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/kcookiejar.so
#%%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/kpasswdserver.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kded/proxyscout.so
%dir %{qt5dir}/plugins/kf5/kio
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/file.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/ftp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/ghelp.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/help.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/http.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kio/trash.so
%dir %{qt5dir}/plugins/kf5/kiod
%attr(755,root,root) %{qt5dir}/plugins/kf5/kiod/kssld.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/kiod/kpasswdserver.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/fixhosturifilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kshorturifilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kuriikwsfilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/kurisearchfilter.so
%attr(755,root,root) %{qt5dir}/plugins/kf5/urifilters/localdomainurifilter.so

#%%{_desktopdir}/kmailservice5.desktop
%{_desktopdir}/ktelnetservice5.desktop
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KCookieServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KDirNotify.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KPasswdServer.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.KSlaveLauncher.xml
%{_datadir}/dbus-1/interfaces/kf5_org.kde.kio.FileUndoManager.xml
%{_datadir}/dbus-1/services/org.kde.kiod5.service
%{_datadir}/dbus-1/services/org.kde.kcookiejar5.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver.service
%{_datadir}/dbus-1/services/org.kde.kssld5.service

%{_docdir}/HTML/en/kioslave5

%{_datadir}/kf5/kcookiejar/domain_info

%{_datadir}/knotifications5/proxyscout.notifyrc

%{_datadir}/kservices5/cache.desktop
%{_datadir}/kservices5/cookies.desktop
%{_datadir}/kservices5/data.protocol
#%%{_datadir}/kservices5/file.protocol
#%%{_datadir}/kservices5/fixhosturifilter.desktop
#%%{_datadir}/kservices5/ftp.protocol
#%%{_datadir}/kservices5/ghelp.protocol
#%%{_datadir}/kservices5/help.protocol
#%%{_datadir}/kservices5/http.protocol
%{_datadir}/kservices5/http_cache_cleaner.desktop
#%%{_datadir}/kservices5/https.protocol
%{_datadir}/kservices5/kcmtrash.desktop
#%%{_datadir}/kservices5/kded/proxyscout.desktop
#%%{_datadir}/kservices5/kshorturifilter.desktop
#%%{_datadir}/kservices5/kuriikwsfilter.desktop
#%%{_datadir}/kservices5/kurisearchfilter.desktop
#%%{_datadir}/kservices5/localdomainurifilter.desktop
%{_datadir}/kservices5/mms.protocol
%{_datadir}/kservices5/mmst.protocol
%{_datadir}/kservices5/mmsu.protocol
%{_datadir}/kservices5/netpref.desktop
%{_datadir}/kservices5/pnm.protocol
%{_datadir}/kservices5/proxy.desktop
%{_datadir}/kservices5/rtsp.protocol
%{_datadir}/kservices5/rtspt.protocol
%{_datadir}/kservices5/rtspu.protocol
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
%{_datadir}/kservices5/searchproviders/blip.desktop
%{_datadir}/kservices5/searchproviders/bugft.desktop
%{_datadir}/kservices5/searchproviders/bugno.desktop
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
%{_datadir}/kservices5/searchproviders/dmoz.desktop
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
%{_datadir}/kservices5/searchproviders/ethicle.desktop
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
%{_datadir}/kservices5/searchproviders/gitorious.desktop
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
%{_datadir}/kservices5/searchproviders/ibl.desktop
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
%{_datadir}/kservices5/searchproviders/kde_look.desktop
%{_datadir}/kservices5/searchproviders/kde_projects.desktop
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
%{_datadir}/kservices5/searchproviders/qt.desktop
%{_datadir}/kservices5/searchproviders/qt4.desktop
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
#%%{_datadir}/kservices5/trash.protocol
%{_datadir}/kservices5/useragent.desktop
%{_datadir}/kservices5/useragentstrings
#%%{_datadir}/kservices5/webdav.protocol
#%%{_datadir}/kservices5/webdavs.protocol
%{_datadir}/kservices5/webshortcuts.desktop
%{_datadir}/kservicetypes5/kfileitemactionplugin.desktop
%{_datadir}/kservicetypes5/kiodndpopupmenuplugin.desktop
%{_datadir}/kservicetypes5/konqpopupmenuplugin.desktop
%{_datadir}/kservicetypes5/kpropertiesdialogplugin.desktop
%{_datadir}/kservicetypes5/kurifilterplugin.desktop
%{_datadir}/kservicetypes5/searchprovider.desktop
%{_datadir}/kservicetypes5/uasprovider.desktop
%{_mandir}/man8/kcookiejar5.8*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KIOCore
%{_includedir}/KF5/KIOFileWidgets
%{_includedir}/KF5/KIOWidgets
%{_includedir}/KF5/KIOGui
%dir %{_includedir}/KF5/kio
%{_includedir}/KF5/kio/kntlm.h
%{_includedir}/KF5/kio/kntlm_export.h
%{_includedir}/KF5/kio_version.h
%{_libdir}/cmake/KF5KIO
%attr(755,root,root) %{_libdir}/libKF5KIOCore.so
%attr(755,root,root) %{_libdir}/libKF5KIOFileWidgets.so
%attr(755,root,root) %{_libdir}/libKF5KIOGui.so
%attr(755,root,root) %{_libdir}/libKF5KIONTLM.so
%attr(755,root,root) %{_libdir}/libKF5KIOWidgets.so
%{qt5dir}/mkspecs/modules/qt_KIOCore.pri
%{qt5dir}/mkspecs/modules/qt_KIOFileWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KIOGui.pri
%{qt5dir}/mkspecs/modules/qt_KIOWidgets.pri
%{qt5dir}/mkspecs/modules/qt_KNTLM.pri
