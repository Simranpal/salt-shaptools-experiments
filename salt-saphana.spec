#
# spec file for package salt-saphana
#
# Copyright (c) 2016 SUSE LLC, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           salt-saphana
Version:        0.3.0
Release:        1
Summary:        Salt modules and states for SAP HANA

License:        Apache-2.0
Url:            https://github.com/arbulu89/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%define fname hana

%description
Salt modules and states for SAP HANA

%prep
%setup -q

%build

%install
pwd
mkdir -p %{buildroot}/srv/salt/_modules
mkdir -p %{buildroot}/srv/salt/_states
cp -R salt/modules/hanamod.py %{buildroot}/srv/salt/_modules
cp -R salt/states/hanamod.py %{buildroot}/srv/salt/_states
cp -R salt/modules/crmshmod.py %{buildroot}/srv/salt/_modules
cp -R salt/states/crmshmod.py %{buildroot}/srv/salt/_states


%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
/srv/salt/_modules
/srv/salt/_states

%dir %attr(0755, root, salt) /srv/salt
%dir %attr(0755, root, salt) /srv/salt/_modules
%dir %attr(0755, root, salt) /srv/salt/_states

%changelog CHANGELOG.md