# TODO:
# - what to do with net subdir?
Summary:	Net::SSH is a pure-Ruby implementation of the SSH2 client protocol
Name:		ruby-net-ssh
Version:	2.0.8
Release:	0.1
License:	Ruby License
Source0:	http://rubyforge.org/frs/download.php/49300/net-ssh-%{version}.tar.gz
# Source0-md5:	050bf405bf40a1e70412fbc902990acb
Group:		Development/Languages
URL:		http://rubyforge.org/projects/net-ssh/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Net::SSH is a pure-Ruby implementation of the SSH2 client protocol.

%package rdoc
Summary:	Documentation files for ruby-net-ssh
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ruby-net-ssh.

%prep
%setup -q -n net-ssh-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib

rm -rf ri/OpenSSL
rm -rf ri/String
rm -f ri/Net/cdesc-Net.yaml
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rdoc README.rdoc THANKS.rdoc
# XXX?
%dir %{ruby_rubylibdir}/net
%{ruby_rubylibdir}/net/._ssh.rb
%{ruby_rubylibdir}/net/ssh.rb
%{ruby_rubylibdir}/net/ssh

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
# XXX ?
%dir %{ruby_ridir}/Net
%{ruby_ridir}/Net/SSH
