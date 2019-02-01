Name: shadowsocks-go
Summary: Shadowsocks Golang Implementaion
Version: 1.2.2
Release: 1
License: MIT
Group: Net Tools
Source0: https://github.com/shadowsocks/shadowsocks-go/releases/download/%{version}/shadowsocks-server.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: golang >= 1.11.2
URL: http://shadowsocks.github.io/shadowsocks-go
Prefix: %{_prefix}
Docdir: %{_docdir}

%description
shadowsocks-go is golang implementation of shadowsocks(aka an socks proxy utils).

%prep
%setup -q

%build
%configure
make

%install
rm -fr %{buildroot}

%makeinstall

%clean
rm -fr %{buildroot}

%post

%postun

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet.pdf
%doc %{_mandir}/man1/xmlstarlet.1*

%{prefix}/bin/xml
%changelog

