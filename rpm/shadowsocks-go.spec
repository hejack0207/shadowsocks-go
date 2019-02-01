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

%install
mkdir -p "%{buildroot}/usr/bin"
install -p -m755 "bin/shadowsocks-server" "%{buildroot}/usr/bin/"
mkdir -p "%{buildroot}/usr/lib/systemd/system"
cat > "%{buildroot}/usr/lib/systemd/system/shadowsocks-go-server@.service" <<EOF
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
cp -f shadowsocks-go/sample-config/client-multi-server.json %{buildroot}/etc/shadowsocks-go/config.json

mkdir -p "%{buildroot}/usr/bin"
install -p -m755 "$srcdir/bin/shadowsocks-local" "%{buildroot}/usr/bin/"
mkdir -p "%{buildroot}/usr/lib/systemd/system"
cat > "%{buildroot}/usr/lib/systemd/system/shadowsocks-go@.service" <<EOF
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

%clean
#rm -fr %{buildroot}

%post

%postun

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README Copyright TODO

%changelog

