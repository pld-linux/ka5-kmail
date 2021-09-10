%define		kdeappsver	21.08.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kmail
Summary:	kmail
Name:		ka5-%{kaname}
Version:	21.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	64166a5b20a3042c2c386df1652eddaa
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
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-search-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kldap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-kontactinterface-devel >= %{kdeappsver}
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka5-ktnef-devel >= %{kdeappsver}
BuildRequires:	ka5-libgravatar-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	ka5-libkleo-devel >= %{kdeappsver}
BuildRequires:	ka5-libksieve-devel >= %{kdeappsver}
BuildRequires:	ka5-mailcommon-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-messagelib-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemviews-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-sonnet-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMail is the email component of Kontact, the integrated personal
information manager from KDE.

%description -l pl.UTF-8
KMail jest komponentem poczty Kontaktu, zintegrowanego menadżera
informacji osobistej dla KDE.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

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
%attr(755,root,root) %{_bindir}/akonadi_archivemail_agent
%attr(755,root,root) %{_bindir}/akonadi_followupreminder_agent
%attr(755,root,root) %{_bindir}/akonadi_mailfilter_agent
%attr(755,root,root) %{_bindir}/akonadi_sendlater_agent
%attr(755,root,root) %{_bindir}/akonadi_unifiedmailbox_agent
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/ktnef
%ghost %{_libdir}/libkmailprivate.so.5
%attr(755,root,root) %{_libdir}/libkmailprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kmailpart.so
%dir %{_libdir}/qt5/plugins/akonadi/config
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/archivemailagentconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/followupreminderagentconfig.so
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
%dir %{_datadir}/kmail2
%dir %{_datadir}/kmail2/pics
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
%{_datadir}/kxmlgui5/kontactsummary
%{_datadir}/metainfo/org.kde.kmail2.appdata.xml
%attr(755,root,root) %{_bindir}/kmail-refresh-settings
%{_desktopdir}/org.kde.kmail-refresh-settings.desktop
%{_datadir}/dbus-1/services/org.kde.kmail.service
%{_datadir}/qlogging-categories5/kmail.categories
%{_datadir}/qlogging-categories5/kmail.renamecategories
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact5/kontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kontact5/kontact_summaryplugin.so
%attr(755,root,root) %{_bindir}/akonadi_mailmerge_agent
%{_datadir}/akonadi/agents/mailmergeagent.desktop
%{_datadir}/knotifications5/akonadi_mailmerge_agent.notifyrc
%dir %{_libdir}/qt5/plugins/pim/kcms/kmail
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_accounts.so
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_appearance.so
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_composer.so
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_misc.so
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_plugins.so
%{_libdir}/qt5/plugins/pim/kcms/kmail/kcm_kmail_security.so
%dir %{_libdir}/qt5/plugins/pim/kcms/summary
%{_libdir}/qt5/plugins/pim/kcms/summary/kcmkmailsummary.so
%{_libdir}/qt5/plugins/pim/kcms/summary/kcmkontactsummary.so
