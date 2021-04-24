#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-crfsuite
Version  : 0.9.7
Release  : 18
URL      : https://files.pythonhosted.org/packages/e1/4d/abbe0dc125b0a11ecd55fa3a5b33b44656227d214a61deb73e2a152aa257/python-crfsuite-0.9.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/4d/abbe0dc125b0a11ecd55fa3a5b33b44656227d214a61deb73e2a152aa257/python-crfsuite-0.9.7.tar.gz
Summary  : Python binding for CRFsuite
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-crfsuite-license = %{version}-%{release}
Requires: python-crfsuite-python = %{version}-%{release}
Requires: python-crfsuite-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
python-crfsuite
        ===============

%package license
Summary: license components for the python-crfsuite package.
Group: Default

%description license
license components for the python-crfsuite package.


%package python
Summary: python components for the python-crfsuite package.
Group: Default
Requires: python-crfsuite-python3 = %{version}-%{release}

%description python
python components for the python-crfsuite package.


%package python3
Summary: python3 components for the python-crfsuite package.
Group: Default
Requires: python3-core
Provides: pypi(python_crfsuite)

%description python3
python3 components for the python-crfsuite package.


%prep
%setup -q -n python-crfsuite-0.9.7
cd %{_builddir}/python-crfsuite-0.9.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603401819
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-crfsuite
cp %{_builddir}/python-crfsuite-0.9.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/python-crfsuite/48fc66e2f58aa63627bd74410013defb0c874c1d
cp %{_builddir}/python-crfsuite-0.9.7/crfsuite/COPYING %{buildroot}/usr/share/package-licenses/python-crfsuite/2e0ac6915545102c1ea6b0a3c8c6c85187684bdd
cp %{_builddir}/python-crfsuite-0.9.7/crfsuite/lib/cqdb/COPYING %{buildroot}/usr/share/package-licenses/python-crfsuite/b040fe0b773c5b368b78f9aedce9c156857092e7
cp %{_builddir}/python-crfsuite-0.9.7/liblbfgs/COPYING %{buildroot}/usr/share/package-licenses/python-crfsuite/a2dc68f3a713ad04c1811f6c5468bb6e0755fa23
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-crfsuite/2e0ac6915545102c1ea6b0a3c8c6c85187684bdd
/usr/share/package-licenses/python-crfsuite/48fc66e2f58aa63627bd74410013defb0c874c1d
/usr/share/package-licenses/python-crfsuite/a2dc68f3a713ad04c1811f6c5468bb6e0755fa23
/usr/share/package-licenses/python-crfsuite/b040fe0b773c5b368b78f9aedce9c156857092e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
