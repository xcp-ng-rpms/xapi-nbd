Name:           xapi-nbd
Version:        1.11.0
Release:        3.1%{?dist}
Summary:        NBD server that exposes XenServer disks
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xapi-nbd

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-nbd/archive?at=v1.11.0&format=tar.gz&prefix=xapi-nbd-1.11.0#/xapi-nbd-1.11.0.tar.gz
Source1: SOURCES/xapi-nbd/xapi-nbd.service
Source2: SOURCES/xapi-nbd/xapi-nbd.path


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xapi-nbd/archive?at=v1.11.0&format=tar.gz&prefix=xapi-nbd-1.11.0#/xapi-nbd-1.11.0.tar.gz) = 40168edbe1857e993f417af5af554764e751a9e0

# XCP-ng patches
# Patch not necessary anymore in xapi-nbd 1.12.0 and above
Patch1000: xapi-nbd-1.11.0-adapt-vbd.create-call.XCP-ng.patch

BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  ocaml-xen-api-client-devel
BuildRequires:  openssl-devel

%{?systemd_requires}

%description
NBD server that exposes XCP-ng disks

%prep
%autosetup -p1

%build
make release

%check
make test

%install
%{__install} -D -m 0755 _build/default/src/main.exe %{buildroot}/%{_sbindir}/xapi-nbd
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/xapi-nbd.service
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/xapi-nbd.path

%files
%doc README.md LICENSE MAINTAINERS
%{_sbindir}/xapi-nbd
%{_unitdir}/xapi-nbd.service
%{_unitdir}/xapi-nbd.path

%post
%systemd_post xapi-nbd.service
%systemd_post xapi-nbd.path

%preun
%systemd_preun xapi-nbd.service
%systemd_preun xapi-nbd.path

%postun
%systemd_postun xapi-nbd.service
%systemd_postun xapi-nbd.path

%changelog
* Mon Dec 20 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.11.0-3.1
- Sync with CH 8.2.1
- *** Upstream changelog ***
- * Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.11.0-3
- - Bump package after xs-opam update
- * Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.11.0-2
- - bump packages after xs-opam update

* Wed Jul 01 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.11.0-1.1
- Rebase on CH 8.2
- add xapi-nbd-1.11.0-adapt-vbd.create-call.XCP-ng.patch to adapt to new API

* Fri Apr 03 2020 Christian Lindig <christian.lindig@citrix.com> - 1.11.0-1
- CP-33058 centralize cipherstrings

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.10.0-3
- bump packages after xs-opam update

* Tue May 14 2019 Christian Lindig <christian.lindig@citrix.com> - 1.10.0-1
- XSI-338 improve signal handling and program exit

* Tue Jan 15 2019 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-1
- CA-307773: initialize EC curve to the one XAPI would use

* Wed Jan 09 2019 Christian Lindig <christian.lindig@citrix.com> - 1.8.0-1
- CA-303570 use same cipher suite as xapi

* Wed Jan 02 2019 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-1
- CP-30062 Update dependencies for Lwt 4.1, OCaml 4.07

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.6.0-1
- Reference xapi-inventory as xcp-invenotry is being deprecated.

* Tue Oct 09 2018 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- CA-298461 use local session for cleanups

* Tue Sep 18 2018 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- Update Travis setup, move to Dune from Jbuilder

* Wed Mar 28 2018 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- Use Alcotest_lwt for Lwt-based unit tests

* Wed Mar 21 2018 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- Fix compiler warnings
- .travis.yml: switch to centos-7

* Fri Jan 26 2018 Christian Lindig <christian.lindig@citrix.com> - 1.1.0-1
- Update to newer Lwt and NBD libraries

* Mon Dec 11 2017 Gabor Igloi <gabor.igloi@citrix.com> - 1.0.0-1
- Remove an unnecessary VDI.get_record XenAPI call

* Fri Oct 27 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.5.0-1
- CP-24917: Limit simultaneous connections to a maximum of 16

* Thu Oct 12 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.4.0-1
- Update dependencies to work with xen-api-client 0.11.0
- CP-25017: Ask xapi whether to use TLS or NOTLS
- CA-267340: Attach VBD & serve VDI as read-only

* Thu Oct 09 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.3.0-1
- Do VBD.plug to dom0 using XenAPI calls instead of interacting with SMAPIv2
- Make sure we clean up the VBDs we create & plug to dom0
- Improved logging
- Compatibility update for xen-api-client v0.10.0

* Fri Sep 15 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.2.0-1
- Point to 0.2.0, which has TLS support and improved logging

* Mon Aug 07 2017 Gabor Igloi <gabor.igloi@citrix.com> - 0.1.0-1
- Initial package

