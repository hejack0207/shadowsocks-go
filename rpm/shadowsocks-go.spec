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
#make

%install
cp -f /home/he/dev/Go/hejack0207/shadowsocks-go/sample-config/client-multi-server.json ${RPM_BUILD_ROOT}/etc/shadowsocks-go/config.json
mkdir -p "$pkgdir/usr/bin"
install -p -m755 "$srcdir/bin/shadowsocks-server" "$pkgdir/usr/bin/"
mkdir -p "$pkgdir/usr/lib/systemd/system"
cat > "$pkgdir/usr/lib/systemd/system/shadowsocks-go-server@.service" <<EOF
[Unit]
Description=Shadowsocks Server Service (Go Version)
After=network.target

[Service]
Type=simple
#User=nobody
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ExecStart=/usr/bin/shadowsocks-server -c /etc/shadowsocks/%i.json

[Install]
WantedBy=multi-user.target
EOF

mkdir -p "$pkgdir/usr/bin"
install -p -m755 "$srcdir/bin/shadowsocks-local" "$pkgdir/usr/bin/"
mkdir -p "$pkgdir/usr/lib/systemd/system"
cat > "$pkgdir/usr/lib/systemd/system/shadowsocks-go@.service" <<EOF
[Unit]
Description=Shadowsocks Client Service (Go Version)
After=network.target

[Service]
Type=simple
#User=nobody
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ExecStart=/usr/bin/shadowsocks-local -c /etc/shadowsocks/%i.json

[Install]
WantedBy=multi-user.target
EOF

%makeinstall

%clean
#rm -fr %{buildroot}

%post

%postun

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO doc/xmlstarlet.txt doc/xmlstarlet.pdf
%doc %{_mandir}/man1/xmlstarlet.1*

%{prefix}/bin/xml
%changelog

