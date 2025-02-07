%define luarocks_pkg_name lua-path
%define luarocks_pkg_version 0.3.1-1
%define luarocks_pkg_prefix lua-path-0.3.1-1
%define luarocks_pkg_major 0.3.1
%define luarocks_pkg_minor 1
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true

Name: lua-path
BuildRequires: lua-rpm-macros

%if %{defined luarocks_requires}
%luarocks_requires
%else
BuildRequires: lua51-luarocks lua53-luarocks lua54-luarocks
BuildRequires: lua51-devel lua53-devel lua54-devel
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: make
%endif
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: File system path manipulation library
Url: https://github.com/moteus/lua-path
License: MIT/X11
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
Requires: %{luadist lua >= 5.1, < 5.5}

Source0: lua-path-0.3.1-1.tar.gz
Source1: lua-path-0.3.1-1.rockspec
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  

%prep
%autosetup -p1 -n %luarocks_pkg_prefix
%luarocks_prep

%generate_buildrequires

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}
%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
