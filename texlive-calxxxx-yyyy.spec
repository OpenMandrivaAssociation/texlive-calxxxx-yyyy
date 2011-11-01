Name:		texlive-calxxxx-yyyy
Version:	1.0c
Release:	1
Summary:	Print a calendar for a group of years
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calxxxx-yyyy
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package prints a calendar for 2 or more years, according to
a language selection. The package is also "culture dependent",
in the sense that it will start weeks according to local rules:
e.g., weeks conventionally start on Monday in the English-
speaking world.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calxxxx-yyyy/calxxxx-yyyy.tex
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README.tex
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/calxxxx-yyyy_DE.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/calxxxx-yyyy_DK.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/calxxxx-yyyy_EN.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
