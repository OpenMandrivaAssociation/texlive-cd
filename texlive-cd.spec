# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cd
# catalog-date 2008-05-06 19:08:04 +0200
# catalog-license gpl
# catalog-version 1.3
Name:		texlive-cd
Version:	1.3
Release:	1
Summary:	Typeset CD covers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Normal usage will ordinarily require no more than a simple data
file per cover; the package will make a full insert for a CD
case (it copes with both normal and slim cases).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
