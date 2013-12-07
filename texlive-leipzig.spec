# revision 31045
# category Package
# catalog-ctan /macros/latex/contrib/leipzig
# catalog-date 2013-06-19 00:57:02 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-leipzig
Version:	1.1
Release:	4
Summary:	Typeset and index linguistic gloss abbreviations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leipzig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leipzig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leipzig.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leipzig.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The leipzig package provides a set of macros for standard
glossing abbreviations, with options to create new ones. They
are mnemonic (e.g. \Acc{} for accusative, abbreviated acc).
These abbre can be used alone or on top of the glossaries
package for easy indexing and glossary printing.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/leipzig/leipzig.sty
%doc %{_texmfdistdir}/doc/latex/leipzig/README
%doc %{_texmfdistdir}/doc/latex/leipzig/README.txt
%doc %{_texmfdistdir}/doc/latex/leipzig/leipzig.pdf
%doc %{_texmfdistdir}/doc/latex/leipzig/leipzig.tex
#- source
%doc %{_texmfdistdir}/source/latex/leipzig/leipzig.dtx
%doc %{_texmfdistdir}/source/latex/leipzig/leipzig.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
