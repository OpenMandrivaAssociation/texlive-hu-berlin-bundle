Name:		texlive-hu-berlin-bundle
Version:	67128
Release:	1
Summary:	LaTeX classes for the Humboldt-Universitat zu Berlin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hu-berlin-bundle
License:	lppl1.3c gpl2 bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hu-berlin-bundle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hu-berlin-bundle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hu-berlin-bundle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides files according to the corporate design
of the Humboldt-Universitat zu Berlin. This is not an official
package by the university itself, and not officially approved
by it. More information can be found in the Humboldt
University's corporate design guideline and on the website
https://www.hu-berlin.de/de/hu-intern/design. At present, the
bundle contains a letter class based on scrlttr2 and a package
hu-berlin-base.sty which contains all relevant code for
documents and documentclasses of the bundle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/hu-berlin-bundle
%{_texmfdistdir}/tex/lualatex/hu-berlin-bundle
%doc %{_texmfdistdir}/doc/lualatex/hu-berlin-bundle

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
