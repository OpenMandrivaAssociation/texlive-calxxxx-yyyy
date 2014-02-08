# revision 25001
# category Package
# catalog-ctan /macros/latex/contrib/calxxxx-yyyy
# catalog-date 2012-01-03 11:34:51 +0100
# catalog-license lppl1.3
# catalog-version 1.0d
Name:		texlive-calxxxx-yyyy
Version:	1.0d
Release:	2
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
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2012-2029_DE.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2012-2029_DK.pdf
%doc %{_texmfdistdir}/doc/latex/calxxxx-yyyy/cal2012-2029_EN.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0d-1
+ Revision: 758834
- texlive-calxxxx-yyyy

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-2
+ Revision: 749967
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0c-1
+ Revision: 717999
- texlive-calxxxx-yyyy
- texlive-calxxxx-yyyy
- texlive-calxxxx-yyyy
- texlive-calxxxx-yyyy
- texlive-calxxxx-yyyy

