#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		kio

Summary:	Network transparent access to files and data
Name:		kf5-%{kfname}
Version:	5.249.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	c9de88568931fc0a644674d29f16710b
Patch0:		kio_help-fallback-to-kde4-docs.patch
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel >= %{qtver}
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
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
Requires:	Qt6Core >= %{qtver}
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Gui >= %{qtver}
Requires:	Qt6Network >= %{qtver}
Requires:	Qt6Qml >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	Qt6Xml >= %{qtver}
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

%define		qt6dir		%{_libdir}/qt6

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
Requires:	Qt6Concurrent-devel >= %{qtver}
Requires:	Qt6DBus-devel >= %{qtver}
Requires:	Qt6Network-devel >= %{qtver}
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

install -d $RPM_BUILD_ROOT%{qt6dir}/plugins/kf5/{kfileitemaction,kio_dnd}
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr@latin

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,tok}

%find_lang %{kfname}6 --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ktelnetservice6
%attr(755,root,root) %{_bindir}/ktrash6
%attr(755,root,root) %{_libdir}/libKF6KIOCore.so.*.*
%ghost %{_libdir}/libKF6KIOCore.so.6
%attr(755,root,root) %{_libdir}/libKF6KIOFileWidgets.so.*.*
%ghost %{_libdir}/libKF6KIOFileWidgets.so.6
%attr(755,root,root) %{_libdir}/libKF6KIOGui.so.*.*
%ghost %{_libdir}/libKF6KIOGui.so.6
%attr(755,root,root) %{_libdir}/libKF6KIOWidgets.so.*.*
%ghost %{_libdir}/libKF6KIOWidgets.so.6
%attr(755,root,root) %{_libdir}/libkuriikwsfiltereng_private.so
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/kio6widgets.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/remotenotifier.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_file.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_ftp.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_ghelp.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_help.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_http.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_remote.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kio/kio_trash.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kiod/kioexecd.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kiod/kpasswdserver.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kiod/kssld.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/urifilters/fixhosturifilter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/urifilters/kshorturifilter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/urifilters/kuriikwsfilter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/urifilters/kurisearchfilter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/urifilters/localdomainurifilter.so
%attr(755,root,root) %{_prefix}/libexec/kf6/kiod6
%attr(755,root,root) %{_prefix}/libexec/kf6/kioexec
%attr(755,root,root) %{_prefix}/libexec/kf6/kioworker
%{_desktopdir}/ktelnetservice6.desktop
%{_datadir}/dbus-1/services/org.kde.kiod6.service
%{_datadir}/dbus-1/services/org.kde.kioexecd6.service
%{_datadir}/dbus-1/services/org.kde.kpasswdserver6.service
%{_datadir}/dbus-1/services/org.kde.kssld6.service
%{_datadir}/kdevappwizard/templates/kioworker6.tar.bz2
%dir %{_datadir}/kf6/searchproviders
%{_datadir}/kf6/searchproviders/7digital.desktop
%{_datadir}/kf6/searchproviders/acronym.desktop
%{_datadir}/kf6/searchproviders/amazon.desktop
%{_datadir}/kf6/searchproviders/amazon_mp3.desktop
%{_datadir}/kf6/searchproviders/amg.desktop
%{_datadir}/kf6/searchproviders/archpkg.desktop
%{_datadir}/kf6/searchproviders/archwiki.desktop
%{_datadir}/kf6/searchproviders/backports.desktop
%{_datadir}/kf6/searchproviders/baidu.desktop
%{_datadir}/kf6/searchproviders/beolingus.desktop
%{_datadir}/kf6/searchproviders/bing.desktop
%{_datadir}/kf6/searchproviders/boo.desktop
%{_datadir}/kf6/searchproviders/bug.desktop
%{_datadir}/kf6/searchproviders/call.desktop
%{_datadir}/kf6/searchproviders/cia.desktop
%{_datadir}/kf6/searchproviders/citeseer.desktop
%{_datadir}/kf6/searchproviders/codeberg.desktop
%{_datadir}/kf6/searchproviders/cpan.desktop
%{_datadir}/kf6/searchproviders/cplusplus.desktop
%{_datadir}/kf6/searchproviders/cppreference.desktop
%{_datadir}/kf6/searchproviders/ctan.desktop
%{_datadir}/kf6/searchproviders/ctan_cat.desktop
%{_datadir}/kf6/searchproviders/dbug.desktop
%{_datadir}/kf6/searchproviders/de2en.desktop
%{_datadir}/kf6/searchproviders/de2fr.desktop
%{_datadir}/kf6/searchproviders/deb.desktop
%{_datadir}/kf6/searchproviders/deepl.desktop
%{_datadir}/kf6/searchproviders/dictfr.desktop
%{_datadir}/kf6/searchproviders/docbook.desktop
%{_datadir}/kf6/searchproviders/doi.desktop
%{_datadir}/kf6/searchproviders/duckduckgo.desktop
%{_datadir}/kf6/searchproviders/duckduckgo_info.desktop
%{_datadir}/kf6/searchproviders/duckduckgo_shopping.desktop
%{_datadir}/kf6/searchproviders/ecosia.desktop
%{_datadir}/kf6/searchproviders/en2de.desktop
%{_datadir}/kf6/searchproviders/en2es.desktop
%{_datadir}/kf6/searchproviders/en2fr.desktop
%{_datadir}/kf6/searchproviders/en2it.desktop
%{_datadir}/kf6/searchproviders/es2en.desktop
%{_datadir}/kf6/searchproviders/facebook.desktop
%{_datadir}/kf6/searchproviders/feedster.desktop
%{_datadir}/kf6/searchproviders/flatpak.desktop
%{_datadir}/kf6/searchproviders/flickr.desktop
%{_datadir}/kf6/searchproviders/flickrcc.desktop
%{_datadir}/kf6/searchproviders/foldoc.desktop
%{_datadir}/kf6/searchproviders/fr2de.desktop
%{_datadir}/kf6/searchproviders/fr2en.desktop
%{_datadir}/kf6/searchproviders/freecode.desktop
%{_datadir}/kf6/searchproviders/freedb.desktop
%{_datadir}/kf6/searchproviders/fsd.desktop
%{_datadir}/kf6/searchproviders/github.desktop
%{_datadir}/kf6/searchproviders/gitlab.desktop
%{_datadir}/kf6/searchproviders/google.desktop
%{_datadir}/kf6/searchproviders/google_advanced.desktop
%{_datadir}/kf6/searchproviders/google_code.desktop
%{_datadir}/kf6/searchproviders/google_groups.desktop
%{_datadir}/kf6/searchproviders/google_images.desktop
%{_datadir}/kf6/searchproviders/google_lucky.desktop
%{_datadir}/kf6/searchproviders/google_maps.desktop
%{_datadir}/kf6/searchproviders/google_movie.desktop
%{_datadir}/kf6/searchproviders/google_news.desktop
%{_datadir}/kf6/searchproviders/google_shopping.desktop
%{_datadir}/kf6/searchproviders/grec.desktop
%{_datadir}/kf6/searchproviders/hyperdictionary.desktop
%{_datadir}/kf6/searchproviders/hyperdictionary_thesaurus.desktop
%{_datadir}/kf6/searchproviders/identica_groups.desktop
%{_datadir}/kf6/searchproviders/identica_notices.desktop
%{_datadir}/kf6/searchproviders/identica_people.desktop
%{_datadir}/kf6/searchproviders/imdb.desktop
%{_datadir}/kf6/searchproviders/invent.desktop
%{_datadir}/kf6/searchproviders/invent_issues.desktop
%{_datadir}/kf6/searchproviders/invent_mr.desktop
%{_datadir}/kf6/searchproviders/invent_repo.desktop
%{_datadir}/kf6/searchproviders/it2en.desktop
%{_datadir}/kf6/searchproviders/jamendo.desktop
%{_datadir}/kf6/searchproviders/jeeves.desktop
%{_datadir}/kf6/searchproviders/kde.desktop
%{_datadir}/kf6/searchproviders/kde_apps.desktop
%{_datadir}/kf6/searchproviders/kde_forums.desktop
%{_datadir}/kf6/searchproviders/kde_store.desktop
%{_datadir}/kf6/searchproviders/kde_techbase.desktop
%{_datadir}/kf6/searchproviders/kde_userbase.desktop
%{_datadir}/kf6/searchproviders/kreddit.desktop
%{_datadir}/kf6/searchproviders/krita.desktop
%{_datadir}/kf6/searchproviders/learncpp.desktop
%{_datadir}/kf6/searchproviders/leo.desktop
%{_datadir}/kf6/searchproviders/linguee.desktop
%{_datadir}/kf6/searchproviders/magnatune.desktop
%{_datadir}/kf6/searchproviders/metacrawler.desktop
%{_datadir}/kf6/searchproviders/microsoft_cpp.desktop
%{_datadir}/kf6/searchproviders/msdn.desktop
%{_datadir}/kf6/searchproviders/multitran-deru.desktop
%{_datadir}/kf6/searchproviders/multitran-enru.desktop
%{_datadir}/kf6/searchproviders/multitran-esru.desktop
%{_datadir}/kf6/searchproviders/multitran-frru.desktop
%{_datadir}/kf6/searchproviders/multitran-itru.desktop
%{_datadir}/kf6/searchproviders/multitran-nlru.desktop
%{_datadir}/kf6/searchproviders/netcraft.desktop
%{_datadir}/kf6/searchproviders/nl-telephone.desktop
%{_datadir}/kf6/searchproviders/nl-teletekst.desktop
%{_datadir}/kf6/searchproviders/opendesktop.desktop
%{_datadir}/kf6/searchproviders/opensuse.desktop
%{_datadir}/kf6/searchproviders/pgpkeys.desktop
%{_datadir}/kf6/searchproviders/php.desktop
%{_datadir}/kf6/searchproviders/protondb.desktop
%{_datadir}/kf6/searchproviders/pypi.desktop
%{_datadir}/kf6/searchproviders/python.desktop
%{_datadir}/kf6/searchproviders/qt5.desktop
%{_datadir}/kf6/searchproviders/qt6.desktop
%{_datadir}/kf6/searchproviders/qwant.desktop
%{_datadir}/kf6/searchproviders/qwant_images.desktop
%{_datadir}/kf6/searchproviders/qwant_news.desktop
%{_datadir}/kf6/searchproviders/qwant_shopping.desktop
%{_datadir}/kf6/searchproviders/qwant_social.desktop
%{_datadir}/kf6/searchproviders/qwant_videos.desktop
%{_datadir}/kf6/searchproviders/rae.desktop
%{_datadir}/kf6/searchproviders/rag.desktop
%{_datadir}/kf6/searchproviders/reddit.desktop
%{_datadir}/kf6/searchproviders/rfc.desktop
%{_datadir}/kf6/searchproviders/rpmfind.desktop
%{_datadir}/kf6/searchproviders/ruby_application_archive.desktop
%{_datadir}/kf6/searchproviders/rust.desktop
%{_datadir}/kf6/searchproviders/soundcloud.desktop
%{_datadir}/kf6/searchproviders/sourceforge.desktop
%{_datadir}/kf6/searchproviders/technorati.desktop
%{_datadir}/kf6/searchproviders/technoratitags.desktop
%{_datadir}/kf6/searchproviders/thesaurus.desktop
%{_datadir}/kf6/searchproviders/tvtome.desktop
%{_datadir}/kf6/searchproviders/ubuntu.desktop
%{_datadir}/kf6/searchproviders/urbandictionary.desktop
%{_datadir}/kf6/searchproviders/uspto.desktop
%{_datadir}/kf6/searchproviders/vimeo.desktop
%{_datadir}/kf6/searchproviders/voila.desktop
%{_datadir}/kf6/searchproviders/webster.desktop
%{_datadir}/kf6/searchproviders/wikia.desktop
%{_datadir}/kf6/searchproviders/wikipedia.desktop
%{_datadir}/kf6/searchproviders/wiktionary.desktop
%{_datadir}/kf6/searchproviders/wine.desktop
%{_datadir}/kf6/searchproviders/wolfram_alpha.desktop
%{_datadir}/kf6/searchproviders/wordref.desktop
%{_datadir}/kf6/searchproviders/yahoo.desktop
%{_datadir}/kf6/searchproviders/yahoo_image.desktop
%{_datadir}/kf6/searchproviders/yahoo_local.desktop
%{_datadir}/kf6/searchproviders/yahoo_shopping.desktop
%{_datadir}/kf6/searchproviders/yahoo_video.desktop
%{_datadir}/kf6/searchproviders/yandex.desktop
%{_datadir}/kf6/searchproviders/youtube.desktop
%{_datadir}/qlogging-categories6/kio.categories
%{_datadir}/qlogging-categories6/kio.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KIO
%{_includedir}/KF6/KIOCore
%{_includedir}/KF6/KIOFileWidgets
%{_includedir}/KF6/KIOWidgets
%{_includedir}/KF6/KIOGui
%{_libdir}/cmake/KF6KIO
%{_libdir}/libKF6KIOCore.so
%{_libdir}/libKF6KIOFileWidgets.so
%{_libdir}/libKF6KIOGui.so
%{_libdir}/libKF6KIOWidgets.so
