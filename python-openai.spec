%global pypi_name openai

Name:           python-%{pypi_name}
Version:        1.65.2
Release:        1
Summary:        The official Python library for the openai API
Group:          Development/Python
License:        ASL
URL:            https://github.com/openai/openai-python
Source0:        https://files.pythonhosted.org/packages/source/o/openai/openai-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(anyio)
#BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(hatch-fancy-pypi-readme)
#BuildRequires:  python3dist(jiter)
BuildSystem:	python

%description
The OpenAI Python library provides convenient access to the OpenAI REST API
from any Python 3.7+ application. The library includes type definitions for
all request params and response fields, and offers both synchronous and
asynchronous clients powered by httpx.


%files
%license LICENSE
%{_bindir}/openai
