# Run tests in check section
%bcond_without check

# https://github.com/google/pprof
%global goipath         github.com/google/pprof
%global commit          2b5d4350d687b058368c98ab141d34d08162ec7b

%global common_description %{expand:
pprof is a tool for visualization and analysis of profiling data.

pprof reads a collection of profiling samples in profile.proto format and 
generates reports to visualize and help analyze the data. It can generate 
both text and graphical reports (through the use of the dot visualization 
package).

profile.proto is a protocol buffer that describes a set of callstacks and 
symbolization information. A common usage is to represent a set of sampled 
callstacks from statistical profiling. The format is described on the 
proto/profile.proto file. For details on protocol buffers, 
see https://developers.google.com/protocol-buffers

Profiles can be read from a local file, or over http. Multiple profiles of 
the same type can be aggregated or compared.

If the profile samples contain machine addresses, pprof can symbolize them 
through the use of the native binutils tools (addr2line and nm).}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Tool for visualization and analysis of profiling data
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/ianlancetaylor/demangle)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS CONTRIBUTING.md AUTHORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git2b5d435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180628git2b5d435
- Bump to commit 2b5d4350d687b058368c98ab141d34d08162ec7b

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180416git6167805
- First package for Fedora

