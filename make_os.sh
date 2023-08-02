# ZDEFINIOWANIE WERSJI SYSTEMU OPERACYJNEGO
VERSION=$(date +%s)

# STWORZENIE KATALOGU ROBOCZEGO I GENEROWANIE KONFIGURACJI POCZATKOWEJ
mkdir ready_${VERSION}; cd ready_${VERSION}; lb config -d bookworm;

# NADPISANIE DOMYSLNYCH USTAWIEN KONFIGURACYJNYCH WLASNYMI
cp ../config auto/
chmod 700 ./auto/config
./auto/config

# ZMIANY W MOTYWIE GRAFICZNYM SYSTEMU
cp -ar ../files/includes.chroot/ config/
cp -ar ../files/includes.binary/ config/
cp -ar ../files/hooks/2137-depedencies.chroot config/hooks/live

# KOLEJNE KROKI TWORZENIA SYSTEMU OPERACYJNEGO
# 1. DODANIE INTERFEJSU GRAFICZNEGO
echo lxde-core >> config/package-lists/gui.list.chroot

# 2. DODANIE POZOSTALYCH PAKIETOW
echo "zip unzip firefox-esr python3-pip python3-tk python3-gdal gdal-bin libspatialindex-dev" >> config/package-lists/software.list.chroot

# ZBUDOWANIE PLIKU ISO Z SYSTEMEM OPERACYJNYM
lb build 2>&1 | tee build.log
