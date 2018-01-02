Name:		texlive-leipzig
Version:	2.0
Release:	1
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
%{_texmfdistdir}/tex/latex/leipzig
%doc %{_texmfdistdir}/doc/latex/leipzig
#- source
%doc %{_texmfdistdir}/source/latex/leipzig

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
