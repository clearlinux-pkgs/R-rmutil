#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rmutil
Version  : 1.1.3
Release  : 7
URL      : https://cran.r-project.org/src/contrib/rmutil_1.1.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rmutil_1.1.3.tar.gz
Summary  : Utilities for Nonlinear Regression and Repeated Measurements
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rmutil-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
measurements not to be used by itself but called by other Lindsey packages such
    as 'gnlm', 'stable', 'growth', 'repeated', and 'event'

%package lib
Summary: lib components for the R-rmutil package.
Group: Libraries

%description lib
lib components for the R-rmutil package.


%prep
%setup -q -c -n rmutil

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552786157

%install
export SOURCE_DATE_EPOCH=1552786157
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmutil
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmutil
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rmutil
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  rmutil || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rmutil/DESCRIPTION
/usr/lib64/R/library/rmutil/INDEX
/usr/lib64/R/library/rmutil/Meta/Rd.rds
/usr/lib64/R/library/rmutil/Meta/features.rds
/usr/lib64/R/library/rmutil/Meta/hsearch.rds
/usr/lib64/R/library/rmutil/Meta/links.rds
/usr/lib64/R/library/rmutil/Meta/nsInfo.rds
/usr/lib64/R/library/rmutil/Meta/package.rds
/usr/lib64/R/library/rmutil/NAMESPACE
/usr/lib64/R/library/rmutil/NEWS.md
/usr/lib64/R/library/rmutil/R/rmutil
/usr/lib64/R/library/rmutil/R/rmutil.rdb
/usr/lib64/R/library/rmutil/R/rmutil.rdx
/usr/lib64/R/library/rmutil/help/AnIndex
/usr/lib64/R/library/rmutil/help/aliases.rds
/usr/lib64/R/library/rmutil/help/paths.rds
/usr/lib64/R/library/rmutil/help/rmutil.rdb
/usr/lib64/R/library/rmutil/help/rmutil.rdx
/usr/lib64/R/library/rmutil/html/00Index.html
/usr/lib64/R/library/rmutil/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rmutil/libs/rmutil.so
/usr/lib64/R/library/rmutil/libs/rmutil.so.avx2
/usr/lib64/R/library/rmutil/libs/rmutil.so.avx512
