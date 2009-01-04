Name:           hello
Version:        2.4
Release:        1%{?dist}
Summary:        Prints a Familiar, Friendly Greeting
Group:          Development/Tools
# Parts of the documentation are under GFDL, BSD, and Public Domain
# *All* code is GPLv3+.
License:        GPLv3+ and GFDL and BSD and Public Domain
URL:            http://www.gnu.org/software/hello/
Source0:        http://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gettext
Requires(post): info
Requires(preun): info


%description
Hello prints a friendly greeting. It also serves as a sample GNU
package, showing practices that may be useful for GNU projects.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%find_lang hello


%check
cd tests
make check-TESTS


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :


%preun
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi


%files -f hello.lang
%defattr(-,root,root,-)
%doc COPYING
%{_mandir}/man1/hello.1*
%{_bindir}/hello
%{_infodir}/hello.info*


%changelog
* Wed Dec 17 2008 Conrad Meyer <konrad@tylerc.org> - 2.4-1
- Initial package.
