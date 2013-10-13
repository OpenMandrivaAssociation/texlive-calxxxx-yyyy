# revision 28675
# category Package
# catalog-ctan /macros/latex/contrib/calxxxx-yyyy
# catalog-date 2012-12-31 22:53:16 +0100
# catalog-license lppl1.3
# catalog-version 1.0e
Name:		texlive-calxxxx-yyyy
Version:	1.0e
Release:	1
Summary:	Print a calendar for a group of years
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/calxxxx-yyyy
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package prints a calendar for 2 or more years, according to
a language selection. The package is also "culture dependent",
in the sense that it will start weeks according to local rules:
e.g., weeks conventionally start on Monday in the English-
speaking world.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/calxxxx-yyyy/calxxxx-yyyy.tex
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/README.tex
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2013-2030_DE.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2013-2030_DK.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2013-2030_EN.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
