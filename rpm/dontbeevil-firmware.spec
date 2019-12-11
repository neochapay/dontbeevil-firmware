%define debug_package %{nil}

Name:       dontbeevil-firmware
Summary:    Firmware PinePhone64
Version:    1
Release:    0
Group:      System/Kernel
License:    GPLv2
URL:        https://github.com/neochapay/dontbeevil-firmware
Source:     %{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
This package contains the firmware for for PinePhone, PineTab 
and PinePhone Devboard aka DontBeEvel board.

%prep
%setup -q

%build
ls .

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware/rtl_bt
cp rtl8723bt/rtl_bt/*.bin $RPM_BUILD_ROOT/lib/firmware/rtl_bt

%files
/lib/firmware
