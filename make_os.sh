# ZDEFINIOWANIE WERSJI SYSTEMU OPERACYJNEGO
VERSION="0"

# STWORZENIE KATALOGU ROBOCZEGO I GENEROWANIE KONFIGURACJI POCZATKOWEJ
mkdir ready_${VERSION}; cd ready_${VERSION}; lb config;

# NADPISANIE DOMYSLNYCH USTAWIEN KONFIGURACYJNYCH WLASNYMI
cp ../config auto/
chmod 700 ./auto/config
./auto/config

# ZMIANY W MOTYWIE GRAFICZNYM SYSTEMU
cp -ar ../files/includes.chroot/ config/
cp -ar ../files/includes.binary/ config/
#cp -ar ../files/hooks/ config/

# KOLEJNE KROKI TWORZENIA SYSTEMU OPERACYJNEGO
# 1. DODANIE INSTALATORA
# echo debian-installer-launcher >> config/package-lists/installer.list.chroot

# 2. DODANIE INTERFEJSU GRAFICZNEGO
echo lxde-core >> config/package-lists/gui.list.chroot

# 3. DODANIE POZOSTALYCH PAKIETOW
echo "zip unzip" >> config/package-lists/software.list.chroot

# ZBUDOWANIE PLIKU ISO Z SYSTEMEM OPERACYJNYM
lb build 2>&1 | tee build.log