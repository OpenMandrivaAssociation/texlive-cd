Name:		texlive-cd
Version:	34452
Release:	1
Summary:	Typeset CD covers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cd
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.r34452.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.doc.r34452.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cd.source.r34452.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
