#
# spec file for package instsource-susedata
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           instsource-susedata
Summary:        Utility to add susedata to repomd metadata
License:        GPL-2.0
Group:          System/Management
Version:        0.1
Release:        0
Source:         %{name}-%{version}.tar.bz2
Patch0:         instsource-susedata-diskusage.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?is_opensuse}
Requires:       openSUSE-EULAs
%else
Requires:       SLE-EULAs
%endif
Requires:       perl-XML-Structured
Supplements:    kiwi-instsource
BuildArch:      noarch

%description
This utility scans repodata and adds susedata and EULAs where needed.

%prep
%setup -q
%patch0 -p0

%build
# empty because of rpmlint warning rpm-buildroot-usage

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 add_product_susedata $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-, root, root)
%doc COPYING
/usr/bin/add_product_susedata

%changelog
