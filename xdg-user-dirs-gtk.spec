Name:		xdg-user-dirs-gtk
Version:	0.8
Release:	7%{?dist}
Summary:	Gnome integration of special directories

Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	http://download.gnome.org/sources/xdg-user-dirs-gtk/%{version}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gettext, gtk2-devel, pkgconfig, perl-XML-Parser, xdg-user-dirs
BuildRequires:	intltool
Requires:	xdg-user-dirs

# [mr_IN] [xdg-user-dirs-gtk] Missing Translations
# https://bugzilla.redhat.com/show_bug.cgi?id=559550
Patch0:		xdg-user-dirs-gtk-0.8-mr_IN-translation.patch
# more translations
# https://bugzilla.redhat.com/show_bug.cgi?id=586399
Patch1:         xdg-user-dirs-gtk-translations.patch

%description
Contains some integration of xdg-user-dirs with the gnome
desktop, including creating default bookmarks and detecting
locale changes.

%prep
%setup -q
%patch0 -p1 -b .translation-mr
%patch1 -p1 -b .translations

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc NEWS AUTHORS README ChangeLog COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop

%changelog
* Mon May  3 2010 Matthias Clasen <mclasen@redhat.com - 0.8-7
- Add translations for as, bn_IN, gu, hi, kn, ml, or, pa, ru,
  ta, te, zh_CN, zh_TW
Resolves: #586399

* Fri Jan 29 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.8-6
- Add mr_IN translation (#559550)

* Tue Jan  5 2010 Tomas Bzatek <tbzatek@redhat.com> - 0.8-5
- Fix license tag

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.8-4.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tomas Bzatek <tbzatek@redhat.com> - 0.8-2
- Require intltool

* Fri Sep  5 2008 Matthias Clasen  <mclasen@redhat.com> - 0.8-1
- Update to 0.8
 
* Tue Aug 12 2008 Jason L Tibbitts III <tibbs@math.uh.edu> - 0.7-2
- Fix license tag.

* Tue Feb 12 2008 Alexander Larsson <alexl@redhat.com> - 0.7-1
- Update to 0.7
- Uncomment missing patches

* Sun Nov  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.6-4
- Correct the URL

* Mon Oct  1 2007 Matthias Clasen <mclasen@redhat.com> - 0.6-2
- Fix the special case for en_US  (#307881)

* Tue Aug 21 2007 Alexander Larsson <alexl@redhat.com> - 0.6-1
- Update to 0.6 (new translations)

* Fri Jul  6 2007  Matthias Clasen  <mclasen@redhat.com> - 0.5-2
- Make the autostart file work in KDE (#247304)

* Wed Apr 25 2007  <alexl@redhat.com> - 0.5-1
- Update to 0.5
- Fixes silly dialog when no translations (#237384)

* Wed Apr 11 2007 Alexander Larsson <alexl@redhat.com> - 0.4-1
- update to 0.4 (#234512)

* Tue Mar  6 2007 Alexander Larsson <alexl@redhat.com> - 0.3-1
- update to 0.3
- Add xdg-user-dirs buildreq

* Fri Mar  2 2007 Alexander Larsson <alexl@redhat.com> - 0.2-1
- Update to 0.2

* Fri Mar  2 2007 Alexander Larsson <alexl@redhat.com> - 0.1-2
- Add buildrequires
- Mark autostart file as config

* Wed Feb 28 2007 Alexander Larsson <alexl@redhat.com> - 0.1-1
- Initial version

