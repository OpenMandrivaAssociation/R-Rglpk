%global packname  Rglpk
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.3.10
Release:          1
Summary:          R/GNU Linear Programming Kit Interface
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Rglpk_0.3-10.tar.gz
Requires:         R-slam 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-slam
BuildRequires:    glpk-devel

%description
R interface to the GNU Linear Programing Kit (GLPK version 4.47 is shipped
with the source package).  GLPK is open source software for solving
large-scale linear programming (LP), mixed integer linear programming
(MILP) and other related problems.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGELOG
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
