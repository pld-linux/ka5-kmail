%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kmail
Summary:	kmail
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	10fd41b581e947306e8925e943bf7581
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel >= 1.8.0
BuildRequires:	ka5-akonadi-contacts-devel >= 18.12.0
BuildRequires:	ka5-akonadi-devel >= 18.12.0
BuildRequires:	ka5-akonadi-mime-devel >= 18.12.0
BuildRequires:	ka5-akonadi-search-devel >= 18.12.0
BuildRequires:	ka5-kcalcore-devel >= 18.12.0
BuildRequires:	ka5-kcalutils-devel >= 18.12.0
BuildRequires:	ka5-kcontacts-devel >= 18.12.0
BuildRequires:	ka5-kdepim-apps-libs-devel >= 18.12.0
BuildRequires:	ka5-kidentitymanagement-devel >= 18.12.0
BuildRequires:	ka5-kldap-devel >= 18.12.0
BuildRequires:	ka5-kmailtransport-devel >= 18.12.0
BuildRequires:	ka5-kmime-devel >= 18.12.0
BuildRequires:	ka5-kontactinterface-devel >= 18.12.0
BuildRequires:	ka5-kpimtextedit-devel >= 18.12.0
BuildRequires:	ka5-ktnef-devel >= 18.12.0
BuildRequires:	ka5-libgravatar-devel >= 18.12.0
BuildRequires:	ka5-libkdepim-devel >= 18.12.0
BuildRequires:	ka5-libkleo-devel >= 18.12.0
BuildRequires:	ka5-libksieve-devel >= 18.12.0
BuildRequires:	ka5-mailcommon-devel >= 18.12.0
BuildRequires:	ka5-messagelib-devel >= 18.12.0
BuildRequires:	ka5-messagelib-devel >= 18.12.0
BuildRequires:	ka5-pimcommon-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kbookmarks-devel >= 5.51.0
BuildRequires:	kf5-kcmutils-devel >= 5.51.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.51.0
BuildRequires:	kf5-kcrash-devel >= 5.51.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.51.0
BuildRequires:	kf5-kdoctools-devel >= 5.51.0
BuildRequires:	kf5-kguiaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kiconthemes-devel >= 5.51.0
BuildRequires:	kf5-kio-devel >= 5.51.0
BuildRequires:	kf5-kitemviews-devel >= 5.51.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.51.0
BuildRequires:	kf5-knotifications-devel >= 5.51.0
BuildRequires:	kf5-knotifyconfig-devel >= 5.51.0
BuildRequires:	kf5-kparts-devel >= 5.51.0
BuildRequires:	kf5-kservice-devel >= 5.51.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
BuildRequires:	kf5-kxmlgui-devel >= 5.51.0
BuildRequires:	kf5-sonnet-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMail is the email component of Kontact, the integrated personal
information manager from KDE.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
/sbin/ldconfig

%postun
%update_icon_cache hicolor
/sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kmail.categories
/etc/xdg/kmail.renamecategories
/etc/xdg/ktnefapps.categories
/etc/xdg/ktnefapps.renamecategories
%attr(755,root,root) %{_bindir}/akonadi_archivemail_agent
%attr(755,root,root) %{_bindir}/akonadi_followupreminder_agent
%attr(755,root,root) %{_bindir}/akonadi_mailfilter_agent
%attr(755,root,root) %{_bindir}/akonadi_sendlater_agent
%attr(755,root,root) %{_bindir}/akonadi_unifiedmailbox_agent
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/ktnef
%attr(755,root,root) %ghost %{_libdir}/libkmailprivate.so.5
%attr(755,root,root) %{_libdir}/libkmailprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kmail.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kmailsummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kontactsummary.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kmailpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact_summaryplugin.so
%{_datadir}/akonadi/agents/archivemailagent.desktop
%{_datadir}/akonadi/agents/followupreminder.desktop
%{_datadir}/akonadi/agents/mailfilteragent.desktop
%{_datadir}/akonadi/agents/sendlateragent.desktop
%{_datadir}/akonadi/agents/unifiedmailboxagent.desktop
%{_desktopdir}/kmail_view.desktop
%{_desktopdir}/org.kde.kmail2.desktop
%{_desktopdir}/org.kde.ktnef.desktop
%{_datadir}/config.kcfg/archivemailagentsettings.kcfg
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmail.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmail.kmailpart.xml
%dir %{_iconsdir}/breeze-dark/16x16
%dir %{_iconsdir}/breeze-dark/16x16/emblems
%{_iconsdir}/breeze-dark/16x16/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/breeze-dark/16x16/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/breeze-dark/16x16/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/breeze-dark/16x16/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/breeze-dark/16x16/emblems/gpg-key-trust-level-4.svg
%dir %{_iconsdir}/breeze-dark/22x22
%dir %{_iconsdir}/breeze-dark/22x22/emblems
%{_iconsdir}/breeze-dark/22x22/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/breeze-dark/22x22/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/breeze-dark/22x22/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/breeze-dark/22x22/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/breeze-dark/22x22/emblems/gpg-key-trust-level-4.svg
%dir %{_iconsdir}/breeze-dark/8x8
%dir %{_iconsdir}/breeze-dark/8x8/emblems
%{_iconsdir}/breeze-dark/8x8/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/breeze-dark/8x8/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/breeze-dark/8x8/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/breeze-dark/8x8/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/breeze-dark/8x8/emblems/gpg-key-trust-level-4.svg
%{_iconsdir}/hicolor/128x128/apps/kmail.png
%{_iconsdir}/hicolor/16x16/apps/kmail.png
%{_iconsdir}/hicolor/16x16/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/hicolor/16x16/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/hicolor/16x16/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/hicolor/16x16/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/hicolor/16x16/emblems/gpg-key-trust-level-4.svg
%{_iconsdir}/hicolor/22x22/actions/ktnef_extract_all_to.png
%{_iconsdir}/hicolor/22x22/actions/ktnef_extract_to.png
%{_iconsdir}/hicolor/22x22/apps/kmail.png
%{_iconsdir}/hicolor/22x22/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/hicolor/22x22/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/hicolor/22x22/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/hicolor/22x22/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/hicolor/22x22/emblems/gpg-key-trust-level-4.svg
%{_iconsdir}/hicolor/32x32/apps/kmail.png
%{_iconsdir}/hicolor/48x48/apps/kmail.png
%{_iconsdir}/hicolor/48x48/apps/ktnef.png
%{_iconsdir}/hicolor/64x64/apps/kmail.png
%{_iconsdir}/hicolor/8x8/emblems/gpg-key-trust-level-0.svg
%{_iconsdir}/hicolor/8x8/emblems/gpg-key-trust-level-1.svg
%{_iconsdir}/hicolor/8x8/emblems/gpg-key-trust-level-2.svg
%{_iconsdir}/hicolor/8x8/emblems/gpg-key-trust-level-3.svg
%{_iconsdir}/hicolor/8x8/emblems/gpg-key-trust-level-4.svg
%{_iconsdir}/hicolor/scalable/apps/kmail.svg
%attr(755,root,root) %{_datadir}/kconf_update/kmail-15.08-kickoff.sh
%{_datadir}/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/kconf_update/kmail2.sh
%{_datadir}/kconf_update/kmail2.upd
%{_datadir}/kmail2/pics/pgp-keys.png
%{_datadir}/knotifications5/akonadi_archivemail_agent.notifyrc
%{_datadir}/knotifications5/akonadi_followupreminder_agent.notifyrc
%{_datadir}/knotifications5/akonadi_mailfilter_agent.notifyrc
%{_datadir}/knotifications5/akonadi_sendlater_agent.notifyrc
%{_datadir}/knotifications5/kmail2.notifyrc
%{_datadir}/kontact/ksettingsdialog/kmail.setdlg
%{_datadir}/kontact/ksettingsdialog/summary.setdlg
%{_datadir}/kservices5/kcmkmailsummary.desktop
%{_datadir}/kservices5/kcmkontactsummary.desktop
%{_datadir}/kservices5/kmail_config_accounts.desktop
%{_datadir}/kservices5/kmail_config_appearance.desktop
%{_datadir}/kservices5/kmail_config_composer.desktop
%{_datadir}/kservices5/kmail_config_misc.desktop
%{_datadir}/kservices5/kmail_config_plugins.desktop
%{_datadir}/kservices5/kmail_config_security.desktop
%{_datadir}/kservices5/kontact/kmailplugin.desktop
%{_datadir}/kservices5/kontact/summaryplugin.desktop
%{_datadir}/kservicetypes5/dbusmail.desktop
%{_datadir}/kxmlgui5/kontactsummary
%{_datadir}/metainfo/org.kde.kmail2.appdata.xml
