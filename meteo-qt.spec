Name:           meteo-qt
Version:        4.3
Release:        1%{?dist}
Summary:        Weather status system tray application
License:        GPL-3.0-or-later
URL:            https://github.com/dglent/%{name}
Source:         https://github.com/dglent/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyqt6-base
BuildRequires:  python%{python3_pkgversion}-pyqt6-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools

Requires:       hicolor-icon-theme
Requires:       python%{python3_pkgversion}-lxml
Requires:       python%{python3_pkgversion}-pyqt6
Requires:       python%{python3_pkgversion}-pyqt6-sip

%description
A Qt system tray application for the weather status
Weather data from: http://openweathermap.org/

%prep
%autosetup -p1
# Use Fedora specific variant for qt6
sed -i 's/lrelease-pro-qt6/lrelease-qt6/' setup.py
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files meteo_qt
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}%{python3_sitelib}%{_datadir}/applications/%{name}.desktop
install -Dm0644 \
    %{buildroot}%{python3_sitelib}%{_datadir}/icons/weather-few-clouds.png \
    %{buildroot}%{_datadir}/icons/weather-few-clouds.png
mkdir -p %{buildroot}%{_datadir}/meteo_qt/translations
mv %{buildroot}%{python3_sitelib}%{_datadir}/meteo_qt/translations/*.qm \
    %{buildroot}%{_datadir}/meteo_qt/translations/
rm -rf %{buildroot}%{python3_sitelib}/usr
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{pyproject_files}
%license LICENSE
%doc TODO CHANGELOG README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/weather-few-clouds.png
%dir %{_datadir}/meteo_qt
%dir %{_datadir}/meteo_qt/translations
%{_datadir}/meteo_qt/translations/*.qm

%changelog
* Fri Dec 30 2026 Basil Crow <me@basilcrow.com> - 4.3-1
- Initial packaging.
