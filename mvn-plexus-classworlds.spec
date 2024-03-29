#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plexus-classworlds
Version  : 1.2.alpha.7
Release  : 8
URL      : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.pom
Source2  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/1.2-alpha-9/plexus-classworlds-1.2-alpha-9.pom
Source3  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.jar
Source4  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.pom
Source5  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.pom
Source6  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.jar
Source7  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.pom
Source8  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.jar
Source9  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.pom
Source10  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.jar
Source11  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.pom
Source12  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.jar
Source13  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.pom
Source14  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.jar
Source15  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.pom
Source16  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar
Source17  : https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 Plexus
Requires: mvn-plexus-classworlds-data = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-plexus-classworlds package.
Group: Data

%description data
data components for the mvn-plexus-classworlds package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-9
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-9/plexus-classworlds-1.2-alpha-9.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-7/plexus-classworlds-1.2-alpha-7.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/1.2-alpha-9/plexus-classworlds-1.2-alpha-9.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.2/plexus-classworlds-2.2.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.2.3/plexus-classworlds-2.2.3.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4.2/plexus-classworlds-2.4.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.4/plexus-classworlds-2.4.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.1/plexus-classworlds-2.5.1.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.pom
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.jar
/usr/share/java/.m2/repository/org/codehaus/plexus/plexus-classworlds/2.6.0/plexus-classworlds-2.6.0.pom
