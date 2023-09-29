pkgname=bat
pkgver=1.0
pkgrel=1 
pkgdesc="A simple 'package manager' for aur"
arch=('any')

package() {
  cd .. 
  sudo install -Dm755 ./main.py /usr/bin/bat-install 
  chmod +x /usr/bin/bat-install 
}
