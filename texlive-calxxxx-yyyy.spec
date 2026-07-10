%global tl_name calxxxx-yyyy
%global tl_revision 77222

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20.26a
Release:	%{tl_revision}.1
Summary:	Print a calendar for a group of years
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/calxxxx-yyyy
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/calxxxx-yyyy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package prints a calendar for two or more years, according to a
language selection. The package is also "culture dependent" in the sense
that it will start weeks according to local rules: e.g., weeks
conventionally start on Monday in the English-speaking world. The
package requires array, babel, and geometry.

