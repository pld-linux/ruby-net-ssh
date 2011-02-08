# TODO:
# - what to do with net subdir?
%define pkgname net-ssh
Summary:	Net::SSH - a pure-Ruby implementation of the SSH2 client protocol
Summary(pl.UTF-8):	Net::SSH - implementacja protokołu klienckiego SSH2 w czystym Rubym
Name:		ruby-%{pkgname}
Version:	2.0.20
Release:	3
License:	Ruby License
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	68fbaa033678be355fb93422d6062f79
Group:		Development/Languages
URL:		http://github.com/net-ssh/net-ssh
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Provides:	ruby-Net-SSH
Obsoletes:	ruby-Net-SSH
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Net::SSH is a pure-Ruby implementation of the SSH2 client protocol.

%description -l pl.UTF-8
Net::SSH to implementacja protokołu klienckiego SSH2 w czystym Rubym.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.rdoc -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{OpenSSL,String}
rm ri/created.rid

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
%{ruby_rubylibdir}/net/ssh.rb
%{ruby_rubylibdir}/net/ssh

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
# XXX?
%dir %{ruby_ridir}/Net
%{ruby_ridir}/Net/SSH
