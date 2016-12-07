#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/OHPC_macros
%{!?PROJ_DELIM: %global PROJ_DELIM -ohpc}

Name:           docs%{PROJ_DELIM}
Version:        1.2.1
Release:        1
Summary:        OpenHPC documentation
License:        BSD-3-Clause
Group:          %{PROJ_NAME}/admin
URL:            https://github.com/openhpc/ohpc
Source0:        docs-ohpc.tar

%if 0%{?suse_version}
BuildRequires:  libstdc++6
%endif
BuildRequires:  texlive-latex
BuildRequires:  texlive-caption
BuildRequires:  texlive-colortbl
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-mdwtools
BuildRequires:  texlive-multirow
BuildRequires:  texlive-draftwatermark
BuildRequires:  texlive-tcolorbox
BuildRequires:  texlive-environ
BuildRequires:  texlive-trimspaces
BuildRequires:  texlive-amsmath
BuildRequires:  latexmk
BuildRequires:  git
Requires:       make

%if 0%{?rhel_version} || 0%{?centos_version}
Requires:       net-tools
%endif

%define debug_package %{nil}

BuildRoot:     %{_tmppath}/%{name}-%{version}-build
DocDir:        %{OHPC_PUB}/doc/contrib

%description 

This guide presents a simple cluster installation procedure using components
from the OpenHPC software stack.

%prep
%setup -n docs-ohpc

%build
%if 0%{?suse_version}
%define source_path docs/recipes/install/sles12sp1
%else
%if 0%{?rhel_version} || 0%{?centos_version}
%define source_path docs/recipes/install/centos7.2
%endif
%endif

%define parser ../../../../parse_doc.pl

#----------------------
# x86_64-based recipes
#----------------------

pushd docs/recipes/install/centos7.2/x86_64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/centos7.2/x86_64/warewulf/pbspro
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/sles12sp1/x86_64/warewulf/slurm
make ; %{parser} steps.tex > recipe.sh ; popd

pushd docs/recipes/install/sles12sp1/x86_64/warewulf/pbspro
make ; %{parser} steps.tex > recipe.sh ; popd



%install

%{__mkdir_p} %{buildroot}%{OHPC_PUB}/doc

install -m 0644 -p docs/ChangeLog %{buildroot}/%{OHPC_PUB}/doc/ChangeLog
install -m 0644 -p docs/Release_Notes.txt %{buildroot}/%{OHPC_PUB}/doc/Release_Notes.txt

%define lpath centos7.2/x86_64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath centos7.2/x86_64/warewulf/pbspro
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath sles12sp1/x86_64/warewulf/slurm
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

%define lpath sles12sp1/x86_64/warewulf/pbspro
install -m 0644 -p -D docs/recipes/install/%{lpath}/steps.pdf %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/Install_guide.pdf
install -m 0755 -p -D docs/recipes/install/%{lpath}/recipe.sh %{buildroot}/%{OHPC_PUB}/doc/recipes/%{lpath}/recipe.sh

install -m 0644 -p docs/recipes/install/centos7.2/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/centos7.2/input.local
install -m 0644 -p docs/recipes/install/sles12sp1/input.local.template %{buildroot}/%{OHPC_PUB}/doc/recipes/sles12sp1/input.local

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%files
%defattr(-,root,root)
%dir %{OHPC_HOME}
%{OHPC_PUB}
%doc %{_sourcedir}/LICENSE

%changelog
