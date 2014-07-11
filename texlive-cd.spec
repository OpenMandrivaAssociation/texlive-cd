# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cd
# catalog-date 2008-05-06 19:08:04 +0200
# catalog-license gpl
# catalog-version 1.3
Name:		texlive-cd
Version:	1.3
Release:	8
Summary:	Typeset CD covers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Normal usage will ordinarily require no more than a simple data
file per cover; the package will make a full insert for a CD
case (it copes with both normal and slim cases).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cd/cd.cls
%doc %{_texmfdistdir}/doc/latex/cd/CD.tex
%doc %{_texmfdistdir}/doc/latex/cd/CDlist.tex
%doc %{_texmfdistdir}/doc/latex/cd/README
%doc %{_texmfdistdir}/doc/latex/cd/cd.pdf
%doc %{_texmfdistdir}/doc/latex/cd/example.dat
%doc %{_texmfdistdir}/doc/latex/cd/parsecd.rb
%doc %{_texmfdistdir}/doc/latex/cd/slimCD.tex
%doc %{_texmfdistdir}/doc/latex/cd/slimCDlist.tex
#- source
%doc %{_texmfdistdir}/source/latex/cd/cd.dtx
%doc %{_texmfdistdir}/source/latex/cd/cd.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 750045
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718022
- texlive-cd
- texlive-cd
- texlive-cd
- texlive-cd
- texlive-cd

